"""Bit-stream parser for `ac_update_dlc_ownership` (AC 0x72).

Sent S->C with the player's DLC ownership state. Handler 0x08233924
reads a u8 status; the rest of the body depends on its value:

    u8 status
    if status == 0:
        bag    DLC ownership map -> profile+0xada4c (Bag_Deserialize
               @8b1ed60). Keys are Steam product GUIDs
               (e.g. "7741E9BF-1E8D-4D15-A264-C1A196CC8BCB"); 16 entries
               in every observed capture.
    else:
        u32 count
        for each of count items (the same per-item reader FUN_088ead70
        used by ac_player_inventory):
            u64    iid
            cstrN  name        (<=60 chars)
            u32    quantity
            u1     flag        (1-bit)
            u64    misc

All 26 captured bodies have status=0 and decode as the 16-entry GUID
bag (7 bits of trailing padding -- the bag's u1 use_indexed_keys flag
plus the trailing bit-misaligned variants leave the body 7 bits short
of a whole byte). The item-list path is modelled per the handler but
hasn't been seen on the wire, so any non-zero-status capture would
exercise an untested code path.

The old `u1 status` stub captured only the first byte.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field, _read_bag


_NAME_MAX = 60


def _read_dlc_item(br: BitReader) -> dict:
    """One DLC item record (same shape as inventory items, FUN_088ead70)."""
    start = br.pos
    out: dict[str, object] = {}
    out["iid"]      = read_field(br, "u64", br.read_u64())
    out["name"]     = read_field(br, "str",
                                 br.read_cstring(max_len=_NAME_MAX))
    out["quantity"] = read_field(br, "u32", br.read_u32())
    out["flag"]     = read_field(br, "bool", br.read_bool())
    out["misc"]     = read_field(br, "u64", br.read_u64())
    br.last_read_start = start
    return out


class AcUpdateDlcOwnershipBody:
    """Parsed body of `ac_update_dlc_ownership`. The wire shape is
    `u8 status` then EITHER a property bag (status==0; observed in every
    capture) OR a count + item list (status!=0; modelled but untested)."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.status = read_field(br, "u8", br.read_u8())

            if self.status.value == 0:
                # Status-0 path: the rest is a property bag mapping
                # Steam product GUID -> ownership variant.
                self.dlc_bag = read_field(br, "bag", _read_bag(br))
            else:
                # Item-list path (untested -- no captures observed).
                self.count = read_field(br, "u32", br.read_u32())
                items_start = br.pos
                items: List[dict] = [
                    _read_dlc_item(br) for _ in range(self.count.value)
                ]
                br.last_read_start = items_start
                self.items = Variant("list", items, 0xff,
                                     (items_start, br.pos))
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
            return f"AcUpdateDlcOwnershipBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "status"):
            return (f"AcUpdateDlcOwnershipBody({len(self._raw)}B{suffix} "
                    f"slack={slack}b)")
        parts = [f"{len(self._raw)}B{suffix}",
                 f"status={self.status.value}"]
        if hasattr(self, "dlc_bag"):
            parts.append(f"dlc_entries={len(self.dlc_bag.value)}")
        if hasattr(self, "count"):
            parts.append(f"count={self.count.value}")
        parts.append(f"slack={slack}b")
        return "AcUpdateDlcOwnershipBody(" + ", ".join(parts) + ")"
