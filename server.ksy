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
    doc: Server response to initial load; variable content (login data or keepalive)
    seq:
    - id: dummy
      type: u1
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
      Matchmaking queue state update. Variable 213–305 bytes. Bit-packed,
      structure not fully reversed. Byte 2 = flags (0x80 = in queue).
      Subsequent bytes: player list + team compositions, encoded.
    seq:
    - id: flags
      type: u1
    - id: payload
      size-eos: true
  ac_enter_tournament:
    seq:
    - id: dummy
      type: u1
  ac_leave_tournament:
    seq:
    - id: dummy
      type: u1
  ac_get_userdata:
    seq:
    - id: dummy
      type: u1
  ac_set_userdata:
    seq:
    - id: unknown
      type: u2be
    - id: value
      type: u2be
  ac_player_credentials:
    doc: Player nickname and session credentials
    seq:
    - id: nickname
      type: strz
      encoding: ASCII
    - id: dummy
      type: u1
  ac_player_credits:
    doc: All currency balances for the player; variable-length, structure not fully understood
    seq:
    - id: dummy
      type: u1
  ac_player_stats:
    seq:
    - id: dummy
      type: u1
  ac_player_arc_balance:
    seq:
    - id: dummy
      type: u1
  ac_titles_set_active:
    seq:
    - id: dummy
      type: u1
  ac_avatars_set_active:
    seq:
    - id: dummy
      type: u1
  ac_mottos_set_active:
    seq:
    - id: dummy
      type: u1
  ac_choose_starting_station:
    seq:
    - id: dummy
      type: u1
  ac_change_player_nickname:
    seq:
    - id: dummy
      type: u1
  ac_steam_user_info:
    seq:
    - id: dummy
      type: u1
  ac_premium_info:
    doc: Premium account expiry timestamp in milliseconds
    seq:
    - id: expiry_ms
      type: u8be
  ac_premium_buy:
    seq:
    - id: dummy
      type: u1
  ac_account_auras:
    seq:
    - id: dummy
      type: u1
  ac_add_account_aura:
    seq:
    - id: dummy
      type: u1
  ac_cancel_account_aura:
    seq:
    - id: dummy
      type: u1
  ac_quests:
    seq:
    - id: dummy
      type: u1
  ac_quest_accept:
    seq:
    - id: dummy
      type: u1
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
    - id: dummy
      type: u1
  ac_ship_quests:
    seq:
    - id: dummy
      type: u1
  ac_ship_quest_start:
    seq:
    - id: dummy
      type: u1
  ac_ship_quest_change:
    seq:
    - id: dummy
      type: u1
  ac_ship_quest_end:
    seq:
    - id: dummy
      type: u1
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
    seq:
    - id: dummy
      type: u1
  ac_player_inventory:
    seq:
    - id: dummy
      type: u1
  ac_player_autogen_inventory:
    seq:
    - id: dummy
      type: u1
  ac_player_vessels:
    seq:
    - id: dummy
      type: u1
  ac_vessel_equipment:
    seq:
    - id: dummy
      type: u1
  ac_buy_item:
    seq:
    - id: dummy
      type: u1
  ac_sell_item:
    seq:
    - id: dummy
      type: u1
  ac_sell_items:
    seq:
    - id: dummy
      type: u1
  ac_enchant_item:
    seq:
    - id: dummy
      type: u1
  ac_salvage_item:
    seq:
    - id: dummy
      type: u1
  ac_salvage_items:
    seq:
    - id: dummy
      type: u1
  ac_upgrade_items:
    seq:
    - id: dummy
      type: u1
  ac_upgrade_autogen_item:
    seq:
    - id: dummy
      type: u1
  ac_craft_upgrade_item:
    seq:
    - id: dummy
      type: u1
  ac_find_autogen_item:
    seq:
    - id: dummy
      type: u1
  ac_activate_resource_vessel:
    seq:
    - id: dummy
      type: u1
  ac_sell_vessel:
    seq:
    - id: dummy
      type: u1
  ac_vessel_change_equip:
    seq:
    - id: dummy
      type: u1
  ac_vessel_change_equip_multi:
    seq:
    - id: dummy
      type: u1
  ac_vessel_cheat_change_equip:
    seq:
    - id: dummy
      type: u1
  ac_vessel_transfer_equip:
    seq:
    - id: dummy
      type: u1
  ac_vessel_strip_equip:
    seq:
    - id: dummy
      type: u1
  ac_vessel_change_munition:
    seq:
    - id: dummy
      type: u1
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
    seq:
    - id: dummy
      type: u1
  ac_vessel_autogen_destroy:
    seq:
    - id: dummy
      type: u1
  ac_vessel_autogen_dismantle:
    seq:
    - id: dummy
      type: u1
  ac_vessel_extract_exp:
    seq:
    - id: dummy
      type: u1
  ac_vessel_levelup:
    seq:
    - id: dummy
      type: u1
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
    seq:
    - id: dummy
      type: u1
  ac_vessel_refill_battle:
    seq:
    - id: dummy
      type: u1
  ac_vessel_strip_improper_battle:
    doc: Vessels removed from battle slots due to invalid configuration
    seq:
    - id: count
      type: u4be
    - id: entry_ids
      type: u1
      repeat: expr
      repeat-expr: count
  ac_vessel_free_custom_elements:
    seq:
    - id: dummy
      type: u1
  ac_vessel_custom_elements_buy:
    seq:
    - id: dummy
      type: u1
  ac_vessel_custom_elements_acknowledge_expiration:
    seq:
    - id: dummy
      type: u1
  ac_vessel_craft:
    seq:
    - id: dummy
      type: u1
  ac_vessel_recraft:
    seq:
    - id: dummy
      type: u1
  ac_vessel_budget_levelup:
    seq:
    - id: dummy
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
    - id: dummy
      type: u1
  ac_vessel_activate_node:
    seq:
    - id: dummy
      type: u1
  ac_battle_slots:
    doc: Battle loadout slots; slot_count active slots out of 6 total
    seq:
    - id: slot_count
      type: u4be
    - id: slots
      type: battle_slot
      repeat: expr
      repeat-expr: 6
    types:
      battle_slot:
        seq:
        - id: unknown
          type: u4be
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
    seq:
    - id: dummy
      type: u1
  ac_battle_slot_cheat_change_vessel:
    seq:
    - id: dummy
      type: u1
  ac_inv_ext_buy:
    seq:
    - id: dummy
      type: u1
  ac_autogen_inv_ext_buy:
    seq:
    - id: dummy
      type: u1
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
    seq:
    - id: dummy
      type: u1
  ac_buy_arc_dlc:
    seq:
    - id: dummy
      type: u1
  ac_talents_acquire:
    seq:
    - id: dummy
      type: u1
  ac_talents_update:
    seq:
    - id: dummy
      type: u1
  ac_talents_reset:
    seq:
    - id: dummy
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
    seq:
    - id: dummy
      type: u1
  ac_react_on_abandoned_game:
    seq:
    - id: dummy
      type: u1
  ac_squad_info:
    doc: Current squad state; zero fields when not in a squad
    seq:
    - id: squad_id
      type: u8be
    - id: leader_uid
      type: u8be
  ac_squad_invite_accept:
    seq:
    - id: dummy
      type: u1
  ac_squad_invite_decline:
    seq:
    - id: dummy
      type: u1
  ac_squad_leave:
    seq:
    - id: dummy
      type: u1
  ac_squad_invite_send:
    seq:
    - id: dummy
      type: u1
  ac_squad_invite_cancel:
    doc: Cancel Squad invite
    seq:
     - id: dummy
       type: u1
  ac_squad_kick:
    seq:
    - id: dummy
      type: u1
  ac_squad_ready:
    seq:
    - id: dummy
      type: u1
  ac_squad_convert_to_wing:
    seq:
    - id: dummy
      type: u1
  ac_league_team_info:
    seq:
    - id: dummy
      type: u1
  ac_league_team_create:
    seq:
    - id: dummy
      type: u1
  ac_league_team_invite_send:
    seq:
    - id: dummy
      type: u1
  ac_league_team_invite_cancel:
    seq:
    - id: dummy
      type: u1
  ac_league_team_invite_accept:
    seq:
    - id: dummy
      type: u1
  ac_league_team_kick:
    seq:
    - id: dummy
      type: u1
  ac_league_team_leave:
    seq:
    - id: dummy
      type: u1
  ac_league_team_invite_decline:
    seq:
    - id: dummy
      type: u1
  ac_league_team_request_names:
    seq:
    - id: dummy
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
    seq:
    - id: dummy
      type: u1
  ac_report_player:
    seq:
    - id: dummy
      type: u1
  ac_update_yup_purchases:
    seq:
    - id: dummy
      type: u1
  ac_check_yup_purchases:
    seq:
    - id: dummy
      type: u1
  ac_update_dlc_ownership:
    seq:
    - id: dummy
      type: u1
  ac_friends_send_request:
    doc: Friends list with UIDs and per-friend data
    seq:
    - id: dummy
      type: u1
  ac_friends_accept_request:
    doc: Result of accepting a friend request; uid is the new friend
    seq:
    - id: status
      type: u1
    - id: uid
      type: u8be
  ac_friends_reject_request:
    seq:
    - id: dummy
      type: u1
  ac_friends_remove:
    seq:
    - id: dummy
      type: u1
  ac_friends_list:
    seq:
    - id: dummy
      type: u1
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
    - id: dummy
      type: u1
  ac_social_suggest_fb:
    seq:
    - id: dummy
      type: u1
  ac_social_suggest_vk:
    seq:
    - id: dummy
      type: u1
  ac_teaching_list:
    seq:
    - id: dummy
      type: u1
  ac_teaching_request_to_teacher:
    seq:
    - id: dummy
      type: u1
  ac_teaching_request_to_student:
    seq:
    - id: dummy
      type: u1
  ac_teaching_accept:
    seq:
    - id: dummy
      type: u1
  ac_teaching_reject:
    seq:
    - id: dummy
      type: u1
  ac_teaching_check:
    seq:
    - id: dummy
      type: u1
  ac_teaching_allow:
    seq:
    - id: dummy
      type: u1
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
    seq:
    - id: dummy
      type: u1
  ac_obtain_referral_key:
    seq:
    - id: dummy
      type: u1
  ac_attach_steam_account:
    seq:
    - id: dummy
      type: u1
  ac_finalize_steam_mtxn:
    seq:
    - id: dummy
      type: u1
  ac_attach_yup_account:
    seq:
    - id: dummy
      type: u1
  ac_attach_email:
    seq:
    - id: dummy
      type: u1
  ac_lobby_list:
    seq:
    - id: dummy
      type: u1
  ac_lobby_join:
    seq:
    - id: dummy
      type: u1
  ac_lobby_create:
    seq:
    - id: dummy
      type: u1
  ac_lobby_info:
    seq:
    - id: dummy
      type: u1
  ac_lobby_kick:
    seq:
    - id: dummy
      type: u1
  ac_lobby_leave:
    seq:
    - id: dummy
      type: u1
  ac_lobby_invite:
    seq:
    - id: dummy
      type: u1
  ac_lobby_modify:
    seq:
    - id: dummy
      type: u1
  ac_lobby_start_game:
    seq:
    - id: dummy
      type: u1
  ac_lobby_group_list:
    seq:
    - id: dummy
      type: u1
  ac_lobby_group_info:
    seq:
    - id: dummy
      type: u1
  ac_lobby_group_create:
    seq:
    - id: dummy
      type: u1
  ac_lobby_group_modify:
    seq:
    - id: dummy
      type: u1
  ac_lobby_group_delete:
    seq:
    - id: dummy
      type: u1
  ac_lobby_group_joinreq_create:
    seq:
    - id: dummy
      type: u1
  ac_lobby_group_joinreq_cancel:
    seq:
    - id: dummy
      type: u1
  ac_lobby_group_joinreq_reject:
    seq:
    - id: dummy
      type: u1
  ac_clan_request_credentials:
    seq:
    - id: dummy
      type: u1
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
      doc: |
        Remaining bytes: a binary serialization of the `clanShips` map
        (keyed by design name: EmpireDesign, FederationDesign, JerichoDesign
        in the captured clans) and possibly `clanItemKeys`. Each ship entry
        carries defName, productionStartTime, productionCompleteAt,
        repairStartTime, repairEndTime, broken, boostBuildingBudget,
        boostRepairingBudget, partBeingBuilt, slotBeingBuilt, curZone,
        moduleSlots, mainParts.

        The stream mixes three string encodings within the same record —
        cs-shifted keys (e.g. main_1, moduleSlots, productionStartTime,
        broken, curZone), x2-encoded keys (e.g. FederationDesign at
        offset 0x5b1 of the FD stream), and cleartext null-terminated
        keys (e.g. defName, mainParts, FederationDesign at 0x5d0). At
        least one ship record also contains a 160-byte opaque binary
        hash-table header inside moduleSlots whose bytes are constant
        across sessions.

        Observed sizes: 4238 bytes (GD3F, 300-member clan) and 4168
        bytes (TerraLuX, 254-member clan). Size varies with fitted/built
        module counts per ship slot.
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
    doc: Clan profile for a player; uid is the queried player
    seq:
    - id: uid
      type: u8be
    - id: unknown
      type: u8be
  ac_clan_joinreq_create:
    seq:
    - id: dummy
      type: u1
  ac_clan_joinreq_cancel:
    seq:
    - id: dummy
      type: u1
  ac_clan_joinreq_accept:
    seq:
    - id: dummy
      type: u1
  ac_clan_invite_send:
    seq:
    - id: dummy
      type: u1
  ac_clan_invite_accept:
    seq:
    - id: dummy
      type: u1
  ac_clan_invite_cancel:
    seq:
    - id: dummy
      type: u1
  ac_clan_kick:
    seq:
    - id: dummy
      type: u1
  ac_clan_leave:
    seq:
    - id: dummy
      type: u1
  ac_clan_set_role:
    seq:
    - id: dummy
      type: u1
  ac_clan_change_motd:
    seq:
    - id: dummy
      type: u1
  ac_clan_change_desc:
    seq:
    - id: dummy
      type: u1
  ac_clan_change_recruiting:
    seq:
    - id: dummy
      type: u1
  ac_clan_resource_convert:
    seq:
    - id: dummy
      type: u1
  ac_clan_ship_build:
    seq:
    - id: dummy
      type: u1
  ac_clan_ship_boost_building:
    seq:
    - id: dummy
      type: u1
  ac_clan_ship_repair:
    seq:
    - id: dummy
      type: u1
  ac_clan_ship_boost_repairing:
    seq:
    - id: dummy
      type: u1
  ac_clan_ship_fit:
    seq:
    - id: dummy
      type: u1
  ac_clan_ship_set_current:
    seq:
    - id: dummy
      type: u1
  ac_clan_universe_move:
    seq:
    - id: dummy
      type: u1
  ac_clan_set_civilian_zone:
    seq:
    - id: dummy
      type: u1
  ac_clan_revive_in_war:
    seq:
    - id: dummy
      type: u1
  ac_clan_war_start:
    seq:
    - id: dummy
      type: u1
  ac_clan_quest_accept:
    seq:
    - id: dummy
      type: u1
  ac_clan_create:
    seq:
    - id: dummy
      type: u1
  ac_clan_upgrade:
    seq:
    - id: dummy
      type: u1
  ac_clan_change_name:
    seq:
    - id: dummy
      type: u1
  ac_clan_change_tag:
    seq:
    - id: dummy
      type: u1
  ac_clan_assign_emblem:
    seq:
    - id: dummy
      type: u1
  ac_clan_bank_transfer:
    seq:
    - id: dummy
      type: u1
  ac_clan_list_recruiting:
    seq:
    - id: dummy
      type: u1
  ac_clan_history_get:
    seq:
    - id: dummy
      type: u1
  ac_related_quest_enable:
    seq:
    - id: dummy
      type: u1
  ac_user_profile_get:
    seq:
    - id: dummy
      type: u1
  ac_achievements:
    seq:
    - id: dummy
      type: u1
  ac_admin_cmd:
    seq:
    - id: dummy
      type: u1
  ac_games_info:
    seq:
    - id: dummy
      type: u1
  ac_zone_instances_info:
    seq:
    - id: dummy
      type: u1
  ac_get_punishments:
    seq:
    - id: dummy
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
    doc: Response to survey poll; all-zero when no surveys available
    seq:
    - id: reserved
      type: u4be
    - id: status
      type: u1
  ac_survey_vote:
    seq:
    - id: dummy
      type: u1
  ac_survey_results:
    doc: Survey result data; all-zero when no surveys active
    seq:
    - id: reserved
      type: u4be
    - id: status
      type: u1
  ac_universe_get:
    seq:
    - id: dummy
      type: u1
  ac_universe_counters:
    seq:
    - id: dummy
      type: u1
  ac_warmap_get:
    seq:
    - id: dummy
      type: u1
  ac_mail_get:
    doc: Mailbox response; contains zero or more mail messages
    seq:
    - id: num_messages
      type: u4be
    - id: messages
      type: mail_message
      repeat: expr
      repeat-expr: num_messages
    types:
      mail_message:
        seq:
        - id: dummy
          type: u1
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
    doc: Result of sending mail; status + assigned mail ID
    seq:
    - id: status
      type: u1
    - id: unknown
      type: u1
    - id: mail_id
      type: u4be
  ac_mail_remove:
    seq:
    - id: dummy
      type: u1
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
    - id: dummy
      type: u1
  ac_auto_pilot_space_station:
    seq:
    - id: dummy
      type: u1
  ac_undock_space_station:
    doc: Undock result; status 0 = success
    seq:
    - id: status
      type: u1
  ac_set_visited_zone:
    seq:
    - id: dummy
      type: u1
  ac_zone_coordinator_gm_command:
    seq:
    - id: dummy
      type: u1
  ac_space_stations_population:
    seq:
    - id: dummy
      type: u1
  ac_karma_reset:
    seq:
    - id: dummy
      type: u1
  ac_faction_rep_reset:
    seq:
    - id: dummy
      type: u1
  ac_leaderboard_get:
    seq:
    - id: dummy
      type: u1
  ac_leaderboard_get_descs:
    seq:
    - id: dummy
      type: u1
  ac_set_fb_token:
    seq:
    - id: dummy
      type: u1
  ac_get_fb_token:
    doc: Facebook token (18-byte blob, all-zero when not linked)
    seq:
    - id: token
      size: 18
  ac_log_fb_event:
    seq:
    - id: dummy
      type: u1
  ac_get_craft_resources:
    seq:
    - id: dummy
      type: u1
  ac_use_blueprint:
    seq:
    - id: dummy
      type: u1
  ac_sell_craft_resource:
    seq:
    - id: dummy
      type: u1
  ac_sell_craft_resources:
    seq:
    - id: dummy
      type: u1
  ac_get_blueprints:
    seq:
    - id: dummy
      type: u1
  ac_learn_blueprint:
    seq:
    - id: dummy
      type: u1
  ac_get_free_space_save_data:
    seq:
    - id: dummy
      type: u1
  ac_disassemble_item:
    seq:
    - id: dummy
      type: u1
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
    seq:
    - id: dummy
      type: u1
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
    seq:
    - id: dummy
      type: u1
  ac_advert_header_get:
    seq:
    - id: dummy
      type: u1
  ac_advert_get:
    seq:
    - id: dummy
      type: u1
  ac_buy_product_from_advert:
    doc: Simple ACK — echo(2B) + result byte (0 = success).
    seq:
    - id: result
      type: u1
  ac_emm_change_ready:
    seq:
    - id: dummy
      type: u1
  ac_unlim_pve_upgrade_player_level:
    seq:
    - id: dummy
      type: u1
  ac_unlim_pve_disable_player_buffs:
    seq:
    - id: dummy
      type: u1
  ac_ta_stats_send_tutorial_entter:
    seq:
    - id: dummy
      type: u1
  ac_ta_stats_send_tutorial_exit:
    seq:
    - id: dummy
      type: u1
  ac_user_notes:
    seq:
    - id: dummy
      type: u1
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
    seq:
    - id: dummy
      type: u1
  ac_zones_lua_active_events_update:
    doc: Active Lua event status for zones
    seq:
    - id: status
      type: u1
  ac_adventures:
    doc: Available adventures list; status=0 ok, count=number of adventures
    seq:
    - id: status
      type: u1
    - id: count
      type: u1
    - id: reserved
      type: u2be
  ac_adventure_cancel:
    seq:
    - id: dummy
      type: u1

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
