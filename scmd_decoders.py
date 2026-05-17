#!/usr/bin/env python3
"""The single dispatch point for decoding framed SCMD packets.

`decode_packet(pkt_type, body, direction)` is what the proxy calls for
every packet. It routes by scmd_pkt_type:

    0x0d  CSCMD_ASYNC_REQ   → kaitai (StarConflictPackage{Client,Server})
    0x0e  SCMD_NOTIFICATION → notification.decode (bag protocol)
    0x0f..0x26              → the DECODERS registry below
    anything else          → left opaque

Everything needed to name and decode a packet lives here: the
scmd_pkt_type → name table (`SCMD_NAMES` / `scmd_name`), the per-SCMD
struct decoders, and the async-req kaitai bridge. `proxy_util` only does
transport, logging and capture — it no longer carries decode logic.

Each entry in DECODERS maps an scmd_pkt_type to a function that takes the
raw body bytes and returns a representation suitable for logging. The
representation is formatted in-line via format_payload() — by default a
dict, but bag-shaped payloads are returned as Notification-like objects
with .bag so that notification.format_bag colours each variant by tag.

Coverage status (from MasterServerEndpoint::OnRecieve, switch cases at
0x08243f74 and earlier; sub-handlers at the addresses listed):

    pkt_type  name                              shape                 sub-handler
    --------  --------------------------------  --------------------  --------------
    0x0d (13) CSCMD_ASYNC_REQ                   u16 ac + body         ac_types + server.ksy
    0x0e (14) SCMD_NOTIFICATION                 u8 sn + bag           notification.py
    0x0f (15) SCMD_SQUAD_NOTIFICATION           u8 sub + struct       OnSquadNotification
                                                                       (0x08215fd0)
    0x10 (16) SCMD_SOCIAL_NOTIFICATION          u8 sub + u64          OnSocialNotification
                                                                       (0x0820b860)
    0x11 (17) SCMD_TEACH_NOTIFICATION           u8 sub + u64          OnTeachingNotification
                                                                       (0x0820bc30)
    0x12 (18) SCMD_CLAN_NOTIFICATION            u8 sub + u64×3 + u8   OnClanNotification
                                                                       (0x0820e420)
    0x13 (19) SCMD_USER_PROFILE_NOTIFICATION    u8 sub + u64 + struct OnUserProfileNotification
                                                                       (0x0832ed90)
    0x14 (20) SCMD_QUEST_NOTIFICATION           u8 sub + struct       inline; partial
    0x15 (21) SCMD_LEAGUE_NOTIFICATION          u8 sub + u64×2 + …    OnLeagueNotification
                                                                       (0x08202f90)
    0x16 (22) SCMD_VESSEL_NOTIFICATION          u8 sub + struct       OnVesselNotification
                                                                       (0x08212ca0)
    0x17 (23) SCMD_LOBBY_NOTIFICATION           u8 sub + struct       OnLobbyNotification
                                                                       (0x082184d0)
    0x18 (24) SCMD_KEEP_ALIVE                   u64 timestamp         full
    0x1b (27) SCMD_DOCK_SPACE_STATION           u8 sub + struct       partial
    0x1c (28) SCMD_FREE_SPACE_DEBRIEFING        u1 docked + bag       full
    0x20 (32) SCMD_REWARD_SCHEDULE              bag                   full
    0x21 (33) SCMD_PVE_SCHEDULE                 bag                   full
    0x25 (37) SCMD_ADVENTURE_NOTIFICATION       u8 sub + struct       partial (sub byte)
    0x26 (38) SCMD_REPLACE_CHAT_MSG             u64 + u8              full
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable

from ac_types import pkt_type_name
from sn_types import sn_name
from notification import (BitReader, Variant, _read_bag, format_bag,
                          decode as decode_notification,
                          format_issues, _RED, _RESET)
from star_conflict_package_client import StarConflictPackageClient
from star_conflict_package_server import StarConflictPackageServer
from kaitaistruct import KaitaiStream, BytesIO


# ── scmd_pkt_type → name ─────────────────────────────────────────────────────
# Mirrors the binary's table at VMA 0x08fe7ac0. See
# Documentation/SCMD-protocol.md for the full mapping and how this differs
# from the wire send_counter.
SCMD_NAMES = [
    "SCMD_ASSIGNED_SHARD", "SCMD_LB_QUEUE_INFO", "SCMD_LB_CVARS",
    "SCMD_AUTH_REQ", "CCMD_AUTH_REQUEST", "SCMD_AUTH_ACK",
    "SCMD_STEAM_NOT_ATTACHED", "SCMD_ARC_NOT_ATTACHED", "CCMD_STORE",
    "SCMD_STORE", "SCMD_STORE_SPOILED", "SCMD_CONNECT_DEDICATED_SERVER",
    "SCMD_GAME_ENDED", "CSCMD_ASYNC_REQ", "SCMD_NOTIFICATION",
    "SCMD_SQUAD_NOTIFICATION", "SCMD_SOCIAL_NOTIFICATION",
    "SCMD_TEACH_NOTIFICATION", "SCMD_CLAN_NOTIFICATION",
    "SCMD_USER_PROFILE_NOTIFICATION", "SCMD_QUEST_NOTIFICATION",
    "SCMD_LEAGUE_NOTIFICATION", "SCMD_VESSEL_NOTIFICATION",
    "SCMD_LOBBY_NOTIFICATION", "SCMD_KEEP_ALIVE", "SCMD_BAN_INFO",
    "SCMD_WELCOME_MSG", "SCMD_DOCK_SPACE_STATION",
    "SCMD_FREE_SPACE_DEBRIEFING", "SCMD_NEW_MOTD",
    "SCMD_TOURNAMENT_TEAMS_INFO", "SCMD_BRAWL_SCHEDULE",
    "SCMD_REWARD_SCHEDULE", "SCMD_PVE_SCHEDULE",
    "SCMD_LEAGUE_FORBIDDEN_EQUIPMENT", "SCMD_BATTLE_PASS_ACTIVATION",
    "SCMD_ZONES_WITH_DISABLED_QUESTS", "SCMD_ADVENTURE_NOTIFICATION",
    "SCMD_REPLACE_CHAT_MSG",
]


def scmd_name(pkt_type: int) -> str:
    """scmd_pkt_type → symbolic name, or `?<n>` if out of range."""
    if 0 <= pkt_type < len(SCMD_NAMES):
        return SCMD_NAMES[pkt_type]
    return f"?{pkt_type}"


@dataclass
class ScmdPayload:
    """Container for a decoded non-notification SCMD body. Has a .bag dict
    so the existing format_bag() colourer renders it identically."""
    name: str
    bag: dict


def _kv(tag: str, val: Any, br: BitReader | None = None) -> Variant:
    """Wrap a directly-read scalar so format_bag() can colour it.

    `tag` is the wire-level type at the bit position read (u8/u16/u32/u64/u1
    /str/bag/...) — *not* a bag-variant tag, since these decoders read raw
    bit-stream fields, not bag entries. We reuse the Variant container
    purely for the colour-aware repr; itag=0xff signals "no on-wire
    variant tag byte" (this field was a direct read).

    When `br` is given, the Variant is annotated with the (start, end)
    bit range of the value's wire bytes (read from `br.last_read_start`
    + `br.pos`) so the Qt UI can highlight the matching hex bytes.
    """
    rng = (br.last_read_start, br.pos) if br is not None else None
    return Variant(tag, val, 0xff, rng)


# ── Per-SCMD decoders ────────────────────────────────────────────────────────

def _scmd_keep_alive(body: bytes) -> ScmdPayload:
    """0x18: u64 client_timestamp_ms (echoed by client to compute RTT).

    Source: case 0x18 of OnRecieve. Reads u64, computes
        rtt = current_time_ms - timestamp.
    """
    br = BitReader(body)
    return ScmdPayload("SCMD_KEEP_ALIVE",
                       {"timestamp_ms": _kv("u64", br.read_u64(), br)})


def _scmd_free_space_debriefing(body: bytes) -> ScmdPayload:
    """0x1c: u1 docked + property bag.

    Source: case 0x1c. Reads `cVar15 = ReadBit()`, deserialises bag, then
    augments the bag with `{"docked": cVar15}` before dispatching to UI.
    """
    br = BitReader(body)
    docked_kv = _kv("bool", br.read_bool(), br)   # capture range NOW
    bag = _read_bag(br)
    bag = {"docked": docked_kv, **bag}
    return ScmdPayload("SCMD_FREE_SPACE_DEBRIEFING", bag)


def _scmd_reward_schedule(body: bytes) -> ScmdPayload:
    """0x20: pure property bag (deserialised into a member at +0xb84c0)."""
    br = BitReader(body)
    return ScmdPayload("SCMD_REWARD_SCHEDULE", _read_bag(br))


def _scmd_pve_schedule(body: bytes) -> ScmdPayload:
    """0x21: pure property bag (deserialised into a member at +0xb84d4)."""
    br = BitReader(body)
    return ScmdPayload("SCMD_PVE_SCHEDULE", _read_bag(br))


def _scmd_dock_space_station(body: bytes) -> ScmdPayload:
    """0x1b: u8 status + u32 zone_id + u1 dock_flag + u1 freespace_flag.

    Source: case 0x1b. status=0 success path uses zone_id+flags.
    """
    br = BitReader(body)
    return ScmdPayload("SCMD_DOCK_SPACE_STATION", {
        "status":         _kv("i32",  br.read_u8(),   br),
        "zone_id":        _kv("i32",  br.read_u32(),  br),
        "dock_flag":      _kv("bool", br.read_bool(), br),
        "freespace_flag": _kv("bool", br.read_bool(), br),
    })


def _scmd_replace_chat_msg(body: bytes) -> ScmdPayload:
    """0x26: u64 chat_msg_id + u8 flag (synthesised into a 2-entry bag for UI).

    Source: case 0x26.
    """
    br = BitReader(body)
    return ScmdPayload("SCMD_REPLACE_CHAT_MSG", {
        "chat_msg_id": _kv("u64", br.read_u64(), br),
        "flag":        _kv("i32", br.read_u8(),  br),
    })


def _scmd_squad_notification(body: bytes) -> ScmdPayload:
    """0x0f: u8 sqn_type + per-sub-type struct.

    Source: OnSquadNotification (0x08215fd0). 0x24 sub-types observed:

      0   u64 squad_id, u64 leader_uid, [u64 invitee_or_new_leader]
      1   u64 squad_id, u64 leader_uid (or 0 = clear)
      2   u64 squad_id, u64 joining_uid                       — JOIN
      3   u64 squad_id, u64 leaving_uid                       — LEAVE
      4   u64 squad_id, u64 kicker_uid, u64 kickee_uid        — KICK
      5-8 u64 squad_id, u64 uid, u64 rcType                   — READY CHANGE
      9   u1  done_flag, u64 uid                              — MM start
      10  u1  done_flag, u64 uid, u8 result, u8 minRank,
          u8 maxRank, u8 accountRank, u8 maxHighestSquadRank
          • result=='"' (0x22): + u8 minHighestSquadRank
          • result=='-' (0x2d): + bag badLeagueEquipment,
                                + bag badLeagueAutogenEquipment
          • result=='0' (0x30): + u64 leaverBanTill
      11/12  u1 done_flag                                     — MM cancel
      0x0d/0x20  u8 reason
      0x0e/0x21  u64 uid
      0x22  u64 squad_id, u64 uid
      0x23  u64 squad_id, u64 uid
      0xf-0x1f (gap): no payload
    """
    br = BitReader(body)
    out: dict = {"sqn_type": _kv("u8", br.read_u8(), br)}
    sub = out["sqn_type"].value
    try:
        if sub == 0:
            out["squad_id"]  = _kv("u64", br.read_u64(), br)
            out["leader_uid"] = _kv("u64", br.read_u64(), br)
            if br.remaining() >= 64:
                out["invitee_or_new_leader"] = _kv("u64", br.read_u64(), br)
        elif sub == 1:
            out["squad_id"]   = _kv("u64", br.read_u64(), br)
            out["leader_uid"] = _kv("u64", br.read_u64(), br)
        elif sub == 2:
            out["squad_id"]    = _kv("u64", br.read_u64(), br)
            out["joining_uid"] = _kv("u64", br.read_u64(), br)
        elif sub == 3:
            out["squad_id"]    = _kv("u64", br.read_u64(), br)
            out["leaving_uid"] = _kv("u64", br.read_u64(), br)
        elif sub == 4:
            out["squad_id"]   = _kv("u64", br.read_u64(), br)
            out["kicker_uid"] = _kv("u64", br.read_u64(), br)
            out["kickee_uid"] = _kv("u64", br.read_u64(), br)
        elif sub in (5, 6, 7, 8):
            out["squad_id"] = _kv("u64", br.read_u64(), br)
            out["uid"]      = _kv("u64", br.read_u64(), br)
            out["rcType"]   = _kv("u64", br.read_u64(), br)
        elif sub == 9:
            out["done_flag"] = _kv("u1", br.read_bool(), br)
            out["uid"]       = _kv("u64", br.read_u64(), br)
        elif sub == 10:
            out["done_flag"]            = _kv("u1", br.read_bool(), br)
            out["uid"]                  = _kv("u64", br.read_u64(), br)
            out["result"]               = _kv("u8", br.read_u8(), br)
            result                      = out["result"].value
            out["minRank"]              = _kv("u8", br.read_u8(), br)
            out["maxRank"]              = _kv("u8", br.read_u8(), br)
            out["accountRank"]          = _kv("u8", br.read_u8(), br)
            out["maxHighestSquadRank"]  = _kv("u8", br.read_u8(), br)
            if result == 0x22:    # '"'
                out["minHighestSquadRank"] = _kv("u8", br.read_u8(), br)
            elif result == 0x2d:  # '-'
                out["badLeagueEquipment"]        = _kv("bag", _read_bag(br), br)
                out["badLeagueAutogenEquipment"] = _kv("bag", _read_bag(br), br)
            elif result == 0x30:  # '0'
                out["leaverBanTill"] = _kv("u64", br.read_u64(), br)
        elif sub in (0x0b, 0x0c):
            out["done_flag"] = _kv("u1", br.read_bool(), br)
        elif sub in (0x0d, 0x20):
            out["reason"] = _kv("u8", br.read_u8(), br)
        elif sub in (0x0e, 0x21):
            out["uid"] = _kv("u64", br.read_u64(), br)
        elif sub in (0x22, 0x23):
            out["squad_id"] = _kv("u64", br.read_u64(), br)
            out["uid"]      = _kv("u64", br.read_u64(), br)
        # 0xf..0x1f (excluding above): no payload
    except EOFError:
        out["_truncated"] = _kv("?", True)
    return ScmdPayload("SCMD_SQUAD_NOTIFICATION", out)


def _scmd_social_notification(body: bytes) -> ScmdPayload:
    """0x10: u8 soc_type + u64 uid.

    Source: OnSocialNotification (0x0820b860). All sub-types share the
    same 9-byte payload; only the C++ side reaction differs (add/remove
    friend/ignore/watch entry).

      0  add_friend     1  remove_friend
      2  ignore_add     3  ignore_remove
      4  watch_add      5  watch_remove
      6/7  no-op
    """
    br = BitReader(body)
    return ScmdPayload("SCMD_SOCIAL_NOTIFICATION", {
        "soc_type": _kv("u8",  br.read_u8(),  br),
        "uid":      _kv("u64", br.read_u64(), br),
    })


def _scmd_teaching_notification(body: bytes) -> ScmdPayload:
    """0x11: u8 cmd + u64 uid + (cmd=8 only) i32 expReward.

    Source: OnTeachingNotification (0x0820bc30).

      0  request to teacher                  uid
      1  request to student                  uid
      2  accept                              uid
      3  reject                              uid
      4  check                               uid
      5  allow                               uid
      6  cancel                              uid
      7  finish                              uid
      8  reward                              uid + i32 expReward
      9  list refresh                        no extra
      10 reset                               no extra
      11 unknown                             uid
    """
    br = BitReader(body)
    out: dict = {"command": _kv("u8", br.read_u8(), br)}
    sub = out["command"].value
    if sub in (9, 10):
        return ScmdPayload("SCMD_TEACH_NOTIFICATION", out)
    out["uid"] = _kv("u64", br.read_u64(), br)
    if sub == 8:
        out["expReward"] = _kv("i32", br.read_i32(), br)
    return ScmdPayload("SCMD_TEACH_NOTIFICATION", out)


def _scmd_clan_notification(body: bytes) -> ScmdPayload:
    """0x12: u8 cmd + u64 field_1 + u64 field_2 + u64 field_3 + u8 field_4.

    Source: OnClanNotification (0x0820e420). The 30-byte prologue is
    fixed; the cmd dispatches to per-cmd handlers that mostly just call
    methods on the in-memory clan struct (no further wire reads). A few
    cmds read additional fields:

      cmd 0x19  + u32                    (cs.clanItemKeys delta?)
      cmd 0x1a  + cstring(<=251 bytes)   (cs.changedItemKey, length-bounded)

    Field semantics depend on cmd; the bag synthesised for Lua names them
    "field_1".."field_4" generically, so we mirror that here.
    """
    br = BitReader(body)
    out: dict = {
        "clan_cmd": _kv("u8",  br.read_u8(),  br),
        "field_1":  _kv("u64", br.read_u64(), br),
        "field_2":  _kv("u64", br.read_u64(), br),
        "field_3":  _kv("u64", br.read_u64(), br),
        "field_4":  _kv("u8",  br.read_u8(),  br),
    }
    cmd = out["clan_cmd"].value
    try:
        if cmd == 0x19:
            out["extra_u32"] = _kv("u32", br.read_u32(), br)
        elif cmd == 0x1a:
            out["extra_cstring"] = _kv("str", br.read_cstring(max_len=251), br)
    except EOFError:
        out["_truncated"] = _kv("?", True)
    return ScmdPayload("SCMD_CLAN_NOTIFICATION", out)


def _scmd_user_profile_notification(body: bytes) -> ScmdPayload:
    """0x13: u8 upn_type + u64 uid + per-sub-type struct.

    Source: OnUserProfileNotification (0x0832ed90). The on-wire sub-id
    is NOT the lua-side UserProfileField (UPF_*) — the C++ side maps
    each case to a UPF_* before invoking lua's
    MasterServer_OnUserProfileUpdate(result, requestId, uid, UPF_*).
    Cross-referenced via Ghidra:

      sub  payload                              → lua UPF_*
      ---  -------------------------------------  ------------------
      0    u8 state                              UPF_STATE        (0)
      1    u16 ach_id + u32 old + u32 new        UPF_ACHIEVEMENTS (4)
                                                 (progress delta)
      2    u16 ach_id + u8 stage + u64 ts_ms     UPF_ACHIEVEMENTS (4)
                                                 (unlock event)
      3    u16 title_id                          UPF_TITLES       (6)
      4    cstring + (cstring + u16 + N×cstr)    UPF_AVATARS      (7)
      5    cstring + (cstring + u16 + N×cstr)    UPF_MOTTOS       (8)
      6    i32 accountExpPool                    UPF_ATLAS        (9)
      7    Atlas_Deserialize struct              UPF_ATLAS        (9)

    Sub=6 and sub=7 both update the same lua field (profile.atlas).
    Sub=6 is a fast path that only updates accountExpPool (the i32
    that's displayed in-game as "Clearance Score"). Sub=7 reloads the
    full atlas.

    Atlas struct (44 bytes — see Atlas_Deserialize at 0x088c0ce0,
    Atlas_PushToLua at 0x088c06c0):
      i32  accountExpPool        (signed; lua exposes as i64)
      bag  modules              (key=tier-group index;
                                  u64 value packs 21×3-bit module
                                  ranks per tier — see
                                  AtlasModules_PackedToLua at 0x088bfc20)
      bag  vesselsProgress       (per-vessel research)

    The 0x9249249249249249-style pattern observed in modules-bag values
    is fully-maxed adjacent modules: each rank=4 packs as `100`, so
    every 3-bit chunk reads `100` → repeating 0x9249.
    """
    br = BitReader(body)
    out: dict = {
        "upn_type": _kv("u8",  br.read_u8(),  br),
        "uid":      _kv("u64", br.read_u64(), br),
    }
    sub = out["upn_type"].value
    try:
        if sub == 0:        # state byte
            out["state"] = _kv("u8", br.read_u8(), br)
        elif sub == 1:      # achievement progress delta
            out["achievement_id"] = _kv("u16", br.read_u16(), br)
            out["old_value"]      = _kv("u32", br.read_u32(), br)
            out["new_value"]      = _kv("u32", br.read_u32(), br)
        elif sub == 2:      # achievement unlock
            out["achievement_id"] = _kv("u16", br.read_u16(), br)
            out["stage"]          = _kv("u8",  br.read_u8(), br)
            out["unlock_time_ms"] = _kv("u64", br.read_u64(), br)
        elif sub == 3:      # u16 (uncaptured)
            out["v16"] = _kv("u16", br.read_u16(), br)
        elif sub == 4:      # avatar unlock (+ optional current + full list)
            out["unlocked_avatar"] = _kv("str", br.read_cstring(max_len=60), br)
            # Tail (FUN_08919100) is only emitted when the profile already
            # has an avatars list — server-side state we can't see. Detect
            # by checking that there's room for at least cstring + u16.
            if br.remaining() >= 8 + 16:
                out["current_avatar"] = _kv("str",
                    br.read_cstring(max_len=60), br)
                out["unlocked_count"] = _kv("u16", br.read_u16(), br)
                n = out["unlocked_count"].value
                for i in range(n):
                    out[f"unlocked[{i}]"] = _kv("str",
                        br.read_cstring(max_len=60), br)
        elif sub == 5:      # cstring (uncaptured — possibly motto)
            out["text"] = _kv("str", br.read_cstring(max_len=60), br)
        elif sub == 6:      # accountExpPool fast-path (i32 only)
            out["accountExpPool"] = _kv("i32", br.read_i32(), br)
        elif sub == 7:      # full atlas reload (Atlas_Deserialize)
            out["accountExpPool"] = _kv("i32", br.read_i32(), br)
            if not br.read_bool():
                # modules bag: key=tier-group, value=u64 packing
                # 21 × 3-bit module ranks (see Atlas_PushToLua).
                out["modules"] = _kv("bag", _read_bag(br), br)
            if br.remaining() >= 1 and not br.read_bool():
                # vesselsProgress bag (per-vessel research data;
                # not observed populated in captures so far).
                out["vesselsProgress"] = _kv("bag", _read_bag(br), br)
    except EOFError:
        out["_truncated"] = _kv("?", True)
    return ScmdPayload("SCMD_USER_PROFILE_NOTIFICATION", out)


def _scmd_league_notification(body: bytes) -> ScmdPayload:
    """0x15: u8 cmd + u64 league_id + u64 team_id + per-sub-type struct.

    Source: OnLeagueNotification (0x08202f90).

      0  u64 ext       (set ext)
      1  u64 ext       (leave league)
      2  u64 ext       (kick member)
      3  u64 ext, u8 flag                            (kick + flag)
      4/5  u64 invitee_uid                           (invite recv/cancel)
      6  no extra                                    (clear)
      7  f32 X, u32 Y, u32 Z                          (stats?)
      8  u1 flag                                     (toggle)
    """
    br = BitReader(body)
    out: dict = {
        "league_cmd": _kv("u8",  br.read_u8(),  br),
        "league_id":  _kv("u64", br.read_u64(), br),
        "team_id":    _kv("u64", br.read_u64(), br),
    }
    sub = out["league_cmd"].value
    try:
        if sub in (0, 1, 2):
            out["ext"] = _kv("u64", br.read_u64(), br)
        elif sub == 3:
            out["ext"]  = _kv("u64", br.read_u64(), br)
            out["flag"] = _kv("u8",  br.read_u8(),  br)
        elif sub in (4, 5):
            out["invitee_uid"] = _kv("u64", br.read_u64(), br)
        elif sub == 6:
            pass  # no extra
        elif sub == 7:
            out["f32_x"] = _kv("f32", br.read_f32(), br)
            out["u32_y"] = _kv("u32", br.read_u32(), br)
            out["u32_z"] = _kv("u32", br.read_u32(), br)
        elif sub == 8:
            out["flag"] = _kv("u1", br.read_bool(), br)
    except EOFError:
        out["_truncated"] = _kv("?", True)
    return ScmdPayload("SCMD_LEAGUE_NOTIFICATION", out)


def _scmd_vessel_notification(body: bytes) -> ScmdPayload:
    """0x16: u8 vssln_type + per-sub-type struct.

    Source: OnVesselNotification (0x08212ca0).

      0   complex vessel record (FUN_08925ae0 reads ~70 fields incl.
          floats, strings, ids — see in-memory layout starting at +0x178)
      1   u64 vid                              — vessel changed/repaired
      2   f32 prestige
      3   u64 vid, u64 quest_state, u8 count, then per-i (count×):
                u64 sub_vid                    — quest progress array
      4   u64 vid                              — quest reset
      5   u8 count, then per-i (count×):
                u64 vid, f32 hp, u32 stat,
                u8 flags                       — vessel-status batch
      6   u64 vid, u64 mod_mask, u8 flags      — module presence delta
      7   u64 vid, u8 flags                    — battle slot flag clear
      8   u64 vid, u8 flags                    — battle slot flag set
      9   u64 vid, u32 stat                    — stat update
      10  u64 vid, f32 hp                      — hp/shield update
      11  u64 vid, u8 misc                     — generic byte
      12  u64 vid, u64 budget, u64 boost       — clan ship budget
      13  u64 vid, u8 level, u32 budget,
          u1 was_repaired                      — budget level/repair flag
    """
    br = BitReader(body)
    out: dict = {"vssln_type": _kv("u8", br.read_u8(), br)}
    sub = out["vssln_type"].value
    try:
        if sub == 0:
            out["_vessel_record_bytes"] = _kv("?", br.remaining())
        elif sub == 1:
            out["vid"] = _kv("u64", br.read_u64(), br)
        elif sub == 2:
            out["prestige"] = _kv("f32", br.read_f32(), br)
        elif sub == 3:
            out["vid"]         = _kv("u64", br.read_u64(), br)
            out["quest_state"] = _kv("u64", br.read_u64(), br)
            out["count"]       = _kv("u8",  br.read_u8(), br)
            count = out["count"].value
            for i in range(count):
                out[f"sub_vid_{i}"] = _kv("u64", br.read_u64(), br)
        elif sub == 4:
            out["vid"] = _kv("u64", br.read_u64(), br)
        elif sub == 5:
            out["count"] = _kv("u8", br.read_u8(), br)
            count = out["count"].value
            for i in range(count):
                out[f"vid_{i}"]   = _kv("u64", br.read_u64(), br)
                out[f"hp_{i}"]    = _kv("f32", br.read_f32(), br)
                out[f"stat_{i}"]  = _kv("u32", br.read_u32(), br)
                out[f"flags_{i}"] = _kv("u8",  br.read_u8(),  br)
        elif sub == 6:
            out["vid"]      = _kv("u64", br.read_u64(), br)
            out["mod_mask"] = _kv("u64", br.read_u64(), br)
            out["flags"]    = _kv("u8",  br.read_u8(),  br)
        elif sub in (7, 8, 11):
            out["vid"]   = _kv("u64", br.read_u64(), br)
            out["flags"] = _kv("u8",  br.read_u8(),  br)
        elif sub == 9:
            out["vid"]  = _kv("u64", br.read_u64(), br)
            out["stat"] = _kv("u32", br.read_u32(), br)
        elif sub == 10:
            out["vid"] = _kv("u64", br.read_u64(), br)
            out["hp"]  = _kv("f32", br.read_f32(), br)
        elif sub == 12:
            out["vid"]    = _kv("u64", br.read_u64(), br)
            out["budget"] = _kv("u64", br.read_u64(), br)
            out["boost"]  = _kv("u64", br.read_u64(), br)
        elif sub == 13:
            out["vid"]            = _kv("u64", br.read_u64(), br)
            out["level"]          = _kv("u8",  br.read_u8(),  br)
            out["repair_budget"]  = _kv("u32", br.read_u32(), br)
            out["was_repaired"]   = _kv("u1",  br.read_bool(), br)
    except EOFError:
        out["_truncated"] = _kv("?", True)
    return ScmdPayload("SCMD_VESSEL_NOTIFICATION", out)


def _scmd_lobby_notification(body: bytes) -> ScmdPayload:
    """0x17: u8 lbn_type + per-sub-type struct.

    Source: OnLobbyNotification (0x082184d0).

      0  bag {uid: u64, ?: str}     — generic lobby event with text
      1  u32 lobby_id, u32 ready_flag
      2  u32 lobby_id, u32 op       (op=2 = participant added; else removed)
      3  u32 lobby_id, u32 incdec   (incdec=0 = decrement counter; else inc)
    """
    br = BitReader(body)
    out: dict = {"lbn_type": _kv("u8", br.read_u8(), br)}
    sub = out["lbn_type"].value
    try:
        if sub == 0:
            out["bag"] = _kv("bag", _read_bag(br), br)
        elif sub in (1, 2, 3):
            out["lobby_id"] = _kv("u32", br.read_u32(), br)
            out["arg"]      = _kv("u32", br.read_u32(), br)
    except EOFError:
        out["_truncated"] = _kv("?", True)
    return ScmdPayload("SCMD_LOBBY_NOTIFICATION", out)


def _scmd_quest_notification(body: bytes) -> ScmdPayload:
    """0x14: u8 sub_type + per-sub-type struct.

    Source: case 0x14. Sub-types observed include 0x01 (quest accepted with
    quest_id u16, ship_id u16, state u64-or-sentinel, etc.). Full struct
    layout for each subtype not modelled — only the sub-type byte is
    decoded here so the proxy log shows which kind it is.
    """
    br = BitReader(body)
    return ScmdPayload("SCMD_QUEST_NOTIFICATION", {
        "sub_type":        _kv("u8", br.read_u8(), br),
        "_remaining_bits": _kv("?", br.remaining()),
    })


def _scmd_adventure_notification(body: bytes) -> ScmdPayload:
    """0x25: u8 sub_type + per-sub-type struct.

    Source: case 0x25. Four sub-cases:
      0  → u64 + bag + u64           (adventure progress?)
      1  → u64 + u8 + u32            (state change)
      2  → u64 + u8                  (ack)
      3  → u64 + u8 + u16 + ...      (extended)
    Only the sub-type byte is decoded here.
    """
    br = BitReader(body)
    return ScmdPayload("SCMD_ADVENTURE_NOTIFICATION", {
        "sub_type":        _kv("u8", br.read_u8(), br),
        "_remaining_bits": _kv("?", br.remaining()),
    })


# ── Dispatch ──────────────────────────────────────────────────────────────────

DECODERS: dict[int, Callable[[bytes], ScmdPayload]] = {
    0x0f: _scmd_squad_notification,
    0x10: _scmd_social_notification,
    0x11: _scmd_teaching_notification,
    0x12: _scmd_clan_notification,
    0x13: _scmd_user_profile_notification,
    0x14: _scmd_quest_notification,
    0x15: _scmd_league_notification,
    0x16: _scmd_vessel_notification,
    0x17: _scmd_lobby_notification,
    0x18: _scmd_keep_alive,
    0x1b: _scmd_dock_space_station,
    0x1c: _scmd_free_space_debriefing,
    0x20: _scmd_reward_schedule,
    0x21: _scmd_pve_schedule,
    0x25: _scmd_adventure_notification,
    0x26: _scmd_replace_chat_msg,
}


def decode(pkt_type: int, body: bytes) -> ScmdPayload | None:
    """Dispatch to a per-SCMD decoder. Returns None if no decoder is
    registered (caller should leave the body opaque)."""
    fn = DECODERS.get(pkt_type)
    if fn is None:
        return None
    return fn(body)


def format_payload(payload: ScmdPayload) -> str:
    """Render a decoded SCMD payload using the same colour scheme as
    notification.format_bag, prefixed with the SCMD name."""
    return f"{payload.name} {format_bag(payload.bag)}"


# ── CSCMD_ASYNC_REQ (0x0d) — kaitai bridge ────────────────────────────────────

def _kaitai_repr(obj) -> str:
    """Render the non-private fields of a KaitaiStruct as key=value pairs.

    Opaque types (e.g. BagPayload, AcLoadInitialPlayerDataBody) define their
    own __repr__ — defer to it instead of walking __dict__ blindly, otherwise
    placeholder/None attributes pre-set for failure paths leak out as noise.
    """
    if not hasattr(obj, '__dict__'):
        return repr(obj)
    # If the value's class has a custom __repr__ (not the bare object default),
    # trust it — opaque types use this to filter out None placeholders.
    if type(obj).__repr__ is not object.__repr__:
        return repr(obj)
    fields = {k: v for k, v in obj.__dict__.items()
              if not k.startswith('_') and k != 'dummy'}
    if not fields:
        return ""
    parts = []
    for k, v in fields.items():
        if v is None:
            continue
        if isinstance(v, (bytes, bytearray)):
            parts.append(f"{k}={v.hex()}")
        elif isinstance(v, list):
            parts.append(f"{k}=[{', '.join(_kaitai_repr(i) for i in v)}]")
        elif hasattr(v, '__dict__') and hasattr(v, '_io'):
            parts.append(f"{k}=({_kaitai_repr(v)})")
        else:
            parts.append(f"{k}={v!r}")
    return " ".join(parts)


def _decode_async_req(body: bytes, direction: str) -> tuple[str, bool]:
    """Decode a CSCMD_ASYNC_REQ body via the generated kaitai schema.

    `direction` ("C→S" / "S→C") selects the client vs server schema.
    Returns (detail, ok) — detail has a leading space so it can be
    appended straight onto a log line.
    """
    try:
        if direction == "C→S":
            parsed = StarConflictPackageClient(KaitaiStream(BytesIO(body)))
        else:
            parsed = StarConflictPackageServer(KaitaiStream(BytesIO(body)))
        name = type(parsed.body).__name__
        detail = _kaitai_repr(parsed.body)
        return f" [{name}{': ' + detail if detail else ''}]", bool(detail)
    except Exception as e:
        return f" [{e}]", False


# ── Unified dispatch ──────────────────────────────────────────────────────────

@dataclass
class DecodedPacket:
    """Result of dispatching one framed packet through decode_packet().

    `detail` is ready to append to a log line — it carries a leading
    space and any embedded ANSI colour from the bag/struct formatters.
    `sub_id` / `sub_name` are the AC index (CSCMD_ASYNC_REQ) or SN id
    (SCMD_NOTIFICATION); both are None for packet types that have neither.
    `ok` is False when decoding failed or the payload flagged issues.
    """
    pkt_type: int
    pkt_name: str
    detail: str = ""
    ok: bool = True
    sub_id: int | None = None
    sub_name: str | None = None


def decode_packet(pkt_type: int, body: bytes, direction: str) -> DecodedPacket:
    """Decode one framed SCMD packet — the single entry point the proxy uses.

    Routes SCMD_NOTIFICATION through notification.decode, CSCMD_ASYNC_REQ
    through the kaitai schema, and 0x0f..0x26 through the DECODERS registry.
    Any other packet type is left opaque (empty detail, ok=True).
    """
    out = DecodedPacket(pkt_type=pkt_type, pkt_name=scmd_name(pkt_type))

    if out.pkt_name == "SCMD_NOTIFICATION" and body:
        out.sub_id = body[0]
        out.sub_name = sn_name(out.sub_id)
        out.detail = f" sn=0x{out.sub_id:02x}({out.sub_name})"
        try:
            n = decode_notification(body)
            out.detail += f" {format_bag(n.bag)}{format_issues(n.validate())}"
            if n.validate():
                out.ok = False  # so the line as a whole reads as a fault
        except Exception as e:
            out.detail += f" {_RED}[decode_err: {type(e).__name__}: {e}]{_RESET}"
            out.ok = False
        return out

    if pkt_type in DECODERS and body:
        try:
            out.detail = " " + format_payload(decode(pkt_type, body))
        except Exception as e:
            out.detail = f" {_RED}[decode_err: {type(e).__name__}: {e}]{_RESET}"
            out.ok = False
        return out

    if out.pkt_name == "CSCMD_ASYNC_REQ":
        if len(body) >= 2:
            out.sub_id = int.from_bytes(body[:2], "big")
            out.sub_name = pkt_type_name(out.sub_id)
        out.detail, out.ok = _decode_async_req(body, direction)
        return out

    return out


# ── Structured decode (tree view) ─────────────────────────────────────────────

@dataclass
class DecodeNode:
    """One node in the structured decode tree the UI renders.

    `value` is the rendered scalar ("" for pure branches); `wire_type`
    is the on-wire type tag (u64/str/bag/…), "struct"/"bytes" for
    composite values, "error" for a failed decode, or "" when not
    applicable. `children` are nested fields. `bit_range` (when set) is
    the (start_bit, end_bit_exclusive) span in the packet's body bytes
    — the UI uses it to highlight the matching hex in the side pane.
    """
    name: str
    value: str = ""
    wire_type: str = ""
    children: list["DecodeNode"] = field(default_factory=list)
    bit_range: tuple[int, int] | None = None


_BYTES_PREVIEW = 64  # how many bytes of a blob to show inline before eliding


def _struct_attrs(value: Any) -> list[tuple[str, Any]] | None:
    """Public (name, value) attributes of an object, or None if `value`
    isn't a walkable struct.

    Handles both __dict__ objects (generated kaitai classes) and
    __slots__ objects (the hand-written opaque types — BagPayload,
    PrefixedBagPayload, …). Skips private/dummy attrs and None
    placeholders that opaque types pre-set on their failure paths.
    """
    if hasattr(value, "__dict__"):
        raw: Any = vars(value).items()
    else:
        names: list[str] = []
        for klass in type(value).__mro__:
            names.extend(getattr(klass, "__slots__", ()))
        if not names:
            return None
        raw = ((n, getattr(value, n, None)) for n in names)
    return [(k, v) for k, v in raw
            if not k.startswith("_") and k != "dummy" and v is not None]


def _union_ranges(children: list[DecodeNode]) -> tuple[int, int] | None:
    """Smallest range that covers every child's range. Used so a parent
    node (a plain dict / list / struct that didn't itself carry a range)
    can still highlight its children's combined span on click."""
    rs = [c.bit_range for c in children if c.bit_range is not None]
    if not rs:
        return None
    return (min(r[0] for r in rs), max(r[1] for r in rs))


def _value_node(name: str, value: Any) -> DecodeNode:
    """Recursively turn any decoded value into a DecodeNode subtree.

    Handles the shapes the decoders actually emit: Variant (bag entry),
    plain dict/list (parser records), bytes, kaitai/opaque structs
    (walked via __dict__ or __slots__), and scalars. Parent nodes that
    don't carry an explicit range derive one from their children's union.
    """
    if isinstance(value, Variant):
        inner = value.value
        rng = value.bit_range
        # `display` lets the parser override the value-column text — e.g.
        # for a bitmask, show the decoded role list instead of "0x07fc".
        shown = value.display if value.display is not None else None
        if isinstance(inner, dict):
            return DecodeNode(name, shown or "", value.tag,
                              [_value_node(str(k), v) for k, v in inner.items()],
                              bit_range=rng)
        if isinstance(inner, (list, tuple)):
            return DecodeNode(name, shown or f"{len(inner)} items", value.tag,
                              [_value_node(f"[{i}]", v)
                               for i, v in enumerate(inner)],
                              bit_range=rng)
        return DecodeNode(name, shown if shown is not None else repr(inner),
                          value.tag, [], bit_range=rng)
    if isinstance(value, dict):
        children = [_value_node(str(k), v) for k, v in value.items()]
        return DecodeNode(name, "", "", children,
                          bit_range=_union_ranges(children))
    if isinstance(value, (list, tuple)):
        children = [_value_node(f"[{i}]", v) for i, v in enumerate(value)]
        return DecodeNode(name, f"{len(value)} items", "", children,
                          bit_range=_union_ranges(children))
    if isinstance(value, (bytes, bytearray)):
        if len(value) > _BYTES_PREVIEW:
            shown = f"{value[:_BYTES_PREVIEW].hex()}… ({len(value)} bytes)"
        else:
            shown = value.hex()
        return DecodeNode(name, shown, "bytes", [])
    attrs = _struct_attrs(value)
    if attrs is not None:
        children = [_value_node(k, v) for k, v in attrs]
        return DecodeNode(name, type(value).__name__, "struct", children,
                          bit_range=_union_ranges(children))
    return DecodeNode(name, repr(value), "", [])


def decode_structured(pkt_type: int, body: bytes,
                      direction: str) -> DecodeNode | None:
    """Decode a packet into a DecodeNode tree for the UI's tree view.

    Same dispatch as decode_packet, but returns the structured payload
    instead of a flat string. Returns None for packet types with no
    structured decode — the UI falls back to the flat log line there.
    """
    name = scmd_name(pkt_type)

    if name == "SCMD_NOTIFICATION" and body:
        try:
            n = decode_notification(body)
        except Exception as e:
            return DecodeNode(name, f"{type(e).__name__}: {e}", "error", [])
        children = [_value_node(str(k), v) for k, v in n.bag.items()]
        issues = n.validate()
        if issues:
            children.append(
                DecodeNode("⚠ issues", "; ".join(issues), "error", []))
        sn_id = body[0]
        return DecodeNode(f"{name}  sn=0x{sn_id:02x}({sn_name(sn_id)})",
                          "", "", children)

    if pkt_type in DECODERS and body:
        try:
            payload = decode(pkt_type, body)
        except Exception as e:
            return DecodeNode(name, f"{type(e).__name__}: {e}", "error", [])
        return DecodeNode(payload.name, "", "",
                          [_value_node(str(k), v)
                           for k, v in payload.bag.items()])

    if name == "CSCMD_ASYNC_REQ":
        try:
            if direction == "C→S":
                parsed = StarConflictPackageClient(KaitaiStream(BytesIO(body)))
            else:
                parsed = StarConflictPackageServer(KaitaiStream(BytesIO(body)))
        except Exception as e:
            return DecodeNode(name, f"{type(e).__name__}: {e}", "error", [])
        node = _value_node(type(parsed.body).__name__, parsed.body)
        # The opaque body's BitReader operates on `body[2:]` (kaitai
        # consumed the 2-byte AC index first), so every range produced
        # under here is body-relative-to-body[2:]. Shift by +16 bits so
        # the UI's hex pane (which shows full body) lines up.
        _shift_bit_ranges(node, 16)
        return node

    return None


def _shift_bit_ranges(node: DecodeNode, bits: int) -> None:
    """In-place add `bits` to every bit_range in the subtree."""
    if node.bit_range is not None:
        a, b = node.bit_range
        node.bit_range = (a + bits, b + bits)
    for c in node.children:
        _shift_bit_ranges(c, bits)


# ── Self-test ─────────────────────────────────────────────────────────────────

def _selftest() -> None:
    import struct

    def make_bits(*items):
        """items: list of (value, nbits)."""
        bits = []
        for v, n in items:
            for i in range(n - 1, -1, -1):
                bits.append((v >> i) & 1)
        while len(bits) % 8: bits.append(0)
        return bytes(int("".join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8))

    # SCMD_KEEP_ALIVE: 8-byte BE u64 timestamp
    p = decode(0x18, struct.pack(">Q", 0x0000018e_a4310f0d))
    assert p.bag["timestamp_ms"].value == 0x0000018e_a4310f0d
    print(f"OK  {format_payload(p)}")

    # SCMD_REWARD_SCHEDULE: empty bag (count=0, no flag bit)
    p = decode(0x20, b"\x00\x00\x00\x00")
    assert p.bag == {}
    print(f"OK  {format_payload(p)}")

    # SCMD_FREE_SPACE_DEBRIEFING: u1=1 then count=0 bag
    body = make_bits((1, 1), (0, 32))
    p = decode(0x1c, body)
    assert p.bag["docked"].value is True
    print(f"OK  {format_payload(p)}")

    # SCMD_SQUAD_NOTIFICATION sub_type=2 (JOIN) — squad_id + joining_uid
    body = make_bits((2, 8), (0xabc, 64), (0xdef, 64))
    p = decode(0x0f, body)
    assert p.bag["squad_id"].value == 0xabc and p.bag["joining_uid"].value == 0xdef
    print(f"OK  {format_payload(p)}")

    # SCMD_SOCIAL_NOTIFICATION sub_type=0 (add_friend) + uid
    body = make_bits((0, 8), (0xdeadbeef, 64))
    p = decode(0x10, body)
    assert p.bag["soc_type"].value == 0 and p.bag["uid"].value == 0xdeadbeef
    print(f"OK  {format_payload(p)}")

    # SCMD_TEACH_NOTIFICATION cmd=8 (reward) — uid + i32 expReward
    body = make_bits((8, 8), (1234, 64), (5000, 32))
    p = decode(0x11, body)
    assert p.bag["expReward"].value == 5000
    print(f"OK  {format_payload(p)}")

    # SCMD_CLAN_NOTIFICATION cmd=2 — fixed prologue (cmd + 3×u64 + u8)
    body = make_bits((2, 8), (0xa, 64), (0xb, 64), (0xc, 64), (0xff, 8))
    p = decode(0x12, body)
    assert p.bag["clan_cmd"].value == 2 and p.bag["field_1"].value == 0xa
    assert p.bag["field_4"].value == 0xff
    print(f"OK  {format_payload(p)}")

    # SCMD_USER_PROFILE_NOTIFICATION sub_type=6 (i32 accountExpPool)
    body = make_bits((6, 8), (0x1234, 64), (42, 32))
    p = decode(0x13, body)
    assert p.bag["accountExpPool"].value == 42
    print(f"OK  {format_payload(p)}")

    # SCMD_LEAGUE_NOTIFICATION cmd=3 — ext + flag
    body = make_bits((3, 8), (1, 64), (2, 64), (3, 64), (0x42, 8))
    p = decode(0x15, body)
    assert p.bag["ext"].value == 3 and p.bag["flag"].value == 0x42
    print(f"OK  {format_payload(p)}")

    # SCMD_VESSEL_NOTIFICATION sub_type=10 (hp update)
    body = make_bits((10, 8), (0xfeedface, 64),
                     (int.from_bytes(struct.pack(">f", 0.5), "big"), 32))
    p = decode(0x16, body)
    assert p.bag["vid"].value == 0xfeedface
    assert abs(p.bag["hp"].value - 0.5) < 1e-6
    print(f"OK  {format_payload(p)}")

    # SCMD_LOBBY_NOTIFICATION sub_type=2 — lobby_id + op
    body = make_bits((2, 8), (100, 32), (2, 32))
    p = decode(0x17, body)
    assert p.bag["lobby_id"].value == 100 and p.bag["arg"].value == 2
    print(f"OK  {format_payload(p)}")

    # Unknown type
    assert decode(0xff, b"") is None
    print("OK  unknown-type fallback")


def _decoder_short_name(fn: Callable) -> str:
    """`_scmd_user_profile_notification` → `user_profile_notification`."""
    n = fn.__name__
    return n[len("_scmd_"):] if n.startswith("_scmd_") else n


def _resolve_decoder(spec: str) -> int | None:
    """Map a CLI `<decoder>` spec to a registered pkt_type, or None.

    Accepts:
      • hex/decimal int  ("0x13", "19")
      • exact short name ("user_profile_notification")
      • unique substring ("user_profile", "vessel")
    """
    spec = spec.strip().lower()
    try:
        pkt = int(spec, 0)
        return pkt if pkt in DECODERS else None
    except ValueError:
        pass
    short_to_type = {_decoder_short_name(fn): t for t, fn in DECODERS.items()}
    if spec in short_to_type:
        return short_to_type[spec]
    matches = [t for n, t in short_to_type.items() if spec in n]
    return matches[0] if len(matches) == 1 else None


if __name__ == "__main__":
    import argparse
    import sys

    ap = argparse.ArgumentParser(
        description="Decode a raw SCMD body from a .bin file.",
        epilog="Examples:\n"
               "  scmd_decoders.py --list\n"
               "  scmd_decoders.py user_profile body.bin\n"
               "  scmd_decoders.py 0x13 body.bin\n"
               "  scmd_decoders.py --selftest",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("decoder", nargs="?",
                    help="pkt_type as int (0x13 / 19) or short name "
                         "(unique substring of the SCMD name; e.g. "
                         "'user_profile', 'vessel')")
    ap.add_argument("path", nargs="?", help="path to a .bin body file")
    ap.add_argument("--selftest", action="store_true",
                    help="run the built-in self-tests and exit")
    ap.add_argument("--list", action="store_true",
                    help="list registered decoders and exit")
    args = ap.parse_args()

    if args.selftest:
        _selftest()
        sys.exit(0)

    if args.list:
        print("  pkt   short-name                         payload .name")
        for t, fn in sorted(DECODERS.items()):
            sample = fn.__doc__.splitlines()[0] if fn.__doc__ else ""
            sample_name = sample.split(":", 1)[0].strip() if ":" in sample else fn.__name__
            print(f"  0x{t:02x}  {_decoder_short_name(fn):<33} {fn.__name__}")
        sys.exit(0)

    if not args.decoder or not args.path:
        ap.error("supply <decoder> <path>, or use --selftest / --list")

    pkt = _resolve_decoder(args.decoder)
    if pkt is None:
        ap.error(f"could not resolve {args.decoder!r} to a registered "
                 f"decoder; use --list to see options")

    with open(args.path, "rb") as f:
        body = f.read()

    payload = decode(pkt, body)
    if payload is None:
        sys.exit(f"no decoder registered for pkt_type 0x{pkt:02x}")
    print(format_payload(payload))
