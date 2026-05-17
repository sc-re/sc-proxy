"""Bit-stream parser for `ac_account_auras` (AC 0x15).

S→C response carrying the player's full set of account auras —
permanent unlocks (`Steamer_2` from owning DLCs), per-day multipliers
(`Daily_Pvp_2x`, `Daily_Coop_2x`, …), and a few special tags
(`BattlePassExp30`, `RW_Loot`, `Raid_Loot`).

Wire format (matches MasterServer_GetAccountAuras' table — see
`UI.OnAccountAurasChanged` in uigamefuncs.lua, which reads `.defName`):

    u1   status_flag        (always 1 in observed captures)
    u8   count
    count × {
        cstring  def_name   (e.g. 'Daily_Coop_2x', 'Steamer_2')
        u32      flags      (always 0x80000000 — bit 31 set,
                              likely 'active'/'persistent')
        u64      value      (count/expiry: 1/2/3/27 for daily
                              multipliers, 0xffffffff for permanent
                              auras that never expire)
    }

Tested against 80+ captures across 6 distinct body sizes (320–708 B,
13–22 auras) — every body parses with 7 bits of sub-byte slack.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field


def _read_aura(br: BitReader) -> dict:
    """One aura entry. Each field is wrapped via read_field() so the
    tree node carries its bit_range for hex-pane highlighting."""
    start = br.pos
    out: dict[str, object] = {}
    out["def_name"] = read_field(br, "str", br.read_cstring(max_len=120))
    out["flags"]    = read_field(br, "u32", br.read_u32())
    out["value"]    = read_field(br, "u64", br.read_u64())
    br.last_read_start = start
    return out


class AcAccountAurasBody:
    """Decoded body of an `ac_account_auras` async-request.

    `auras` is a Variant whose value is a list of dicts (each dict
    keyed by field-name → Variant), so every aura's fields land in the
    Qt tree with their bit ranges intact.
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.status_flag = read_field(br, "bool", br.read_bool())
            self.count       = read_field(br, "u8",   br.read_u8())
            auras_start = br.pos
            auras: List[dict] = [
                _read_aura(br) for _ in range(self.count.value)
            ]
            br.last_read_start = auras_start
            self.auras = Variant("list", auras, 0xff,
                                 (auras_start, br.pos))
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
            return f"AcAccountAurasBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "count"):
            return f"AcAccountAurasBody({len(self._raw)}B{suffix} slack={slack}b)"
        names = []
        for a in self.auras.value:
            n = a["def_name"].value
            v = a["value"].value
            if v == 0xffffffff:
                names.append(f"{n}")
            else:
                names.append(f"{n}={v}")
        return (f"AcAccountAurasBody({len(self._raw)}B{suffix}, "
                f"status={self.status_flag.value}, "
                f"count={self.count.value}, "
                f"auras=[{', '.join(names)}], slack={slack}b)")
