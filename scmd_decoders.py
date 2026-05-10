#!/usr/bin/env python3
"""Per-SCMD body decoders for packet types beyond SCMD_NOTIFICATION.

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
from dataclasses import dataclass
from typing import Any, Callable

from notification import BitReader, Variant, _read_bag, format_bag, _BRRED, _RESET


@dataclass
class ScmdPayload:
    """Container for a decoded non-notification SCMD body. Has a .bag dict
    so the existing format_bag() colourer renders it identically."""
    name: str
    bag: dict


def _kv(tag: str, val: Any) -> Variant:
    """Wrap a directly-read scalar so format_bag() can colour it.

    `tag` is the wire-level type at the bit position read (u8/u16/u32/u64/u1
    /str/bag/...) — *not* a bag-variant tag, since these decoders read raw
    bit-stream fields, not bag entries. We reuse the Variant container
    purely for the colour-aware repr; itag=0xff signals "no on-wire
    variant tag byte" (this field was a direct read).
    """
    return Variant(tag, val, 0xff)


# ── Per-SCMD decoders ────────────────────────────────────────────────────────

def _scmd_keep_alive(body: bytes) -> ScmdPayload:
    """0x18: u64 client_timestamp_ms (echoed by client to compute RTT).

    Source: case 0x18 of OnRecieve. Reads u64, computes
        rtt = current_time_ms - timestamp.
    """
    br = BitReader(body)
    ts = br.read_u64()
    return ScmdPayload("SCMD_KEEP_ALIVE", {"timestamp_ms": _kv("u64", ts)})


def _scmd_free_space_debriefing(body: bytes) -> ScmdPayload:
    """0x1c: u1 docked + property bag.

    Source: case 0x1c. Reads `cVar15 = ReadBit()`, deserialises bag, then
    augments the bag with `{"docked": cVar15}` before dispatching to UI.
    """
    br = BitReader(body)
    docked = br.read_bool()
    bag = _read_bag(br)
    bag = {"docked": _kv("bool", docked), **bag}
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
    status = br.read_u8()
    zone_id = br.read_u32()
    dock_flag = br.read_bool()
    freespace_flag = br.read_bool()
    return ScmdPayload("SCMD_DOCK_SPACE_STATION", {
        "status": _kv("i32", status),
        "zone_id": _kv("i32", zone_id),
        "dock_flag": _kv("bool", dock_flag),
        "freespace_flag": _kv("bool", freespace_flag),
    })


def _scmd_replace_chat_msg(body: bytes) -> ScmdPayload:
    """0x26: u64 chat_msg_id + u8 flag (synthesised into a 2-entry bag for UI).

    Source: case 0x26.
    """
    br = BitReader(body)
    msg_id = br.read_u64()
    flag = br.read_u8()
    return ScmdPayload("SCMD_REPLACE_CHAT_MSG", {
        "chat_msg_id": _kv("u64", msg_id),
        "flag": _kv("i32", flag),
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
    sub = br.read_u8()
    out: dict = {"sqn_type": _kv("u8", sub)}
    try:
        if sub == 0:
            out["squad_id"]  = _kv("u64", br.read_u64())
            out["leader_uid"] = _kv("u64", br.read_u64())
            if br.remaining() >= 64:
                out["invitee_or_new_leader"] = _kv("u64", br.read_u64())
        elif sub == 1:
            out["squad_id"]   = _kv("u64", br.read_u64())
            out["leader_uid"] = _kv("u64", br.read_u64())
        elif sub == 2:
            out["squad_id"]    = _kv("u64", br.read_u64())
            out["joining_uid"] = _kv("u64", br.read_u64())
        elif sub == 3:
            out["squad_id"]    = _kv("u64", br.read_u64())
            out["leaving_uid"] = _kv("u64", br.read_u64())
        elif sub == 4:
            out["squad_id"]   = _kv("u64", br.read_u64())
            out["kicker_uid"] = _kv("u64", br.read_u64())
            out["kickee_uid"] = _kv("u64", br.read_u64())
        elif sub in (5, 6, 7, 8):
            out["squad_id"] = _kv("u64", br.read_u64())
            out["uid"]      = _kv("u64", br.read_u64())
            out["rcType"]   = _kv("u64", br.read_u64())
        elif sub == 9:
            out["done_flag"] = _kv("u1", br.read_bool())
            out["uid"]       = _kv("u64", br.read_u64())
        elif sub == 10:
            out["done_flag"]            = _kv("u1", br.read_bool())
            out["uid"]                  = _kv("u64", br.read_u64())
            result                      = br.read_u8()
            out["result"]               = _kv("u8", result)
            out["minRank"]              = _kv("u8", br.read_u8())
            out["maxRank"]              = _kv("u8", br.read_u8())
            out["accountRank"]          = _kv("u8", br.read_u8())
            out["maxHighestSquadRank"]  = _kv("u8", br.read_u8())
            if result == 0x22:    # '"'
                out["minHighestSquadRank"] = _kv("u8", br.read_u8())
            elif result == 0x2d:  # '-'
                out["badLeagueEquipment"]        = _kv("bag", _read_bag(br))
                out["badLeagueAutogenEquipment"] = _kv("bag", _read_bag(br))
            elif result == 0x30:  # '0'
                out["leaverBanTill"] = _kv("u64", br.read_u64())
        elif sub in (0x0b, 0x0c):
            out["done_flag"] = _kv("u1", br.read_bool())
        elif sub in (0x0d, 0x20):
            out["reason"] = _kv("u8", br.read_u8())
        elif sub in (0x0e, 0x21):
            out["uid"] = _kv("u64", br.read_u64())
        elif sub in (0x22, 0x23):
            out["squad_id"] = _kv("u64", br.read_u64())
            out["uid"]      = _kv("u64", br.read_u64())
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
    sub = br.read_u8()
    uid = br.read_u64()
    return ScmdPayload("SCMD_SOCIAL_NOTIFICATION", {
        "soc_type": _kv("u8", sub),
        "uid":      _kv("u64", uid),
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
    sub = br.read_u8()
    out: dict = {"command": _kv("u8", sub)}
    if sub in (9, 10):
        return ScmdPayload("SCMD_TEACH_NOTIFICATION", out)
    out["uid"] = _kv("u64", br.read_u64())
    if sub == 8:
        out["expReward"] = _kv("i32", br.read_i32())
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
    cmd = br.read_u8()
    f1  = br.read_u64()
    f2  = br.read_u64()
    f3  = br.read_u64()
    f4  = br.read_u8()
    out: dict = {
        "clan_cmd": _kv("u8",  cmd),
        "field_1":  _kv("u64", f1),
        "field_2":  _kv("u64", f2),
        "field_3":  _kv("u64", f3),
        "field_4":  _kv("u8",  f4),
    }
    try:
        if cmd == 0x19:
            out["extra_u32"] = _kv("u32", br.read_u32())
        elif cmd == 0x1a:
            out["extra_cstring"] = _kv("str", br.read_cstring(max_len=251))
    except EOFError:
        out["_truncated"] = _kv("?", True)
    return ScmdPayload("SCMD_CLAN_NOTIFICATION", out)


def _scmd_user_profile_notification(body: bytes) -> ScmdPayload:
    """0x13: u8 upn_type + u64 uid + per-sub-type struct.

    Source: OnUserProfileNotification (0x0832ed90). The on-wire sub-id is
    NOT the lua-side MasterServer.UserProfileField (UPF_*) value — the
    C++ side translates each sub-id through some mapping table before
    invoking lua's MasterServer_OnUserProfileUpdate(result, requestId,
    uid, UPF_*). The shapes below are inferred from captures + the
    dispatch table at FUN_0832ed90's `jmp *0x8f6d040(,%ebp,4)`.

      0   u8  state                                     (online/offline byte;
                                                        matches UserState enum)
      1   u16 achievement_id + u32 old_value + u32 new_value
                                                       (achievement progress
                                                        delta — e.g. id=80
                                                        (MILEAGE) bumps from
                                                        1416 to 1438)
      2   u16 achievement_id, u8 stage, u64 unlock_time_ms
                                                       (achievement unlock —
                                                        e.g. id=88 (Bandit)
                                                        stage=0 t=2026-05-10
                                                        12:39:58 UTC. Stage
                                                        is the achievement
                                                        rank/tier; the u64
                                                        is a Unix-epoch
                                                        timestamp in ms)
      3   u16                                             (no captures yet)
      4   cstring newly_unlocked_def
          (then, when the profile already had an avatars list — case-4
           handler in OnUserProfileNotification calls FUN_08919100 to
           read the rest, otherwise it uses the al=0 init path with no
           tail):
              cstring current_avatar_def     (often empty)
              u16     count
              count × cstring full_list      (every unlocked avatar)
          Discrimination is server-side state, so the parser uses
          remaining-bytes as the heuristic.
      5   cstring                                         (no captures yet —
                                                        plausibly motto text)
      6   i32 clearance_score                             (in-game name;
                                                        bumps in steps that
                                                        match achievement
                                                        unlocks — observed
                                                        750 → 760 right
                                                        after a batch of
                                                        sub=2 unlocks)
      7   FUN_088c0ce0 struct — see sub=7 branch:
              u32 clearance_score   (matches sub=6's value for the same uid;
                                     observed: uid 2440894 prefix 750→760
                                     across captures, identical to its
                                     sub=6 clearance_score)
              u1  bag1_present (b1==0)
              if bag1_present: bag — fixed sparse keys (always 16,
                30, 31, 32, 48) with u64 values. The keys coincide
                numerically with both ai.AchievementId and ai.MedalType
                entries, but neither interpretation fits the data:
                • Key "16" is non-zero for accounts that didn't alpha-
                  test, so it's not SC_VETERAN.
                • Values are 10^17-10^19, far too large to be medal
                  counts (medals never exceed ~30k).
                Bit-pop scales with player rank (uid 1438647: 68 bits
                set, clearance=1480; uid 2440894: 22 bits set,
                clearance 750/760). Real meaning still TBD.
              u1  bag2_present (b2==0); never observed in captures.
    """
    br = BitReader(body)
    sub = br.read_u8()
    uid = br.read_u64()
    out: dict = {
        "upn_type": _kv("u8",  sub),
        "uid":      _kv("u64", uid),
    }
    try:
        if sub == 0:        # state byte
            out["state"] = _kv("u8", br.read_u8())
        elif sub == 1:      # achievement progress delta
            out["achievement_id"] = _kv("u16", br.read_u16())
            out["old_value"]      = _kv("u32", br.read_u32())
            out["new_value"]      = _kv("u32", br.read_u32())
        elif sub == 2:      # achievement unlock
            out["achievement_id"] = _kv("u16", br.read_u16())
            out["stage"]          = _kv("u8",  br.read_u8())
            out["unlock_time_ms"] = _kv("u64", br.read_u64())
        elif sub == 3:      # u16 (uncaptured)
            out["v16"] = _kv("u16", br.read_u16())
        elif sub == 4:      # avatar unlock (+ optional current + full list)
            out["unlocked_avatar"] = _kv("str", br.read_cstring(max_len=60))
            # Tail (FUN_08919100) is only emitted when the profile already
            # has an avatars list — server-side state we can't see. Detect
            # by checking that there's room for at least cstring + u16.
            if br.remaining() >= 8 + 16:
                out["current_avatar"] = _kv("str",
                    br.read_cstring(max_len=60))
                n = br.read_u16()
                out["unlocked_count"] = _kv("u16", n)
                for i in range(n):
                    out[f"unlocked[{i}]"] = _kv("str",
                        br.read_cstring(max_len=60))
        elif sub == 5:      # cstring (uncaptured — possibly motto)
            out["text"] = _kv("str", br.read_cstring(max_len=60))
        elif sub == 6:      # in-game "Clearance Score"
            out["clearance_score"] = _kv("i32", br.read_i32())
        elif sub == 7:      # FUN_088c0ce0 struct
            # FUN_088c0ce0(buf, struct):
            #     struct[0] = read_u32(buf)                # clearance_score
            #     if read_bool(buf) == 0:                   # b1
            #         FUN_08b1ed60(buf, &struct[+0x4])      # → _read_bag
            #     if read_bool(buf) == 0:                   # b2
            #         FUN_08b1ed60(buf, &struct[+0x18])     # → _read_bag
            # bag1: fixed keys (16, 30, 31, 32, 48) with u64 values
            # whose magnitudes (10^17-10^19) rule out simple counters.
            # See docstring above for ruled-out hypotheses.
            out["clearance_score"] = _kv("u32", br.read_u32())
            if not br.read_bool():
                out["bag1"] = _kv("bag", _read_bag(br))
            if br.remaining() >= 1 and not br.read_bool():
                out["bag2"] = _kv("bag", _read_bag(br))
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
    sub = br.read_u8()
    league_id = br.read_u64()
    team_id   = br.read_u64()
    out: dict = {
        "league_cmd": _kv("u8",  sub),
        "league_id":  _kv("u64", league_id),
        "team_id":    _kv("u64", team_id),
    }
    try:
        if sub in (0, 1, 2):
            out["ext"] = _kv("u64", br.read_u64())
        elif sub == 3:
            out["ext"]  = _kv("u64", br.read_u64())
            out["flag"] = _kv("u8",  br.read_u8())
        elif sub in (4, 5):
            out["invitee_uid"] = _kv("u64", br.read_u64())
        elif sub == 6:
            pass  # no extra
        elif sub == 7:
            out["f32_x"] = _kv("f32", br.read_f32())
            out["u32_y"] = _kv("u32", br.read_u32())
            out["u32_z"] = _kv("u32", br.read_u32())
        elif sub == 8:
            out["flag"] = _kv("u1", br.read_bool())
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
    sub = br.read_u8()
    out: dict = {"vssln_type": _kv("u8", sub)}
    try:
        if sub == 0:
            out["_vessel_record_bytes"] = _kv("?", br.remaining())
        elif sub == 1:
            out["vid"] = _kv("u64", br.read_u64())
        elif sub == 2:
            out["prestige"] = _kv("f32", br.read_f32())
        elif sub == 3:
            out["vid"]         = _kv("u64", br.read_u64())
            out["quest_state"] = _kv("u64", br.read_u64())
            count = br.read_u8()
            out["count"]  = _kv("u8",  count)
            for i in range(count):
                out[f"sub_vid_{i}"] = _kv("u64", br.read_u64())
        elif sub == 4:
            out["vid"] = _kv("u64", br.read_u64())
        elif sub == 5:
            count = br.read_u8()
            out["count"] = _kv("u8", count)
            for i in range(count):
                out[f"vid_{i}"]   = _kv("u64", br.read_u64())
                out[f"hp_{i}"]    = _kv("f32", br.read_f32())
                out[f"stat_{i}"]  = _kv("u32", br.read_u32())
                out[f"flags_{i}"] = _kv("u8",  br.read_u8())
        elif sub == 6:
            out["vid"]      = _kv("u64", br.read_u64())
            out["mod_mask"] = _kv("u64", br.read_u64())
            out["flags"]    = _kv("u8",  br.read_u8())
        elif sub in (7, 8, 11):
            out["vid"]   = _kv("u64", br.read_u64())
            out["flags"] = _kv("u8",  br.read_u8())
        elif sub == 9:
            out["vid"]  = _kv("u64", br.read_u64())
            out["stat"] = _kv("u32", br.read_u32())
        elif sub == 10:
            out["vid"] = _kv("u64", br.read_u64())
            out["hp"]  = _kv("f32", br.read_f32())
        elif sub == 12:
            out["vid"]    = _kv("u64", br.read_u64())
            out["budget"] = _kv("u64", br.read_u64())
            out["boost"]  = _kv("u64", br.read_u64())
        elif sub == 13:
            out["vid"]            = _kv("u64", br.read_u64())
            out["level"]          = _kv("u8",  br.read_u8())
            out["repair_budget"]  = _kv("u32", br.read_u32())
            out["was_repaired"]   = _kv("u1",  br.read_bool())
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
    sub = br.read_u8()
    out: dict = {"lbn_type": _kv("u8", sub)}
    try:
        if sub == 0:
            out["bag"] = _kv("bag", _read_bag(br))
        elif sub in (1, 2, 3):
            out["lobby_id"] = _kv("u32", br.read_u32())
            out["arg"]      = _kv("u32", br.read_u32())
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
    sub = br.read_u8()
    return ScmdPayload("SCMD_QUEST_NOTIFICATION", {
        "sub_type": _kv("u8", sub),
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
    sub = br.read_u8()
    return ScmdPayload("SCMD_ADVENTURE_NOTIFICATION", {
        "sub_type": _kv("u8", sub),
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

    # SCMD_USER_PROFILE_NOTIFICATION sub_type=6 (i32 clearance_score)
    body = make_bits((6, 8), (0x1234, 64), (42, 32))
    p = decode(0x13, body)
    assert p.bag["clearance_score"].value == 42
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
        print(f"  pkt   short-name                         payload .name")
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
