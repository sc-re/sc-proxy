"""Bit-stream parser for `ac_player_vessels` (AC 0x25).

Sent S→C with the player's owned-vessel catalogue. The handler is at
0x0822e436; each vessel record is read by FUN_08925ae0. Field names and
struct offsets below are taken straight from that function's stores
(param_1 is the vessel record, an undefined8* so `param_1[n]` == byte
n*8). Names were cross-checked against decoded captures (see the value
notes); fields whose meaning is still unconfirmed keep an `unknown_<off>`
name that records their struct offset for further RE.

Wire format:

    u16    num_vessels
    num_vessels × VesselRecord (FUN_08925ae0):
        u64   iid               vessel instance id (+0x3c). If 0 the rest
                                 of the record is skipped (empty slot).
        cstr60 def_name          ship def (+0x10), e.g. 'Ship_Race1_M_T1'
        u64 × 35  equipped_iids  installed module/weapon instance ids (+0x44)
        2 × { cstr59 def_name, u8 flag1, u8 flag2 }   munitions (+0x15c):
                                 active weapon-mod + missile/ammo selection
                                 (names like WeaponMod_*/SpaceMissile_*).
        i32   unknown_0x174      observed always -1 (sentinel)
        u64   unknown_0x178      observed always 0
        u32   unknown_0x188      ~900-1100, 0 when unused (per-ship rating?)
        u32   unknown_0x18c      large/varied stat counter, 0 when unused
        u8    rank               ship rank (+0x38); fixed per def, faction
                                 variants rank higher (5/6/7 for T1 here)
        f32   durability         normalized hull wear 0.0-1.0 (+0x190)
        u32   unknown_0x198      almost always 0
        u8    unknown_0x19c      0 or 0xff (index sentinel)
        u64   unknown_0x1a0      rare instance id (+0x1a0)
        u64   unknown_0x14       rare instance id (+0x14)
        u32   synergy            accumulated synergy points (+0x5fc);
                                 varies per ship with use, scales with rank
        u1    unknown_flag_0x194 single bit, observed always 0
        u64   unknown_iid_a      rare large id (+0x0)
        u64   unknown_iid_b      rare large id (+0x8)
        cstr60 special_module    a module def name (+0x1a8), e.g.
                                 'Module_CloakingDevice_Uniq_T3'; usually ''
        14 × { cstr60 def_name, u64 iid }   decals (+0x1d4): cosmetic
                                 decal/sticker slots (names like
                                 'WomansDay_2017', 'death_01').
        10 × cstr256  modifiers  ship stat-modifier def names (+0x1ac),
                                 e.g. 'PRIMARY_DAMAGE_4', 'ROTATION_SPEED'.
    f32    last_seen_or_decay    (handler tail, +0x28e768)
    f32    prestige_or_score     (handler tail, +0x787e8)

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

    # 35 × u64 — installed module/weapon instance ids, one per ship slot.
    slots_start = br.pos
    equipped_iids = [read_field(br, "u64", br.read_u64()) for _ in range(35)]
    br.last_read_start = slots_start
    out["equipped_iids"] = Variant("list", equipped_iids, 0xff,
                                   (slots_start, br.pos))

    # 2 × { cstr59 def_name, u8 flag1, u8 flag2 } — active weapon-mod +
    # missile/ammo selection.
    mun_start = br.pos
    munitions = []
    for _ in range(2):
        entry_start = br.pos
        entry = {
            "def_name": read_field(br, "str",
                                   br.read_cstring(max_len=_SHORT_NAME_MAX)),
            "flag1":    read_field(br, "u8", br.read_u8()),
            "flag2":    read_field(br, "u8", br.read_u8()),
        }
        br.last_read_start = entry_start
        munitions.append(entry)
    br.last_read_start = mun_start
    out["munitions"] = Variant("list", munitions, 0xff, (mun_start, br.pos))

    out["unknown_0x174"]      = read_field(br, "i32",  br.read_i32())
    out["unknown_0x178"]      = read_field(br, "u64",  br.read_u64())
    out["unknown_0x188"]      = read_field(br, "u32",  br.read_u32())
    out["unknown_0x18c"]      = read_field(br, "u32",  br.read_u32())
    out["rank"]               = read_field(br, "u8",   br.read_u8())
    out["durability"]         = read_field(br, "f32",  br.read_f32())
    out["unknown_0x198"]      = read_field(br, "u32",  br.read_u32())
    out["unknown_0x19c"]      = read_field(br, "u8",   br.read_u8())
    out["unknown_0x1a0"]      = read_field(br, "u64",  br.read_u64())
    out["unknown_0x14"]       = read_field(br, "u64",  br.read_u64())
    out["synergy"]            = read_field(br, "u32",  br.read_u32())
    out["unknown_flag_0x194"] = read_field(br, "bool", br.read_bool())
    out["unknown_iid_a"]      = read_field(br, "u64",  br.read_u64())
    out["unknown_iid_b"]      = read_field(br, "u64",  br.read_u64())
    out["special_module"]     = read_field(br, "str",
                                           br.read_cstring(max_len=_NAME_MAX))

    # 14 × { cstr60 def_name, u64 iid } — cosmetic decal / sticker slots.
    decals_start = br.pos
    decals = []
    for _ in range(14):
        e_start = br.pos
        entry = {
            "def_name": read_field(br, "str",
                                   br.read_cstring(max_len=_NAME_MAX)),
            "iid":      read_field(br, "u64", br.read_u64()),
        }
        br.last_read_start = e_start
        decals.append(entry)
    br.last_read_start = decals_start
    out["decals"] = Variant("list", decals, 0xff, (decals_start, br.pos))

    # 10 × cstr256 — ship stat-modifier def names.
    mods_start = br.pos
    modifiers = [
        read_field(br, "str", br.read_cstring(max_len=_LONG_NAME_MAX))
        for _ in range(10)
    ]
    br.last_read_start = mods_start
    out["modifiers"] = Variant("list", modifiers, 0xff,
                               (mods_start, br.pos))

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
