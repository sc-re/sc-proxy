meta:
  id: star_conflict_package_client
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
## Client request encodings overview
##
## After the 2-byte u2be packet_type that opens every CSCMD_ASYNC_REQ, the
## body uses one of the following encodings. Most ACs (~80% of the table)
## have *no* body — they're pure RPC verbs whose meaning is the AC ID
## itself. Across the 27 ACs we have C-to-S captures for, the observed
## encodings are:
##
## 1. **empty** (body length 0)
##    Most polling/list-fetch verbs: ac_server_info, ac_quests,
##    ac_squad_info, ac_clan_request_desc, ac_universe_get, …
##
## 2. **cleartext NUL-terminated locale** ("en\0", 3 bytes)
##    ac_welcome_msg, ac_motd, ac_survey_get_new, ac_survey_results,
##    ac_mail_get. Written byte-aligned.
##
## 3. **single u8be value** (8 bytes) — a player UID or clan ID
##    ac_clan_request_profile / ac_achievements (player UID),
##    ac_warmap_get (clan ID), ac_zones_lua_active_events_update
##
## 4. **u4be count + count × u8be UID** (4 + N×8 bytes)
##    ac_get_nicknames, ac_clan_request_credentials. Bulk fetch keyed by
##    a list of UIDs.
##
## 5. **bit-packed property bag** (notification.py format, 0x08b1ed60)
##    ac_set_userdata, ac_leaderboard_get. Wire format identical to
##    SCMD_NOTIFICATION:
##      u32be num_entries
##      if num_entries > 0:
##        u1 use_indexed_keys
##        repeat num_entries:
##          if !use_indexed_keys: cstring key (8-bit chars in bit-stream)
##          variant value: u8 tag + per-tag payload
##    Variant tags: 0x00 nil, 0x01 i32, 0x02 u64a, 0x03 u64b, 0x04 f32,
##    0x05 str, 0x06 nested-bag, 0x07 blob12, 0x08 bool. Because the bag
##    is bit-aligned, cstring reads at bit-offset 1 produce what we call
##    "cs0" strings in the server's FedDesign TGP format — i.e., cs0 is
##    a *consequence* of bit-packing, not a separate encoding the client
##    is using.
##
## 6. **u4be count + N × {u8be uid + u8 flag} + variable trailer**
##    ac_user_profile_get larger forms (≥98 B). count=N, then 9-byte
##    records, then a 2/14/etc-byte trailer whose semantics we have not
##    yet identified. Small forms (16/17 B) use one record + 2/3-byte
##    trailer.
##
## What's *not* used in client requests:
##   * x2 strings (char<<1) — only seen in server FedDesign TGP streams
##   * 0x0c-tagged structs / 0x06-tagged arrays / 0x18-tagged u32be —
##     part of the FedDesign TGP type system, not the client's.
##
## The actual byte-level writing primitives all live in the BitStream
## helpers: FUN_08b21130 (write_bits), called by FUN_08b19fc0 (write_u16
## for the AC ID) and through the per-AC handlers that build the body.

types:
  ac_load_initial_player_data:
    doc: |
      Empty body in keepalive captures (just the 2-byte u2be packet_type).
      Some game versions have observed it carrying a 4-byte session token,
      but our captures all show body=0.
    seq:
    - id: maybe_session
      size-eos: true
  ac_server_info:
    doc: Empty request, server responds with server info
  ac_enter_mm_queue:
    seq:
    - id: unknown
      size-eos: true
  ac_leave_mm_queue:
    seq:
    - id: unknown
      size-eos: true
  ac_mm_info:
    seq:
    - id: unknown
      size-eos: true
  ac_enter_tournament:
    seq:
    - id: unknown
      size-eos: true
  ac_leave_tournament:
    seq:
    - id: unknown
      size-eos: true
  ac_get_userdata:
    seq:
    - id: unknown
      size-eos: true
  ac_set_userdata:
    doc: |
      Bit-packed property bag (encoding #5 — see overview above). Observed
      18 or 24 entries depending on which user-data slots changed; each
      entry has a cstring key (cs0 keys when read at bit-offset 1) and a
      variant value. Sample keys: helpShown, magenta, etc.
    seq:
    - id: bag
      type: bag_payload
  ac_player_credentials:
    seq:
    - id: unknown
      size-eos: true
  ac_player_credits:
    seq:
    - id: unknown
      size-eos: true
  ac_player_stats:
    seq:
    - id: unknown
      size-eos: true
  ac_player_arc_balance:
    seq:
    - id: unknown
      size-eos: true
  ac_titles_set_active:
    seq:
    - id: unknown
      size-eos: true
  ac_avatars_set_active:
    seq:
    - id: unknown
      size-eos: true
  ac_mottos_set_active:
    doc: Set active motto by name
    seq:
    - id: motto_id
      type: strz
      encoding: ASCII
  ac_choose_starting_station:
    seq:
    - id: unknown
      size-eos: true
  ac_change_player_nickname:
    seq:
    - id: unknown
      size-eos: true
  ac_steam_user_info:
    seq:
    - id: unknown
      size-eos: true
  ac_premium_info:
    seq:
    - id: unknown
      size-eos: true
  ac_premium_buy:
    seq:
    - id: unknown
      size-eos: true
  ac_account_auras:
    seq:
    - id: unknown
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
    doc: Empty request, server responds with quest list
  ac_quest_accept:
    seq:
    - id: unknown
      size-eos: true
  ac_quest_change:
    seq:
    - id: unknown
      size-eos: true
  ac_quest_complete:
    seq:
    - id: unknown
      size-eos: true
  ac_quest_complete_all:
    seq:
    - id: unknown
      size-eos: true
  ac_ship_quests:
    seq:
    - id: unknown
      size-eos: true
  ac_ship_quest_start:
    seq:
    - id: unknown
      size-eos: true
  ac_ship_quest_change:
    seq:
    - id: unknown
      size-eos: true
  ac_ship_quest_end:
    seq:
    - id: unknown
      size-eos: true
  ac_rewarded_tutorials:
    seq:
    - id: unknown
      size-eos: true
  ac_reward_tutorial:
    seq:
    - id: unknown
      size-eos: true
  ac_player_inventory:
    seq:
    - id: unknown
      size-eos: true
  ac_player_autogen_inventory:
    seq:
    - id: unknown
      size-eos: true
  ac_player_vessels:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_equipment:
    seq:
    - id: unknown
      size-eos: true
  ac_buy_item:
    doc: |
      Buy-item C->S request. Encoder FUN_082576a0 (called by the
      `GameStore_Buy(storeItemId, amount, creditsType, [mode])` Lua
      binding @FUN_082640a0) writes: u32 store_item_id + u32 amount
      (clamped 1..0x3fff) + u8 credits_type + u1 has_discount
      (client-computed from the discount-aura catalog) + u32 mode (the
      4th Lua arg; 0xffffffff when omitted). 14-byte body with 7 bits
      of trailing padding. The 1-bit has_discount makes the trailing
      u32 bit-misaligned, so decoded by
      ac_buy_item_request_body.AcBuyItemRequestBody.
    seq:
    - id: data
      type: ac_buy_item_request_body
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
    seq:
    - id: unknown
      size-eos: true
  ac_salvage_item:
    seq:
    - id: unknown
      size-eos: true
  ac_salvage_items:
    seq:
    - id: unknown
      size-eos: true
  ac_upgrade_items:
    seq:
    - id: unknown
      size-eos: true
  ac_upgrade_autogen_item:
    seq:
    - id: unknown
      size-eos: true
  ac_craft_upgrade_item:
    seq:
    - id: unknown
      size-eos: true
  ac_find_autogen_item:
    seq:
    - id: unknown
      size-eos: true
  ac_activate_resource_vessel:
    seq:
    - id: unknown
      size-eos: true
  ac_sell_vessel:
    doc: Sell vessel by ID
    seq:
    - id: unknown
      type: u4be
    - id: vessel_id
      type: u4be
  ac_vessel_change_equip:
    doc: |
      Equip a single module into one of the vessel's slots — fully
      byte-aligned, no bit-packing.
    seq:
    - id: vessel_id
      type: u8be
    - id: slot_idx
      type: u1
    - id: module_id
      type: u8be
  ac_vessel_change_equip_multi:
    doc: |
      Equip several modules into a vessel in one packet. Bit-packed
      (cs0/cleartext strings interleaved with binary fields), unlike the
      byte-aligned single-equip variant. Surfaced via
      ac_vessel_change_equip_multi_request_body, which decodes the
      vessel_id + num_changes header and reports any cs0/cleartext
      strings (slot categories like "ammo" and module def-names like
      "WeaponMod_RailPerfect_Mk1") it finds in the body.
    seq:
    - id: data
      type: ac_vessel_change_equip_multi_request_body
      size-eos: true
  ac_vessel_cheat_change_equip:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_transfer_equip:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_strip_equip:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_change_munition:
    seq:
    - id: vessel_id
      type: u8be
    - id: slot
      type: u1
      enum: slot_type
    - id: resource
      type: u1
    - id: def_name
      type: strz
      encoding: ASCII
    enums:
      slot_type:
        0: ammunition
        1: missile
  ac_vessel_refill_munition:
    doc: Refill vessel munitions
    seq:
    - id: vessel_id
      type: u8be
  ac_vessel_transfer_munition:
    doc: Switch Munition between two vessels
    seq:
    - id: vessel_id1
      doc: Vessel ID 1
      type: u8be
    - id: vessel_id2
      doc: Vessel ID 2
      type: u8be
    - id: slot1
      type: u1
      enum: slot_type
    - id: slot2
      type: u1
      enum: slot_type
    enums:
      slot_type:
        0: ammunition
        1: missile
  ac_vessel_autogen_destroy:
    seq:
    - id: iid
      type: u8be
  ac_vessel_autogen_dismantle:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_extract_exp:
    doc: |
      Request to extract experience from a list of vessels.
      Fully byte-aligned: u4 count + count × u8 vessel_id + u4 amount.
    seq:
    - id: num_vessels
      type: u4be
    - id: vessel_ids
      type: u8be
      repeat: expr
      repeat-expr: num_vessels
    - id: amount
      type: u4be
  ac_vessel_levelup:
    doc: Level up vessel
    seq:
    - id: vessel_id
      type: u8be
  ac_vessel_repair:
    doc: Repair vessel
    seq:
    - id: vessel_id
      type: u8be
    - id: flags
      type: u1
  ac_vessel_repair_battle:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_refill_battle:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_strip_improper_battle:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_free_custom_elements:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_custom_elements_buy:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_custom_elements_acknowledge_expiration:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_craft:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_recraft:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_budget_levelup:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_budget_activate:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_unlock_node:
    seq:
    - id: unknown
      size-eos: true
  ac_vessel_activate_node:
    seq:
    - id: unknown
      size-eos: true
  ac_battle_slots:
    seq:
    - id: unknown
      size-eos: true
  ac_battle_slot_change_vessel:
    doc: Change vessel in a battle slot
    seq:
    - id: slot
      type: u1
    - id: vessel_id
      type: u8be
  ac_battle_slot_swap_vessels:
    seq:
    - id: slot1
      type: u1
    - id: slot2
      type: u1
  ac_battle_slot_cheat_change_vessel:
    seq:
    - id: slot
      type: u1
    - id: def_name
      type: strz
      encoding: ASCII
  ac_inv_ext_buy:
    seq:
    - id: unknown
      size-eos: true
  ac_autogen_inv_ext_buy:
    seq:
    - id: unknown
      size-eos: true
  ac_exchange_gold:
    doc: Request the exchange of gold for credits
    seq:
    - id: id
      type: u1
      enum: credit_gs_level
    enums:
      credit_gs_level:
        0: gs20_credits_140_000
        1: gs100_credits_740_000
        2: gs1_000_credits_7_700_000
        3: gs2_500_credits_19_900_000
        4: gs5_000_credits_41_200_000
        5: gs10_000_credits_87_500_000
  ac_buy_gold:
    seq:
    - id: unknown
      size-eos: true
  ac_buy_arc_dlc:
    seq:
    - id: unknown
      size-eos: true
  ac_talents_acquire:
    doc: Acquire talent by bitmask
    seq:
    - id: unknown
      type: u4be
    - id: talent_mask
      type: u4be
    - id: reserved
      type: u1
  ac_talents_update:
    seq:
    - id: unknown
      size-eos: true
  ac_talents_reset:
    seq:
    - id: talent_set
      type: u4be
  ac_talents_assign_sets:
    doc: Assign talent sets to 4 battle role slots
    seq:
    - id: set_ids
      type: u1
      repeat: expr
      repeat-expr: 4
  ac_buy_talent_set:
    seq:
    - id: unknown
      size-eos: true
  ac_react_on_abandoned_game:
    doc: |
      Player's reaction to a previously-abandoned game (sub of single-player
      practice cleanup). gameMode determines result code: 5→0 (abandon),
      7→3 (request review), 6→1 (dismiss; only when payload flag is set).
      Wire format: u8 result + u64be ship_id_pair + u8(0).
      Confirmed via FUN_082051a0 (WriteU8 + WriteU64 + WriteU8).
    seq:
    - id: result
      type: u1
    - id: ship_id
      type: u8be
    - id: reserved
      type: u1
  ac_squad_info:
    doc: Empty request, server responds with squad info
  ac_squad_invite_accept:
    seq:
    - id: unknown
      size-eos: true
  ac_squad_invite_decline:
    seq:
    - id: unknown
      size-eos: true
  ac_squad_leave:
    seq:
    - id: unknown
      size-eos: true
  ac_squad_invite_send:
    doc: Request to invite player by UID into the player's squad.
    seq:
    - id: uid
      type: u8be
  ac_squad_invite_cancel:
    doc: Cancel a pending outbound squad-invite by UID.
    seq:
    - id: uid
      type: u8be
  ac_squad_kick:
    seq:
    - id: unknown
      size-eos: true
  ac_squad_ready:
    seq:
    - id: unknown
      size-eos: true
  ac_squad_convert_to_wing:
    seq:
    - id: unknown
      size-eos: true
  ac_league_team_info:
    doc: Empty request, server responds with league team info
  ac_league_team_create:
    seq:
    - id: unknown
      size-eos: true
  ac_league_team_invite_send:
    seq:
    - id: unknown
      size-eos: true
  ac_league_team_invite_cancel:
    seq:
    - id: unknown
      size-eos: true
  ac_league_team_invite_accept:
    seq:
    - id: unknown
      size-eos: true
  ac_league_team_kick:
    seq:
    - id: unknown
      size-eos: true
  ac_league_team_leave:
    seq:
    - id: unknown
      size-eos: true
  ac_league_team_invite_decline:
    seq:
    - id: unknown
      size-eos: true
  ac_league_team_request_names:
    seq:
    - id: unknown
      size-eos: true
  ac_get_nicknames:
    doc: |
      Bulk nickname lookup — encoding #4 (u4be count + count×u8be UID).
      Observed counts up to 256 across captures (likely the server-side
      page size).
    seq:
    - id: num_uids
      type: u4be
    - id: uids
      type: u8be
      repeat: expr
      repeat-expr: num_uids
  ac_get_uids:
    seq:
    - id: unknown
      size-eos: true
  ac_report_player:
    seq:
    - id: unknown
      size-eos: true
  ac_update_yup_purchases:
    seq:
    - id: unknown
      size-eos: true
  ac_check_yup_purchases:
    seq:
    - id: unknown
      size-eos: true
  ac_update_dlc_ownership:
    seq:
    - id: unknown
      size-eos: true
  ac_friends_send_request:
    doc: Empty request, initiates friend request flow
  ac_friends_accept_request:
    doc: Accept friend request from player UID
    seq:
    - id: uid
      type: u8be
  ac_friends_reject_request:
    doc: |
      Reject incoming friend request by player UID.
      Confirmed via FUN_08210a20 ("/friends reject" CLI handler).
    seq:
    - id: uid
      type: u8be
  ac_friends_remove:
    doc: |
      Remove existing friend by player UID.
      Confirmed via FUN_08210a20 ("/friends remove" CLI handler).
    seq:
    - id: uid
      type: u8be
  ac_friends_list:
    seq:
    - id: unknown
      size-eos: true
  ac_social_ignore_add:
    doc: Request to add/remove player by UID
    seq:
    - id: uid
      type: u8be
  ac_social_ignore_remove:
    doc: Request to add/remove player by UID
    seq:
    - id: uid
      type: u8be
  ac_social_watch_add:
    doc: Request to add/remove player by UID
    seq:
    - id: uid
      type: u8be
  ac_social_watch_remove:
    doc: Request to add/remove player by UID
    seq:
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
    doc: Empty request, server responds with teaching list
  ac_teaching_request_to_teacher:
    seq:
    - id: unknown
      size-eos: true
  ac_teaching_request_to_student:
    seq:
    - id: unknown
      size-eos: true
  ac_teaching_accept:
    seq:
    - id: unknown
      size-eos: true
  ac_teaching_reject:
    seq:
    - id: unknown
      size-eos: true
  ac_teaching_check:
    seq:
    - id: unknown
      size-eos: true
  ac_teaching_allow:
    doc: |
      Teaching-allow toggle — single u1 `allow` bit. The role (teacher
      vs student) is not on the wire; the server keeps the current role
      context and updates the matching allow slot.
    seq:
    - id: allow
      type: b1
  ac_referrals:
    seq:
    - id: unknown
      size-eos: true
  ac_set_referrer:
    seq:
    - id: unknown
      size-eos: true
  ac_obtain_referral_key:
    seq:
    - id: unknown
      size-eos: true
  ac_attach_steam_account:
    seq:
    - id: unknown
      size-eos: true
  ac_finalize_steam_mtxn:
    seq:
    - id: unknown
      size-eos: true
  ac_attach_yup_account:
    seq:
    - id: unknown
      size-eos: true
  ac_attach_email:
    doc: |
      Attach email account credentials. Four ASCII strings:
      auth_token, email, password, system_id.
      Confirmed via FUN_082078c0 (writes 4 cstrings via WriteCString).
    seq:
    - id: auth_token
      type: strz
      encoding: ASCII
    - id: email
      type: strz
      encoding: ASCII
    - id: password
      type: strz
      encoding: ASCII
    - id: system_id
      type: strz
      encoding: ASCII
  ac_lobby_list:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_join:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_create:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_info:
    doc: Empty request, server responds with lobby info
  ac_lobby_kick:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_leave:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_invite:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_modify:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_start_game:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_list:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_info:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_create:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_modify:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_delete:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_joinreq_create:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_joinreq_cancel:
    seq:
    - id: unknown
      size-eos: true
  ac_lobby_group_joinreq_reject:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_request_credentials:
    doc: |
      Bulk-fetch clan credentials for a list of UIDs — encoding #4
      (u4be count + count × u8be UID).
    seq:
    - id: num_uids
      type: u4be
    - id: uids
      type: u8be
      repeat: expr
      repeat-expr: num_uids
  ac_clan_request_desc:
    doc: |
      Empty body — encoding #1. Server responds with the clan's full
      description (including the FedDesign TGP stream, see server.ksy).
  ac_clan_request_profile:
    doc: |
      Single u8be player UID — encoding #3.
    seq:
    - id: uid
      type: u8be
  ac_clan_joinreq_create:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_joinreq_cancel:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_joinreq_accept:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_invite_send:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_invite_accept:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_invite_cancel:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_kick:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_leave:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_set_role:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_change_motd:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_change_desc:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_change_recruiting:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_resource_convert:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_ship_build:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_ship_boost_building:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_ship_repair:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_ship_boost_repairing:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_ship_fit:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_ship_set_current:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_universe_move:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_set_civilian_zone:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_revive_in_war:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_war_start:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_quest_accept:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_create:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_upgrade:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_change_name:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_change_tag:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_assign_emblem:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_bank_transfer:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_list_recruiting:
    seq:
    - id: unknown
      size-eos: true
  ac_clan_history_get:
    seq:
    - id: unknown
      size-eos: true
  ac_related_quest_enable:
    seq:
    - id: unknown
      size-eos: true
  ac_user_profile_get:
    doc: |
      Bulk-fetch user profiles request — bit-packed u32 count + count ×
      {u64 uid + varuint flags}, where `flags` is a UPF_* bitmask asking
      the server which fields to include in the response. No per-flag
      payload follows in the request; that's why each record is exactly
      73 bits (when flags fit in 1+8 varuint) and successive records'
      byte-alignment slides by 1 bit per record. Decoded by
      ac_user_profile_get_request_body.AcUserProfileGetRequestBody.
    seq:
    - id: data
      type: ac_user_profile_get_request_body
      size-eos: true
  ac_achievements:
    doc: |
      Single u8be player UID — encoding #3.
    seq:
    - id: uid
      type: u8be
  ac_admin_cmd:
    seq:
    - id: unknown
      size-eos: true
  ac_games_info:
    seq:
    - id: unknown
      size-eos: true
  ac_zone_instances_info:
    seq:
    - id: unknown
      size-eos: true
  ac_get_punishments:
    seq:
    - id: unknown
      size-eos: true
  ac_welcome_msg:
    doc: Client requests welcome message in specified language
    seq:
    - id: lang
      type: strz
      encoding: ASCII
  ac_motd:
    doc: Client requests MOTD in specified language
    seq:
    - id: lang
      type: strz
      encoding: ASCII
  ac_survey_get_new:
    doc: Request new survey in specified language
    seq:
    - id: lang
      type: strz
      encoding: ASCII
  ac_survey_vote:
    seq:
    - id: unknown
      size-eos: true
  ac_survey_results:
    doc: Request survey results in specified language
    seq:
    - id: lang
      type: strz
      encoding: ASCII
  ac_universe_get:
    doc: Empty request, server responds with universe data
  ac_universe_counters:
    seq:
    - id: unknown
      size-eos: true
  ac_warmap_get:
    doc: |
      Single u8be — encoding #3. Treated as a zone-or-clan id (we've
      observed the clan id 1534 for GD3F here). Server answers with the
      sector ownership map.
    seq:
    - id: zone_id
      type: u8be
  ac_mail_get:
    doc: Client requests mailbox contents in specified language
    seq:
    - id: lang
      type: strz
      encoding: ASCII
  ac_mail_deliver:
    doc: |
      Confirm pickup of a mail item. u64be mail_id + u1 flag (bit-packed).
      Confirmed via FUN_08208e30 (WriteU64 + WriteBit).
    seq:
    - id: mail_id
      type: u8be
    - id: flag_byte
      type: u1
      doc: Top bit (0x80) = u1 flag; remaining bits padding.
  ac_mail_send:
    doc: |
      Send-mail request — u64 recipient + cstring subject + cstring body
      + attachment bag. Decoded by
      ac_mail_send_request_body.AcMailSendRequestBody.
    seq:
    - id: data
      type: ac_mail_send_request_body
      size-eos: true
  ac_mail_remove:
    doc: Delete-mail request — single u64 mail_id.
    seq:
    - id: mail_id
      type: u8be
  ac_mail_acknowledge_expiration:
    seq:
    - id: unknown
      size-eos: true
  ac_send_early_player_log:
    seq:
    - id: unknown
      size-eos: true
  ac_auto_pilot_space_station:
    seq:
    - id: unknown
      size-eos: true
  ac_undock_space_station:
    seq:
    - id: unknown
      size-eos: true
  ac_set_visited_zone:
    doc: |
      Mark a zone as visited. u16be zone_id + u1 flag (bit-packed; 17 bits
      total, padded to 3 bytes). Validated zone_id in [1, 0x200].
      Confirmed via FUN_08208930 (WriteU16 + WriteBit).
    seq:
    - id: zone_id
      type: u2be
    - id: flag_byte
      type: u1
      doc: High bit (0x80) carries the u1 flag; remaining bits padding.
  ac_zone_coordinator_gm_command:
    seq:
    - id: unknown
      size-eos: true
  ac_space_stations_population:
    seq:
    - id: unknown
      size-eos: true
  ac_karma_reset:
    seq:
    - id: unknown
      size-eos: true
  ac_faction_rep_reset:
    seq:
    - id: unknown
      size-eos: true
  ac_leaderboard_get:
    doc: |
      Bit-packed property bag — encoding #5. Observed 2-4 entries
      including a "lb" key with the leaderboard name (e.g.
      "player_eff_rating_weekly", "player_eff_rating_player_total")
      and pagination/filter scalars.
    seq:
    - id: bag
      type: bag_payload
  ac_leaderboard_get_descs:
    doc: Empty request, server responds with leaderboard descriptors
  ac_set_fb_token:
    seq:
    - id: unknown
      size-eos: true
  ac_get_fb_token:
    seq:
    - id: unknown
      size-eos: true
  ac_log_fb_event:
    seq:
    - id: unknown
      size-eos: true
  ac_get_craft_resources:
    seq:
    - id: unknown
      size-eos: true
  ac_use_blueprint:
    doc: |
      Use (craft from) a blueprint by name. Fully byte-aligned.
    seq:
    - id: blueprint_name
      type: strz
      encoding: ASCII
    - id: count
      type: u4be
  ac_sell_craft_resource:
    seq:
    - id: unknown
      size-eos: true
  ac_sell_craft_resources:
    seq:
    - id: unknown
      size-eos: true
  ac_get_blueprints:
    seq:
    - id: unknown
      size-eos: true
  ac_learn_blueprint:
    seq:
    - id: unknown
      size-eos: true
  ac_get_free_space_save_data:
    seq:
    - id: unknown
      size-eos: true
  ac_disassemble_item:
    seq:
    - id: unknown
      size-eos: true
  ac_add_thumb_up:
    seq:
    - id: unknown
      size-eos: true
  ac_get_visited_free_space_zones:
    seq:
    - id: unknown
      size-eos: true
  ac_advert_create:
    seq:
    - id: unknown
      size-eos: true
  ac_advert_delete:
    seq:
    - id: unknown
      size-eos: true
  ac_advert_header_get:
    seq:
    - id: unknown
      size-eos: true
  ac_advert_get:
    seq:
    - id: unknown
      size-eos: true
  ac_buy_product_from_advert:
    seq:
    - id: unknown
      size-eos: true
  ac_emm_change_ready:
    seq:
    - id: unknown
      size-eos: true
  ac_unlim_pve_upgrade_player_level:
    seq:
    - id: unknown
      size-eos: true
  ac_unlim_pve_disable_player_buffs:
    seq:
    - id: unknown
      size-eos: true
  ac_ta_stats_send_tutorial_entter:
    seq:
    - id: unknown
      size-eos: true
  ac_ta_stats_send_tutorial_exit:
    seq:
    - id: unknown
      size-eos: true
  ac_user_notes:
    seq:
    - id: unknown
      size-eos: true
  ac_user_notes_add:
    seq:
    - id: uid
      type: u8be
    - id: note
      type: strz
      encoding: UTF-8
  ac_user_notes_delete:
    doc: |
      Delete one or more user notes. Wire format: u16be count + count×u64be uid.
      Single-uid form (count=1) is used by FUN_0820b340; the multi-uid array
      form is used by FUN_0820b450 / FUN_0820b5c0.
      Confirmed via WriteU16 + N× WriteU64 in those builders.
    seq:
    - id: count
      type: u2be
    - id: uids
      type: u8be
      repeat: expr
      repeat-expr: count
  ac_battle_pass_unlock_level:
    seq:
    - id: unknown
      size-eos: true
  ac_zones_lua_active_events_update:
    doc: |
      Zone events poll. u64be timestamp (milliseconds). Confirmed via FUN_0820c100
      (single WriteU64 of the counter, then increments it).
    seq:
    - id: timestamp
      type: u8be
  ac_adventures:
    doc: Empty request, server responds with adventures list
  ac_adventure_cancel:
    seq:
    - id: unknown
      size-eos: true
