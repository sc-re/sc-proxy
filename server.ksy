meta:
  id: star_conflict_package_server
  application: Star Conflict
  endian: be
seq:
  - id: packet_type
    type: s2be
  - id: body
    type:
      switch-on: packet_type
      cases:
        0: ac_load_initial_player_data
        1: ac_server_info
        2: ac_enter_mm_queue
        3: ac_leave_mm_queue
        4: ac_mm_info
        5: ac_enter_tournament
        6: ac_leave_tournament
        7: ac_get_userdata
        8: ac_set_userdata
        9: ac_player_credentials
        10: ac_player_credits
        11: ac_player_stats
        12: ac_player_arc_balance
        13: ac_titles_set_active
        14: ac_avatars_set_active
        15: ac_mottos_set_active
        16: ac_choose_starting_station
        17: ac_change_player_nickname
        18: ac_steam_user_info
        19: ac_premium_info
        20: ac_premium_buy
        21: ac_account_auras
        22: ac_add_account_aura
        23: ac_cancel_account_aura
        24: ac_quests
        25: ac_quest_accept
        26: ac_quest_change
        27: ac_quest_complete
        28: ac_quest_complete_all
        29: ac_ship_quests
        30: ac_ship_quest_start
        31: ac_ship_quest_change
        32: ac_ship_quest_end
        33: ac_rewarded_tutorials
        34: ac_reward_tutorial
        35: ac_player_inventory
        36: ac_player_autogen_inventory
        37: ac_player_vessels
        38: ac_vessel_equipment
        39: ac_buy_item
        40: ac_sell_item
        41: ac_sell_items
        42: ac_enchant_item
        43: ac_salvage_item
        44: ac_salvage_items
        45: ac_upgrade_items
        46: ac_upgrade_autogen_item
        47: ac_craft_upgrade_item
        48: ac_find_autogen_item
        49: ac_activate_resource_vessel
        50: ac_sell_vessel
        51: ac_vessel_change_equip
        52: ac_vessel_change_equip_multi
        53: ac_vessel_cheat_change_equip
        54: ac_vessel_transfer_equip
        55: ac_vessel_strip_equip
        56: ac_vessel_change_munition
        57: ac_vessel_refill_munition
        58: ac_vessel_transfer_munition
        59: ac_vessel_autogen_destroy
        60: ac_vessel_autogen_dismantle
        61: ac_vessel_extract_exp
        62: ac_vessel_levelup
        63: ac_vessel_repair
        64: ac_vessel_repair_battle
        65: ac_vessel_refill_battle
        66: ac_vessel_strip_improper_battle
        67: ac_vessel_free_custom_elements
        68: ac_vessel_custom_elements_buy
        69: ac_vessel_custom_elements_acknowledge_expiration
        70: ac_vessel_craft
        71: ac_vessel_recraft
        72: ac_vessel_budget_levelup
        73: ac_vessel_budget_activate
        74: ac_vessel_unlock_node
        75: ac_vessel_activate_node
        76: ac_battle_slots
        77: ac_battle_slot_change_vessel
        78: ac_battle_slot_swap_vessels
        79: ac_battle_slot_cheat_change_vessel
        80: ac_inv_ext_buy
        81: ac_autogen_inv_ext_buy
        82: ac_exchange_gold
        83: ac_buy_gold
        84: ac_buy_arc_dlc
        85: ac_talents_acquire
        86: ac_talents_update
        87: ac_talents_reset
        88: ac_talents_assign_sets
        89: ac_buy_talent_set
        90: ac_react_on_abandoned_game
        91: ac_squad_info
        92: ac_squad_invite_accept
        93: ac_squad_invite_decline
        94: ac_squad_leave
        95: ac_squad_invite_send
        96: ac_squad_invite_cancel
        97: ac_squad_kick
        98: ac_squad_ready
        99: ac_squad_convert_to_wing
        100: ac_league_team_info
        101: ac_league_team_create
        102: ac_league_team_invite_send
        103: ac_league_team_invite_cancel
        104: ac_league_team_invite_accept
        105: ac_league_team_kick
        106: ac_league_team_leave
        107: ac_league_team_invite_decline
        108: ac_league_team_request_names
        109: ac_get_nicknames
        110: ac_get_uids
        111: ac_report_player
        112: ac_update_yup_purchases
        113: ac_check_yup_purchases
        114: ac_update_dlc_ownership
        115: ac_friends_send_request
        116: ac_friends_accept_request
        117: ac_friends_reject_request
        118: ac_friends_remove
        119: ac_friends_list
        120: ac_social_ignore_add
        121: ac_social_ignore_remove
        122: ac_social_watch_add
        123: ac_social_watch_remove
        124: ac_social_suggest_steam
        125: ac_social_suggest_fb
        126: ac_social_suggest_vk
        127: ac_teaching_list
        128: ac_teaching_request_to_teacher
        129: ac_teaching_request_to_student
        130: ac_teaching_accept
        131: ac_teaching_reject
        132: ac_teaching_check
        133: ac_teaching_allow
        134: ac_referrals
        135: ac_set_referrer
        136: ac_obtain_referral_key
        137: ac_attach_steam_account
        138: ac_finalize_steam_mtxn
        139: ac_attach_yup_account
        140: ac_attach_email
        141: ac_lobby_list
        142: ac_lobby_join
        143: ac_lobby_create
        144: ac_lobby_info
        145: ac_lobby_kick
        146: ac_lobby_leave
        147: ac_lobby_invite
        148: ac_lobby_modify
        149: ac_lobby_start_game
        150: ac_lobby_group_list
        151: ac_lobby_group_info
        152: ac_lobby_group_create
        153: ac_lobby_group_modify
        154: ac_lobby_group_delete
        155: ac_lobby_group_joinreq_create
        156: ac_lobby_group_joinreq_cancel
        157: ac_lobby_group_joinreq_reject
        158: ac_clan_request_credentials
        159: ac_clan_request_desc
        160: ac_clan_request_profile
        161: ac_clan_joinreq_create
        162: ac_clan_joinreq_cancel
        163: ac_clan_joinreq_accept
        164: ac_clan_invite_send
        165: ac_clan_invite_accept
        166: ac_clan_invite_cancel
        167: ac_clan_kick
        168: ac_clan_leave
        169: ac_clan_set_role
        170: ac_clan_change_motd
        171: ac_clan_change_desc
        172: ac_clan_change_recruiting
        173: ac_clan_resource_convert
        174: ac_clan_ship_build
        175: ac_clan_ship_boost_building
        176: ac_clan_ship_repair
        177: ac_clan_ship_boost_repairing
        178: ac_clan_ship_fit
        179: ac_clan_ship_set_current
        180: ac_clan_universe_move
        181: ac_clan_set_civilian_zone
        182: ac_clan_revive_in_war
        183: ac_clan_war_start
        184: ac_clan_quest_accept
        185: ac_clan_create
        186: ac_clan_upgrade
        187: ac_clan_change_name
        188: ac_clan_change_tag
        189: ac_clan_assign_emblem
        190: ac_clan_bank_transfer
        191: ac_clan_list_recruiting
        192: ac_clan_history_get
        193: ac_related_quest_enable
        194: ac_user_profile_get
        195: ac_achievements
        196: ac_admin_cmd
        197: ac_games_info
        198: ac_zone_instances_info
        199: ac_get_punishments
        200: ac_welcome_msg
        201: ac_motd
        202: ac_survey_get_new
        203: ac_survey_vote
        204: ac_survey_results
        205: ac_universe_get
        206: ac_universe_counters
        207: ac_warmap_get
        208: ac_mail_get
        209: ac_mail_deliver
        210: ac_mail_send
        211: ac_mail_remove
        212: ac_mail_acknowledge_expiration
        213: ac_send_early_player_log
        214: ac_auto_pilot_space_station
        215: ac_undock_space_station
        216: ac_set_visited_zone
        217: ac_zone_coordinator_gm_command
        218: ac_space_stations_population
        219: ac_karma_reset
        220: ac_faction_rep_reset
        221: ac_leaderboard_get
        222: ac_leaderboard_get_descs
        223: ac_set_fb_token
        224: ac_get_fb_token
        225: ac_log_fb_event
        226: ac_get_craft_resources
        227: ac_use_blueprint
        228: ac_sell_craft_resource
        229: ac_sell_craft_resources
        230: ac_get_blueprints
        231: ac_learn_blueprint
        232: ac_get_free_space_save_data
        233: ac_disassemble_item
        234: ac_add_thumb_up
        235: ac_get_visited_free_space_zones
        236: ac_advert_create
        237: ac_advert_delete
        238: ac_advert_header_get
        239: ac_advert_get
        240: ac_buy_product_from_advert
        241: ac_emm_change_ready
        242: ac_unlim_pve_upgrade_player_level
        243: ac_unlim_pve_disable_player_buffs
        244: ac_ta_stats_send_tutorial_entter
        245: ac_ta_stats_send_tutorial_exit
        246: ac_user_notes
        247: ac_user_notes_add
        248: ac_user_notes_delete
        249: ac_battle_pass_unlock_level
        250: ac_zones_lua_active_events_update
        251: ac_adventures
        252: ac_adventure_cancel
        # High-range types seen in open-space / zone sessions
        0x0400: zone_instance_join     # zone instance join notification (9B short or 1097B long)
        0x0500: zone_stats_list        # zone stat counters: munitionTransfered, credits, etc.
        0x0504: zone_player_health     # zone player health/shield floats (70B)
        0x0700: zone_player_data       # player presence (10B) or full stats (78B)
        0x0900: zone_player_update     # player credits/status update in zone (13B)
        0x0a00: zone_player_join       # player join notification in zone (13B)
        0x0c00: zone_membership        # zone membership event (26B)
        0x3233: zone_server_23         # server addr 23.x.x.x + port (30B)
        0x3600: zone_kv_data           # open-space K-V stream: tier/auras/bundles (376B)
        0x3700: zone_player_list       # player list in zone (283B)
        0x3839: zone_server_89         # server addr 89.x.x.x + port (29B)
        0x6200: zone_military_rank     # militaryRank updates, count=3 entries (49B)
        0x6800: zone_player_status     # brief player status: 3B id + varying value (19B)
types:
  ac_load_initial_player_data:
    doc: |
      Initial player-state snapshot, sent S→C right after login. The
      handler at 0x0823103b reads the body as a single bit-stream:

        head      : profile_revision (u64), format_version (u32, =2),
                    flags, head_account_field (u32), head_text (cstr60)
        catalogue : 3 BundleRecord arrays — bundles_steam (~320),
                    bundles_yuplay (~455), bundles_owned (~6) —
                    populating the player's purchasable / owned DLC list
        rotation  : pve_level_reward_modifiers, reward_schedule_default,
                    reward_schedule_per_gameplay (28 fixed slots)
        tail      : reward_schedule + pve_scheduled_levels bags,
                    max_vessel_rank (u8), account_rank (u8),
                    account_exp_pool (i32, "Clearance Score"),
                    leading_advert bag (MasterServer_GetLeadingAdvertInfo),
                    event_item_unlocks bag, BattlePass activation + player
                    data, plus a per-gameplay scripted-event progress bag

      Sizes range from 2B (echo-only) and 8B (truncated short form —
      handler tolerates short reads via its lastReadOK flag) up to
      ~240 kB full state. Decoded by the ac_load_initial_player_data_body
      opaque type which mirrors the binary's read sequence and stops
      cleanly on EOFError when bodies are truncated.
    seq:
    - id: data
      type: ac_load_initial_player_data_body
  ac_server_info:
    doc: |
      Server metadata. The 20-byte canonical form is memcpy'd verbatim
      into a singleton struct at 0x096285b4 from which Lua binding
      MasterServer_GetServerInfo (fn at 0x086ff780) reads field-by-field.
      Unlike most AC packets on this channel the scalar fields are
      LITTLE-ENDIAN — the client reads them with native x86 loads
      (fldl/mov), so the wire bytes are whatever the server had in memory.

      Short-form variants also appear on this type code (e.g. 14-byte and
      6-byte bodies) which look like periodic status updates with a
      different shape; the fields below are gated on remaining bytes so
      those don't fail to parse.
    seq:
    - id: server_time_ms
      type: f8le
      if: '_io.size - _io.pos >= 8'
      doc: |
        Milliseconds since the Unix epoch, as an IEEE 754 double (LE).
        Lua binding truncates it to int64 and exposes it as `serverTime`.
    - id: unknown_8
      size: 4
      if: '_io.size - _io.pos >= 4'
      doc: |
        4 bytes not surfaced by MasterServer_GetServerInfo. Differs per
        session (observed 0x0bd18549 and 0xf7398e49). Possibly a session
        token / world ID.
    - id: sandbox_access
      type: u4le
      if: '_io.size - _io.pos >= 4'
      doc: |
        Sandbox access level. Lua exposes both `sandboxAccess` (raw value)
        and `sandboxDisabled` (= sandboxAccess == 0). Observed: 4.
    - id: mm_disabled
      type: u1
      if: '_io.size - _io.pos >= 1'
    - id: mm_enable_pve_raids
      type: u1
      if: '_io.size - _io.pos >= 1'
    - id: mm_enable_league
      type: u1
      if: '_io.size - _io.pos >= 1'
    - id: mm_enable_coop_vs_ai
      type: u1
      if: '_io.size - _io.pos >= 1'
    - id: tail
      size-eos: true
      doc: Extra bytes on short-form variants (status updates).
  ac_enter_mm_queue:
    doc: Matchmaking queue update; flags=0x80 means queued
    seq:
    - id: flags
      type: u1
    - id: queue_id
      type: u4be
    - id: slot
      type: u1
  ac_leave_mm_queue:
    doc: |
      2B echo + 2B status. Observed: 0xc240 (normal leave), 0x8000 (queue closed).
      The status is a bit-packed field; exact bit layout not reversed.
    seq:
    - id: status
      type: u2be
  ac_mm_info:
    doc: |
      Matchmaking queue state. Handler 0x08231dbc reads two 1-bit bools
      then a property bag (ReadBool, ReadBool, Bag_Deserialize). The two
      leading bits leave the bag bit-misaligned, so it can't be modelled
      with the byte-aligned bag_payload — decoded by
      ac_mm_info_body.AcMmInfoBody. The bag carries clientsInQueue,
      averageTimeInQueue, maxTimeInQueue, playersByMMValue, etc.
    seq:
    - id: data
      type: ac_mm_info_body
      size-eos: true
  ac_enter_tournament:
    doc: Tournament entry ACK — u8 status + bag of state.
    seq:
    - id: status
      type: u1
    - id: bag
      type: bag_payload
  ac_leave_tournament:
    seq:
    - id: unknown
      size-eos: true
  ac_get_userdata:
    doc: User-data dict (UI layout, preferences) — bag.
    seq:
    - id: bag
      type: bag_payload
  ac_set_userdata:
    seq:
    - id: unknown
      type: u2be
    - id: value
      type: u2be
  ac_player_credentials:
    doc: |
      Player nickname and session credentials. Handler 0x082305c7 reads
      (bit-stream order): nickname (NUL-terminated), flag1 (u8 byte,
      always 1), steam_id64 (SteamID64, 0 if not Steam-linked), account_id
      (stable 64-bit account id), level (small account-progress level),
      flag2 (a single-BIT bool — ReadBool @8b1b6d0), then a trailing
      property bag. Because flag2 is 1 bit, the bag is read bit-misaligned
      (shifted 1 bit) with up to 7 padding bits at the end, so this can't
      be modelled with native byte-aligned kaitai — decoded by
      ac_player_credentials_body.AcPlayerCredentialsBody. Verified against
      all 96 captures (flag1=1, flag2=0, bag empty).
    seq:
    - id: data
      type: ac_player_credentials_body
      size-eos: true
  ac_player_credits:
    doc: |
      Player wallet snapshot. Handler 0x08231c56 → FUN_088e9ec0 reads
      a u16 flag word then byte-aligned per-bit currency balances:
      bit 1 → credits, bit 2 → goldCredits, bit 3 → iridium,
      bit 4 → xenochips + premium_time (premium-expiry ms timestamp),
      bit 5 → vid, bit 6 → freeSynergy (free experience — confirmed
      against FUN_088e9ec0, a u32 read at flag 0x40; previously
      mislabeled "premium"), bit 7 → faction_rep (5 × u32 reputation,
      previously mislabeled "craft resources"). All fields are
      byte-sized so the layout maps cleanly to native kaitai.
    seq:
    - id: flags
      type: u2be
    - id: credits
      type: u8be
      if: 'flags & 0x02 != 0'
    - id: gold_credits
      type: u8be
      if: 'flags & 0x04 != 0'
    - id: iridium
      type: u8be
      if: 'flags & 0x08 != 0'
    - id: xenochips
      type: u8be
      if: 'flags & 0x10 != 0'
    - id: premium_time
      doc: Premium-expiry timestamp in ms (paired with xenochips under bit 4).
      type: u8be
      if: 'flags & 0x10 != 0'
    - id: vid
      type: u8be
      if: 'flags & 0x20 != 0'
    - id: free_synergy
      doc: Free synergy / free experience (not bound to a ship).
      type: u4be
      if: 'flags & 0x40 != 0'
    - id: faction_rep
      doc: |
        Per-faction reputation points, indexed by ai.Faction (cosmos_constants.lua):
        [0]=Empire, [1]=Federation, [2]=Jericho, [3]=Enclave, [4]=Cyber_2 (Ellydium).
        Read into the profile's u32[5] at +0xada04 (the array GetFactionRep(i) indexes).
        Values are raw reputation matching the rank thresholds in reputation.lua
        (e.g. 3800000 = FieldMarshal, 0 = Private). Was mislabeled "craft_resources".
      type: u4be
      repeat: expr
      repeat-expr: 5
      if: 'flags & 0x80 != 0'
  ac_player_stats:
    doc: 92B FIXED. Player stat record encoded as a bag.
    seq:
    - id: bag
      type: bag_payload
  ac_player_arc_balance:
    doc: |
      Field sequence from handler at 0x08232318 in OnRecieve dispatch.
      Reads: i32
    seq:
    - id: value
      type: s4be
  ac_titles_set_active:
    doc: |
      Field sequence from handler at 0x0822c6ed in OnRecieve dispatch.
      Reads: u8 u16
    seq:
    - id: status
      type: u1
    - id: value
      type: u2be
  ac_avatars_set_active:
    doc: |
      Field sequence from handler at 0x0822c752 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_mottos_set_active:
    doc: |
      Currently-active motto plus the list of acquired motto / taunt names.
      Confirmed via two capture variants:
        62B: status=0 + empty active_motto + count=6 + 6 entries.
        70B: status=0 + active_motto="Taunt_68" + count=6 + 6 entries.
    seq:
    - id: status
      type: u1
    - id: active_motto
      type: strz
      encoding: ASCII
    - id: count
      type: u2be
    - id: taunts
      type: strz
      encoding: ASCII
      repeat: expr
      repeat-expr: count
  ac_choose_starting_station:
    doc: |
      Field sequence from handler at 0x0822ecbb in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_change_player_nickname:
    doc: |
      Nickname-change ack. Handler 0x0822ebd8 reads u8 status + cstr
      new_nickname (NUL-terminated).
    seq:
    - id: status
      type: u1
    - id: new_nickname
      type: strz
      encoding: ASCII
  ac_steam_user_info:
    doc: |
      Field sequence from handler at 0x0822eb94 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_premium_info:
    doc: Premium account expiry timestamp in milliseconds
    seq:
    - id: expiry_ms
      type: u8be
  ac_premium_buy:
    doc: |
      Field sequence from handler at 0x0822f442 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_account_auras:
    doc: |
      Player's account auras — daily multipliers, permanent DLC
      bonuses, etc. Handler 0x0822f87d. Wire shape:
        u1 status_flag + u8 count + count × { cstring def_name,
        u32 flags, u64 value }. Decoded by
        ac_account_auras_body.AcAccountAurasBody.
    seq:
    - id: data
      type: ac_account_auras_body
      size-eos: true
  ac_add_account_aura:
    seq:
    - id: unknown
      size-eos: true
  ac_cancel_account_aura:
    seq:
    - id: unknown
      size-eos: true
  ac_quests:
    doc: |
      Active and template quest list. Handler 0x0822d960 has a multi-section
      inline reader: 3×u4 totals + 4×u1 flags, then a u4+u1 dailies array,
      a per-quest array (FUN_088f8e20 prelude + u2 id + u1 status + u4
      progress + 2 optional u8s), then a quest-desc array, two u2-prefixed
      quest-id arrays, and a flag-byte/i32-pair stream terminated by 0xff.
      Surfaced through ac_unknown_bodies.AcQuestsBody (top fields only).
    seq:
    - id: data
      type: ac_quests_body
      size-eos: true
  ac_quest_accept:
    doc: |
      19 bytes. Same shape as ac_quest_change (just shorter opaque tail):
      echo + u8(status=0) + u16be(quest_id_echo) + 14B opaque payload.
      Confirmed against capture ac_0019_unknown.bin (quest_id=0x035a).
    seq:
    - id: status
      type: u1
    - id: quest_id
      type: u2be
    - id: opaque
      size: 14
  ac_quest_change:
    doc: |
      21 bytes. Request: echo + u16be(quest_id).
      Response: echo + u8(status=0) + u16be(quest_id_echo) + u16be(new_state) + 12B opaque.
    seq:
    - id: status
      type: u1
    - id: quest_id
      type: u2be
    - id: new_state
      type: u2be
    - id: opaque
      size: 14
  ac_quest_complete:
    doc: |
      41 or 53 bytes. Request: echo + u16be(quest_id).
      Response: echo + u8(status=0) + u16be(quest_id_echo) + bit-packed reward/stat data.
      Shorter form (41B) omits the extra reward block present in the 53B form.
    seq:
    - id: status
      type: u1
    - id: quest_id
      type: u2be
    - id: payload
      size-eos: true
  ac_quest_complete_all:
    seq:
    - id: unknown
      size-eos: true
  ac_ship_quests:
    doc: |
      Per-ship quest record(s). Handler 0x0822bdf8 reads u1 `loaded` +
      u8 `num_records` (always 1 in captures), then num_records × per-
      record { u8 + u8 + u32 + u64 primary_iid + 8 × u64 iids }. Each
      iid is 0 when no active quest. The leading u1 leaves the rest
      bit-misaligned, so decoded by
      ac_ship_quests_body.AcShipQuestsBody (BitReader). Verified
      against all 106 captures (exactly 7 bits trailing padding).
    seq:
    - id: data
      type: ac_ship_quests_body
      size-eos: true
  ac_ship_quest_start:
    doc: |
      Field sequence from handler at 0x082340f8 in OnRecieve dispatch.
      Reads: u8 u8
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
  ac_ship_quest_change:
    doc: |
      Field sequence from handler at 0x082340b4 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_ship_quest_end:
    seq:
    - id: unknown
      size-eos: true
  ac_rewarded_tutorials:
    doc: List of tutorial IDs that have been completed and rewarded
    seq:
    - id: count
      type: u1
    - id: tutorial_ids
      type: u1
      repeat: expr
      repeat-expr: count
  ac_reward_tutorial:
    doc: |
      Tutorial-reward ack. Handler 0x0823444a reads (bit-stream order):
      u8 status + u8 + u1 flag + u64. The mid-stream u1 makes the
      trailing u64 bit-misaligned; faithful decode needs a BitReader
      body module (TODO; no S->C captures observed). The native model
      below uses kaitai `b1` with implicit byte-alignment of the u64,
      which will diverge from the wire if the encoder doesn't pad.
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
    - id: flag
      type: b1
    - id: field_3
      type: u8be
  ac_player_inventory:
    doc: |
      Inventory dump. Handler at 0x08233968 reads, bit-packed:

        u4be  num_items
        num_items × {
          u8be  item_id           (server-side primary key, small dense u64)
          cstring  name (≤60 ch)  (8-bit chars in the bit-stream)
          u4be  quantity          (1 for unique gear; >1 for stacked
                                   ammo/consumables)
          u1    flag              (set on a small subset — looks like
                                   "currently equipped"/active state)
          u8be  misc              (0 in our captures; probably expiry)
        }
        u8    cur_size            (matches captured 25 ↔ 10)
        u4be  max_size            (matches captured 1500 ↔ 450)

      Implemented in `ac_player_inventory_body.AcPlayerInventoryBody`.
    seq:
    - id: data
      type: ac_player_inventory_body
      size-eos: true
  ac_player_autogen_inventory:
    doc: |
      Catalogue of the player's autogen (procedurally-rolled modular)
      items. Handler 0x082342e0 reads `u32 count + count × ItemRecord +
      u8 cur_size + u32 max_size`. Each ItemRecord (FUN_088eb190) is
      `u64 iid + i32 + i32 + property-bag of the rolled stat parameters`.
      Bit-packed (the bag's cstrings/bools leave the cursor sub-byte
      aligned), so it's decoded by
      ac_player_autogen_inventory_body.AcPlayerAutogenInventoryBody.
    seq:
    - id: data
      type: ac_player_autogen_inventory_body
      size-eos: true
  ac_player_vessels:
    doc: |
      Player's owned-vessel catalogue. The handler at 0x0822e436 reads
      `u16 num_vessels + num_vessels × VesselRecord + f32 + f32`, where
      each VesselRecord (FUN_08925ae0) starts with a u64 iid (0 = empty
      slot, body skipped) followed by def_name, a 35×u64 slot array,
      slot-config pairs, a handful of scalars, a perk list and ten
      long-string customisation slots. Decoded by
      ac_player_vessels_body.AcPlayerVesselsBody.
    seq:
    - id: data
      type: ac_player_vessels_body
      size-eos: true
  ac_vessel_equipment:
    seq:
    - id: unknown
      size-eos: true
  ac_buy_item:
    doc: |
      Item-purchase ACK. Handler 0x08233dd0 (Ghidra-decompiled) reads:
      u32 store_item_id_echo, u8 status, then an InventoryItem via the
      shared FUN_088ead70 (u64 iid + cstrN def_name + u32 qty + u1 flag
      + u64 misc). If iid != 0 (a new inventory slot was created), the
      handler reads a trailing u1 + u8 count + count NUL-terminated
      cstrings (the consumed/affected def-names). When iid == 0 the
      handler stops after the InventoryItem, even when the server has
      sent a longer body -- the client ignores the tail. The
      InventoryItem's u1 flag bit-misaligns the rest, so decoded by
      ac_buy_item_response_body.AcBuyItemResponseBody.
    seq:
    - id: data
      type: ac_buy_item_response_body
      size-eos: true
  ac_sell_item:
    seq:
    - id: unknown
      size-eos: true
  ac_sell_items:
    seq:
    - id: unknown
      size-eos: true
  ac_enchant_item:
    doc: |
      Field sequence from handler at 0x08234d86 in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_salvage_item:
    doc: |
      Single-item salvage ack. Handler 0x08234a1b reads (bit-stream order):
      u64 iid + u8 + u1 flag + u32. The mid-stream u1 leaves the trailing
      u32 bit-misaligned, so a faithful decode needs a BitReader body
      module (TODO; no S->C captures observed yet to validate). The
      native model below treats the bool as kaitai's `b1` with implicit
      byte-alignment of the subsequent u32 — fine when flag=0 and the
      u32 happens to be byte-aligned in the encoder, but the trailing
      value will diverge if the wire encoding is truly bit-misaligned.
    seq:
    - id: iid
      type: u8be
    - id: field_1
      type: u1
    - id: flag
      type: b1
    - id: field_3
      type: u4be
  ac_salvage_items:
    doc: |
      Field sequence from handler at 0x0822fa48 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_upgrade_items:
    doc: |
      Field sequence from handler at 0x08232ed8 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_upgrade_autogen_item:
    doc: |
      Field sequence from handler at 0x082348e0 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_craft_upgrade_item:
    doc: |
      Field sequence from handler at 0x0822d32b in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_find_autogen_item:
    doc: |
      Field sequence from handler at 0x08234001 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_activate_resource_vessel:
    doc: |
      Field sequence from handler at 0x08233fbd in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_sell_vessel:
    doc: |
      Field sequence from handler at 0x08234b30 in OnRecieve dispatch.
      Reads: u64 u8 u32 f32
    seq:
    - id: u64_0
      type: u8be
    - id: field_1
      type: u1
    - id: u32_2
      type: u4be
    - id: value
      type: f4be
  ac_vessel_change_equip:
    doc: |
      Server response to a vessel-equip change. Handler 0x082352c8 reads,
      bit-packed:
        u8   status                                (0 = success)
        u8be vessel_id
        if status == 0:
          35 × u8be slot_module_id                 (full vessel loadout)
          u1   has_inventory_update
          if has_inventory_update:
            u4 num_items
            num_items × {u8be id, cstring name (≤60), u4 quantity,
                          u1 flag, u8be misc}    (same record as inventory)
      Implemented in `ac_vessel_change_equip_body.AcVesselChangeEquipResponseBody`.
    seq:
    - id: data
      type: ac_vessel_change_equip_response_body
      size-eos: true
  ac_vessel_change_equip_multi:
    doc: |
      Multi-equip response. Shares handler 0x082352c8 with the single
      variant for the prefix (status + vessel_id + 35 slot_module_ids)
      but the multi case has a much longer tail with per-change cleartext
      records (item_name + 2 flag bytes) and an inventory delta.
      Surfaced through ac_vessel_change_equip_multi_response_body.
    seq:
    - id: data
      type: ac_vessel_change_equip_multi_response_body
      size-eos: true
  ac_vessel_cheat_change_equip:
    doc: |
      Vessel cheat-change-equip ack. Handler 0x0823010c reads u8 status
      + u64 iid + u8 + u1 flag (1 bit; trailing).
    seq:
    - id: status
      type: u1
    - id: iid
      type: u8be
    - id: field_2
      type: u1
    - id: flag
      type: b1
  ac_vessel_transfer_equip:
    doc: |
      Transfer equipment between vessels. Confirmed against 38B captures:
      u4be status + u8be vessel_id_from + u8be vessel_id_to + opaque
      module-list tail.
    seq:
    - id: status
      type: u4be
    - id: vessel_id_from
      type: u8be
    - id: vessel_id_to
      type: u8be
    - id: payload
      size-eos: true
  ac_vessel_strip_equip:
    doc: |
      Vessel strip-equip ack. Handler 0x0823353e reader_calls list says
      u8 + u64 + u1; that matches the 10-byte C->S request shape. But
      the matching S->C response in captures is ~125 KB — the handler
      clearly does much more than the recognized-reader-call set
      captures (probably a sub-deserializer call into a larger vessel
      snapshot). Modelled minimally as the request shape; the S->C body
      needs further RE before it can be faithfully decoded.
    seq:
    - id: status
      type: u1
    - id: iid
      type: u8be
    - id: flag
      type: b1
  ac_vessel_change_munition:
    doc: |
      Vessel munition-change ack. Handler 0x08234924 reads u8 status +
      u64 iid + u1 flag (1 bit; trailing).
    seq:
    - id: status
      type: u1
    - id: iid
      type: u8be
    - id: flag
      type: b1
  ac_vessel_refill_munition:
    doc: Munition refill confirmation; count = munitions restored
    seq:
    - id: status
      type: u4be
    - id: unknown
      type: u1
    - id: vessel_id
      type: u4be
    - id: count
      type: u2be
    - id: reserved
      type: u1
  ac_vessel_transfer_munition:
    doc: |
      Transfer munition between vessels. 22B FIXED:
      u4be status + u8be vessel_id_from + u8be vessel_id_to.
    seq:
    - id: status
      type: u4be
    - id: vessel_id_from
      type: u8be
    - id: vessel_id_to
      type: u8be
  ac_vessel_autogen_destroy:
    doc: |
      Autogen module destroy ACK. Variable size (10B / 274B observed).
      Header u4be status + bit-packed per-item payload listing
      destroyed items + refunds. Layout not fully reversed.
    seq:
    - id: status
      type: u4be
    - id: payload
      size-eos: true
  ac_vessel_autogen_dismantle:
    doc: |
      Autogen module dismantle ACK. 64B captures.
      Header u4be status + bit-packed payload. Layout not fully reversed.
    seq:
    - id: status
      type: u4be
    - id: payload
      size-eos: true
  ac_vessel_extract_exp:
    doc: |
      Server response after a vessel-XP extraction. Handler 0x0822f3ad
      reads u1 status; on success, follows with a u4 extracted_amount,
      a u4 count, and `count` × {u8 vessel_id, u4 new_xp_value} records.
      Fully byte-aligned.
    seq:
    - id: status
      type: u1
    - id: extracted_amount
      type: u4be
      if: status == 0
    - id: num_vessels
      type: u4be
      if: status == 0
    - id: vessels
      type: vessel_xp_update
      repeat: expr
      repeat-expr: num_vessels
      if: status == 0
    types:
      vessel_xp_update:
        seq:
          - id: vessel_id
            type: u8be
          - id: new_xp
            type: u4be
  ac_vessel_levelup:
    doc: |
      Vessel level-up confirmation. 29B FIXED:
      u4be status + u8be vessel_id + opaque level/xp/credit data.
    seq:
    - id: status
      type: u4be
    - id: vessel_id
      type: u8be
    - id: payload
      size-eos: true
  ac_vessel_repair:
    doc: Repair confirmation; vessel_id identifies the repaired vessel
    seq:
    - id: unknown
      type: u4be
    - id: vessel_id
      type: u4be
    - id: status
      type: u2be
  ac_vessel_repair_battle:
    doc: |
      Vessel battle-repair ack. Handler 0x08230d28 reads u8 status +
      three 1-bit bools (trailing; ~5 bits padding).
    seq:
    - id: status
      type: u1
    - id: flag_a
      type: b1
    - id: flag_b
      type: b1
    - id: flag_c
      type: b1
  ac_vessel_refill_battle:
    doc: |
      Vessel refill-in-battle ack. Handler 0x08233754 reads
      u8 status + u8 + u1 flag (1 bit; trailing).
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
    - id: flag
      type: b1
  ac_vessel_strip_improper_battle:
    doc: |
      Server-pushed notification that one or more vessel modules were
      stripped from a vessel because the player brought a loadout into
      battle that the queue/league didn't allow. Handler at 0x08233d8c:
        u8  status                   (0 = OK; non-zero takes an early-
                                      exit branch into the event pump,
                                      no extra wire data)
        if status == 0:
          u1  has_vessel
          if has_vessel: u32 vessel_id   (invalidates the cached
                                          vessel slot via FUN_0832ed00)
          u32 account_exp_pool       (player's current Clearance Score —
                                      matches the same uid's
                                      Atlas.accountExpPool)
      All 49 observed captures take the status=0, has_vessel=0 path.
    seq:
    - id: data
      type: ac_vessel_strip_improper_battle_body
      size-eos: true
  ac_vessel_free_custom_elements:
    doc: |
      The customization elements (decal/sticker def-names) the player has
      unlocked for free. Handler 0x082308a3 reads u32 count, then count ×
      NUL-terminated def-name (the ReadCStringLen is looped). The old
      model read the count + only the first string, so the list was
      truncated. Verified against all 106 captures (count 13..552, 0
      leftover bytes).
    seq:
    - id: count
      type: u4be
    - id: elements
      type: strz
      encoding: ASCII
      repeat: expr
      repeat-expr: count
  ac_vessel_custom_elements_buy:
    doc: |
      Field sequence from handler at 0x0823080e in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_vessel_custom_elements_acknowledge_expiration:
    doc: |
      Field sequence from handler at 0x08230779 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_vessel_craft:
    doc: |
      Field sequence from handler at 0x08233f81 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_vessel_recraft:
    doc: |
      Field sequence from handler at 0x08233a55 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_vessel_budget_levelup:
    doc: |
      Field sequence from handler at 0x08233ea8 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_vessel_budget_activate:
    doc: Budget vessel activation confirmation
    seq:
    - id: status
      type: u4be
    - id: vessel_id
      type: u4be
    - id: unknown
      type: u1
  ac_vessel_unlock_node:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_activate_node:
    doc: |
      Activate / unlock vessel skill node. 34B captures show:
      u4be status + u8be vessel_id + opaque node-state tail.
    seq:
    - id: status
      type: u4be
    - id: vessel_id
      type: u8be
    - id: payload
      size-eos: true
  ac_battle_slots:
    doc: |
      Battle loadout slots. Handler 0x0822fe20 reads u32 slot_count, then
      slot_count × u64 (the active vessel id in each battle slot — max 4
      slots), then a constant 16-byte footer (u64 0 + u64 0x0c in every
      one of 106 captures; slot_count is only ever 3 or 4). The earlier
      `repeat: eos` model wrongly consumed the footer as 1-2 phantom
      slots; use `repeat-expr: slot_count` so the count matches reality.
    seq:
    - id: slot_count
      type: u4be
    - id: slots
      type: battle_slot
      repeat: expr
      repeat-expr: slot_count
    - id: footer_reserved
      type: u8be
      doc: always 0 observed.
    - id: footer_const
      type: u8be
      doc: always 0x0c (12) observed; purpose unconfirmed.
    types:
      battle_slot:
        seq:
        - id: unknown
          type: u4be
          doc: high 32 bits of the slot u64; always 0 observed.
        - id: vessel_id
          type: u4be
  ac_battle_slot_change_vessel:
    doc: |
      13 bytes. Request: echo + slot(u8) + 8B ship data (u32be zeros + u32be ship_id).
      Response: same + u16be result at end (observed: 0x0004).
    seq:
    - id: slot
      type: u1
    - id: ship_data
      size: 8
    - id: result
      type: u2be
  ac_battle_slot_swap_vessels:
    doc: |
      Field sequence from handler at 0x08233002 in OnRecieve dispatch.
      Reads: u8 u8 u8
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
    - id: field_2
      type: u1
  ac_battle_slot_cheat_change_vessel:
    doc: |
      Field sequence from handler at 0x08232f6d in OnRecieve dispatch.
      Reads: u8 u8
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
  ac_inv_ext_buy:
    doc: |
      Inventory expansion purchase. 15B FIXED.
      u1 status + u4be cost + u4be capacity + u4be timestamp.
      Verified against capture (cost=1500, capacity=2_000_000).
    seq:
    - id: status
      type: u1
    - id: cost
      type: u4be
    - id: capacity
      type: u4be
    - id: timestamp
      type: u4be
  ac_autogen_inv_ext_buy:
    doc: |
      Autogen / seed-chip storage expansion purchase. 15B FIXED. Same
      shape as ac_inv_ext_buy. Verified (cost=40, capacity=4_000_000).
    seq:
    - id: status
      type: u1
    - id: cost
      type: u4be
    - id: capacity
      type: u4be
    - id: timestamp
      type: u4be
  ac_exchange_gold:
    doc: Exchange gold for credits
    seq:
    - id: status
      type: u1
    - id: credits
      type: u4be
    - id: gold
      type: u4be
  ac_buy_gold:
    doc: |
      Field sequence from handler at 0x0823364b in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_buy_arc_dlc:
    doc: |
      Field sequence from handler at 0x082336d4 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_talents_acquire:
    doc: |
      Field sequence from handler at 0x082302a0 in OnRecieve dispatch.
      Reads: u8 u8 u64
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
    - id: u64_2
      type: u8be
  ac_talents_update:
    doc: |
      Talent-preset state. Handler 0x082304ad reads 4 × u8 (set_ids,
      observed [0,1,2,3]) + 4 × bool (per-set active flag) + 4 ×
      48-bit blocks (each: 45 talent-acquired bools + 3 ignored bits,
      via ReadBytes(6)). The 4 bools make the rest bit-misaligned, so
      this can't be modelled with native byte-aligned kaitai — decoded
      by ac_talents_update_body.AcTalentsUpdateBody. The old "u1 status"
      stub captured only the first byte.
    seq:
    - id: data
      type: ac_talents_update_body
      size-eos: true
  ac_talents_reset:
    doc: |
      Field sequence from handler at 0x082303a7 in OnRecieve dispatch.
      Reads: u8 u8
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
  ac_talents_assign_sets:
    doc: Confirmed talent set assignments for 4 role slots
    seq:
    - id: status
      type: u1
    - id: set_ids
      type: u1
      repeat: expr
      repeat-expr: 4
  ac_buy_talent_set:
    doc: |
      Field sequence from handler at 0x0822dcb4 in OnRecieve dispatch.
      Reads: u8 u8
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
  ac_react_on_abandoned_game:
    doc: |
      Field sequence from handler at 0x08233b19 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_squad_info:
    doc: Current squad state; zero fields when not in a squad
    seq:
    - id: squad_id
      type: u8be
    - id: leader_uid
      type: u8be
  ac_squad_invite_accept:
    doc: |
      Field sequence from handler at 0x08233ad5 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_squad_invite_decline:
    doc: |
      Field sequence from handler at 0x0822f486 in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_squad_leave:
    doc: |
      Field sequence from handler at 0x08230f38 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_squad_invite_send:
    doc: |
      ACK for outbound squad-invite. 11 bytes: status + invitee uid.
      Confirmed against capture ac_005f_unknown.bin.
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_squad_invite_cancel:
    doc: |
      ACK for cancelling an outbound squad-invite. 11 bytes: status + invitee uid.
      Confirmed against capture ac_0060_unknown.bin (status=0 = success).
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_squad_kick:
    doc: |
      Field sequence from handler at 0x0822c328 in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_squad_ready:
    doc: |
      Squad-ready ack. Handler 0x08232bf4 reads u8 status + u1 flag
      (1 bit). Verified against the 4-byte S->C captures (1 byte status
      + 1 bit flag + 7 bits padding).
    seq:
    - id: status
      type: u1
    - id: flag
      type: b1
  ac_squad_convert_to_wing:
    doc: |
      Field sequence from handler at 0x08232ae4 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_league_team_info:
    doc: |
      League-team state — handler 0x08232b6c reads u8 status and on
      status==0 calls FUN_088ee800 (the body reader). Decoded by
      ac_league_team_info_body.AcLeagueTeamInfoBody.
    seq:
    - id: data
      type: ac_league_team_info_body
      size-eos: true
  ac_league_team_create:
    doc: |
      Field sequence from handler at 0x082306bf in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_league_team_invite_send:
    doc: |
      Field sequence from handler at 0x08232a28 in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_league_team_invite_cancel:
    doc: |
      Field sequence from handler at 0x082329b1 in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_league_team_invite_accept:
    doc: |
      Field sequence from handler at 0x08232aa0 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_league_team_kick:
    doc: |
      Field sequence from handler at 0x0822e295 in OnRecieve dispatch.
      Reads: u8 u64 u64
    seq:
    - id: status
      type: u1
    - id: u64_1
      type: u8be
    - id: u64_2
      type: u8be
  ac_league_team_leave:
    doc: |
      Field sequence from handler at 0x08232c98 in OnRecieve dispatch.
      Reads: u8 u64 u64
    seq:
    - id: status
      type: u1
    - id: u64_1
      type: u8be
    - id: u64_2
      type: u8be
  ac_league_team_invite_decline:
    doc: |
      Field sequence from handler at 0x08232b28 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_league_team_request_names:
    doc: |
      Field sequence from handler at 0x08232bb0 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_get_nicknames:
    doc: Return list of nicknames
    seq:
    - id: unknown
      type: u2be
    - id: num_nicks
      type: u2be
    - id: nicks
      type: nick
      repeat: expr
      repeat-expr: num_nicks
    types:
      nick:
        seq:
          - id: uid
            type: u8be
          - id: nickname
            type: strz
            encoding: UTF-8
  ac_get_uids:
    doc: |
      Field sequence from handler at 0x08232521 in OnRecieve dispatch.
      Reads: u16
    seq:
    - id: value
      type: u2be
  ac_report_player:
    doc: |
      Field sequence from handler at 0x082324e5 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_update_yup_purchases:
    doc: |
      Server-pushed Yuplay (Gaijin storefront) purchase state. Sent
      unsolicited shortly after connect to seed the cache; can also be
      refreshed by the client via MasterServer_UpdateYupPurchases().
      Wire format (handler 0x082327ae inside OnRecieve):
        u8  status
        bag yupPurchases           (DLCs / premium / etc.)
        u8  num_invalidate
        N × cstring                (≤60 — purchase IDs to invalidate)
      Bag cache is exposed to lua via MasterServer_GetCachedYupPurchases.
    seq:
    - id: data
      type: ac_update_yup_purchases_body
      size-eos: true
  ac_check_yup_purchases:
    doc: |
      Field sequence from handler at 0x0822c796 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_update_dlc_ownership:
    doc: |
      DLC ownership snapshot. Handler 0x08233924 reads u8 status, then
      branches: status==0 -> Bag_Deserialize (a Steam-product-GUID-keyed
      bag); status!=0 -> u32 count + count × {u64 iid, cstr name,
      u32 qty, u1 flag, u64 misc} (same per-item shape as
      ac_player_inventory's FUN_088ead70). All 26 captures take the
      status=0 path with a 16-entry GUID bag. The leading u8 stays
      byte-aligned but the bag's inner u1 misaligns subsequent reads,
      so this is decoded by
      ac_update_dlc_ownership_body.AcUpdateDlcOwnershipBody.
    seq:
    - id: data
      type: ac_update_dlc_ownership_body
      size-eos: true
  ac_friends_send_request:
    doc: |
      Despite the AC name, the response carries the player's full social
      state. Handler 0x082338d8 → FUN_08901240 reads, byte-aligned:

        u1 num_friends,        num_friends × u8be UID
        u1 num_requests_in,    num × u8be UID
        u1 num_requests_out,   num × u8be UID
        u1 num_ignored,        num × u8be UID
        u1 num_watched,        num × u8be UID
        u1 num_pairs_a,        num × {u8be uid, u8be uid}
        u1 num_pairs_b,        num × {u8be uid, u8be uid}

      Surfaced through ac_unknown_bodies.AcFriendsSendRequestBody.
    seq:
    - id: data
      type: ac_friends_send_request_body
      size-eos: true
  ac_friends_accept_request:
    doc: Result of accepting a friend request; uid is the new friend
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_friends_reject_request:
    doc: |
      Field sequence from handler at 0x0822ff6c in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_friends_remove:
    doc: |
      Field sequence from handler at 0x08232dfc in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_friends_list:
    doc: |
      Field sequence from handler at 0x08232d20 in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_social_ignore_add:
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_social_ignore_remove:
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_social_watch_add:
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_social_watch_remove:
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_social_suggest_steam:
    seq:
    - id: unknown
      size-eos: true
  ac_social_suggest_fb:
    seq:
    - id: unknown
      size-eos: true
  ac_social_suggest_vk:
    seq:
    - id: unknown
      size-eos: true
  ac_teaching_list:
    doc: |
      Teach/learn relationship state. Handler 0x0822bf58 → FUN_08917c10
      calls a u4be-count + u8be-UID list reader six times, then reads two
      u1 flag bits. Empty teaching state shows up as 6×0-count lists +
      both flags=true (25-byte body). Surfaced through
      ac_unknown_bodies.AcTeachingListBody.
    seq:
    - id: data
      type: ac_teaching_list_body
      size-eos: true
  ac_teaching_request_to_teacher:
    doc: |
      Field sequence from handler at 0x0822be79 in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_teaching_request_to_student:
    doc: |
      Field sequence from handler at 0x082309f6 in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_teaching_accept:
    doc: |
      Teaching-accept ack. Handler 0x0822bb58 reads u8 status + u64 iid
      + u8 + u1 flag (1 bit; trailing).
    seq:
    - id: status
      type: u1
    - id: iid
      type: u8be
    - id: field_2
      type: u1
    - id: flag
      type: b1
  ac_teaching_reject:
    doc: |
      Field sequence from handler at 0x0822b9c6 in OnRecieve dispatch.
      Reads: u8 u8 u64
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
    - id: u64_2
      type: u8be
  ac_teaching_check:
    doc: |
      Field sequence from handler at 0x0822b97f in OnRecieve dispatch.
      Reads: u8 u64 u8
    seq:
    - id: status
      type: u1
    - id: u64_1
      type: u8be
    - id: field_2
      type: u1
  ac_teaching_allow:
    doc: |
      Teaching-allow update — handler 0x0822b852 reads u8 status + u8
      role + u1 allow, then (when status==0) writes `allow` into game
      state at +0xba709 for role==2 (teacher) or +0xba708 for role==1
      (student). Role values outside {1, 2} are ignored.
    seq:
    - id: status
      type: u1
    - id: role
      type: u1
    - id: allow
      type: b1
  ac_referrals:
    doc: Referral program info; flags=0x80 when no active referrer
    seq:
    - id: flags
      type: u1
    - id: uid
      type: u8be
    - id: reserved
      type: u1
  ac_set_referrer:
    doc: |
      Field sequence from handler at 0x0822b4e7 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_obtain_referral_key:
    doc: |
      Referral / promotion key. 36B FIXED. Body is a cs0-shifted
      string (each byte = (char>>1) | (carry<<7)) encoding the
      promo code; layout opaque.
    seq:
    - id: cs0_key
      size: 34
  ac_attach_steam_account:
    doc: |
      Field sequence from handler at 0x0822b8fc in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_finalize_steam_mtxn:
    doc: |
      Steam micro-transaction finalisation ack. Handler 0x0822b52b reads
      (bit-stream order): u1 flag + u8 + cstrN. The leading u1 leaves
      the rest of the body bit-misaligned, so a faithful decode needs
      a BitReader body module (TODO; no S->C captures observed). The
      native model below applies kaitai's `b1` with implicit alignment,
      which can mis-decode the trailing bytes if the encoder doesn't
      pad after the bit.
    seq:
    - id: flag
      type: b1
    - id: status
      type: u1
    - id: text
      type: strz
      encoding: ASCII
  ac_attach_yup_account:
    doc: |
      Field sequence from handler at 0x0822b8b8 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_attach_email:
    doc: |
      Field sequence from handler at 0x0822b0fe in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_lobby_list:
    doc: |
      Current open-lobbies list — `u32 count + count × LobbyInfo`, with
      each LobbyInfo using the same wire format as `ac_lobby_info`.
      Decoded by `ac_lobby_list_body.AcLobbyListBody`.
    seq:
    - id: data
      type: ac_lobby_list_body
      size-eos: true
  ac_lobby_join:
    doc: |
      Lobby join ack. Handler 0x0822b264 reads u8 status + u1 flag
      (1 bit; ~7 bits of trailing padding).
    seq:
    - id: status
      type: u1
    - id: flag
      type: b1
  ac_lobby_create:
    doc: |
      Newly-created lobby info. Layout from 88-114B captures:
        u8be lobby_id (zero before creation completes) + cstring name +
        u4be reserved + cstring level_def_name + opaque settings tail.
      Tail contains mode + slot caps + flags but exact layout varies.
    seq:
    - id: lobby_id
      type: u8be
    - id: name
      type: strz
      encoding: UTF-8
    - id: reserved
      type: u4be
    - id: level_def_name
      type: strz
      encoding: ASCII
    - id: settings_payload
      size-eos: true
  ac_lobby_info:
    doc: |
      Lobby state — handler 0x0822b1c7 → FUN_088f1690. Inline reader:
      u8 lobby_id, cstring name, u4 unknown, cstring desc, plus a long
      tail (u8/u8/u8/6×u1/2×f32/u2/u4/u1/u8 + member array + 4 strings).
      Surfaced through ac_unknown_bodies.AcLobbyInfoBody (header
      decoded, tail kept opaque).
    seq:
    - id: data
      type: ac_lobby_info_body
      size-eos: true
  ac_lobby_kick:
    doc: |
      Field sequence from handler at 0x0822b42a in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_lobby_leave:
    doc: |
      Lobby-leave ACK. 3B captures: echo + u1 status (0x00 = success).
    seq:
    - id: status
      type: u1
  ac_lobby_invite:
    doc: |
      Field sequence from handler at 0x0822b466 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_lobby_modify:
    doc: |
      Lobby modification ACK. 5B FIXED — observed identical bytes
      (0xd0, 0x80, 0x52) across captures, suggesting bit-packed flags
      or reserved status. Layout not yet fully reversed.
    seq:
    - id: opaque_status
      size: 3
  ac_lobby_start_game:
    doc: |
      Field sequence from handler at 0x0822b069 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_lobby_group_list:
    doc: |
      List of joinable lobby groups. 4B captures show empty list (count=0).
      Per-entry layout for non-empty lists not yet documented.
    seq:
    - id: count
      type: u2be
    - id: payload
      size-eos: true
  ac_lobby_group_info:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_create:
    doc: |
      Field sequence from handler at 0x0822ac9c in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_lobby_group_modify:
    doc: |
      Field sequence from handler at 0x0822bfa4 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_lobby_group_delete:
    doc: |
      Field sequence from handler at 0x0822ac58 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_lobby_group_joinreq_create:
    doc: |
      Field sequence from handler at 0x0822abb8 in OnRecieve dispatch.
      Reads: u8 u32
    seq:
    - id: status
      type: u1
    - id: value
      type: u4be
  ac_lobby_group_joinreq_cancel:
    doc: |
      Field sequence from handler at 0x0822ab17 in OnRecieve dispatch.
      Reads: u8 u32
    seq:
    - id: status
      type: u1
    - id: value
      type: u4be
  ac_lobby_group_joinreq_reject:
    doc: |
      Field sequence from handler at 0x0822c55e in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_clan_request_credentials:
    doc: |
      Tabular response: list of (cid, name, tag, emblem) for the
      requested clans (typically 1, but recruiting list returns many).
      Confirmed against captures of varying sizes (44B count=1,
      274B count=7).
    seq:
    - id: count
      type: u4be
    - id: clans
      type: clan_credential
      repeat: expr
      repeat-expr: count
    types:
      clan_credential:
        seq:
        - id: cid
          type: u8be
        - id: name
          type: strz
          encoding: UTF-8
        - id: tag
          type: strz
          encoding: ASCII
        - id: emblem
          type: strz
          encoding: ASCII
  ac_clan_request_desc:
    doc: |
      Full clan description (0x009f). Field names and types match the Lua
      binding MasterServer_ClanGetDesc (fn at 0x086fc350), which delegates
      to the clan_desc → Lua table converter at 0x088e1280. The converter
      reads a singleton clan struct at 0x0945b430 and pushes ~20 named
      top-level fields. The packet carries structured prefix fields (cid,
      strings, timestamps, counters, quest state, members) followed by a
      TGP-encoded FedDesign K-V stream that holds the invites, joinReqs,
      upgrades, resources, clanShips and clanItemKeys arrays.

      TGP stream format:
      Keys use three different encodings depending on first byte:
        - cs-encoded (carry-shift-right): byte[i] = (char[i]>>1)|(carry<<7),
          null terminator when ((b0&0x7f)<<1)|(b1>>7)==0.
        - x2-encoded: byte = char*2, first byte >= 0x80 for uppercase.
        - cleartext: raw ASCII, null-terminated.
      TGP wire type tags: 0x02=cs-string, 0x03=counted K-V map,
        0x04=u64be, 0x05=cleartext-str, 0x06=array-of-cs-strings,
        0x0a=x2-str, 0x0c=struct(u32be-header + K-V body), 0x14=marker,
        0x15=cs-string-value, 0x18=u32be.

      The TGP stream contains one entry per clanShip (keyed by design name
      e.g. EmpireDesign, FederationDesign, JerichoDesign) with per-ship
      fields: defName, productionStartTime, productionCompleteAt,
      repairStartTime, repairEndTime, broken, boostBuildingBudget,
      boostRepairingBudget, partBeingBuilt, slotBeingBuilt, curZone,
      moduleSlots, mainParts. Plus the top-level arrays invites (u64
      uids), joinReqs (empty when none), upgrades (small u32 ids),
      resources (4 u32 balances) and clanItemKeys.

      moduleSlots structure: type 0x03 map with a 160-byte constant
      binary header (identical between captured sessions) followed by
      variable K-V entries. Each slot key is x2-encoded (main_1..main_3,
      additional_1..additional_2, turret_1..turret_3). Slot values: type
      0x0c struct with u32be header (= installed-module count) + K-V body
      containing "fit" (cs-string, fitted module name) and "built"
      (nested struct with additional_N entries). Some slots use type
      0x03 instead (count=1 map).
    seq:
    - id: cid
      type: u8be
      doc: |
        Clan ID. Lua exposes as int64 `cid`; observed high 32 bits are
        always zero so practical range fits u32.
    - id: name
      type: strz
      encoding: UTF-8
    - id: tag
      type: strz
      encoding: UTF-8
    - id: motd
      type: strz
      encoding: UTF-8
    - id: desc
      type: strz
      encoding: UTF-8
    - id: emblem
      type: strz
      encoding: UTF-8
      doc: Clan icon/emblem identifier, e.g. "clan_icon_id_1534".
    - id: current_clan_ship
      type: strz
      encoding: UTF-8
      doc: |
        Design name of the clan's currently-active ship, e.g. "EmpireDesign".
        Keys into the clanShips map in the TGP stream.
    - id: creation_date
      type: u8be
      doc: Milliseconds since the Unix epoch — when the clan was founded.
    - id: unknown_a
      type: u4be
      doc: |
        Not surfaced by MasterServer_ClanGetDesc. Observed 0x442fed22 and
        constant between captures for the same clan; role unknown. Possibly
        a boost/budget timestamp or reserved field.
    - id: counter_target
      type: u4be
      doc: Clan contribution counter target (Lua `counterTarget`).
    - id: counter_progress
      type: u4be
      doc: Clan contribution counter progress (Lua `counterProgress`).
    - id: clan_quest_id
      type: s4be
      doc: |
        Active clan quest id; -1 = none. Lua exposes as `clanQuestId` (int).
    - id: clan_quest_progress
      type: u2be
      doc: |
        Clan quest progress. Lua promotes to int32 via setInt, but only
        3 bytes are available between clan_quest_id and member_count on the
        wire, split as (u16 progress, u8 recruiting). Both observed zero.
    - id: recruiting
      type: u1
      doc: Boolean — whether the clan is accepting new members.
    - id: member_count
      type: u4be
    - id: members
      type: member
      repeat: expr
      repeat-expr: member_count
    - id: invites_count
      type: u4be
    - id: invites
      type: u8be
      repeat: expr
      repeat-expr: invites_count
      doc: Lua `invites` — player uids (u64 each) with pending clan invites.
    - id: joinreqs_count
      type: u4be
    - id: joinreqs
      type: u8be
      repeat: expr
      repeat-expr: joinreqs_count
      doc: Lua `joinReqs` — player uids (u64 each) with pending join requests.
    - id: upgrade_a
      type: u1
      doc: Lua `upgrades[0]` — first upgrade track level (observed 10..12).
    - id: upgrade_b
      type: u1
      doc: Lua `upgrades[1]` — second upgrade track level (observed 1).
    - id: resources
      type: u4be
      repeat: expr
      repeat-expr: 4
      doc: |
        Lua `resources[0..3]` — four clan resource balances. Observed values
        show resource[0]/resource[1] carry non-zero balances while [2]/[3]
        are zero in captured clans.
    - id: fed_design_tgp_stream_flags
      type: u4be
      doc: |
        Header word of the FedDesign TGP stream. Observed values 0x00000001
        (GD3F) and 0x80000001 (TerraLuX). Low bits likely a count/version;
        high bit likely a flag (possibly "has clanItemKeys"). Not yet fully
        reversed.
    - id: fed_design_tgp_stream
      size-eos: true
      type: fed_design_tgp_stream
      doc: |
        Remaining bytes: a recursive, self-describing serialization of the
        clan's `clanShips` map (keyed by design name — EmpireDesign,
        FederationDesign, JerichoDesign in the captured clans) and
        possibly `clanItemKeys`. The format is what the reader at
        0x0088e7320 calls `lookupKey(container, "defName", type)`; the
        container is built by the recursive parser rooted at 0x08b1ea40
        (called from the 0x009f packet handler around 0x08239aea). Keys
        and type tags are read inline as the parser descends; Kaitai
        struct's static typing cannot encode this, so we delegate to the
        opaque type `fed_design_tgp_stream.FedDesignTgpStream` which walks
        the stream and surfaces every ClanShip name, slot fit, and
        per-slot build queue we could decode. Sections we don't yet model
        (e.g. the ~80-byte hash-table-like outer header, sparse u64/u32
        timestamp fields between ships) come back as `opaque=…` runs.

        What's known about the wire format:
          * Keys appear in three different encodings within one record:
            - cs-shifted (7-bit-per-byte carry-shifted strings) for most
              field keys like main_1, moduleSlots, productionStartTime,
              broken, curZone — e.g. cs("main_1\0") = 36 b0 b4 b7 2f 98 80
            - x2-encoded (char<<1) for some names. Strings of this kind
              observed in-stream: "ClanShip_Angar_t5" at offset 0x85,
              "FederationDesign" at 0x58c, "fit" at 0x97.
            - cleartext (null-terminated ASCII) — observed for "defName",
              "mainParts", "built", and "FederationDesign" at 0x5a2.
          * Type tags (after a key, before the value):
            0x02 = cs-string value, 0x03 = map (u32be count), 0x04 = u64be,
            0x05 = cleartext-string value, 0x06 = array (u32be count),
            0x0a = x2-string value, 0x0c = struct (u32be header),
            0x15 = cs-string value, 0x18 = u32be, 0x82 = cs-string-with-
            array-first-element flag.
          * Per-ship FedDesign struct (offsets in in-memory layout, from
            the serializer at 0x088e7110):
              +0x00  defName           std::string
              +0x04  mainParts         4-item cs-string array (observed
                                       values: Shipyard, Carcas, Engine,
                                       Weapon)
              +0x18  moduleSlots       map with a 160-byte opaque binary
                                       hash-table header before the K-V
                                       entries; slot keys are x2-encoded
                                       (main_1..main_3, additional_1..2,
                                       turret_1..3); slot values are
                                       type 0x0c structs with a u32be
                                       header + body containing "fit"
                                       (cs-string, fitted module name)
                                       and "built" (nested struct)
              +0x2c  partBeingBuilt    std::string
              +0x30  slotBeingBuilt    std::string
              +0x34  productionStartTime     u64be (ms since epoch)
              +0x3c  productionCompleteAt    u64be
              +0x44  boostBuildingBudget     u64be
              +0x4c  broken                  u8 (bool)
              +0x50  repairStartTime         u64be
              +0x58  repairEndTime           u64be
              +0x60  boostRepairingBudget    u64be
              +0x68  curZone                 u32 (low byte used as u8)

        Observed sizes: 4238 bytes (GD3F, 300 members) and 4168 bytes
        (TerraLuX, 254 members). No bytes are stable across captures of
        different clans — every byte in the stream depends on clan
        identity and current clan state.
    types:
      member:
        seq:
        - id: uid
          type: u8be
        - id: role
          type: u1
          enum: role
    enums:
      role:
        3: vice_president
        2: officer
        1: member
        0: ceo
  ac_clan_request_profile:
    doc: |
      Clan profile for a player — `u64 uid + u64 cid`. uid is the
      queried player; cid is their clan id (0 = not in a clan).
      Verified across 304 captures: cid=1867 appears for 256 distinct
      uids (a populated clan), cid=0 for 11 uids (no clan), and a
      tail of small cids for individual members of other clans.
    seq:
    - id: uid
      type: u8be
    - id: cid
      type: u8be
  ac_clan_joinreq_create:
    doc: |
      Field sequence from handler at 0x0822c6a9 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_joinreq_cancel:
    doc: |
      Field sequence from handler at 0x0822bfea in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_joinreq_accept:
    doc: |
      Field sequence from handler at 0x0822c665 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_invite_send:
    doc: |
      Field sequence from handler at 0x0822aa97 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_invite_accept:
    doc: |
      Field sequence from handler at 0x0822aa53 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_invite_cancel:
    doc: |
      Field sequence from handler at 0x0822a812 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_kick:
    doc: |
      Field sequence from handler at 0x0822a9cb in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_leave:
    doc: |
      Field sequence from handler at 0x0822a514 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_set_role:
    doc: |
      Field sequence from handler at 0x0822aa0f in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_change_motd:
    doc: |
      Field sequence from handler at 0x0822a645 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_change_desc:
    doc: |
      Field sequence from handler at 0x0822a941 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_change_recruiting:
    doc: |
      Field sequence from handler at 0x0822a48c in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_resource_convert:
    doc: |
      Field sequence from handler at 0x0822a987 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_ship_build:
    doc: |
      Clan-ship build ack. Handler 0x0822a68b reads u8 status + three
      NUL-terminated def-name strings (e.g. hull/section/component).
    seq:
    - id: status
      type: u1
    - id: def_name_1
      type: strz
      encoding: ASCII
    - id: def_name_2
      type: strz
      encoding: ASCII
    - id: def_name_3
      type: strz
      encoding: ASCII
  ac_clan_ship_boost_building:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_ship_repair:
    doc: |
      Field sequence from handler at 0x0822a4d0 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_ship_boost_repairing:
    doc: |
      Clan-ship boost-repair ack. Handler 0x0822a856 reads u8 status +
      cstr def_name (NUL-terminated).
    seq:
    - id: status
      type: u1
    - id: def_name
      type: strz
      encoding: ASCII
  ac_clan_ship_fit:
    doc: |
      Clan-ship fit ack. Handler 0x0822a558 reads u8 status + cstr
      def_name (NUL-terminated).
    seq:
    - id: status
      type: u1
    - id: def_name
      type: strz
      encoding: ASCII
  ac_clan_ship_set_current:
    doc: |
      Field sequence from handler at 0x0822a448 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_universe_move:
    doc: |
      Clan universe-zone move ACK. 5B FIXED.
      u1 status + u2be zone_id (observed values vary by 1).
    seq:
    - id: status
      type: u1
    - id: zone_id
      type: u2be
  ac_clan_set_civilian_zone:
    doc: |
      Field sequence from handler at 0x0822c7d2 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_revive_in_war:
    doc: |
      Field sequence from handler at 0x0822d2e7 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_war_start:
    doc: |
      Field sequence from handler at 0x0822d25e in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_quest_accept:
    doc: |
      Field sequence from handler at 0x0822d2ab in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_create:
    doc: |
      Field sequence from handler at 0x0822d21a in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_upgrade:
    doc: |
      Field sequence from handler at 0x0822e328 in OnRecieve dispatch.
      Reads: u8 u8
    seq:
    - id: status
      type: u1
    - id: field_1
      type: u1
  ac_clan_change_name:
    doc: |
      Clan-rename ack. Handler 0x0822d72b reads u8 status + cstr
      new_name (NUL-terminated).
    seq:
    - id: status
      type: u1
    - id: new_name
      type: strz
      encoding: ASCII
  ac_clan_change_tag:
    doc: |
      Clan-tag-change ack. Handler 0x0822d136 reads u8 status + cstr
      new_tag (NUL-terminated).
    seq:
    - id: status
      type: u1
    - id: new_tag
      type: strz
      encoding: ASCII
  ac_clan_assign_emblem:
    doc: |
      Clan-emblem-assign ack. Handler 0x0822d050 reads u8 status + cstr
      emblem_id (NUL-terminated).
    seq:
    - id: status
      type: u1
    - id: emblem_id
      type: strz
      encoding: ASCII
  ac_clan_bank_transfer:
    doc: |
      Field sequence from handler at 0x0822f4c6 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_clan_list_recruiting:
    doc: Recruiting clans — u8 status + bag list.
    seq:
    - id: status
      type: u1
    - id: bag
      type: bag_payload
  ac_clan_history_get:
    doc: |
      Clan action history. Handler 0x0822f2da reads a u1 flag first; if
      set, a bag follows with a numbered entry per event (each entry is
      itself a bag with `action`, `time`, `params`). When the flag is 0
      the body is just the single bit. See `prefixed_bag_payload`.
    seq:
    - id: bag
      type: prefixed_bag_payload
  ac_related_quest_enable:
    doc: |
      Field sequence from handler at 0x0822d3f8 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_user_profile_get:
    doc: |
      Bulk player-profile dump. Handler 0x0822ed43 reads u2 num_records
      then `num_records` × per-profile records via FUN_08922e60 (init) +
      FUN_08924e60 (the heavy reader). Each record is bit-packed and
      flag-driven: u8 uid + u32 present_field_mask, then per UPF_* bit:
      0=UPF_STATE (u8 state + u64 sub_id), 1=UPF_CLAN_ID (u64),
      2=UPF_GENERAL_STATS (33×u64 keyed by UPGS_*),
      3=UPF_VESSELS_RANK_STATS (18×33 u64),
      4=UPF_ACHIEVEMENTS, 5=UPF_MEDALS, 6=UPF_TITLES, 7=UPF_AVATARS,
      8=UPF_MOTTOS, 9=UPF_ATLAS (bag). Field shapes / names mirror
      MasterServer.UserProfileField + UserProfileGeneralStat from
      star-conflict-lua-decompiled/scripts/masterserver.lua and the
      profile object's lua use-sites in
      ui/scripts/work/gameobjects/profile.lua. Surfaced through
      `ac_user_profile_get_response_body`; only the simple bits 0-3 are
      consumed cleanly today, since the sub-readers for bits 4-9 use
      width-prefixed varints (FUN_08b1bbd0) that don't line up with
      BitReader's byte-aligned reads.
    seq:
    - id: data
      type: ac_user_profile_get_response_body
      size-eos: true
  ac_achievements:
    doc: |
      Field sequence from handler at 0x0822dd00 in OnRecieve dispatch.
      Reads: u64 u16 u16
    seq:
    - id: u64_0
      type: u8be
    - id: u16_1
      type: u2be
    - id: u16_2
      type: u2be
  ac_admin_cmd:
    doc: |
      Field sequence from handler at 0x0822c2d4 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_games_info:
    doc: |
      Field sequence from handler at 0x0822c20a in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_zone_instances_info:
    doc: |
      Field sequence from handler at 0x0822ef89 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_get_punishments:
    doc: |
      Field sequence from handler at 0x0822eed9 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_welcome_msg:
    seq:
    - id: unknown
      type: u1
    - id: msg
      type: strz
      encoding: UTF-8
  ac_motd:
    doc: Server MOTD notification; status indicates MOTD type/availability
    seq:
    - id: status
      type: u1
  ac_survey_get_new:
    doc: |
      Response to survey-poll request. Handler 0x0822f5b2 reads u8
      status; on success (status == 0) a property bag follows via
      Bag_Deserialize. On error (status != 0) the body is just the
      status byte.

      Expected bag keys when a survey is active (from
      ui/scripts/work/gameobjects/vote.lua + windows/votewnd.lua +
      public/uipublic.lua MasterServer_OnNewSurvey):

        sid           u64     survey id
        question      str     the question text (or loc key)
        multiple      i32     1 = multi-select, otherwise single-select
        answers       bag     indexed bag of answer entries; each entry
                              has at least { text: str, recordIdx: i32 }
                              and is identified by its index in this bag
                              when sent back via MasterServer_SurveyVote
        reward        i32     reward amount (optional; only present
                              when > 0)
        isGoldReward  bool    paired with `reward` -- true = GS,
                              false = credits (optional)

      All 757 S->C captures take the status=0 / EMPTY-bag form
      (5-byte body), so the active-survey bag shape above is from
      Lua client code rather than from observed wire data.
    seq:
    - id: status
      type: u1
    - id: bag
      type: bag_payload
      if: status == 0
  ac_survey_vote:
    doc: |
      Field sequence from handler at 0x0822efcd in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_survey_results:
    doc: |
      Survey results. Handler 0x0822f502 reads u8 status; on success
      (status == 0) a property bag follows via Bag_Deserialize. On
      error (status != 0) the body is just the status byte.

      Expected bag keys when results are present (from
      ui/scripts/windows/votewnd.lua + public/uipublic.lua
      MasterServer_OnSurveyResults):

        sid          u64    survey id
        question     str    the question (re-echoed)
        answers      bag    indexed bag of answer entries
                            (same shape as in ac_survey_get_new)
        results      bag    per-answer vote counts; each entry is a
                            u64 (appears in Lua as { h, l } halves)
                            and is summed by the client to derive a
                            displayed total
        totalVoted   u64    server-sent total vote count

      All 757 S->C captures take the status=0 / EMPTY-bag form (5-byte
      body), so the active-results bag shape above is from Lua client
      code rather than observed wire data.
    seq:
    - id: status
      type: u1
    - id: bag
      type: bag_payload
      if: status == 0
  ac_universe_get:
    doc: |
      Sector-control snapshot — what `MasterServer.UniverseGet` returns
      to Lua. Field names below come from the Lua-binding code at
      FUN_0891de50 (per-zone) and FUN_08921210 (top-level). Wire reader
      is FUN_089214b0; per-zone reader is FUN_0891e800. Bit-packed
      because the per-zone record carries three u1 booleans
      (hasConflict, isCivilian, enableLogic) interleaved between the
      otherwise byte-sized fields.

        u8  unid
        u2  num_zones
        num_zones × {
          u2  zone_slot                             (outer u2 used as
                                                    array index; equals
                                                    zoneId in captures)
          u2  zoneId                                (pushed to Lua as
                                                    "zoneId")
          u1  hasConflict
          u8  unknown_u64                           (read but not exposed
                                                    by the Lua wrapper)
          f32 retentionFactor
          u1  isCivilian
          u8  civilianTime                          (Lua userdata u64)
          i4  race                                  (-1 = empty)
          u1  enableLogic
          u8  owner                                 (clan id u64)
          f32 owner_pressure_total                  Lua: ownerPressureReal =
                                                    total - virtual
          f32 ownerPressureVirtual
          u4  num_rivals
          num_rivals × {
            u8  cid
            f32 pressure_total                      Lua: pressureReal =
                                                    total - virtual
            f32 pressureVirtual
          }
        }

      Implemented in `ac_universe_get_body.AcUniverseGetBody`.
    seq:
    - id: data
      type: ac_universe_get_body
      size-eos: true
  ac_universe_counters:
    doc: |
      Field sequence from handler at 0x0822e0f3 in OnRecieve dispatch.
      Reads: u8 u64 f32
    seq:
    - id: status
      type: u1
    - id: u64_1
      type: u8be
    - id: value
      type: f4be
  ac_warmap_get:
    doc: |
      Sector ownership map. Handler at 0x0822e0a7 → FUN_08929b80; per-sector
      reader is FUN_08927420. All fields are byte-aligned (u4be/u8be/f4be),
      so the layout maps cleanly to native kaitai. The requesting clan's
      home sector (0x5fe = GD3F) appears with real coordinates and ~11
      links; off-map sectors arrive with y=10000.0 / radius=0.
    seq:
    - id: num_sectors
      type: u4be
    - id: sectors
      type: warmap_sector
      repeat: expr
      repeat-expr: num_sectors
    - id: num_locations
      type: u4be
    - id: locations
      type: warmap_location
      repeat: expr
      repeat-expr: num_locations
    types:
      warmap_sector:
        seq:
          - id: sector_id
            type: u8be
          - id: x
            type: f4be
          - id: y
            type: f4be
          - id: radius
            type: f4be
          - id: num_links
            type: u4be
          - id: links
            type: warmap_link
            repeat: expr
            repeat-expr: num_links
      warmap_link:
        seq:
          - id: linked_id
            type: u8be
          - id: weight
            type: f4be
      warmap_location:
        seq:
          - id: id
            type: u8be
          - id: x
            type: f4be
          - id: y
            type: f4be
  ac_mail_get:
    doc: |
      Mailbox listing — handler 0x0822e030 reads u8 status + u1
      keep_existing then calls FUN_088f6480 → u16v2 num_mails followed by
      num_mails × MailRecord (FUN_088f43a0). Each record has mail_id,
      flags, from/to uids, send/read times, two flag bytes, and a list of
      attachments (u8 type + bag). Decoded by
      ac_mail_get_body.AcMailGetBody.
    seq:
    - id: data
      type: ac_mail_get_body
      size-eos: true
  ac_mail_deliver:
    doc: |
      16 bytes. Push from server when mail arrives.
      Layout: echo(2) + u32be(0) + u32be(mail_id) + u32be(expiry_or_ts) + u16be(flags).
      Observed: mail_id=0x00656ca9, expiry=0x77000000, flags=0x0100.
    seq:
    - id: padding
      type: u4be
    - id: mail_id
      type: u4be
    - id: expiry_ts
      type: u4be
    - id: flags
      type: u2be
  ac_mail_send:
    doc: |
      Send-mail ACK — handler 0x0822e200 reads u8 status then branches:
      status==0 → u1 has_data (if set, server echoes the freshly-stored
      mail back via u32 mail_id + bag + MailRecord); status==0x0e → i32
      error_value + u1 error_flag; otherwise nothing. Common observed
      response is status=0 has_data=0 (= u8+u1 = 9 bits + padding).
    seq:
    - id: status
      type: u1
    - id: has_data
      type: b1
      if: status == 0
    - id: error_value
      type: s4be
      if: status == 0x0e
    - id: error_flag
      type: b1
      if: status == 0x0e
  ac_mail_remove:
    doc: |
      Remove-mail ACK — handler 0x0822e184 reads u8 status + u64
      mail_id, then (when status==0) drops the matching mail from the
      local mailbox.
    seq:
    - id: status
      type: u1
    - id: mail_id
      type: u8be
  ac_mail_acknowledge_expiration:
    doc: Acknowledge expired mail; mail_id=0xffffffff means all
    seq:
    - id: status
      type: u1
    - id: mail_id
      type: u4be
    - id: timestamp
      type: u4be
  ac_send_early_player_log:
    seq:
    - id: unknown
      size-eos: true
  ac_auto_pilot_space_station:
    doc: |
      Field sequence from handler at 0x0822cfb0 in OnRecieve dispatch.
      Reads: u8 u32
    seq:
    - id: status
      type: u1
    - id: value
      type: u4be
  ac_undock_space_station:
    doc: Undock result; status 0 = success
    seq:
    - id: status
      type: u1
  ac_set_visited_zone:
    doc: |
      Visited-zone ack. Handler 0x0822cec6 reads u16 zone_id + u1 flag
      (1 bit; ~7 bits of trailing padding).
    seq:
    - id: zone_id
      type: u2be
    - id: flag
      type: b1
  ac_zone_coordinator_gm_command:
    seq:
    - id: unknown
      size-eos: true
  ac_space_stations_population:
    doc: Per-station population dict — a bag.
    seq:
    - id: bag
      type: bag_payload
  ac_karma_reset:
    doc: |
      Field sequence from handler at 0x0822cdb6 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_faction_rep_reset:
    doc: |
      Field sequence from handler at 0x0822cd72 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_leaderboard_get:
    doc: Leaderboard — u8 status + bag of entries.
    seq:
    - id: status
      type: u1
    - id: bag
      type: bag_payload
  ac_leaderboard_get_descs:
    doc: |
      Leaderboard descriptors — u32 count + count × property bag, one
      bag per leaderboard config (name, entityType, dir, decay params,
      rewards). Decoded by
      ac_leaderboard_get_descs_body.AcLeaderboardGetDescsBody.
    seq:
    - id: data
      type: ac_leaderboard_get_descs_body
      size-eos: true
  ac_set_fb_token:
    seq:
    - id: unknown
      size-eos: true
  ac_get_fb_token:
    doc: Facebook token (18-byte blob, all-zero when not linked)
    seq:
    - id: token
      size: 18
  ac_log_fb_event:
    seq:
    - id: unknown
      size-eos: true
  ac_get_craft_resources:
    doc: Craft-resource balances — a bag of u64 amounts.
    seq:
    - id: bag
      type: bag_payload
  ac_use_blueprint:
    doc: |
      ACK for using a blueprint. Handler 0x0822c85a reads, when
      status == 0:
        u1   status
        cstring blueprint_def_name        (e.g. "BP_Iridium_plate")
        u1   ui_flag                      (controls UI notification)
        bag  result                       (a property bag with crafted
                                           item details — bit-aligned)
        cstring secondary_name
        u1   misc_a
        u1   num_item_ids
        num_item_ids × u4 item_id
        u1   has_extra
        if has_extra: i4 + u4 + u8        (bonus / overflow data)

      The bag-in-the-middle makes everything after it bit-aligned, so we
      cannot natively express the trailing fields in kaitai. Surfaced
      through `ac_use_blueprint_response_body` for the bit-aligned tail.
    seq:
    - id: data
      type: ac_use_blueprint_response_body
      size-eos: true
  ac_sell_craft_resource:
    seq:
    - id: unknown
      size-eos: true
  ac_sell_craft_resources:
    doc: |
      Field sequence from handler at 0x0822c816 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_get_blueprints:
    doc: |
      Player blueprint inventory. Handler 0x0822d434 reads a u1 flag
      first (negated and stored as an internal "loaded" state) then the
      bag, so the body is `u1 + bag`. See `prefixed_bag_payload`.
    seq:
    - id: bag
      type: prefixed_bag_payload
  ac_learn_blueprint:
    doc: |
      ACK for learning a blueprint. status=0 success.
      Confirmed against capture ac_00e7_unknown.bin (33B): blueprint name
      "BP_Module_AdvancedHeal_T5_Rel".
    seq:
    - id: status
      type: u1
    - id: blueprint_def_name
      type: strz
      encoding: ASCII
  ac_get_free_space_save_data:
    doc: Free-space save data — a bag.
    seq:
    - id: bag
      type: bag_payload
  ac_disassemble_item:
    doc: |
      Field sequence from handler at 0x0822ee0b in OnRecieve dispatch.
      Reads: u8 u64
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_add_thumb_up:
    doc: |
      13 bytes. Request: echo + u16be(type) + u32be(0) + u32be(instance_id).
      Response: echo + u8(0x80) + u32be(0) + 4B(player/zone_id?) + u16be(flags).
    seq:
    - id: flags
      type: u1
    - id: padding
      type: u4be
    - id: zone_or_player_id
      size: 4
    - id: result_flags
      type: u2be
  ac_get_visited_free_space_zones:
    doc: Visited-zones bitmap — a bag.
    seq:
    - id: bag
      type: bag_payload
  ac_advert_create:
    doc: |
      3B (fail) or 61B (success).
      3B form: echo + u8(result=1 = slot full/fail).
      61B form: echo + u32be(0) + u32be(0) + u16be(advert_id) + null-term item name + more data.
    seq:
    - id: result
      type: u1
    - id: payload
      size-eos: true
  ac_advert_delete:
    doc: |
      Field sequence from handler at 0x08233a99 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_advert_header_get:
    doc: Advert headers — a bag.
    seq:
    - id: bag
      type: bag_payload
  ac_advert_get:
    doc: Single advert payload — a bag (advertId, vsender, …).
    seq:
    - id: bag
      type: bag_payload
  ac_buy_product_from_advert:
    doc: Simple ACK — echo(2B) + result byte (0 = success).
    seq:
    - id: result
      type: u1
  ac_emm_change_ready:
    seq:
    - id: unknown
      size-eos: true
  ac_unlim_pve_upgrade_player_level:
    doc: |
      Field sequence from handler at 0x08233710 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_unlim_pve_disable_player_buffs:
    doc: |
      Field sequence from handler at 0x08233d48 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_ta_stats_send_tutorial_entter:
    seq:
    - id: unknown
      size-eos: true
  ac_ta_stats_send_tutorial_exit:
    seq:
    - id: unknown
      size-eos: true
  ac_user_notes:
    doc: |
      Field sequence from handler at 0x0822f662 in OnRecieve dispatch.
      Reads: u32
    seq:
    - id: value
      type: u4be
  ac_user_notes_add:
    doc: Confirmation of user note added; echoes uid and note text
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
    - id: note
      type: strz
      encoding: UTF-8
  ac_user_notes_delete:
    doc: Confirmation of user note deletion
    seq:
    - id: status
      type: u1
    - id: flags
      type: u2be
    - id: uid
      type: u8be
  ac_battle_pass_unlock_level:
    doc: |
      Field sequence from handler at 0x0822c900 in OnRecieve dispatch.
      Reads: u8
    seq:
    - id: status
      type: u1
  ac_zones_lua_active_events_update:
    doc: |
      Scripted-event state for every zone — pushed S→C whenever the
      server's active-events table changes. Wire shape:
      `u1 has_data + bag {zone_id: {event_id: f32 seconds_or_sentinel}}`,
      where the f32 leaves are positive seconds-remaining or one of
      the `ai.ScriptsServer.{DISABLE,TIMEOUT,COMPLETED,FAILED,REMOVED}_EVENT`
      sentinels (-100500..-100504). Same shape as `bag_27` in
      `ac_load_initial_player_data`. Decoded by
      `ac_zones_lua_active_events_update_body.AcZonesLuaActiveEventsUpdateBody`.
    seq:
    - id: data
      type: ac_zones_lua_active_events_update_body
      size-eos: true
  ac_adventures:
    doc: |
      Available adventures list. u1 status + u1 count + count×u2be
      adventure_ids. Verified against 4B (count=0), 6B (count=1) and
      20B (count=8 IDs: 4,2,3,1,6,7,5,?) captures.
    seq:
    - id: status
      type: u1
    - id: count
      type: u1
    - id: adventure_ids
      type: u2be
      repeat: expr
      repeat-expr: count
  ac_adventure_cancel:
    seq:
    - id: unknown
      size-eos: true

  # ── Open-space / zone session packet types ────────────────────────────────
  # These types are pushed by the server during open-space play.
  # All have the standard 2-byte AC echo at the start of the body.

  zone_server_23:
    doc: |
      Server address notification for 23.x.x.x servers (30B).
      The type code 0x3233 = "23" ARE the first two bytes of the IP string,
      so the body starts mid-string at ".111.211.207\0".
      Layout: echo("23") + partial_ip(\0-terminated) + port(u16be)
              + field_a(u32be) + field_b(u32be) + field_c(u32be) + pad(u8).
      When in an active instance: field_a=0, field_b=instance_id, field_c=0.
      When idle: field_a=player_count, field_b=zone_id, field_c=capacity.
    seq:
    - id: ip_suffix
      type: strz
      encoding: ASCII
    - id: port
      type: u2be
    - id: field_a
      type: u4be
    - id: field_b
      type: u4be
    - id: field_c
      type: u4be
    - id: pad
      type: u1

  zone_server_89:
    doc: |
      Server address notification for 89.x.x.x servers (29B). Same
      structure as zone_server_23. Type 0x3839 = "89" = IP prefix.
    seq:
    - id: ip_suffix
      type: strz
      encoding: ASCII
    - id: port
      type: u2be
    - id: field_a
      type: u4be
    - id: field_b
      type: u4be
    - id: field_c
      type: u4be

  zone_instance_join:
    doc: |
      Zone instance notification. Two forms:
      Short (9B): echo + u24be(0) + u32be(instance_id) — join confirmation.
      Long (1097B): echo + u32be(0) + 3B(uid) + list of avatar names + player data.
      The long form is pushed once when a zone fills with players.
    seq:
    - id: payload
      size-eos: true

  zone_stats_list:
    doc: |
      Zone session stat counters (119B). 5 bytes header + 6 cs0-keyed entries.
      Header: u16be(0) + u8(0) + u16be(count=6).
      Entries (cs0-encoded key + u16be value + 3B padding each):
        munitionTransfered, munitionPurchased, credits,
        and 3 more (names still cs-encoded; values bit-packed).
    seq:
    - id: header
      size: 3
    - id: payload
      size-eos: true

  zone_player_health:
    doc: |
      Zone player health/shield status (70B). Contains float32 values
      for each player in the zone. 0x3f800000 = 1.0 (full health/shield).
      Repeating entries: 3B player_id + float32 health + more fields.
    seq:
    - id: padding
      type: u4be
    - id: payload
      size-eos: true

  zone_player_data:
    doc: |
      Player presence data. Two forms:
      Short (10B): echo + u24be(1) + 3B(player_uid_low) + u8(flags=0x03)
        — player online/join indicator.
      Long (78B): echo + u24be(0) + 3B(player_uid_low) + credits(u32be)
        + 64B bit-packed zone stats (damage dealt, kills, etc.) — full stats push.
      Appears after 0x0a00 (join) and 0x0900 (update) for the same player.
    seq:
    - id: payload
      size-eos: true

  zone_player_update:
    doc: |
      Player credits/status update in zone (13B).
      Layout: echo(2) + u24be(1) + 3B(player_uid_low) + 4B(value).
      The 3-byte player UID is the low 3 bytes of the player's full UID.
      Observed alongside zone_player_join for the same player.
    seq:
    - id: unknown_prefix
      type: u4be
    - id: player_uid_low
      size: 3
    - id: value
      type: u4be

  zone_player_join:
    doc: |
      Player join notification in zone (13B).
      Layout: echo(2) + u24be(1) + 3B(player_uid_low) + 4B(flags/status).
      Flags: 0x3f800000 = float 1.0 = player is fully online/active.
      Preceded by 0x8000 (player stats dump) and followed by 0x0700 (presence).
    seq:
    - id: unknown_prefix
      type: u4be
    - id: player_uid_low
      size: 3
    - id: status_flags
      type: u4be

  zone_membership:
    doc: |
      Zone membership event (26B). Contains two 3-byte player IDs.
      Constant bytes: u48be(0) + u16be(0x074b=1867) + u48be(0) + 3B(player_uid_low)
      + u48be(0) + u8(0x32=50) + u8(0x00).
      Appears when players enter/leave a zone.
    seq:
    - id: payload
      size: 24

  zone_kv_data:
    doc: |
      Open-space zone K-V data (376B). cs0-encoded key-value stream.
      Header: u16be(0) + u8(count=3).
      Known keys: "tier" (zone tier/rank), "auras" (active auras), "bundles".
      Values follow each key; type encoding unknown.
    seq:
    - id: header
      size: 2
    - id: payload
      size-eos: true

  zone_player_list:
    doc: Zone player list (283B). Structure not fully reversed.
    seq:
    - id: payload
      size-eos: true

  zone_military_rank:
    doc: |
      Player military rank updates (49B). count=3 at byte 4, then
      3 cs0-keyed entries starting at byte 5. First key = "militaryRank".
      Values are bit-packed after each cs0 key (format not fully reversed).
    seq:
    - id: header
      size: 3
    - id: payload
      size-eos: true

  zone_player_status:
    doc: |
      Brief player status update in zone (19B).
      Layout: echo(2) + u24be(1) + 3B(constant=0x3b34b2) + u8(0) + u8(1)
      + u48be(0) + 4B(varying value).
      The varying 4B at the end changes with player activity (credits? HP?).
      All examples share the same 3B constant, suggesting this is tied to a
      specific player or zone instance.
    seq:
    - id: prefix
      type: u4be
    - id: player_uid_or_constant
      size: 3
    - id: padding
      size: 6
    - id: value
      type: u4be
