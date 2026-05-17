"""Bit-stream parser for `ac_player_vessels` (AC 0x25).

Sent S→C with the player's owned-vessel catalogue. The handler is at
0x0822e436; each vessel record is read by FUN_08925ae0.

Wire format:

    u16v2  num_vessels
    num_vessels × VesselRecord (FUN_08925ae0):
        u64v2  iid              (vessel instance id; if 0 the rest is skipped)
        cstr60 def_name         (e.g. 'Ship_Race1_M_T1')
        u64v2 × 35              (slot iid array — equipped modules /
                                  weapons / ship slots, fixed-size)
        2 × { cstr59 name, u8, u8 }   (per-slot named refs + 2 flags)
        i32    a                (synergy / prestige? — at +0x174)
        u64v2  b                (at +0x178)
        u32    c                (at +0x188)
        u32    d                (at +0x18c)
        u8     e                (at +0x1c)
        f32    f                (at +0x190)
        u32    g                (at +0x194)
        u8     h                (at +0x19c)
        u64v2  i                (at +0x1a0)
        u64v2  j                (at +0x14)
        u32    k                (at +0x5fc)
        u1     flag1            (at +0x194 — a separate bit, not the u32)
        u64v2  uid_a            (at +0; mirrored from the owner / squad?)
        u64v2  uid_b            (at +8)
        cstr60 m                (at +0x1a4 — another short name)
        14 × { cstr60 name, u64v2 id }   (perk/upgrade slots)
        10 × cstr256             (long-string slots — texture / paint /
                                  decal def names)
    f32    last_seen_or_decay   (at +0x28e768)
    f32    prestige_or_score    (at +0x787e8)

Records with iid==0 are placeholders (empty slot in the owned-vessel
table) — the handler skips the body in that case.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field


_NAME_MAX = 60
_SHORT_NAME_MAX = 59
_LONG_NAME_MAX = 256


def _read_vessel_record(br: BitReader) -> dict:
    """One VesselRecord (FUN_08925ae0). Every field is wrapped via
    read_field() so the GUI tree picks up its bit_range. Records with
    iid==0 are placeholder/empty slots in the player's vessel table —
    we read only the iid then leave the rest empty (matching the
    handler's `if (iid != 0)` gate)."""
    start = br.pos
    out: dict[str, object] = {}
    out["iid"] = read_field(br, "u64", br.read_u64())
    if out["iid"].value == 0:
        br.last_read_start = start
        return out

    out["def_name"] = read_field(br, "str",
                                 br.read_cstring(max_len=_NAME_MAX))

    # 35 × u64 — fixed slot-iid array.
    slots_start = br.pos
    slot_iids = [read_field(br, "u64", br.read_u64()) for _ in range(35)]
    br.last_read_start = slots_start
    out["slot_iids"] = Variant("list", slot_iids, 0xff,
                               (slots_start, br.pos))

    # 2 × { cstr59 name, u8 a, u8 b }
    cfg_start = br.pos
    slot_cfg = []
    for _ in range(2):
        cfg_entry_start = br.pos
        entry = {
            "name": read_field(br, "str",
                               br.read_cstring(max_len=_SHORT_NAME_MAX)),
            "a":    read_field(br, "u8", br.read_u8()),
            "b":    read_field(br, "u8", br.read_u8()),
        }
        br.last_read_start = cfg_entry_start
        slot_cfg.append(entry)
    br.last_read_start = cfg_start
    out["slot_cfg"] = Variant("list", slot_cfg, 0xff, (cfg_start, br.pos))

    out["a"]     = read_field(br, "i32",  br.read_i32())
    out["b"]     = read_field(br, "u64",  br.read_u64())
    out["c"]     = read_field(br, "u32",  br.read_u32())
    out["d"]     = read_field(br, "u32",  br.read_u32())
    out["e"]     = read_field(br, "u8",   br.read_u8())
    out["f"]     = read_field(br, "f32",  br.read_f32())
    out["g"]     = read_field(br, "u32",  br.read_u32())
    out["h"]     = read_field(br, "u8",   br.read_u8())
    out["i"]     = read_field(br, "u64",  br.read_u64())
    out["j"]     = read_field(br, "u64",  br.read_u64())
    out["k"]     = read_field(br, "u32",  br.read_u32())
    out["flag1"] = read_field(br, "bool", br.read_bool())
    out["uid_a"] = read_field(br, "u64",  br.read_u64())
    out["uid_b"] = read_field(br, "u64",  br.read_u64())
    out["m"]     = read_field(br, "str",
                              br.read_cstring(max_len=_NAME_MAX))

    # 14 × { cstr60 name, u64 id }
    perks_start = br.pos
    perks = []
    for _ in range(14):
        e_start = br.pos
        entry = {
            "name": read_field(br, "str",
                               br.read_cstring(max_len=_NAME_MAX)),
            "id":   read_field(br, "u64", br.read_u64()),
        }
        br.last_read_start = e_start
        perks.append(entry)
    br.last_read_start = perks_start
    out["perks"] = Variant("list", perks, 0xff, (perks_start, br.pos))

    # 10 × cstr256 — long-string slots (paint / decal / customisation).
    longs_start = br.pos
    long_strings = [
        read_field(br, "str", br.read_cstring(max_len=_LONG_NAME_MAX))
        for _ in range(10)
    ]
    br.last_read_start = longs_start
    out["long_strings"] = Variant("list", long_strings, 0xff,
                                  (longs_start, br.pos))

    br.last_read_start = start
    return out


class AcPlayerVesselsBody:
    """Parsed body of `ac_player_vessels`. Mirrors the binary's wire
    sequence — see module docstring. Records with iid==0 are placeholder
    empty slots; their `def_name` etc. are absent from the dict."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.num_vessels = read_field(br, "u16", br.read_u16())

            vessels_start = br.pos
            vessels: List[dict] = [
                _read_vessel_record(br)
                for _ in range(self.num_vessels.value)
            ]
            br.last_read_start = vessels_start
            self.vessels = Variant("list", vessels, 0xff,
                                   (vessels_start, br.pos))

            # Two tail floats — `last_seen_or_decay` and a prestige/score
            # cache (see comparator at +0x787e8 in the handler).
            self.last_seen_or_decay = read_field(br, "f32", br.read_f32())
            self.prestige_or_score  = read_field(br, "f32", br.read_f32())
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
            return f"AcPlayerVesselsBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "num_vessels"):
            return f"AcPlayerVesselsBody({len(self._raw)}B{suffix} slack={slack}b)"
        n = self.num_vessels.value
        owned = (sum(1 for v in self.vessels.value if v["iid"].value)
                 if hasattr(self, "vessels") else 0)
        parts = [f"{len(self._raw)}B{suffix}", f"num_vessels={n}",
                 f"owned={owned}"]
        # Surface the first few owned vessels' def names so the log line
        # is useful at a glance.
        if hasattr(self, "vessels"):
            names = [v["def_name"].value for v in self.vessels.value
                     if v["iid"].value and "def_name" in v]
            if names:
                preview = ", ".join(names[:5])
                if len(names) > 5:
                    preview += f", … +{len(names) - 5}"
                parts.append(f"defs=[{preview}]")
        if hasattr(self, "last_seen_or_decay"):
            parts.append(
                f"last_seen_or_decay={self.last_seen_or_decay.value:g}")
        if hasattr(self, "prestige_or_score"):
            parts.append(
                f"prestige_or_score={self.prestige_or_score.value:g}")
        parts.append(f"slack={slack}b")
        return "AcPlayerVesselsBody(" + ", ".join(parts) + ")"
