"""Bit-stream parser for `ac_buy_item` S->C response (AC 0x27).

Handler 0x08233dd0 (decompiled in Ghidra) reads:

    u32   store_item_id_echo       echo of the request's storeItemId
    u8    status                   StoreBuyResult / SBR_* code (0 = OK)
    {InventoryItem via FUN_088ead70}:
        u64    iid                 inventory instance id (0 when the
                                   purchase didn't add a new inventory
                                   slot -- e.g. credits-only transactions)
        cstrN  def_name            item def-name (<=60 chars, NUL-term)
        u32    quantity            stack count after the purchase
        u1     flag                1-bit marker (unknown semantics)
        u64    misc                often 0; opaque
    if iid != 0:
        u1     extra_bool          1-bit marker (precedes the dedup list)
        u8     count               number of consumed/affected def-names
        count x cstrN  consumed    NUL-terminated def-names

When iid == 0 the handler stops after the InventoryItem and the rest of
the wire body is ignored by the client (one observed capture has ~42 B
of trailing payload the client never consumes). We mirror that by
exposing `unread_tail` as the bytes the client wouldn't read.

Verified against 4 S->C captures: a 30 B fail (iid=0, empty
def_name, 15 bits trailing pad), a 59 B success (iid set,
'Weapon_Plasmagun_Heavy_T1_Mk1', count=0, 6 bits pad), a 98 B success-
like response with iid=0 + 'WeaponMod_Laser_Alien_Killer' + qty=791
(client ignores the 42 trailing bytes), and another 30 B fail.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field


_NAME_MAX = 60
_CSTR_MAX = 256


_STATUS_NAMES = {
    0: "SBR_OK",
}


def _read_inventory_item(br: BitReader) -> dict:
    """The shared InventoryItem reader (FUN_088ead70 -- same shape as
    ac_player_inventory and ac_update_dlc_ownership items)."""
    start = br.pos
    out: dict[str, object] = {}
    out["iid"]      = read_field(br, "u64", br.read_u64())
    out["def_name"] = read_field(br, "str",
                                 br.read_cstring(max_len=_NAME_MAX))
    out["quantity"] = read_field(br, "u32", br.read_u32())
    out["flag"]     = read_field(br, "bool", br.read_bool())
    out["misc"]     = read_field(br, "u64", br.read_u64())
    br.last_read_start = start
    return out


class AcBuyItemResponseBody:
    """Parsed body of the S->C `ac_buy_item` response."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.store_item_id_echo = read_field(
                br, "u32", br.read_u32())
            st = br.read_u8()
            self.status = read_field(
                br, "u8", st,
                display=f"{st} ({_STATUS_NAMES.get(st, '?')})")

            item_start = br.pos
            self.item = Variant("struct", _read_inventory_item(br),
                                0xff, (item_start, br.pos))

            iid = self.item.value["iid"].value
            if iid != 0:
                self.extra_bool = read_field(
                    br, "bool", br.read_bool())
                cnt = br.read_u8()
                self.count = read_field(br, "u8", cnt)
                consumed_start = br.pos
                consumed = [read_field(br, "str",
                                       br.read_cstring(max_len=_CSTR_MAX))
                            for _ in range(cnt)]
                br.last_read_start = consumed_start
                self.consumed = Variant("list", consumed, 0xff,
                                        (consumed_start, br.pos))

            self.bits_consumed = br.pos
        except EOFError:
            self.ok = False
            self.bits_consumed = br.pos
        except Exception as e:
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"
            self.bits_consumed = br.pos

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcBuyItemResponseBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "store_item_id_echo"):
            return (f"AcBuyItemResponseBody({len(self._raw)}B{suffix} "
                    f"slack={slack}b)")
        item = self.item.value
        parts = [
            f"{len(self._raw)}B{suffix}",
            f"echo={self.store_item_id_echo.value:#x}",
            f"status={_STATUS_NAMES.get(self.status.value, self.status.value)}",
            f"iid={item['iid'].value:#x}",
            f"def_name={item['def_name'].value!r}",
            f"qty={item['quantity'].value}",
        ]
        if hasattr(self, "count"):
            parts.append(f"consumed[{self.count.value}]")
        # Big trailing slack only happens in the iid==0 branch where the
        # client legitimately ignores server-sent tail bytes.
        parts.append(f"slack={slack}b")
        return "AcBuyItemResponseBody(" + ", ".join(parts) + ")"
