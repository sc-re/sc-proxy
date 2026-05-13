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

   reward_schedule_default      FUN_088fe1c0 — single
                                `u32 count + count × {u32, u32} + cstr59`
                                with one (17, 18) pair and empty name.

   reward_schedule_per_gameplay FUN_088fe450 — `28 × FUN_088fe1c0`,
                                one per gameplay mode (Gameplay enum,
                                `ai.Gameplay.NUM == 32`). Each record
                                lists reward-tier thresholds for that
                                gameplay (e.g. (1,2)(9,10)(15,16) for
                                'gtdm').

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
   bag    event_item_unlocks           bool flags keyed by item def, e.g.
                                       'Weapon_Minigun_NY_T3' = true.
                                       (FUN_082590e0 wraps Bag_Deserialize
                                       writing to endpoint+0x193878 — these
                                       are unrolled event-pack contents.)
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
   u8     field_28

The handler tolerates short bodies via its lastReadOK flag: every reader
returns 0 instead of throwing once the stream runs out. We mirror that
by catching EOFError and leaving later fields unset.
"""
from __future__ import annotations
from typing import Any

from notification import BitReader, _read_bag, format_bag


# ── Sub-readers ──────────────────────────────────────────────────────────────

def _read_bundle_record(br: BitReader) -> dict:
    """FUN_088fc1e0 — one BundleRecord. Used by bundles_steam, bundles_yuplay
    and bundles_owned in a loop. See file docstring for field semantics."""
    out: dict[str, Any] = {}
    out["def_name"]      = br.read_cstring(max_len=256)
    out["steam_app_id"]  = br.read_u32()
    out["yuplay_guid"]   = br.read_cstring(max_len=256)
    out["f0"]            = br.read_f32()
    out["f1"]            = br.read_f32()
    out["f2"]            = br.read_f32()
    out["u_b"]           = br.read_u32()
    out["u_c"]           = br.read_u32()
    out["u_d"]           = br.read_u32()
    out["u_e"]           = br.read_u32()
    out["u_f"]           = br.read_u32()
    out["u_g"]           = br.read_u32()
    out["flag1"]         = br.read_bool()
    out["flag2"]         = br.read_bool()
    out["aura_def"]      = br.read_cstring(max_len=256)

    n = br.read_u32()
    out["ships"] = [
        {"name": br.read_cstring(max_len=256),
         "f1": br.read_bool(),
         "f2": br.read_bool()} for _ in range(n)
    ]
    n = br.read_u32()
    out["decals"] = [br.read_cstring(max_len=256) for _ in range(n)]
    n = br.read_u32()
    out["list3"] = [br.read_cstring(max_len=256) for _ in range(n)]
    n = br.read_u32()
    out["items"] = [
        {"name": br.read_cstring(max_len=256),
         "a": br.read_u32(),
         "b": br.read_u32()} for _ in range(n)
    ]
    n = br.read_u32()
    out["qty_pairs"] = [(br.read_i32(), br.read_i32()) for _ in range(n)]
    out["end_marker"] = br.read_u64()
    return out


def _read_pve_level_reward_modifiers(br: BitReader) -> list[dict]:
    """FUN_088fcea0 — `u32 count + count × {u32 a, u32 b, cstr256 name}`.
    Captures show {a,b} stepping in pairs over rank brackets for each of
    a handful of raid def names."""
    n = br.read_u32()
    return [{"a": br.read_u32(),
             "b": br.read_u32(),
             "name": br.read_cstring(max_len=256)} for _ in range(n)]


def _read_reward_schedule_entry(br: BitReader) -> dict:
    """FUN_088fe1c0 — `u32 count + count × {u32, u32} + cstr59` — one
    reward-tier schedule entry: list of (threshold, reward_id) pairs
    plus a gameplay tag string."""
    n = br.read_u32()
    pairs = [(br.read_u32(), br.read_u32()) for _ in range(n)]
    name = br.read_cstring(max_len=59)
    return {"pairs": pairs, "name": name}


def _read_reward_schedule_per_gameplay(br: BitReader) -> list[dict]:
    """FUN_088fe450 — 28 × _read_reward_schedule_entry — fixed-size array
    of reward schedules, one per gameplay mode."""
    return [_read_reward_schedule_entry(br) for _ in range(28)]


def _read_event_item_unlocks_bag(br: BitReader) -> dict:
    """FUN_082590e0 — wraps Bag_Deserialize, writing into a bag at
    endpoint+0x193878. Observed as a flat `{item_def_name: bool}` map
    of event-tier item unlocks (e.g. 'Weapon_Minigun_NY_T3': True)."""
    return _read_bag(br)


def _read_battle_pass_activation(br: BitReader) -> dict:
    """FUN_088d9700 — BattlePass::ReadActivationFromBitStream.
    `u64 token + u16 count + count × {u16 stage, u64 ts}`."""
    token = br.read_u64()
    n = br.read_u16()
    stages = [(br.read_u16(), br.read_u64()) for _ in range(n)]
    return {"token": token, "stages": stages}


def _read_battle_pass_player_data(br: BitReader) -> dict:
    """FUN_088dd630 — BattlePass::PlayerData::ReadFromBitStream.
        u64 token
        u16 stage_count + count×{u16 + u16}
        u32 string_list_count + count×cstr59
        u32 timed_count + count×{u64 ts + u32 sub_count + sub_count×u16}
    """
    token = br.read_u64()
    n_stages = br.read_u16()
    stages = [(br.read_u16(), br.read_u16()) for _ in range(n_stages)]
    n_strings = br.read_u32()
    strings = [br.read_cstring(max_len=59) for _ in range(n_strings)]
    n_timed = br.read_u32()
    timed = []
    for _ in range(n_timed):
        ts = br.read_u64()
        n_inner = br.read_u32()
        inner = [br.read_u16() for _ in range(n_inner)]
        timed.append({"ts": ts, "items": inner})
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
            self.profile_revision     = br.read_u64()
            self.format_version       = br.read_u32()
            self.flag_a               = br.read_bool()
            self.head_account_field   = br.read_u32()
            self.flag_b               = br.read_bool()
            self.head_u64_zero        = br.read_u64()
            self.head_text            = br.read_cstring(max_len=60)

            # ── bundle catalogue ──────────────────────────────────
            n = br.read_u32()
            self.bundles_steam_count = n
            self.bundles_steam = [_read_bundle_record(br) for _ in range(n)]

            n = br.read_u32()
            self.bundles_yuplay_count = n
            self.bundles_yuplay = [_read_bundle_record(br) for _ in range(n)]

            n = br.read_u32()
            self.bundles_owned_count = n
            self.bundles_owned = [_read_bundle_record(br) for _ in range(n)]

            self.pve_level_reward_modifiers   = _read_pve_level_reward_modifiers(br)
            self.reward_schedule_default      = _read_reward_schedule_entry(br)
            self.reward_schedule_per_gameplay = _read_reward_schedule_per_gameplay(br)

            # ── tail: scalars + bags ──────────────────────────────
            self.reward_schedule_bag      = _read_bag(br)
            self.pve_scheduled_levels_bag = _read_bag(br)
            self.field_12         = br.read_u32()
            self.flag_13          = br.read_bool()
            self.max_vessel_rank  = br.read_u8()
            self.account_rank     = br.read_u8()
            self.account_exp_pool = br.read_i32()
            self.flag_17          = br.read_bool()
            self.leading_advert            = _read_bag(br)
            self.unlim_pve_mission_levels  = _read_bag(br)
            self.field_20         = br.read_i32()
            self.field_21         = br.read_i32()
            self.flag_22          = br.read_bool()
            self.field_23         = br.read_i32()
            self.field_24         = br.read_u64()
            # FUN_082590e0 + battle-pass readers — invisible from the
            # outer-handler reader_calls list because they're called via
            # sub-helpers, but present in the wire stream.
            self.event_item_unlocks         = _read_event_item_unlocks_bag(br)
            self.battle_pass_activation     = _read_battle_pass_activation(br)
            self.battle_pass_player_data    = _read_battle_pass_player_data(br)
            self.field_25         = br.read_i32()
            self.flag_26          = br.read_bool()
            self.bag_27           = _read_bag(br)
            self.field_28         = br.read_u8()
        except EOFError:
            self.ok = False
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
                head_parts.append(f"{name}={getattr(self, name)!r}")
        if head_parts:
            lines.append("  " + " ".join(head_parts))

        # ── bundle catalogue: every record on its own line ─────────────
        for sec in ("steam", "yuplay", "owned"):
            recs = getattr(self, f"bundles_{sec}", None)
            cnt  = getattr(self, f"bundles_{sec}_count", None)
            if recs is None:
                continue
            lines.append(f"  bundles_{sec} ({cnt}):")
            for i, r in enumerate(recs):
                lines.append(f"    [{i}] {_fmt_bundle(r)}")

        # ── pve_level_reward_modifiers + reward schedules ──────────────
        if "pve_level_reward_modifiers" in self.__dict__:
            recs = self.pve_level_reward_modifiers
            lines.append(f"  pve_level_reward_modifiers ({len(recs)}):")
            for i, r in enumerate(recs):
                lines.append(f"    [{i}] a={r['a']} b={r['b']} name={r['name']!r}")
        if "reward_schedule_default" in self.__dict__:
            rd = self.reward_schedule_default
            lines.append(
                f"  reward_schedule_default: pairs={rd['pairs']} name={rd['name']!r}")
        if "reward_schedule_per_gameplay" in self.__dict__:
            recs = self.reward_schedule_per_gameplay
            lines.append(f"  reward_schedule_per_gameplay ({len(recs)}):")
            for i, r in enumerate(recs):
                lines.append(
                    f"    [{i:2}] name={r['name']!r:25} pairs={r['pairs']}")

        # ── tail bags (each on its own line) ───────────────────────────
        for name in ("reward_schedule_bag", "pve_scheduled_levels_bag"):
            if name in self.__dict__:
                lines.append(f"  {name}={format_bag(getattr(self, name))}")

        # ── tail scalars line ──────────────────────────────────────────
        tail1 = []
        for name in ("field_12", "flag_13", "max_vessel_rank",
                     "account_rank", "account_exp_pool", "flag_17"):
            if name in self.__dict__:
                tail1.append(f"{name}={getattr(self, name)!r}")
        if tail1:
            lines.append("  " + " ".join(tail1))

        for name in ("leading_advert", "unlim_pve_mission_levels"):
            if name in self.__dict__:
                lines.append(f"  {name}={format_bag(getattr(self, name))}")

        tail2 = []
        for name in ("field_20", "field_21", "flag_22", "field_23",
                     "field_24"):
            if name in self.__dict__:
                tail2.append(f"{name}={getattr(self, name)!r}")
        if tail2:
            lines.append("  " + " ".join(tail2))

        if "event_item_unlocks" in self.__dict__:
            lines.append(
                f"  event_item_unlocks={format_bag(self.event_item_unlocks)}")

        if "battle_pass_activation" in self.__dict__:
            bp = self.battle_pass_activation
            lines.append(
                f"  battle_pass_activation: token={bp['token']} "
                f"stages={bp['stages']}")
        if "battle_pass_player_data" in self.__dict__:
            bp = self.battle_pass_player_data
            lines.append(
                f"  battle_pass_player_data: token={bp['token']} "
                f"stages={bp['stages']} strings={bp['strings']} "
                f"timed={bp['timed']}")

        tail3 = []
        for name in ("field_25", "flag_26"):
            if name in self.__dict__:
                tail3.append(f"{name}={getattr(self, name)!r}")
        if tail3:
            lines.append("  " + " ".join(tail3))

        if "bag_27" in self.__dict__:
            lines.append(f"  bag_27={format_bag(self.bag_27)}")
        if "field_28" in self.__dict__:
            lines.append(f"  field_28={self.field_28!r}")

        return "\n".join(lines) + "\n)"


# ── repr helpers ────────────────────────────────────────────────────────────

def _fmt_bundle(r: dict) -> str:
    """One-line rendering of a BundleRecord with every field present."""
    return (
        f"def_name={r['def_name']!r} steam_app_id={r['steam_app_id']} "
        f"yuplay_guid={r['yuplay_guid']!r} "
        f"f=({r['f0']},{r['f1']},{r['f2']}) "
        f"u=({r['u_b']},{r['u_c']},{r['u_d']},"
        f"{r['u_e']},{r['u_f']},{r['u_g']}) "
        f"flag1={r['flag1']} flag2={r['flag2']} "
        f"aura_def={r['aura_def']!r} "
        f"ships={r['ships']} decals={r['decals']} list3={r['list3']} "
        f"items={r['items']} qty_pairs={r['qty_pairs']} "
        f"end_marker={r['end_marker']}"
    )
