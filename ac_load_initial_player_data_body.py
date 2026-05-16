"""Opaque kaitai type — body of `ac_load_initial_player_data` (AC 0).

Sent S→C as the player's initial-state snapshot right after login. The
handler is at 0x0823103b. Decoded fields populate the master-server
client cache that lua reads via the `MasterServer_Get*` family of
accessors (see `scripts/masterserver.lua` and the
`u32/table/u64 MasterServer_Get…` debug strings inside the binary).

Three string clues from `strings StarConflict | grep AC_LOAD_INITIAL`
anchor parts of the layout:

   "AC_LOAD_INITIAL_PLAYER_DATA - reward schedule is:"
   "AC_LOAD_INITIAL_PLAYER_DATA - pve scheduled levels are:"
   "AC_LOAD_INITIAL_PLAYER_DATA: fail to read BattlePass activation"
   "AC_LOAD_INITIAL_PLAYER_DATA: fail to read BattlePass player data"

…and dispatched lua callbacks (`UI.LoginWnd.MasterServer_OnInitialPlayerData`
in `ui/scripts/windows/loginwnd.lua`,
`UI.UpdateServerData_OnInitialPlayerData` in `ui/scripts/work/uigamefuncs.lua`)
confirm the tail carries BattlePass activation + player progress.

   ── COMPOUND STRUCTURE ─────────────────────────────────────────────
   This packet is not a bespoke monolithic format — it inlines the
   payloads of five *standalone SCMD packets*, so that logging in
   delivers in one shot the state the server would otherwise push as
   separate packets. Verified in Ghidra: the handler at 0x0823103b and
   the matching case in OnRecieve's scmd_pkt_type switch (jump table at
   0x08f4eef8, indexed by pkt_type-9) decode each piece with the *same*
   reader and write it to the *same* master-server cache member:

     embedded field              shared reader    standalone packet                  cache member
     --------------------------  ---------------  ---------------------------------  ----------------
     brawl_schedule              FUN_088fe450     SCMD_BRAWL_SCHEDULE        (0x1f)   +0xb6330, +0xb84bc=1
     reward_schedule_bag         Bag_Deserialize  SCMD_REWARD_SCHEDULE      (0x20)   +0xb84c0
     pve_scheduled_levels_bag    Bag_Deserialize  SCMD_PVE_SCHEDULE         (0x21)   +0xb84d4
     league_forbidden_equipment  FUN_082590e0     SCMD_LEAGUE_FORBIDDEN_EQUIPMENT (0x22)  +0x193878
     battle_pass_activation      FUN_088d9700     SCMD_BATTLE_PASS_ACTIVATION (0x23)  +0x28f9f0
     zones_with_disabled_quests  FUN_0824ae10     SCMD_ZONES_WITH_DISABLED_QUESTS (0x24)  +0x2bb21c

   For brawl_schedule / league_forbidden_equipment / battle_pass_activation
   the proof is a *uniquely shared reader function* (FUN_088fe450 /
   FUN_082590e0 / FUN_088d9700 each have exactly two callers — this
   handler and the one OnRecieve case). For the two `Bag_Deserialize`
   rows the reader is generic, but the destination cache member offset
   is identical to the standalone SCMD_REWARD_SCHEDULE / SCMD_PVE_SCHEDULE
   handler, which pins the equivalence.

   Everything else is exclusive to this packet — the head scalars, the
   three bundle catalogues (FUN_088fc1e0), pve_level_reward_modifiers
   (FUN_088fcea0), brawl_schedule_default (FUN_088fe1c0), and
   battle_pass_player_data (FUN_088dd630) each have no other caller;
   leading_advert / unlim_pve_mission_levels / bag_27 are generic bags
   with no standalone-packet twin.

Wire shape (matches the binary's read sequence):

   ── HEAD ───────────────────────────────────────────────────────────
   u64                 profile_revision         monotonic per-player save
                                                counter (e.g. uid 226372
                                                cycles ~1.17M → +3/save)
   u32                 format_version           always 2 in captures
   u1                  flag_a                   always 0
   u32                 head_account_field       3..5 across captures;
                                                ticks +1 on rank-up
                                                (probably faction/syndicate
                                                tier or "active profile" idx)
   u1                  flag_b                   always 0
   u64                 head_u64_zero            always 0 (penalty-till?)
   cstr60              head_text                always "" in captures
                                                (clan tag / nickname tail?)

   ── BUNDLE CATALOGUE ───────────────────────────────────────────────
   Each section is `u32 count + count × BundleRecord` (FUN_088fc1e0).
   The same record shape is reused across all three sections; only the
   fields populated differ:

   bundles_steam    320 entries — `steam_app_id` (u_a) set, e.g.
                                 'Merc1'=222280, 'Merc2'=222281, …
                                 (the player's Steam-buyable DLC catalog).

   bundles_yuplay   455 entries — `yuplay_guid` (s2) set, e.g.
                                 '80815843-A546-4469-B835-…'.
                                 (the player's Yuplay/Gaijin-buyable
                                 product catalog. UUIDs match
                                 `yuplay_guid` in
                                 `gamedata/ui_properties.lua`.)

   bundles_owned    6 entries — DLCs/promo packs the player owns
                                 (matches the test-account's purchased
                                 Steam DLCs in our captures).

   BundleRecord fields:
       cstr256 def_name                  e.g. 'Merc1', 'Pirate2', 'Fleet1'
       u32     steam_app_id              e.g. 222280 (matches steam_appId in
                                         `gamedata/ui_properties.lua`)
       cstr256 yuplay_guid               '8081…' UUID for Yuplay listings
       f32 × 3 floats                    always 0.0 in captures (prices?)
       u32 × 6 misc                      e.g. (15333032, 4290286736, 0,
                                         3500, 0, 3) — last is rank gate
       u1      flag1                     'owned' / 'active' bit
       u1      flag2                     unused so far
       cstr256 aura_def                  e.g. 'Steamer_1' = account aura
                                         awarded by Merc1 DLC
       u32 count + count × {cstr256 name, u1, u1}    ship rewards
       u32 count + count × cstr256                   decal/decoration rewards
       u32 count + count × cstr256                   (empty in captures)
       u32 count + count × {cstr256 name, u32, u32}  weapon/module rewards
       u32 count + count × {i32, i32}                quantity pairs
       u64     end_marker                always 0 in captures

   ── REWARD-SCHEDULE / PVE-ROTATION TAIL ─────────────────────────────
   pve_level_reward_modifiers   FUN_088fcea0 — `u32 count + count ×
                                {u32 a, u32 b, cstr256 name}`.
                                Observed: 84 entries cycling through
                                {'s8256_pve_raid_planetoid',
                                'pve_raid_waterharvest', 'pve_raid'}
                                with `a == b` stepping by 2 (rank
                                bracket).

   brawl_schedule_default       FUN_088fe1c0 — single
                                `u32 count + count × {u32, u32} + cstr59`
                                with one (17, 18) pair and empty name.
                                FUN_088fe1c0 is the per-entry reader that
                                FUN_088fe450 loops; this lone leading
                                entry is exclusive to the initial-load
                                packet (SCMD_BRAWL_SCHEDULE has only the
                                28-entry block below).

   brawl_schedule               FUN_088fe450 — `28 × FUN_088fe1c0`.
                                Same reader the standalone
                                SCMD_BRAWL_SCHEDULE (0x1f) packet uses;
                                28 entries, each a list of (threshold,
                                reward_id) pairs + a gameplay tag string
                                (e.g. (1,2)(9,10)(15,16) for 'gtdm').
                                Earlier mislabelled "reward_schedule_per
                                _gameplay" before the OnRecieve cross-ref.

   ── TAIL: SCALARS + BAGS interleaved ───────────────────────────────
   bag    reward_schedule_bag          MasterServer_GetRewardSchedule()
                                       — gameplay-id → reward-window
                                       → {goldReward, hourBegin, hourEnd}
   bag    pve_scheduled_levels_bag     MasterServer_GetPveScheduledLevels()
                                       — currently-active raid roster
                                       ('pve_magnificent_seven', …)
   u32    field_12                     always 0 in captures
   u1     flag_13
   u8     max_vessel_rank              17 in our test capture (= T5)
   u8     account_rank                 25 in our test capture (MasterServer_GetAccountRank)
   i32    account_exp_pool             "Clearance Score"
                                       (MasterServer_GetAccountExpPool);
                                       cross-checked against the matching
                                       uid's Atlas.accountExpPool earlier.
   u1     flag_17
   bag    leading_advert               MasterServer_GetLeadingAdvertInfo()
                                       — current shop "hot offer".
                                       Bag keys: advertId, expTime, def,
                                       goldPrice, type, iid, amount.
   bag    unlim_pve_mission_levels     Map of unlimPve mission def → highest
                                       level the player has reached, e.g.
                                       {'planet_war_waves_T1': 25,
                                        'magnificent_seven': 2, …}.
                                       Confirmed by cross-check against
                                       gmt.star-conflict.com/pubapi/v1/
                                       userinfo.php?nickname=…
                                       → .data.pve.unlimPve_missionLevels
                                       (exact match key-by-key).
   i32    field_20
   i32    field_21
   u1     flag_22
   i32    field_23                     -1 sentinel (== UI.INVALID_U64_ID)
   u64    field_24                     always 0 (penalty timestamp?)
   bag    league_forbidden_equipment   bool flags keyed by item def, e.g.
                                       'Weapon_Minigun_NY_T3' = true.
                                       FUN_082590e0 clears the list at
                                       endpoint+0x193878 then Bag_Deserialize
                                       fills it. Same reader as the
                                       standalone SCMD_LEAGUE_FORBIDDEN_
                                       EQUIPMENT (0x22) packet — the bag is
                                       the set of items barred from league
                                       play. Earlier mislabelled
                                       "event_item_unlocks".
   tbl    battle_pass_activation       BattlePass::ReadActivationFromBitStream
                                       at FUN_088d9700:
                                       `u64 token + u16 count + count ×
                                        {u16 stage, u64 ts}`
   tbl    battle_pass_player_data      BattlePass::PlayerData::ReadFromBitStream
                                       at FUN_088dd630.
   i32    field_25                     50 in our test capture
   u1     flag_26                      True in our test capture
   bag    bag_27                       outer u32 keys subset of Gameplay
                                       enum (1=SPACE_BATTLE, 11=BOMB,
                                       12=TDM, …) + larger ids (~200+).
                                       Inner f32 values mostly -100504.0
                                       == ai.ScriptsServer.REMOVED_EVENT,
                                       some 1000.0. Likely a per-mode
                                       scripted-event progression cache.
   blob   zones_with_disabled_quests   513-bit fixed-size blob (≈64 B)
                                       read by FUN_0824ae10 →
                                       FUN_08b1db50 → BitStream_Read
                                       (nbits=0x201). Stored into
                                       master-server cache +0x2bb21c
                                       with the +0xb4a78 "loaded" flag
                                       set to 1. Same wire format and
                                       destination as the standalone
                                       SCMD_ZONES_WITH_DISABLED_QUESTS
                                       (0x24) packet.

The handler tolerates short bodies via its lastReadOK flag: every reader
returns 0 instead of throwing once the stream runs out. We mirror that
by catching EOFError and leaving later fields unset.
"""
from __future__ import annotations
from typing import Any
import traceback

from notification import BitReader, _read_bag, format_bag, read_field


# ── Sub-readers ──────────────────────────────────────────────────────────────

def _read_bundle_record(br: BitReader) -> dict:
    """FUN_088fc1e0 — one BundleRecord. Used by bundles_steam, bundles_yuplay
    and bundles_owned in a loop. See file docstring for field semantics.

    Every field is wrapped via read_field() so the tree builder gets a
    bit range for each one — clicking any node lights up its bytes in
    the hex pane.
    """
    out: dict[str, Any] = {}
    out["def_name"]     = read_field(br, "str",  br.read_cstring(max_len=256))
    out["steam_app_id"] = read_field(br, "u32",  br.read_u32())
    out["yuplay_guid"]  = read_field(br, "str",  br.read_cstring(max_len=256))
    out["f0"]           = read_field(br, "f32",  br.read_f32())
    out["f1"]           = read_field(br, "f32",  br.read_f32())
    out["f2"]           = read_field(br, "f32",  br.read_f32())
    out["u_b"]          = read_field(br, "u32",  br.read_u32())
    out["u_c"]          = read_field(br, "u32",  br.read_u32())
    out["u_d"]          = read_field(br, "u32",  br.read_u32())
    out["u_e"]          = read_field(br, "u32",  br.read_u32())
    out["u_f"]          = read_field(br, "u32",  br.read_u32())
    out["u_g"]          = read_field(br, "u32",  br.read_u32())
    out["flag1"]        = read_field(br, "bool", br.read_bool())
    out["flag2"]        = read_field(br, "bool", br.read_bool())
    out["aura_def"]     = read_field(br, "str",  br.read_cstring(max_len=256))

    n = br.read_u32()
    out["ships"] = [
        {"name": read_field(br, "str",  br.read_cstring(max_len=256)),
         "f1":   read_field(br, "bool", br.read_bool()),
         "f2":   read_field(br, "bool", br.read_bool())} for _ in range(n)
    ]
    n = br.read_u32()
    out["decals"] = [read_field(br, "str", br.read_cstring(max_len=256))
                     for _ in range(n)]
    n = br.read_u32()
    out["list3"] = [read_field(br, "str", br.read_cstring(max_len=256))
                    for _ in range(n)]
    n = br.read_u32()
    out["items"] = [
        {"name": read_field(br, "str", br.read_cstring(max_len=256)),
         "a":    read_field(br, "u32", br.read_u32()),
         "b":    read_field(br, "u32", br.read_u32())} for _ in range(n)
    ]
    n = br.read_u32()
    out["qty_pairs"] = [
        (read_field(br, "i32", br.read_i32()),
         read_field(br, "i32", br.read_i32())) for _ in range(n)
    ]
    out["end_marker"] = read_field(br, "u64", br.read_u64())
    return out


def _read_pve_level_reward_modifiers(br: BitReader) -> list[dict]:
    """FUN_088fcea0 — `u32 count + count × {u32 a, u32 b, cstr256 name}`.
    Captures show {a,b} stepping in pairs over rank brackets for each of
    a handful of raid def names. Restores last_read_start to the u32
    count so an outer read_field() covers count + entries."""
    start = br.pos
    n = br.read_u32()
    items = [{"a":    read_field(br, "u32", br.read_u32()),
              "b":    read_field(br, "u32", br.read_u32()),
              "name": read_field(br, "str", br.read_cstring(max_len=256))}
             for _ in range(n)]
    br.last_read_start = start
    return items


def _read_brawl_schedule_entry(br: BitReader) -> dict:
    """FUN_088fe1c0 — `u32 count + count × {u32, u32} + cstr59` — one
    brawl-schedule entry: list of (threshold, reward_id) pairs plus a
    gameplay tag string. The per-entry reader looped by FUN_088fe450."""
    start = br.pos
    n = br.read_u32()
    pairs = [(read_field(br, "u32", br.read_u32()),
              read_field(br, "u32", br.read_u32())) for _ in range(n)]
    name = read_field(br, "str", br.read_cstring(max_len=59))
    br.last_read_start = start
    return {"pairs": pairs, "name": name}


def _read_brawl_schedule(br: BitReader) -> list[dict]:
    """FUN_088fe450 — 28 × _read_brawl_schedule_entry. The same reader the
    standalone SCMD_BRAWL_SCHEDULE (0x1f) packet uses; see the COMPOUND
    STRUCTURE note in the module docstring."""
    start = br.pos
    items = [_read_brawl_schedule_entry(br) for _ in range(28)]
    br.last_read_start = start
    return items


def _read_league_forbidden_equipment_bag(br: BitReader) -> dict:
    """FUN_082590e0 — clears the list at endpoint+0x193878 then
    Bag_Deserialize fills it. Same reader as the standalone
    SCMD_LEAGUE_FORBIDDEN_EQUIPMENT (0x22) packet — a flat
    `{item_def_name: bool}` set of items barred from league play."""
    return _read_bag(br)


def _read_zones_with_disabled_quests(br: BitReader) -> bytes:
    """FUN_0824ae10 → FUN_08b1db50 → BitStream_Read(buf, 0x201) — reads a
    513-bit fixed-size blob into the master-server cache at +0x2bb21c.
    Same on-wire payload as the standalone SCMD_ZONES_WITH_DISABLED_QUESTS
    (0x24) packet (which calls the same FUN_0824ae10).

    Returned as bytes — 65 bytes, MSB-aligned (the trailing 7 bits of
    byte 64 are padding from the bit-stream's perspective)."""
    nbits = 0x201
    start = br.pos
    raw = br.read_bits(nbits)
    out = raw.to_bytes((nbits + 7) // 8, "big")
    br.last_read_start = start
    return out


def _read_battle_pass_activation(br: BitReader) -> dict:
    """FUN_088d9700 — BattlePass::ReadActivationFromBitStream.
    `u64 token + u16 count + count × {u16 stage, u64 ts}`."""
    start = br.pos
    token = read_field(br, "u64", br.read_u64())
    n = br.read_u16()
    stages = [(read_field(br, "u16", br.read_u16()),
               read_field(br, "u64", br.read_u64())) for _ in range(n)]
    br.last_read_start = start
    return {"token": token, "stages": stages}


def _read_battle_pass_player_data(br: BitReader) -> dict:
    """FUN_088dd630 — BattlePass::PlayerData::ReadFromBitStream.
        u64 token
        u16 stage_count + count×{u16 + u16}
        u32 string_list_count + count×cstr59
        u32 timed_count + count×{u64 ts + u32 sub_count + sub_count×u16}
    """
    start = br.pos
    token = read_field(br, "u64", br.read_u64())
    n_stages = br.read_u16()
    stages = [(read_field(br, "u16", br.read_u16()),
               read_field(br, "u16", br.read_u16())) for _ in range(n_stages)]
    n_strings = br.read_u32()
    strings = [read_field(br, "str", br.read_cstring(max_len=59))
               for _ in range(n_strings)]
    n_timed = br.read_u32()
    timed = []
    for _ in range(n_timed):
        ts = read_field(br, "u64", br.read_u64())
        n_inner = br.read_u32()
        inner = [read_field(br, "u16", br.read_u16()) for _ in range(n_inner)]
        timed.append({"ts": ts, "items": inner})
    br.last_read_start = start
    return {"token": token, "stages": stages, "strings": strings, "timed": timed}


# ── Outer body parser ────────────────────────────────────────────────────────

class AcLoadInitialPlayerDataBody:
    """Bit-stream parse of AC_LOAD_INITIAL_PLAYER_DATA's body.

    See module-level docstring for the full field map. Public attributes
    are only set when successfully reached — the handler tolerates short
    bodies, so we stop cleanly on EOFError and leave the tail unset.
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self.raw: bytes = _io.read_bytes_full()
        self.ok = True
        self.error: str | None = None
        self.bits_read = 0

        if not self.raw:
            return

        br = BitReader(self.raw)
        try:
            # ── head ──────────────────────────────────────────────
            self.profile_revision   = read_field(br, "u64",  br.read_u64())
            self.format_version     = read_field(br, "u32",  br.read_u32())
            self.flag_a             = read_field(br, "bool", br.read_bool())
            self.head_account_field = read_field(br, "u32",  br.read_u32())
            self.flag_b             = read_field(br, "bool", br.read_bool())
            self.head_u64_zero      = read_field(br, "u64",  br.read_u64())
            self.head_text          = read_field(br, "str",
                                                 br.read_cstring(max_len=60))

            # ── bundle catalogue ──────────────────────────────────
            # Each section is `u32 count + count × BundleRecord`. Wrap the
            # whole section so the count u32 is included in the parent
            # node's range (the user can click "bundles_steam" and see
            # the count + every record highlighted).
            def _section() -> list[dict]:
                start = br.pos
                n = br.read_u32()
                recs = [_read_bundle_record(br) for _ in range(n)]
                br.last_read_start = start
                return recs

            self.bundles_steam  = read_field(br, "list", _section())
            self.bundles_yuplay = read_field(br, "list", _section())
            self.bundles_owned  = read_field(br, "list", _section())

            self.pve_level_reward_modifiers = read_field(
                br, "list", _read_pve_level_reward_modifiers(br))
            self.brawl_schedule_default     = read_field(
                br, "struct", _read_brawl_schedule_entry(br))
            self.brawl_schedule             = read_field(
                br, "list", _read_brawl_schedule(br))

            # ── tail: scalars + bags ──────────────────────────────
            # Wrap every bag/struct with read_field so the node's range
            # covers the count/header bytes too (clicking the bag node
            # highlights its u32 num_entries + entries, not just the
            # entries' union).
            self.reward_schedule_bag      = read_field(br, "bag", _read_bag(br))
            self.pve_scheduled_levels_bag = read_field(br, "bag", _read_bag(br))
            self.field_12         = read_field(br, "u32",  br.read_u32())
            self.flag_13          = read_field(br, "bool", br.read_bool())
            self.max_vessel_rank  = read_field(br, "u8",   br.read_u8())
            self.account_rank     = read_field(br, "u8",   br.read_u8())
            self.account_exp_pool = read_field(br, "i32",  br.read_i32())
            self.flag_17          = read_field(br, "bool", br.read_bool())
            self.leading_advert           = read_field(br, "bag", _read_bag(br))
            self.unlim_pve_mission_levels = read_field(br, "bag", _read_bag(br))
            self.field_20         = read_field(br, "i32",  br.read_i32())
            self.field_21         = read_field(br, "i32",  br.read_i32())
            self.flag_22          = read_field(br, "bool", br.read_bool())
            self.field_23         = read_field(br, "i32",  br.read_i32())
            self.field_24         = read_field(br, "u64",  br.read_u64())
            # FUN_082590e0 + battle-pass readers — invisible from the
            # outer-handler reader_calls list because they're called via
            # sub-helpers, but present in the wire stream. See COMPOUND
            # STRUCTURE in the module docstring — these are shared with
            # standalone SCMD packets.
            self.league_forbidden_equipment = read_field(
                br, "bag", _read_league_forbidden_equipment_bag(br))
            self.battle_pass_activation     = read_field(
                br, "struct", _read_battle_pass_activation(br))
            self.battle_pass_player_data    = read_field(
                br, "struct", _read_battle_pass_player_data(br))
            self.field_25         = read_field(br, "i32",  br.read_i32())
            self.flag_26          = read_field(br, "bool", br.read_bool())
            self.bag_27           = read_field(br, "bag", _read_bag(br))
            # 513-bit blob shared with SCMD_ZONES_WITH_DISABLED_QUESTS.
            self.zones_with_disabled_quests = read_field(
                br, "blob", _read_zones_with_disabled_quests(br))
        except EOFError as e:
            self.ok = False
            self.error = f"EOFError {e}\n {traceback.format_exc()}"
        except Exception as e:
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"
        self.bits_read = br.pos

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if not self.raw:
            return "AcLoadInitialPlayerDataBody(empty body)"

        lines: list[str] = [f"AcLoadInitialPlayerDataBody({len(self.raw)}B"]
        if self.error:
            lines[0] += f" err={self.error}"
        if not self.ok and not self.error:
            lines[0] += " truncated"

        # ── head scalars on one line ────────────────────────────────────
        head_parts = []
        for name in ("profile_revision", "format_version", "flag_a",
                     "head_account_field", "flag_b", "head_u64_zero",
                     "head_text"):
            if name in self.__dict__:
                head_parts.append(f"{name}={getattr(self, name).value!r}")
        if head_parts:
            lines.append("  " + " ".join(head_parts))

        # ── bundle catalogue: every record on its own line ─────────────
        for sec in ("steam", "yuplay", "owned"):
            attr = getattr(self, f"bundles_{sec}", None)
            if attr is None:
                continue
            recs = attr.value
            lines.append(f"  bundles_{sec} ({len(recs)}):")
            for i, r in enumerate(recs):
                lines.append(f"    [{i}] {_fmt_bundle(r)}")

        # ── pve_level_reward_modifiers + reward schedules ──────────────
        if "pve_level_reward_modifiers" in self.__dict__:
            recs = self.pve_level_reward_modifiers.value
            lines.append(f"  pve_level_reward_modifiers ({len(recs)}):")
            for i, r in enumerate(recs):
                lines.append(f"    [{i}] a={r['a'].value} b={r['b'].value} "
                             f"name={r['name'].value!r}")
        if "brawl_schedule_default" in self.__dict__:
            rd = self.brawl_schedule_default.value
            pairs = [(a.value, b.value) for a, b in rd["pairs"]]
            lines.append(
                f"  brawl_schedule_default: pairs={pairs} "
                f"name={rd['name'].value!r}")
        if "brawl_schedule" in self.__dict__:
            recs = self.brawl_schedule.value
            lines.append(f"  brawl_schedule ({len(recs)}):")
            for i, r in enumerate(recs):
                pairs = [(a.value, b.value) for a, b in r["pairs"]]
                lines.append(
                    f"    [{i:2}] name={r['name'].value!r:25} pairs={pairs}")

        # ── tail bags (each on its own line) ───────────────────────────
        for name in ("reward_schedule_bag", "pve_scheduled_levels_bag"):
            if name in self.__dict__:
                lines.append(f"  {name}={format_bag(getattr(self, name).value)}")

        # ── tail scalars line ──────────────────────────────────────────
        tail1 = []
        for name in ("field_12", "flag_13", "max_vessel_rank",
                     "account_rank", "account_exp_pool", "flag_17"):
            if name in self.__dict__:
                tail1.append(f"{name}={getattr(self, name).value!r}")
        if tail1:
            lines.append("  " + " ".join(tail1))

        for name in ("leading_advert", "unlim_pve_mission_levels"):
            if name in self.__dict__:
                lines.append(f"  {name}={format_bag(getattr(self, name).value)}")

        tail2 = []
        for name in ("field_20", "field_21", "flag_22", "field_23",
                     "field_24"):
            if name in self.__dict__:
                tail2.append(f"{name}={getattr(self, name).value!r}")
        if tail2:
            lines.append("  " + " ".join(tail2))

        if "league_forbidden_equipment" in self.__dict__:
            lines.append(
                "  league_forbidden_equipment="
                f"{format_bag(self.league_forbidden_equipment.value)}")

        if "battle_pass_activation" in self.__dict__:
            bp = self.battle_pass_activation.value
            stages = [(s.value, t.value) for s, t in bp["stages"]]
            lines.append(
                f"  battle_pass_activation: token={bp['token'].value} "
                f"stages={stages}")
        if "battle_pass_player_data" in self.__dict__:
            bp = self.battle_pass_player_data.value
            stages = [(a.value, b.value) for a, b in bp["stages"]]
            strings = [s.value for s in bp["strings"]]
            timed = [{"ts": e["ts"].value,
                      "items": [x.value for x in e["items"]]}
                     for e in bp["timed"]]
            lines.append(
                f"  battle_pass_player_data: token={bp['token'].value} "
                f"stages={stages} strings={strings} timed={timed}")

        tail3 = []
        for name in ("field_25", "flag_26"):
            if name in self.__dict__:
                tail3.append(f"{name}={getattr(self, name).value!r}")
        if tail3:
            lines.append("  " + " ".join(tail3))

        if "bag_27" in self.__dict__:
            lines.append(f"  bag_27={format_bag(self.bag_27.value)}")
        if "zones_with_disabled_quests" in self.__dict__:
            blob = self.zones_with_disabled_quests.value
            lines.append(
                f"  zones_with_disabled_quests={blob.hex()}  "
                f"({len(blob)} bytes, 513 bits)")

        return "\n".join(lines) + "\n)"


# ── repr helpers ────────────────────────────────────────────────────────────

def _fmt_bundle(r: dict) -> str:
    """One-line rendering of a BundleRecord with every field present.
    Each value in `r` is a Variant; we read `.value` for the human form."""
    def v(key):                                # short helper
        return r[key].value
    ships = [{"name": s["name"].value,
              "f1":   s["f1"].value,
              "f2":   s["f2"].value} for s in r["ships"]]
    decals = [s.value for s in r["decals"]]
    list3  = [s.value for s in r["list3"]]
    items  = [{"name": it["name"].value,
               "a":    it["a"].value,
               "b":    it["b"].value} for it in r["items"]]
    qty_pairs = [(a.value, b.value) for a, b in r["qty_pairs"]]
    return (
        f"def_name={v('def_name')!r} steam_app_id={v('steam_app_id')} "
        f"yuplay_guid={v('yuplay_guid')!r} "
        f"f=({v('f0')},{v('f1')},{v('f2')}) "
        f"u=({v('u_b')},{v('u_c')},{v('u_d')},"
        f"{v('u_e')},{v('u_f')},{v('u_g')}) "
        f"flag1={v('flag1')} flag2={v('flag2')} "
        f"aura_def={v('aura_def')!r} "
        f"ships={ships} decals={decals} list3={list3} "
        f"items={items} qty_pairs={qty_pairs} "
        f"end_marker={v('end_marker')}"
    )
