"""Bit-stream parser for `ac_lobby_info` (AC 0x90).

Sent S→C with the lobby's full state — id, name/level, location, the
member roster, plus a handful of strings + flags. Handler is at
0x0822b1c7, which dispatches to FUN_088f1690 (the body reader);
per-member rows are read by FUN_088efe80.

Wire format (in read order):

    u64v2  lobby_id
    cstrN  name              (≤ 250 bytes)
    u32    field_u32         (maybe owner uid / privacy flags)
    cstrN  level_def         (≤ 250 bytes — map/level def name)
    u8     a                 (game mode / gameplay id)
    u8     bot_count         (number of bots filling empty slots)
    u8     c
    u1     friendly_fire     (allow shooting allies)
    u1     self_fire         (allow your own rockets to damage you)
    u1×4   flag3..flag6
    f32    x                 (position / progress)
    f32    y
    u16v2  allowed_ship_roles  (bitmask — `ai.ShipRoleMask` in
                                 `scripts/ai/cosmos_constants.lua`. Bit i
                                 is set when the corresponding
                                 `ai.ShipRoles` role is allowed:
                                   0=NONE  1=ECM     2=SCOUT  3=RECON
                                   4=ATTACK 5=COMMAND 6=TACKLER 7=SNIPER
                                   8=GUARD 9=ENGINEER 10=OVERSEER
                                 0x0000 in most lobbies; 0x07fc and
                                 0x039e seen in `s1338_pandora_anomaly`.)
    u32    allowed_ship_ranks (bitmap of allowed ship ranks/tiers —
                                 bit i set ⇒ rank i allowed)
    u1     autobalance       (server auto-balances teams)
    u64v2  some_u64
    u8     num_members
    num_members × LobbyMember (FUN_088efe80):
        u64v2 uid               (member's user id)
        u64v2 cid               (member's clan id; 0 if not in a clan)
        u8    team              (0 = reserve, 1 = team 1, 2 = team 2)
        f32   weight
        u8    ship_slot_count
        ship_slot_count × u16v2  ship_slots
        u1    spectator_mode    (set when the member joined as spectator)
    cstrN  bot_preset          (≤ 250 bytes; e.g. 'BotsLobby1',
                                 'BotsLobby3' — picks which set of bots
                                 fill empty slots)
    cstrN  s2                  (empty in every observed capture)
    u1     esports             (esports/competitive ruleset toggle)
    u1     flag9
    cstrN  team1_dreadnought   (def name of team 1's chosen dreadnought)
    cstrN  team2_dreadnought   (def name of team 2's chosen dreadnought)
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field


_CSTR_MAX = 250

# Bit positions for ai.ShipRoles → ai.ShipRoleMask (from
# scripts/ai/cosmos_constants.lua). Used to decode the
# allowed_ship_roles bitmask into a readable list.
SHIP_ROLES = [
    "NONE", "ECM", "SCOUT", "RECON", "ATTACK", "COMMAND",
    "TACKLER", "SNIPER", "GUARD", "ENGINEER", "OVERSEER",
]


def decode_ship_role_mask(mask: int) -> str:
    """Render an `ai.ShipRoleMask` value as a comma-separated role list.

    `mask=0` → "(none)"; unknown high bits (>10) come back as `bit<n>`.
    """
    if mask == 0:
        return "(none)"
    names = []
    for bit in range(16):
        if mask & (1 << bit):
            names.append(SHIP_ROLES[bit] if bit < len(SHIP_ROLES)
                         else f"bit{bit}")
    return ",".join(names)


def decode_ship_rank_mask(mask: int) -> str:
    """Render the allowed_ship_ranks bitmap as a comma-separated rank list.

    SC ships have ranks 1..15 (mostly displayed as T1..T5 with sub-ranks).
    `mask=0` → "(none)"; unset top bits stay quiet.
    """
    if mask == 0:
        return "(none)"
    return ",".join(f"R{bit}" for bit in range(32) if mask & (1 << bit))


def _read_lobby_info(br: BitReader) -> dict:
    """Read one LobbyInfo record from an existing BitReader.

    Used by both AcLobbyInfoBody (which holds exactly one) and
    AcLobbyListBody (which holds `u32 count` of these back-to-back).
    Restores `br.last_read_start` to the lobby's start position so a
    wrapping `read_field(br, "struct", _read_lobby_info(br))` gets the
    full lobby's bit range.
    """
    start = br.pos
    out: dict[str, object] = {}
    out["lobby_id"]   = read_field(br, "u64", br.read_u64())
    out["name"]       = read_field(br, "str",
                                   br.read_cstring(max_len=_CSTR_MAX))
    out["field_u32"]  = read_field(br, "u32", br.read_u32())
    out["level_def"]  = read_field(br, "str",
                                   br.read_cstring(max_len=_CSTR_MAX))
    out["a"]            = read_field(br, "u8",   br.read_u8())
    out["bot_count"]    = read_field(br, "u8",   br.read_u8())
    out["c"]            = read_field(br, "u8",   br.read_u8())
    out["friendly_fire"] = read_field(br, "bool", br.read_bool())
    out["self_fire"]    = read_field(br, "bool", br.read_bool())
    out["flag3"]        = read_field(br, "bool", br.read_bool())
    out["flag4"]        = read_field(br, "bool", br.read_bool())
    out["flag5"]        = read_field(br, "bool", br.read_bool())
    out["flag6"]        = read_field(br, "bool", br.read_bool())
    out["x"]            = read_field(br, "f32",  br.read_f32())
    out["y"]            = read_field(br, "f32",  br.read_f32())
    asr = br.read_u16()
    out["allowed_ship_roles"] = read_field(
        br, "u16", asr,
        display=f"0x{asr:04x} ({decode_ship_role_mask(asr)})")
    asr_ranks = br.read_u32()
    out["allowed_ship_ranks"] = read_field(
        br, "u32", asr_ranks,
        display=f"0x{asr_ranks:08x} ({decode_ship_rank_mask(asr_ranks)})")
    out["autobalance"]  = read_field(br, "bool", br.read_bool())
    out["some_u64"]     = read_field(br, "u64",  br.read_u64())

    # Member array — u8 count + count × FUN_088efe80.
    members_start = br.pos
    out["num_members"] = read_field(br, "u8", br.read_u8())
    members: List[dict] = [
        _read_lobby_member(br) for _ in range(out["num_members"].value)
    ]
    br.last_read_start = members_start
    out["members"] = Variant("list", members, 0xff,
                             (members_start, br.pos))

    out["bot_preset"]        = read_field(br, "str",
                                          br.read_cstring(max_len=_CSTR_MAX))
    out["s2"]                = read_field(br, "str",
                                          br.read_cstring(max_len=_CSTR_MAX))
    out["esports"]           = read_field(br, "bool", br.read_bool())
    out["flag9"]             = read_field(br, "bool", br.read_bool())
    out["team1_dreadnought"] = read_field(br, "str",
                                          br.read_cstring(max_len=_CSTR_MAX))
    out["team2_dreadnought"] = read_field(br, "str",
                                          br.read_cstring(max_len=_CSTR_MAX))
    br.last_read_start = start
    return out


def _read_lobby_member(br: BitReader) -> dict:
    """FUN_088efe80 — one row of the member array.

    Wire shape: u64 + u64 + u8 + f32 + (u8 count + count×u16) + u1.
    Each field is wrapped via read_field() so the tree node carries its
    own bit_range for hex-pane highlighting.
    """
    start = br.pos
    out: dict[str, object] = {}
    out["uid"]     = read_field(br, "u64", br.read_u64())
    out["cid"]     = read_field(br, "u64", br.read_u64())
    out["team"]    = read_field(br, "u8",  br.read_u8())
    out["weight"]  = read_field(br, "f32", br.read_f32())
    out["ship_slot_count"] = read_field(br, "u8", br.read_u8())
    n = out["ship_slot_count"].value
    out["ship_slots"] = [read_field(br, "u16", br.read_u16())
                         for _ in range(n)]
    out["spectator_mode"] = read_field(br, "u1", br.read_bool())
    br.last_read_start = start
    return out


class AcLobbyInfoBody:
    """Decoded body of an `ac_lobby_info` async-request.

    Public attributes are Variants (from `read_field`) so each carries
    its own `bit_range` for the Qt UI's hex highlighting. Sub-bag-like
    aggregates (`members`) are plain lists of Variant-valued dicts —
    the tree builder derives their range as the union of children.
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
            fields = _read_lobby_info(br)
            # Unpack the shared reader's dict into instance attrs so the
            # existing repr/tree code keeps working unchanged.
            for k, v in fields.items():
                setattr(self, k, v)
            self.bits_consumed = br.pos
        except EOFError:
            # Short-form bodies (e.g. 16 B "no lobby" responses) are
            # expected and match the handler's lastReadOK tolerance —
            # stop cleanly and leave the tail unset.
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
            return f"AcLobbyInfoBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        parts: list[str] = [f"{len(self._raw)}B{suffix}"]
        # Render whatever fields were reached before EOF. Each is a
        # Variant from read_field, so `.value` is the unwrapped scalar.
        def _add(label: str, attr: str, fmt=repr) -> None:
            v = getattr(self, attr, None)
            if v is not None:
                parts.append(f"{label}={fmt(v.value)}")
        _add("id", "lobby_id", lambda n: f"0x{n:x}")
        _add("name", "name")
        _add("level_def", "level_def")
        for n in ("bot_count", "friendly_fire", "self_fire",
                  "autobalance", "esports"):
            if hasattr(self, n):
                parts.append(f"{n}={getattr(self, n).value}")
        extra_flags = [f"{n}={int(getattr(self, n).value)}"
                       for n in ("flag3", "flag4", "flag5", "flag6", "flag9")
                       if hasattr(self, n)]
        if extra_flags:
            parts.append("(" + ",".join(extra_flags) + ")")
        if hasattr(self, "x") and hasattr(self, "y"):
            parts.append(f"pos=({self.x.value:g}, {self.y.value:g})")
        if hasattr(self, "allowed_ship_roles"):
            v = self.allowed_ship_roles.value
            parts.append(
                f"allowed_ship_roles=0x{v:04x}({decode_ship_role_mask(v)})")
        if hasattr(self, "allowed_ship_ranks"):
            v = self.allowed_ship_ranks.value
            parts.append(
                f"allowed_ship_ranks=0x{v:08x}({decode_ship_rank_mask(v)})")
        if hasattr(self, "members"):
            parts.append(f"members={len(self.members.value)}")
        if hasattr(self, "bot_preset"):
            parts.append(f"bot_preset={self.bot_preset.value!r}")
        if hasattr(self, "s2"):
            parts.append(f"s2={self.s2.value!r}")
        for n in ("team1_dreadnought", "team2_dreadnought"):
            if hasattr(self, n):
                parts.append(f"{n}={getattr(self, n).value!r}")
        parts.append(f"slack={slack}b")
        return "AcLobbyInfoBody(" + ", ".join(parts) + ")"
