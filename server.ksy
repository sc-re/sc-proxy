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
types:
  ac_load_initial_player_data:
    seq:
     - id: dummy
       type: u1
  ac_server_info:
    seq:
     - id: dummy
       type: u1
  ac_enter_mm_queue:
    seq:
     - id: dummy
       type: u1
  ac_leave_mm_queue:
    seq:
     - id: dummy
       type: u1
  ac_mm_info:
    seq:
     - id: dummy
       type: u1
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
     - id: dummy
       type: u1
  ac_player_credentials:
    seq:
     - id: dummy
       type: u1
  ac_player_credits:
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
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
       type: u1
  ac_quest_complete:
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
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
    seq:
     - id: dummy
       type: u1
  ac_vessel_repair_battle:
    seq:
     - id: dummy
       type: u1
  ac_vessel_refill_battle:
    seq:
     - id: dummy
       type: u1
  ac_vessel_strip_improper_battle:
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
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
    seq:
     - id: dummy
       type: u1
  ac_battle_slot_change_vessel:
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
       type: u1
  ac_buy_talent_set:
    seq:
     - id: dummy
       type: u1
  ac_react_on_abandoned_game:
    seq:
     - id: dummy
       type: u1
  ac_squad_info:
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
       type: u1
  ac_friends_accept_request:
    seq:
     - id: dummy
       type: u1
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
     - id: dummy
       type: u1
  ac_social_ignore_remove:
    seq:
     - id: dummy
       type: u1
  ac_social_watch_add:
    seq:
     - id: dummy
       type: u1
  ac_social_watch_remove:
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
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
    seq:
    - id: unknown
      type: u4
    - id: clan_id
      type: u4be
    - id: clan_name
      type: strz
      encoding: UTF-8
    - id: clan_tag
      type: strz
      encoding: UTF-8
    - id: motd
      type: strz
      encoding: UTF-8
    - id: description
      type: strz
      encoding: UTF-8
    - id: clan_icon
      type: strz
      encoding: UTF-8
    - id: clan_faction
      type: strz
      encoding: UTF-8
    - id: unknown1
      type: u8
    - id: unknown2
      type: u8
    - id: unknown3
      type: u8
    - id: unknown4
      type: u2
    - id: unknown5
      type: u1
    - id: member_count
      type: u4be
    - id: member_uids
      type: member
      repeat: expr
      repeat-expr: member_count
    - id: dummy
      type: u1
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
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
       type: u1
  ac_survey_get_new:
    seq:
     - id: dummy
       type: u1
  ac_survey_vote:
    seq:
     - id: dummy
       type: u1
  ac_survey_results:
    seq:
     - id: dummy
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
    seq:
     - id: dummy
       type: u1
  ac_mail_deliver:
    seq:
     - id: dummy
       type: u1
  ac_mail_send:
    seq:
     - id: dummy
       type: u1
  ac_mail_remove:
    seq:
     - id: dummy
       type: u1
  ac_mail_acknowledge_expiration:
    seq:
     - id: dummy
       type: u1
  ac_send_early_player_log:
    seq:
     - id: dummy
       type: u1
  ac_auto_pilot_space_station:
    seq:
     - id: dummy
       type: u1
  ac_undock_space_station:
    seq:
     - id: dummy
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
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
       type: u1
  ac_get_visited_free_space_zones:
    seq:
     - id: dummy
       type: u1
  ac_advert_create:
    seq:
     - id: dummy
       type: u1
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
    seq:
     - id: dummy
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
    seq:
    - id: dummy
      type: u1
  ac_user_notes_delete:
    seq:
     - id: dummy
       type: u1
  ac_battle_pass_unlock_level:
    seq:
     - id: dummy
       type: u1
  ac_zones_lua_active_events_update:
    seq:
     - id: dummy
       type: u1
  ac_adventures:
    seq:
     - id: dummy
       type: u1
  ac_adventure_cancel:
    seq:
     - id: dummy
       type: u1
