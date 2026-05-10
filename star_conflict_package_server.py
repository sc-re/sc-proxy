# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import bag_payload
import prefixed_bag_payload
import fed_design_tgp_stream
import ac_update_yup_purchases_body
import ac_friends_send_request_body
import ac_load_initial_player_data_body
import ac_lobby_info_body
import ac_player_inventory_body
import ac_quests_body
import ac_ship_quests_body
import ac_teaching_list_body
import ac_universe_get_body
import ac_use_blueprint_response_body
import ac_user_profile_get_response_body
import ac_vessel_change_equip_response_body
import ac_vessel_change_equip_multi_response_body
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class StarConflictPackageServer(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(StarConflictPackageServer, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.packet_type = self._io.read_s2be()
        _on = self.packet_type
        if _on == 0:
            pass
            self.body = StarConflictPackageServer.AcLoadInitialPlayerData(self._io, self, self._root)
        elif _on == 1:
            pass
            self.body = StarConflictPackageServer.AcServerInfo(self._io, self, self._root)
        elif _on == 10:
            pass
            self.body = StarConflictPackageServer.AcPlayerCredits(self._io, self, self._root)
        elif _on == 100:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamInfo(self._io, self, self._root)
        elif _on == 101:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamCreate(self._io, self, self._root)
        elif _on == 102:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamInviteSend(self._io, self, self._root)
        elif _on == 1024:
            pass
            self.body = StarConflictPackageServer.ZoneInstanceJoin(self._io, self, self._root)
        elif _on == 103:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamInviteCancel(self._io, self, self._root)
        elif _on == 104:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamInviteAccept(self._io, self, self._root)
        elif _on == 105:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamKick(self._io, self, self._root)
        elif _on == 106:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamLeave(self._io, self, self._root)
        elif _on == 107:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamInviteDecline(self._io, self, self._root)
        elif _on == 108:
            pass
            self.body = StarConflictPackageServer.AcLeagueTeamRequestNames(self._io, self, self._root)
        elif _on == 109:
            pass
            self.body = StarConflictPackageServer.AcGetNicknames(self._io, self, self._root)
        elif _on == 11:
            pass
            self.body = StarConflictPackageServer.AcPlayerStats(self._io, self, self._root)
        elif _on == 110:
            pass
            self.body = StarConflictPackageServer.AcGetUids(self._io, self, self._root)
        elif _on == 111:
            pass
            self.body = StarConflictPackageServer.AcReportPlayer(self._io, self, self._root)
        elif _on == 112:
            pass
            self.body = StarConflictPackageServer.AcUpdateYupPurchases(self._io, self, self._root)
        elif _on == 113:
            pass
            self.body = StarConflictPackageServer.AcCheckYupPurchases(self._io, self, self._root)
        elif _on == 114:
            pass
            self.body = StarConflictPackageServer.AcUpdateDlcOwnership(self._io, self, self._root)
        elif _on == 115:
            pass
            self.body = StarConflictPackageServer.AcFriendsSendRequest(self._io, self, self._root)
        elif _on == 116:
            pass
            self.body = StarConflictPackageServer.AcFriendsAcceptRequest(self._io, self, self._root)
        elif _on == 117:
            pass
            self.body = StarConflictPackageServer.AcFriendsRejectRequest(self._io, self, self._root)
        elif _on == 118:
            pass
            self.body = StarConflictPackageServer.AcFriendsRemove(self._io, self, self._root)
        elif _on == 119:
            pass
            self.body = StarConflictPackageServer.AcFriendsList(self._io, self, self._root)
        elif _on == 12:
            pass
            self.body = StarConflictPackageServer.AcPlayerArcBalance(self._io, self, self._root)
        elif _on == 120:
            pass
            self.body = StarConflictPackageServer.AcSocialIgnoreAdd(self._io, self, self._root)
        elif _on == 121:
            pass
            self.body = StarConflictPackageServer.AcSocialIgnoreRemove(self._io, self, self._root)
        elif _on == 122:
            pass
            self.body = StarConflictPackageServer.AcSocialWatchAdd(self._io, self, self._root)
        elif _on == 123:
            pass
            self.body = StarConflictPackageServer.AcSocialWatchRemove(self._io, self, self._root)
        elif _on == 124:
            pass
            self.body = StarConflictPackageServer.AcSocialSuggestSteam(self._io, self, self._root)
        elif _on == 125:
            pass
            self.body = StarConflictPackageServer.AcSocialSuggestFb(self._io, self, self._root)
        elif _on == 126:
            pass
            self.body = StarConflictPackageServer.AcSocialSuggestVk(self._io, self, self._root)
        elif _on == 127:
            pass
            self.body = StarConflictPackageServer.AcTeachingList(self._io, self, self._root)
        elif _on == 128:
            pass
            self.body = StarConflictPackageServer.AcTeachingRequestToTeacher(self._io, self, self._root)
        elif _on == 1280:
            pass
            self.body = StarConflictPackageServer.ZoneStatsList(self._io, self, self._root)
        elif _on == 1284:
            pass
            self.body = StarConflictPackageServer.ZonePlayerHealth(self._io, self, self._root)
        elif _on == 12851:
            pass
            self.body = StarConflictPackageServer.ZoneServer23(self._io, self, self._root)
        elif _on == 129:
            pass
            self.body = StarConflictPackageServer.AcTeachingRequestToStudent(self._io, self, self._root)
        elif _on == 13:
            pass
            self.body = StarConflictPackageServer.AcTitlesSetActive(self._io, self, self._root)
        elif _on == 130:
            pass
            self.body = StarConflictPackageServer.AcTeachingAccept(self._io, self, self._root)
        elif _on == 131:
            pass
            self.body = StarConflictPackageServer.AcTeachingReject(self._io, self, self._root)
        elif _on == 132:
            pass
            self.body = StarConflictPackageServer.AcTeachingCheck(self._io, self, self._root)
        elif _on == 133:
            pass
            self.body = StarConflictPackageServer.AcTeachingAllow(self._io, self, self._root)
        elif _on == 134:
            pass
            self.body = StarConflictPackageServer.AcReferrals(self._io, self, self._root)
        elif _on == 135:
            pass
            self.body = StarConflictPackageServer.AcSetReferrer(self._io, self, self._root)
        elif _on == 136:
            pass
            self.body = StarConflictPackageServer.AcObtainReferralKey(self._io, self, self._root)
        elif _on == 137:
            pass
            self.body = StarConflictPackageServer.AcAttachSteamAccount(self._io, self, self._root)
        elif _on == 138:
            pass
            self.body = StarConflictPackageServer.AcFinalizeSteamMtxn(self._io, self, self._root)
        elif _on == 13824:
            pass
            self.body = StarConflictPackageServer.ZoneKvData(self._io, self, self._root)
        elif _on == 139:
            pass
            self.body = StarConflictPackageServer.AcAttachYupAccount(self._io, self, self._root)
        elif _on == 14:
            pass
            self.body = StarConflictPackageServer.AcAvatarsSetActive(self._io, self, self._root)
        elif _on == 140:
            pass
            self.body = StarConflictPackageServer.AcAttachEmail(self._io, self, self._root)
        elif _on == 14080:
            pass
            self.body = StarConflictPackageServer.ZonePlayerList(self._io, self, self._root)
        elif _on == 141:
            pass
            self.body = StarConflictPackageServer.AcLobbyList(self._io, self, self._root)
        elif _on == 142:
            pass
            self.body = StarConflictPackageServer.AcLobbyJoin(self._io, self, self._root)
        elif _on == 143:
            pass
            self.body = StarConflictPackageServer.AcLobbyCreate(self._io, self, self._root)
        elif _on == 14393:
            pass
            self.body = StarConflictPackageServer.ZoneServer89(self._io, self, self._root)
        elif _on == 144:
            pass
            self.body = StarConflictPackageServer.AcLobbyInfo(self._io, self, self._root)
        elif _on == 145:
            pass
            self.body = StarConflictPackageServer.AcLobbyKick(self._io, self, self._root)
        elif _on == 146:
            pass
            self.body = StarConflictPackageServer.AcLobbyLeave(self._io, self, self._root)
        elif _on == 147:
            pass
            self.body = StarConflictPackageServer.AcLobbyInvite(self._io, self, self._root)
        elif _on == 148:
            pass
            self.body = StarConflictPackageServer.AcLobbyModify(self._io, self, self._root)
        elif _on == 149:
            pass
            self.body = StarConflictPackageServer.AcLobbyStartGame(self._io, self, self._root)
        elif _on == 15:
            pass
            self.body = StarConflictPackageServer.AcMottosSetActive(self._io, self, self._root)
        elif _on == 150:
            pass
            self.body = StarConflictPackageServer.AcLobbyGroupList(self._io, self, self._root)
        elif _on == 151:
            pass
            self.body = StarConflictPackageServer.AcLobbyGroupInfo(self._io, self, self._root)
        elif _on == 152:
            pass
            self.body = StarConflictPackageServer.AcLobbyGroupCreate(self._io, self, self._root)
        elif _on == 153:
            pass
            self.body = StarConflictPackageServer.AcLobbyGroupModify(self._io, self, self._root)
        elif _on == 154:
            pass
            self.body = StarConflictPackageServer.AcLobbyGroupDelete(self._io, self, self._root)
        elif _on == 155:
            pass
            self.body = StarConflictPackageServer.AcLobbyGroupJoinreqCreate(self._io, self, self._root)
        elif _on == 156:
            pass
            self.body = StarConflictPackageServer.AcLobbyGroupJoinreqCancel(self._io, self, self._root)
        elif _on == 157:
            pass
            self.body = StarConflictPackageServer.AcLobbyGroupJoinreqReject(self._io, self, self._root)
        elif _on == 158:
            pass
            self.body = StarConflictPackageServer.AcClanRequestCredentials(self._io, self, self._root)
        elif _on == 159:
            pass
            self.body = StarConflictPackageServer.AcClanRequestDesc(self._io, self, self._root)
        elif _on == 16:
            pass
            self.body = StarConflictPackageServer.AcChooseStartingStation(self._io, self, self._root)
        elif _on == 160:
            pass
            self.body = StarConflictPackageServer.AcClanRequestProfile(self._io, self, self._root)
        elif _on == 161:
            pass
            self.body = StarConflictPackageServer.AcClanJoinreqCreate(self._io, self, self._root)
        elif _on == 162:
            pass
            self.body = StarConflictPackageServer.AcClanJoinreqCancel(self._io, self, self._root)
        elif _on == 163:
            pass
            self.body = StarConflictPackageServer.AcClanJoinreqAccept(self._io, self, self._root)
        elif _on == 164:
            pass
            self.body = StarConflictPackageServer.AcClanInviteSend(self._io, self, self._root)
        elif _on == 165:
            pass
            self.body = StarConflictPackageServer.AcClanInviteAccept(self._io, self, self._root)
        elif _on == 166:
            pass
            self.body = StarConflictPackageServer.AcClanInviteCancel(self._io, self, self._root)
        elif _on == 167:
            pass
            self.body = StarConflictPackageServer.AcClanKick(self._io, self, self._root)
        elif _on == 168:
            pass
            self.body = StarConflictPackageServer.AcClanLeave(self._io, self, self._root)
        elif _on == 169:
            pass
            self.body = StarConflictPackageServer.AcClanSetRole(self._io, self, self._root)
        elif _on == 17:
            pass
            self.body = StarConflictPackageServer.AcChangePlayerNickname(self._io, self, self._root)
        elif _on == 170:
            pass
            self.body = StarConflictPackageServer.AcClanChangeMotd(self._io, self, self._root)
        elif _on == 171:
            pass
            self.body = StarConflictPackageServer.AcClanChangeDesc(self._io, self, self._root)
        elif _on == 172:
            pass
            self.body = StarConflictPackageServer.AcClanChangeRecruiting(self._io, self, self._root)
        elif _on == 173:
            pass
            self.body = StarConflictPackageServer.AcClanResourceConvert(self._io, self, self._root)
        elif _on == 174:
            pass
            self.body = StarConflictPackageServer.AcClanShipBuild(self._io, self, self._root)
        elif _on == 175:
            pass
            self.body = StarConflictPackageServer.AcClanShipBoostBuilding(self._io, self, self._root)
        elif _on == 176:
            pass
            self.body = StarConflictPackageServer.AcClanShipRepair(self._io, self, self._root)
        elif _on == 177:
            pass
            self.body = StarConflictPackageServer.AcClanShipBoostRepairing(self._io, self, self._root)
        elif _on == 178:
            pass
            self.body = StarConflictPackageServer.AcClanShipFit(self._io, self, self._root)
        elif _on == 179:
            pass
            self.body = StarConflictPackageServer.AcClanShipSetCurrent(self._io, self, self._root)
        elif _on == 1792:
            pass
            self.body = StarConflictPackageServer.ZonePlayerData(self._io, self, self._root)
        elif _on == 18:
            pass
            self.body = StarConflictPackageServer.AcSteamUserInfo(self._io, self, self._root)
        elif _on == 180:
            pass
            self.body = StarConflictPackageServer.AcClanUniverseMove(self._io, self, self._root)
        elif _on == 181:
            pass
            self.body = StarConflictPackageServer.AcClanSetCivilianZone(self._io, self, self._root)
        elif _on == 182:
            pass
            self.body = StarConflictPackageServer.AcClanReviveInWar(self._io, self, self._root)
        elif _on == 183:
            pass
            self.body = StarConflictPackageServer.AcClanWarStart(self._io, self, self._root)
        elif _on == 184:
            pass
            self.body = StarConflictPackageServer.AcClanQuestAccept(self._io, self, self._root)
        elif _on == 185:
            pass
            self.body = StarConflictPackageServer.AcClanCreate(self._io, self, self._root)
        elif _on == 186:
            pass
            self.body = StarConflictPackageServer.AcClanUpgrade(self._io, self, self._root)
        elif _on == 187:
            pass
            self.body = StarConflictPackageServer.AcClanChangeName(self._io, self, self._root)
        elif _on == 188:
            pass
            self.body = StarConflictPackageServer.AcClanChangeTag(self._io, self, self._root)
        elif _on == 189:
            pass
            self.body = StarConflictPackageServer.AcClanAssignEmblem(self._io, self, self._root)
        elif _on == 19:
            pass
            self.body = StarConflictPackageServer.AcPremiumInfo(self._io, self, self._root)
        elif _on == 190:
            pass
            self.body = StarConflictPackageServer.AcClanBankTransfer(self._io, self, self._root)
        elif _on == 191:
            pass
            self.body = StarConflictPackageServer.AcClanListRecruiting(self._io, self, self._root)
        elif _on == 192:
            pass
            self.body = StarConflictPackageServer.AcClanHistoryGet(self._io, self, self._root)
        elif _on == 193:
            pass
            self.body = StarConflictPackageServer.AcRelatedQuestEnable(self._io, self, self._root)
        elif _on == 194:
            pass
            self.body = StarConflictPackageServer.AcUserProfileGet(self._io, self, self._root)
        elif _on == 195:
            pass
            self.body = StarConflictPackageServer.AcAchievements(self._io, self, self._root)
        elif _on == 196:
            pass
            self.body = StarConflictPackageServer.AcAdminCmd(self._io, self, self._root)
        elif _on == 197:
            pass
            self.body = StarConflictPackageServer.AcGamesInfo(self._io, self, self._root)
        elif _on == 198:
            pass
            self.body = StarConflictPackageServer.AcZoneInstancesInfo(self._io, self, self._root)
        elif _on == 199:
            pass
            self.body = StarConflictPackageServer.AcGetPunishments(self._io, self, self._root)
        elif _on == 2:
            pass
            self.body = StarConflictPackageServer.AcEnterMmQueue(self._io, self, self._root)
        elif _on == 20:
            pass
            self.body = StarConflictPackageServer.AcPremiumBuy(self._io, self, self._root)
        elif _on == 200:
            pass
            self.body = StarConflictPackageServer.AcWelcomeMsg(self._io, self, self._root)
        elif _on == 201:
            pass
            self.body = StarConflictPackageServer.AcMotd(self._io, self, self._root)
        elif _on == 202:
            pass
            self.body = StarConflictPackageServer.AcSurveyGetNew(self._io, self, self._root)
        elif _on == 203:
            pass
            self.body = StarConflictPackageServer.AcSurveyVote(self._io, self, self._root)
        elif _on == 204:
            pass
            self.body = StarConflictPackageServer.AcSurveyResults(self._io, self, self._root)
        elif _on == 205:
            pass
            self.body = StarConflictPackageServer.AcUniverseGet(self._io, self, self._root)
        elif _on == 206:
            pass
            self.body = StarConflictPackageServer.AcUniverseCounters(self._io, self, self._root)
        elif _on == 207:
            pass
            self.body = StarConflictPackageServer.AcWarmapGet(self._io, self, self._root)
        elif _on == 208:
            pass
            self.body = StarConflictPackageServer.AcMailGet(self._io, self, self._root)
        elif _on == 209:
            pass
            self.body = StarConflictPackageServer.AcMailDeliver(self._io, self, self._root)
        elif _on == 21:
            pass
            self.body = StarConflictPackageServer.AcAccountAuras(self._io, self, self._root)
        elif _on == 210:
            pass
            self.body = StarConflictPackageServer.AcMailSend(self._io, self, self._root)
        elif _on == 211:
            pass
            self.body = StarConflictPackageServer.AcMailRemove(self._io, self, self._root)
        elif _on == 212:
            pass
            self.body = StarConflictPackageServer.AcMailAcknowledgeExpiration(self._io, self, self._root)
        elif _on == 213:
            pass
            self.body = StarConflictPackageServer.AcSendEarlyPlayerLog(self._io, self, self._root)
        elif _on == 214:
            pass
            self.body = StarConflictPackageServer.AcAutoPilotSpaceStation(self._io, self, self._root)
        elif _on == 215:
            pass
            self.body = StarConflictPackageServer.AcUndockSpaceStation(self._io, self, self._root)
        elif _on == 216:
            pass
            self.body = StarConflictPackageServer.AcSetVisitedZone(self._io, self, self._root)
        elif _on == 217:
            pass
            self.body = StarConflictPackageServer.AcZoneCoordinatorGmCommand(self._io, self, self._root)
        elif _on == 218:
            pass
            self.body = StarConflictPackageServer.AcSpaceStationsPopulation(self._io, self, self._root)
        elif _on == 219:
            pass
            self.body = StarConflictPackageServer.AcKarmaReset(self._io, self, self._root)
        elif _on == 22:
            pass
            self.body = StarConflictPackageServer.AcAddAccountAura(self._io, self, self._root)
        elif _on == 220:
            pass
            self.body = StarConflictPackageServer.AcFactionRepReset(self._io, self, self._root)
        elif _on == 221:
            pass
            self.body = StarConflictPackageServer.AcLeaderboardGet(self._io, self, self._root)
        elif _on == 222:
            pass
            self.body = StarConflictPackageServer.AcLeaderboardGetDescs(self._io, self, self._root)
        elif _on == 223:
            pass
            self.body = StarConflictPackageServer.AcSetFbToken(self._io, self, self._root)
        elif _on == 224:
            pass
            self.body = StarConflictPackageServer.AcGetFbToken(self._io, self, self._root)
        elif _on == 225:
            pass
            self.body = StarConflictPackageServer.AcLogFbEvent(self._io, self, self._root)
        elif _on == 226:
            pass
            self.body = StarConflictPackageServer.AcGetCraftResources(self._io, self, self._root)
        elif _on == 227:
            pass
            self.body = StarConflictPackageServer.AcUseBlueprint(self._io, self, self._root)
        elif _on == 228:
            pass
            self.body = StarConflictPackageServer.AcSellCraftResource(self._io, self, self._root)
        elif _on == 229:
            pass
            self.body = StarConflictPackageServer.AcSellCraftResources(self._io, self, self._root)
        elif _on == 23:
            pass
            self.body = StarConflictPackageServer.AcCancelAccountAura(self._io, self, self._root)
        elif _on == 230:
            pass
            self.body = StarConflictPackageServer.AcGetBlueprints(self._io, self, self._root)
        elif _on == 2304:
            pass
            self.body = StarConflictPackageServer.ZonePlayerUpdate(self._io, self, self._root)
        elif _on == 231:
            pass
            self.body = StarConflictPackageServer.AcLearnBlueprint(self._io, self, self._root)
        elif _on == 232:
            pass
            self.body = StarConflictPackageServer.AcGetFreeSpaceSaveData(self._io, self, self._root)
        elif _on == 233:
            pass
            self.body = StarConflictPackageServer.AcDisassembleItem(self._io, self, self._root)
        elif _on == 234:
            pass
            self.body = StarConflictPackageServer.AcAddThumbUp(self._io, self, self._root)
        elif _on == 235:
            pass
            self.body = StarConflictPackageServer.AcGetVisitedFreeSpaceZones(self._io, self, self._root)
        elif _on == 236:
            pass
            self.body = StarConflictPackageServer.AcAdvertCreate(self._io, self, self._root)
        elif _on == 237:
            pass
            self.body = StarConflictPackageServer.AcAdvertDelete(self._io, self, self._root)
        elif _on == 238:
            pass
            self.body = StarConflictPackageServer.AcAdvertHeaderGet(self._io, self, self._root)
        elif _on == 239:
            pass
            self.body = StarConflictPackageServer.AcAdvertGet(self._io, self, self._root)
        elif _on == 24:
            pass
            self.body = StarConflictPackageServer.AcQuests(self._io, self, self._root)
        elif _on == 240:
            pass
            self.body = StarConflictPackageServer.AcBuyProductFromAdvert(self._io, self, self._root)
        elif _on == 241:
            pass
            self.body = StarConflictPackageServer.AcEmmChangeReady(self._io, self, self._root)
        elif _on == 242:
            pass
            self.body = StarConflictPackageServer.AcUnlimPveUpgradePlayerLevel(self._io, self, self._root)
        elif _on == 243:
            pass
            self.body = StarConflictPackageServer.AcUnlimPveDisablePlayerBuffs(self._io, self, self._root)
        elif _on == 244:
            pass
            self.body = StarConflictPackageServer.AcTaStatsSendTutorialEntter(self._io, self, self._root)
        elif _on == 245:
            pass
            self.body = StarConflictPackageServer.AcTaStatsSendTutorialExit(self._io, self, self._root)
        elif _on == 246:
            pass
            self.body = StarConflictPackageServer.AcUserNotes(self._io, self, self._root)
        elif _on == 247:
            pass
            self.body = StarConflictPackageServer.AcUserNotesAdd(self._io, self, self._root)
        elif _on == 248:
            pass
            self.body = StarConflictPackageServer.AcUserNotesDelete(self._io, self, self._root)
        elif _on == 249:
            pass
            self.body = StarConflictPackageServer.AcBattlePassUnlockLevel(self._io, self, self._root)
        elif _on == 25:
            pass
            self.body = StarConflictPackageServer.AcQuestAccept(self._io, self, self._root)
        elif _on == 250:
            pass
            self.body = StarConflictPackageServer.AcZonesLuaActiveEventsUpdate(self._io, self, self._root)
        elif _on == 25088:
            pass
            self.body = StarConflictPackageServer.ZoneMilitaryRank(self._io, self, self._root)
        elif _on == 251:
            pass
            self.body = StarConflictPackageServer.AcAdventures(self._io, self, self._root)
        elif _on == 252:
            pass
            self.body = StarConflictPackageServer.AcAdventureCancel(self._io, self, self._root)
        elif _on == 2560:
            pass
            self.body = StarConflictPackageServer.ZonePlayerJoin(self._io, self, self._root)
        elif _on == 26:
            pass
            self.body = StarConflictPackageServer.AcQuestChange(self._io, self, self._root)
        elif _on == 26624:
            pass
            self.body = StarConflictPackageServer.ZonePlayerStatus(self._io, self, self._root)
        elif _on == 27:
            pass
            self.body = StarConflictPackageServer.AcQuestComplete(self._io, self, self._root)
        elif _on == 28:
            pass
            self.body = StarConflictPackageServer.AcQuestCompleteAll(self._io, self, self._root)
        elif _on == 29:
            pass
            self.body = StarConflictPackageServer.AcShipQuests(self._io, self, self._root)
        elif _on == 3:
            pass
            self.body = StarConflictPackageServer.AcLeaveMmQueue(self._io, self, self._root)
        elif _on == 30:
            pass
            self.body = StarConflictPackageServer.AcShipQuestStart(self._io, self, self._root)
        elif _on == 3072:
            pass
            self.body = StarConflictPackageServer.ZoneMembership(self._io, self, self._root)
        elif _on == 31:
            pass
            self.body = StarConflictPackageServer.AcShipQuestChange(self._io, self, self._root)
        elif _on == 32:
            pass
            self.body = StarConflictPackageServer.AcShipQuestEnd(self._io, self, self._root)
        elif _on == 33:
            pass
            self.body = StarConflictPackageServer.AcRewardedTutorials(self._io, self, self._root)
        elif _on == 34:
            pass
            self.body = StarConflictPackageServer.AcRewardTutorial(self._io, self, self._root)
        elif _on == 35:
            pass
            self.body = StarConflictPackageServer.AcPlayerInventory(self._io, self, self._root)
        elif _on == 36:
            pass
            self.body = StarConflictPackageServer.AcPlayerAutogenInventory(self._io, self, self._root)
        elif _on == 37:
            pass
            self.body = StarConflictPackageServer.AcPlayerVessels(self._io, self, self._root)
        elif _on == 38:
            pass
            self.body = StarConflictPackageServer.AcVesselEquipment(self._io, self, self._root)
        elif _on == 39:
            pass
            self.body = StarConflictPackageServer.AcBuyItem(self._io, self, self._root)
        elif _on == 4:
            pass
            self.body = StarConflictPackageServer.AcMmInfo(self._io, self, self._root)
        elif _on == 40:
            pass
            self.body = StarConflictPackageServer.AcSellItem(self._io, self, self._root)
        elif _on == 41:
            pass
            self.body = StarConflictPackageServer.AcSellItems(self._io, self, self._root)
        elif _on == 42:
            pass
            self.body = StarConflictPackageServer.AcEnchantItem(self._io, self, self._root)
        elif _on == 43:
            pass
            self.body = StarConflictPackageServer.AcSalvageItem(self._io, self, self._root)
        elif _on == 44:
            pass
            self.body = StarConflictPackageServer.AcSalvageItems(self._io, self, self._root)
        elif _on == 45:
            pass
            self.body = StarConflictPackageServer.AcUpgradeItems(self._io, self, self._root)
        elif _on == 46:
            pass
            self.body = StarConflictPackageServer.AcUpgradeAutogenItem(self._io, self, self._root)
        elif _on == 47:
            pass
            self.body = StarConflictPackageServer.AcCraftUpgradeItem(self._io, self, self._root)
        elif _on == 48:
            pass
            self.body = StarConflictPackageServer.AcFindAutogenItem(self._io, self, self._root)
        elif _on == 49:
            pass
            self.body = StarConflictPackageServer.AcActivateResourceVessel(self._io, self, self._root)
        elif _on == 5:
            pass
            self.body = StarConflictPackageServer.AcEnterTournament(self._io, self, self._root)
        elif _on == 50:
            pass
            self.body = StarConflictPackageServer.AcSellVessel(self._io, self, self._root)
        elif _on == 51:
            pass
            self.body = StarConflictPackageServer.AcVesselChangeEquip(self._io, self, self._root)
        elif _on == 52:
            pass
            self.body = StarConflictPackageServer.AcVesselChangeEquipMulti(self._io, self, self._root)
        elif _on == 53:
            pass
            self.body = StarConflictPackageServer.AcVesselCheatChangeEquip(self._io, self, self._root)
        elif _on == 54:
            pass
            self.body = StarConflictPackageServer.AcVesselTransferEquip(self._io, self, self._root)
        elif _on == 55:
            pass
            self.body = StarConflictPackageServer.AcVesselStripEquip(self._io, self, self._root)
        elif _on == 56:
            pass
            self.body = StarConflictPackageServer.AcVesselChangeMunition(self._io, self, self._root)
        elif _on == 57:
            pass
            self.body = StarConflictPackageServer.AcVesselRefillMunition(self._io, self, self._root)
        elif _on == 58:
            pass
            self.body = StarConflictPackageServer.AcVesselTransferMunition(self._io, self, self._root)
        elif _on == 59:
            pass
            self.body = StarConflictPackageServer.AcVesselAutogenDestroy(self._io, self, self._root)
        elif _on == 6:
            pass
            self.body = StarConflictPackageServer.AcLeaveTournament(self._io, self, self._root)
        elif _on == 60:
            pass
            self.body = StarConflictPackageServer.AcVesselAutogenDismantle(self._io, self, self._root)
        elif _on == 61:
            pass
            self.body = StarConflictPackageServer.AcVesselExtractExp(self._io, self, self._root)
        elif _on == 62:
            pass
            self.body = StarConflictPackageServer.AcVesselLevelup(self._io, self, self._root)
        elif _on == 63:
            pass
            self.body = StarConflictPackageServer.AcVesselRepair(self._io, self, self._root)
        elif _on == 64:
            pass
            self.body = StarConflictPackageServer.AcVesselRepairBattle(self._io, self, self._root)
        elif _on == 65:
            pass
            self.body = StarConflictPackageServer.AcVesselRefillBattle(self._io, self, self._root)
        elif _on == 66:
            pass
            self.body = StarConflictPackageServer.AcVesselStripImproperBattle(self._io, self, self._root)
        elif _on == 67:
            pass
            self.body = StarConflictPackageServer.AcVesselFreeCustomElements(self._io, self, self._root)
        elif _on == 68:
            pass
            self.body = StarConflictPackageServer.AcVesselCustomElementsBuy(self._io, self, self._root)
        elif _on == 69:
            pass
            self.body = StarConflictPackageServer.AcVesselCustomElementsAcknowledgeExpiration(self._io, self, self._root)
        elif _on == 7:
            pass
            self.body = StarConflictPackageServer.AcGetUserdata(self._io, self, self._root)
        elif _on == 70:
            pass
            self.body = StarConflictPackageServer.AcVesselCraft(self._io, self, self._root)
        elif _on == 71:
            pass
            self.body = StarConflictPackageServer.AcVesselRecraft(self._io, self, self._root)
        elif _on == 72:
            pass
            self.body = StarConflictPackageServer.AcVesselBudgetLevelup(self._io, self, self._root)
        elif _on == 73:
            pass
            self.body = StarConflictPackageServer.AcVesselBudgetActivate(self._io, self, self._root)
        elif _on == 74:
            pass
            self.body = StarConflictPackageServer.AcVesselUnlockNode(self._io, self, self._root)
        elif _on == 75:
            pass
            self.body = StarConflictPackageServer.AcVesselActivateNode(self._io, self, self._root)
        elif _on == 76:
            pass
            self.body = StarConflictPackageServer.AcBattleSlots(self._io, self, self._root)
        elif _on == 77:
            pass
            self.body = StarConflictPackageServer.AcBattleSlotChangeVessel(self._io, self, self._root)
        elif _on == 78:
            pass
            self.body = StarConflictPackageServer.AcBattleSlotSwapVessels(self._io, self, self._root)
        elif _on == 79:
            pass
            self.body = StarConflictPackageServer.AcBattleSlotCheatChangeVessel(self._io, self, self._root)
        elif _on == 8:
            pass
            self.body = StarConflictPackageServer.AcSetUserdata(self._io, self, self._root)
        elif _on == 80:
            pass
            self.body = StarConflictPackageServer.AcInvExtBuy(self._io, self, self._root)
        elif _on == 81:
            pass
            self.body = StarConflictPackageServer.AcAutogenInvExtBuy(self._io, self, self._root)
        elif _on == 82:
            pass
            self.body = StarConflictPackageServer.AcExchangeGold(self._io, self, self._root)
        elif _on == 83:
            pass
            self.body = StarConflictPackageServer.AcBuyGold(self._io, self, self._root)
        elif _on == 84:
            pass
            self.body = StarConflictPackageServer.AcBuyArcDlc(self._io, self, self._root)
        elif _on == 85:
            pass
            self.body = StarConflictPackageServer.AcTalentsAcquire(self._io, self, self._root)
        elif _on == 86:
            pass
            self.body = StarConflictPackageServer.AcTalentsUpdate(self._io, self, self._root)
        elif _on == 87:
            pass
            self.body = StarConflictPackageServer.AcTalentsReset(self._io, self, self._root)
        elif _on == 88:
            pass
            self.body = StarConflictPackageServer.AcTalentsAssignSets(self._io, self, self._root)
        elif _on == 89:
            pass
            self.body = StarConflictPackageServer.AcBuyTalentSet(self._io, self, self._root)
        elif _on == 9:
            pass
            self.body = StarConflictPackageServer.AcPlayerCredentials(self._io, self, self._root)
        elif _on == 90:
            pass
            self.body = StarConflictPackageServer.AcReactOnAbandonedGame(self._io, self, self._root)
        elif _on == 91:
            pass
            self.body = StarConflictPackageServer.AcSquadInfo(self._io, self, self._root)
        elif _on == 92:
            pass
            self.body = StarConflictPackageServer.AcSquadInviteAccept(self._io, self, self._root)
        elif _on == 93:
            pass
            self.body = StarConflictPackageServer.AcSquadInviteDecline(self._io, self, self._root)
        elif _on == 94:
            pass
            self.body = StarConflictPackageServer.AcSquadLeave(self._io, self, self._root)
        elif _on == 95:
            pass
            self.body = StarConflictPackageServer.AcSquadInviteSend(self._io, self, self._root)
        elif _on == 96:
            pass
            self.body = StarConflictPackageServer.AcSquadInviteCancel(self._io, self, self._root)
        elif _on == 97:
            pass
            self.body = StarConflictPackageServer.AcSquadKick(self._io, self, self._root)
        elif _on == 98:
            pass
            self.body = StarConflictPackageServer.AcSquadReady(self._io, self, self._root)
        elif _on == 99:
            pass
            self.body = StarConflictPackageServer.AcSquadConvertToWing(self._io, self, self._root)


    def _fetch_instances(self):
        pass
        _on = self.packet_type
        if _on == 0:
            pass
            self.body._fetch_instances()
        elif _on == 1:
            pass
            self.body._fetch_instances()
        elif _on == 10:
            pass
            self.body._fetch_instances()
        elif _on == 100:
            pass
            self.body._fetch_instances()
        elif _on == 101:
            pass
            self.body._fetch_instances()
        elif _on == 102:
            pass
            self.body._fetch_instances()
        elif _on == 1024:
            pass
            self.body._fetch_instances()
        elif _on == 103:
            pass
            self.body._fetch_instances()
        elif _on == 104:
            pass
            self.body._fetch_instances()
        elif _on == 105:
            pass
            self.body._fetch_instances()
        elif _on == 106:
            pass
            self.body._fetch_instances()
        elif _on == 107:
            pass
            self.body._fetch_instances()
        elif _on == 108:
            pass
            self.body._fetch_instances()
        elif _on == 109:
            pass
            self.body._fetch_instances()
        elif _on == 11:
            pass
            self.body._fetch_instances()
        elif _on == 110:
            pass
            self.body._fetch_instances()
        elif _on == 111:
            pass
            self.body._fetch_instances()
        elif _on == 112:
            pass
            self.body._fetch_instances()
        elif _on == 113:
            pass
            self.body._fetch_instances()
        elif _on == 114:
            pass
            self.body._fetch_instances()
        elif _on == 115:
            pass
            self.body._fetch_instances()
        elif _on == 116:
            pass
            self.body._fetch_instances()
        elif _on == 117:
            pass
            self.body._fetch_instances()
        elif _on == 118:
            pass
            self.body._fetch_instances()
        elif _on == 119:
            pass
            self.body._fetch_instances()
        elif _on == 12:
            pass
            self.body._fetch_instances()
        elif _on == 120:
            pass
            self.body._fetch_instances()
        elif _on == 121:
            pass
            self.body._fetch_instances()
        elif _on == 122:
            pass
            self.body._fetch_instances()
        elif _on == 123:
            pass
            self.body._fetch_instances()
        elif _on == 124:
            pass
            self.body._fetch_instances()
        elif _on == 125:
            pass
            self.body._fetch_instances()
        elif _on == 126:
            pass
            self.body._fetch_instances()
        elif _on == 127:
            pass
            self.body._fetch_instances()
        elif _on == 128:
            pass
            self.body._fetch_instances()
        elif _on == 1280:
            pass
            self.body._fetch_instances()
        elif _on == 1284:
            pass
            self.body._fetch_instances()
        elif _on == 12851:
            pass
            self.body._fetch_instances()
        elif _on == 129:
            pass
            self.body._fetch_instances()
        elif _on == 13:
            pass
            self.body._fetch_instances()
        elif _on == 130:
            pass
            self.body._fetch_instances()
        elif _on == 131:
            pass
            self.body._fetch_instances()
        elif _on == 132:
            pass
            self.body._fetch_instances()
        elif _on == 133:
            pass
            self.body._fetch_instances()
        elif _on == 134:
            pass
            self.body._fetch_instances()
        elif _on == 135:
            pass
            self.body._fetch_instances()
        elif _on == 136:
            pass
            self.body._fetch_instances()
        elif _on == 137:
            pass
            self.body._fetch_instances()
        elif _on == 138:
            pass
            self.body._fetch_instances()
        elif _on == 13824:
            pass
            self.body._fetch_instances()
        elif _on == 139:
            pass
            self.body._fetch_instances()
        elif _on == 14:
            pass
            self.body._fetch_instances()
        elif _on == 140:
            pass
            self.body._fetch_instances()
        elif _on == 14080:
            pass
            self.body._fetch_instances()
        elif _on == 141:
            pass
            self.body._fetch_instances()
        elif _on == 142:
            pass
            self.body._fetch_instances()
        elif _on == 143:
            pass
            self.body._fetch_instances()
        elif _on == 14393:
            pass
            self.body._fetch_instances()
        elif _on == 144:
            pass
            self.body._fetch_instances()
        elif _on == 145:
            pass
            self.body._fetch_instances()
        elif _on == 146:
            pass
            self.body._fetch_instances()
        elif _on == 147:
            pass
            self.body._fetch_instances()
        elif _on == 148:
            pass
            self.body._fetch_instances()
        elif _on == 149:
            pass
            self.body._fetch_instances()
        elif _on == 15:
            pass
            self.body._fetch_instances()
        elif _on == 150:
            pass
            self.body._fetch_instances()
        elif _on == 151:
            pass
            self.body._fetch_instances()
        elif _on == 152:
            pass
            self.body._fetch_instances()
        elif _on == 153:
            pass
            self.body._fetch_instances()
        elif _on == 154:
            pass
            self.body._fetch_instances()
        elif _on == 155:
            pass
            self.body._fetch_instances()
        elif _on == 156:
            pass
            self.body._fetch_instances()
        elif _on == 157:
            pass
            self.body._fetch_instances()
        elif _on == 158:
            pass
            self.body._fetch_instances()
        elif _on == 159:
            pass
            self.body._fetch_instances()
        elif _on == 16:
            pass
            self.body._fetch_instances()
        elif _on == 160:
            pass
            self.body._fetch_instances()
        elif _on == 161:
            pass
            self.body._fetch_instances()
        elif _on == 162:
            pass
            self.body._fetch_instances()
        elif _on == 163:
            pass
            self.body._fetch_instances()
        elif _on == 164:
            pass
            self.body._fetch_instances()
        elif _on == 165:
            pass
            self.body._fetch_instances()
        elif _on == 166:
            pass
            self.body._fetch_instances()
        elif _on == 167:
            pass
            self.body._fetch_instances()
        elif _on == 168:
            pass
            self.body._fetch_instances()
        elif _on == 169:
            pass
            self.body._fetch_instances()
        elif _on == 17:
            pass
            self.body._fetch_instances()
        elif _on == 170:
            pass
            self.body._fetch_instances()
        elif _on == 171:
            pass
            self.body._fetch_instances()
        elif _on == 172:
            pass
            self.body._fetch_instances()
        elif _on == 173:
            pass
            self.body._fetch_instances()
        elif _on == 174:
            pass
            self.body._fetch_instances()
        elif _on == 175:
            pass
            self.body._fetch_instances()
        elif _on == 176:
            pass
            self.body._fetch_instances()
        elif _on == 177:
            pass
            self.body._fetch_instances()
        elif _on == 178:
            pass
            self.body._fetch_instances()
        elif _on == 179:
            pass
            self.body._fetch_instances()
        elif _on == 1792:
            pass
            self.body._fetch_instances()
        elif _on == 18:
            pass
            self.body._fetch_instances()
        elif _on == 180:
            pass
            self.body._fetch_instances()
        elif _on == 181:
            pass
            self.body._fetch_instances()
        elif _on == 182:
            pass
            self.body._fetch_instances()
        elif _on == 183:
            pass
            self.body._fetch_instances()
        elif _on == 184:
            pass
            self.body._fetch_instances()
        elif _on == 185:
            pass
            self.body._fetch_instances()
        elif _on == 186:
            pass
            self.body._fetch_instances()
        elif _on == 187:
            pass
            self.body._fetch_instances()
        elif _on == 188:
            pass
            self.body._fetch_instances()
        elif _on == 189:
            pass
            self.body._fetch_instances()
        elif _on == 19:
            pass
            self.body._fetch_instances()
        elif _on == 190:
            pass
            self.body._fetch_instances()
        elif _on == 191:
            pass
            self.body._fetch_instances()
        elif _on == 192:
            pass
            self.body._fetch_instances()
        elif _on == 193:
            pass
            self.body._fetch_instances()
        elif _on == 194:
            pass
            self.body._fetch_instances()
        elif _on == 195:
            pass
            self.body._fetch_instances()
        elif _on == 196:
            pass
            self.body._fetch_instances()
        elif _on == 197:
            pass
            self.body._fetch_instances()
        elif _on == 198:
            pass
            self.body._fetch_instances()
        elif _on == 199:
            pass
            self.body._fetch_instances()
        elif _on == 2:
            pass
            self.body._fetch_instances()
        elif _on == 20:
            pass
            self.body._fetch_instances()
        elif _on == 200:
            pass
            self.body._fetch_instances()
        elif _on == 201:
            pass
            self.body._fetch_instances()
        elif _on == 202:
            pass
            self.body._fetch_instances()
        elif _on == 203:
            pass
            self.body._fetch_instances()
        elif _on == 204:
            pass
            self.body._fetch_instances()
        elif _on == 205:
            pass
            self.body._fetch_instances()
        elif _on == 206:
            pass
            self.body._fetch_instances()
        elif _on == 207:
            pass
            self.body._fetch_instances()
        elif _on == 208:
            pass
            self.body._fetch_instances()
        elif _on == 209:
            pass
            self.body._fetch_instances()
        elif _on == 21:
            pass
            self.body._fetch_instances()
        elif _on == 210:
            pass
            self.body._fetch_instances()
        elif _on == 211:
            pass
            self.body._fetch_instances()
        elif _on == 212:
            pass
            self.body._fetch_instances()
        elif _on == 213:
            pass
            self.body._fetch_instances()
        elif _on == 214:
            pass
            self.body._fetch_instances()
        elif _on == 215:
            pass
            self.body._fetch_instances()
        elif _on == 216:
            pass
            self.body._fetch_instances()
        elif _on == 217:
            pass
            self.body._fetch_instances()
        elif _on == 218:
            pass
            self.body._fetch_instances()
        elif _on == 219:
            pass
            self.body._fetch_instances()
        elif _on == 22:
            pass
            self.body._fetch_instances()
        elif _on == 220:
            pass
            self.body._fetch_instances()
        elif _on == 221:
            pass
            self.body._fetch_instances()
        elif _on == 222:
            pass
            self.body._fetch_instances()
        elif _on == 223:
            pass
            self.body._fetch_instances()
        elif _on == 224:
            pass
            self.body._fetch_instances()
        elif _on == 225:
            pass
            self.body._fetch_instances()
        elif _on == 226:
            pass
            self.body._fetch_instances()
        elif _on == 227:
            pass
            self.body._fetch_instances()
        elif _on == 228:
            pass
            self.body._fetch_instances()
        elif _on == 229:
            pass
            self.body._fetch_instances()
        elif _on == 23:
            pass
            self.body._fetch_instances()
        elif _on == 230:
            pass
            self.body._fetch_instances()
        elif _on == 2304:
            pass
            self.body._fetch_instances()
        elif _on == 231:
            pass
            self.body._fetch_instances()
        elif _on == 232:
            pass
            self.body._fetch_instances()
        elif _on == 233:
            pass
            self.body._fetch_instances()
        elif _on == 234:
            pass
            self.body._fetch_instances()
        elif _on == 235:
            pass
            self.body._fetch_instances()
        elif _on == 236:
            pass
            self.body._fetch_instances()
        elif _on == 237:
            pass
            self.body._fetch_instances()
        elif _on == 238:
            pass
            self.body._fetch_instances()
        elif _on == 239:
            pass
            self.body._fetch_instances()
        elif _on == 24:
            pass
            self.body._fetch_instances()
        elif _on == 240:
            pass
            self.body._fetch_instances()
        elif _on == 241:
            pass
            self.body._fetch_instances()
        elif _on == 242:
            pass
            self.body._fetch_instances()
        elif _on == 243:
            pass
            self.body._fetch_instances()
        elif _on == 244:
            pass
            self.body._fetch_instances()
        elif _on == 245:
            pass
            self.body._fetch_instances()
        elif _on == 246:
            pass
            self.body._fetch_instances()
        elif _on == 247:
            pass
            self.body._fetch_instances()
        elif _on == 248:
            pass
            self.body._fetch_instances()
        elif _on == 249:
            pass
            self.body._fetch_instances()
        elif _on == 25:
            pass
            self.body._fetch_instances()
        elif _on == 250:
            pass
            self.body._fetch_instances()
        elif _on == 25088:
            pass
            self.body._fetch_instances()
        elif _on == 251:
            pass
            self.body._fetch_instances()
        elif _on == 252:
            pass
            self.body._fetch_instances()
        elif _on == 2560:
            pass
            self.body._fetch_instances()
        elif _on == 26:
            pass
            self.body._fetch_instances()
        elif _on == 26624:
            pass
            self.body._fetch_instances()
        elif _on == 27:
            pass
            self.body._fetch_instances()
        elif _on == 28:
            pass
            self.body._fetch_instances()
        elif _on == 29:
            pass
            self.body._fetch_instances()
        elif _on == 3:
            pass
            self.body._fetch_instances()
        elif _on == 30:
            pass
            self.body._fetch_instances()
        elif _on == 3072:
            pass
            self.body._fetch_instances()
        elif _on == 31:
            pass
            self.body._fetch_instances()
        elif _on == 32:
            pass
            self.body._fetch_instances()
        elif _on == 33:
            pass
            self.body._fetch_instances()
        elif _on == 34:
            pass
            self.body._fetch_instances()
        elif _on == 35:
            pass
            self.body._fetch_instances()
        elif _on == 36:
            pass
            self.body._fetch_instances()
        elif _on == 37:
            pass
            self.body._fetch_instances()
        elif _on == 38:
            pass
            self.body._fetch_instances()
        elif _on == 39:
            pass
            self.body._fetch_instances()
        elif _on == 4:
            pass
            self.body._fetch_instances()
        elif _on == 40:
            pass
            self.body._fetch_instances()
        elif _on == 41:
            pass
            self.body._fetch_instances()
        elif _on == 42:
            pass
            self.body._fetch_instances()
        elif _on == 43:
            pass
            self.body._fetch_instances()
        elif _on == 44:
            pass
            self.body._fetch_instances()
        elif _on == 45:
            pass
            self.body._fetch_instances()
        elif _on == 46:
            pass
            self.body._fetch_instances()
        elif _on == 47:
            pass
            self.body._fetch_instances()
        elif _on == 48:
            pass
            self.body._fetch_instances()
        elif _on == 49:
            pass
            self.body._fetch_instances()
        elif _on == 5:
            pass
            self.body._fetch_instances()
        elif _on == 50:
            pass
            self.body._fetch_instances()
        elif _on == 51:
            pass
            self.body._fetch_instances()
        elif _on == 52:
            pass
            self.body._fetch_instances()
        elif _on == 53:
            pass
            self.body._fetch_instances()
        elif _on == 54:
            pass
            self.body._fetch_instances()
        elif _on == 55:
            pass
            self.body._fetch_instances()
        elif _on == 56:
            pass
            self.body._fetch_instances()
        elif _on == 57:
            pass
            self.body._fetch_instances()
        elif _on == 58:
            pass
            self.body._fetch_instances()
        elif _on == 59:
            pass
            self.body._fetch_instances()
        elif _on == 6:
            pass
            self.body._fetch_instances()
        elif _on == 60:
            pass
            self.body._fetch_instances()
        elif _on == 61:
            pass
            self.body._fetch_instances()
        elif _on == 62:
            pass
            self.body._fetch_instances()
        elif _on == 63:
            pass
            self.body._fetch_instances()
        elif _on == 64:
            pass
            self.body._fetch_instances()
        elif _on == 65:
            pass
            self.body._fetch_instances()
        elif _on == 66:
            pass
            self.body._fetch_instances()
        elif _on == 67:
            pass
            self.body._fetch_instances()
        elif _on == 68:
            pass
            self.body._fetch_instances()
        elif _on == 69:
            pass
            self.body._fetch_instances()
        elif _on == 7:
            pass
            self.body._fetch_instances()
        elif _on == 70:
            pass
            self.body._fetch_instances()
        elif _on == 71:
            pass
            self.body._fetch_instances()
        elif _on == 72:
            pass
            self.body._fetch_instances()
        elif _on == 73:
            pass
            self.body._fetch_instances()
        elif _on == 74:
            pass
            self.body._fetch_instances()
        elif _on == 75:
            pass
            self.body._fetch_instances()
        elif _on == 76:
            pass
            self.body._fetch_instances()
        elif _on == 77:
            pass
            self.body._fetch_instances()
        elif _on == 78:
            pass
            self.body._fetch_instances()
        elif _on == 79:
            pass
            self.body._fetch_instances()
        elif _on == 8:
            pass
            self.body._fetch_instances()
        elif _on == 80:
            pass
            self.body._fetch_instances()
        elif _on == 81:
            pass
            self.body._fetch_instances()
        elif _on == 82:
            pass
            self.body._fetch_instances()
        elif _on == 83:
            pass
            self.body._fetch_instances()
        elif _on == 84:
            pass
            self.body._fetch_instances()
        elif _on == 85:
            pass
            self.body._fetch_instances()
        elif _on == 86:
            pass
            self.body._fetch_instances()
        elif _on == 87:
            pass
            self.body._fetch_instances()
        elif _on == 88:
            pass
            self.body._fetch_instances()
        elif _on == 89:
            pass
            self.body._fetch_instances()
        elif _on == 9:
            pass
            self.body._fetch_instances()
        elif _on == 90:
            pass
            self.body._fetch_instances()
        elif _on == 91:
            pass
            self.body._fetch_instances()
        elif _on == 92:
            pass
            self.body._fetch_instances()
        elif _on == 93:
            pass
            self.body._fetch_instances()
        elif _on == 94:
            pass
            self.body._fetch_instances()
        elif _on == 95:
            pass
            self.body._fetch_instances()
        elif _on == 96:
            pass
            self.body._fetch_instances()
        elif _on == 97:
            pass
            self.body._fetch_instances()
        elif _on == 98:
            pass
            self.body._fetch_instances()
        elif _on == 99:
            pass
            self.body._fetch_instances()

    class AcAccountAuras(KaitaiStruct):
        """Field sequence from handler at 0x0822f87d in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAccountAuras, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAchievements(KaitaiStruct):
        """Field sequence from handler at 0x0822dd00 in OnRecieve dispatch.
        Reads: u64 u16 u16
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAchievements, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.u64_0 = self._io.read_u8be()
            self.u16_1 = self._io.read_u2be()
            self.u16_2 = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcActivateResourceVessel(KaitaiStruct):
        """Field sequence from handler at 0x08233fbd in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcActivateResourceVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAddAccountAura(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAddAccountAura, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcAddThumbUp(KaitaiStruct):
        """13 bytes. Request: echo + u16be(type) + u32be(0) + u32be(instance_id).
        Response: echo + u8(0x80) + u32be(0) + 4B(player/zone_id?) + u16be(flags).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAddThumbUp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.flags = self._io.read_u1()
            self.padding = self._io.read_u4be()
            self.zone_or_player_id = self._io.read_bytes(4)
            self.result_flags = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcAdminCmd(KaitaiStruct):
        """Field sequence from handler at 0x0822c2d4 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdminCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdventureCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdventureCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcAdventures(KaitaiStruct):
        """Available adventures list. u1 status + u1 count + count×u2be
        adventure_ids. Verified against 4B (count=0), 6B (count=1) and
        20B (count=8 IDs: 4,2,3,1,6,7,5,?) captures.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdventures, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.count = self._io.read_u1()
            self.adventure_ids = []
            for i in range(self.count):
                self.adventure_ids.append(self._io.read_u2be())



        def _fetch_instances(self):
            pass
            for i in range(len(self.adventure_ids)):
                pass



    class AcAdvertCreate(KaitaiStruct):
        """3B (fail) or 61B (success).
        3B form: echo + u8(result=1 = slot full/fail).
        61B form: echo + u32be(0) + u32be(0) + u16be(advert_id) + null-term item name + more data.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdvertCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.result = self._io.read_u1()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcAdvertDelete(KaitaiStruct):
        """Field sequence from handler at 0x08233a99 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdvertDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertGet(KaitaiStruct):
        """Single advert payload — a bag (advertId, vsender, …)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdvertGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcAdvertHeaderGet(KaitaiStruct):
        """Advert headers — a bag."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdvertHeaderGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcAttachEmail(KaitaiStruct):
        """Field sequence from handler at 0x0822b0fe in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAttachEmail, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachSteamAccount(KaitaiStruct):
        """Field sequence from handler at 0x0822b8fc in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAttachSteamAccount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachYupAccount(KaitaiStruct):
        """Field sequence from handler at 0x0822b8b8 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAttachYupAccount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAutoPilotSpaceStation(KaitaiStruct):
        """Field sequence from handler at 0x0822cfb0 in OnRecieve dispatch.
        Reads: u8 u32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAutoPilotSpaceStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.value = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcAutogenInvExtBuy(KaitaiStruct):
        """Autogen / seed-chip storage expansion purchase. 15B FIXED. Same
        shape as ac_inv_ext_buy. Verified (cost=40, capacity=4_000_000).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAutogenInvExtBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.cost = self._io.read_u4be()
            self.capacity = self._io.read_u4be()
            self.timestamp = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcAvatarsSetActive(KaitaiStruct):
        """Field sequence from handler at 0x0822c752 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAvatarsSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattlePassUnlockLevel(KaitaiStruct):
        """Field sequence from handler at 0x0822c900 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattlePassUnlockLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotChangeVessel(KaitaiStruct):
        """13 bytes. Request: echo + slot(u8) + 8B ship data (u32be zeros + u32be ship_id).
        Response: same + u16be result at end (observed: 0x0004).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattleSlotChangeVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.slot = self._io.read_u1()
            self.ship_data = self._io.read_bytes(8)
            self.result = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcBattleSlotCheatChangeVessel(KaitaiStruct):
        """Field sequence from handler at 0x08232f6d in OnRecieve dispatch.
        Reads: u8 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattleSlotCheatChangeVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotSwapVessels(KaitaiStruct):
        """Field sequence from handler at 0x08233002 in OnRecieve dispatch.
        Reads: u8 u8 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattleSlotSwapVessels, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()
            self.field_2 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlots(KaitaiStruct):
        """Battle loadout slots. u4be slot_count + variable-length slot list.
        Captures show 54B (count=4 + 6 slots) and 46B (count=3 + 5 slots),
        so the slot count != displayed slot count. Use `repeat: eos` to
        consume all remaining battle_slot entries regardless of count.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattleSlots, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.slot_count = self._io.read_u4be()
            self.slots = []
            i = 0
            while not self._io.is_eof():
                self.slots.append(StarConflictPackageServer.AcBattleSlots.BattleSlot(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.slots)):
                pass
                self.slots[i]._fetch_instances()


        class BattleSlot(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageServer.AcBattleSlots.BattleSlot, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.unknown = self._io.read_u4be()
                self.vessel_id = self._io.read_u4be()


            def _fetch_instances(self):
                pass



    class AcBuyArcDlc(KaitaiStruct):
        """Field sequence from handler at 0x082336d4 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyArcDlc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyGold(KaitaiStruct):
        """Field sequence from handler at 0x0823364b in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyGold, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyItem(KaitaiStruct):
        """Item-purchase ACK. 30B form is fail/queued (item_def empty).
        81B form is success: u4be amount + 8 zero bytes + cstring
        item_def_name (e.g. "SpaceMissile_ChildRockets_T5_Mk3") + opaque
        tail with new balances.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcBuyProductFromAdvert(KaitaiStruct):
        """Simple ACK — echo(2B) + result byte (0 = success)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyProductFromAdvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.result = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyTalentSet(KaitaiStruct):
        """Field sequence from handler at 0x0822dcb4 in OnRecieve dispatch.
        Reads: u8 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyTalentSet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCancelAccountAura(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcCancelAccountAura, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcChangePlayerNickname(KaitaiStruct):
        """Field sequence from handler at 0x0822ebd8 in OnRecieve dispatch.
        Reads: u8 cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcChangePlayerNickname, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.nickname = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcCheckYupPurchases(KaitaiStruct):
        """Field sequence from handler at 0x0822c796 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcCheckYupPurchases, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcChooseStartingStation(KaitaiStruct):
        """Field sequence from handler at 0x0822ecbb in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcChooseStartingStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanAssignEmblem(KaitaiStruct):
        """Field sequence from handler at 0x0822d050 in OnRecieve dispatch.
        Reads: u8 cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanAssignEmblem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.emblem = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcClanBankTransfer(KaitaiStruct):
        """Field sequence from handler at 0x0822f4c6 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanBankTransfer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeDesc(KaitaiStruct):
        """Field sequence from handler at 0x0822a941 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeMotd(KaitaiStruct):
        """Field sequence from handler at 0x0822a645 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeMotd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeName(KaitaiStruct):
        """Field sequence from handler at 0x0822d72b in OnRecieve dispatch.
        Reads: u8 cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeName, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcClanChangeRecruiting(KaitaiStruct):
        """Field sequence from handler at 0x0822a48c in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeRecruiting, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeTag(KaitaiStruct):
        """Field sequence from handler at 0x0822d136 in OnRecieve dispatch.
        Reads: u8 cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeTag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.tag = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcClanCreate(KaitaiStruct):
        """Field sequence from handler at 0x0822d21a in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanHistoryGet(KaitaiStruct):
        """Clan action history. Handler 0x0822f2da reads a u1 flag first; if
        set, a bag follows with a numbered entry per event (each entry is
        itself a bag with `action`, `time`, `params`). When the flag is 0
        the body is just the single bit. See `prefixed_bag_payload`.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanHistoryGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = prefixed_bag_payload.PrefixedBagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcClanInviteAccept(KaitaiStruct):
        """Field sequence from handler at 0x0822aa53 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteCancel(KaitaiStruct):
        """Field sequence from handler at 0x0822a812 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteSend(KaitaiStruct):
        """Field sequence from handler at 0x0822aa97 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqAccept(KaitaiStruct):
        """Field sequence from handler at 0x0822c665 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanJoinreqAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqCancel(KaitaiStruct):
        """Field sequence from handler at 0x0822bfea in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanJoinreqCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqCreate(KaitaiStruct):
        """Field sequence from handler at 0x0822c6a9 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanJoinreqCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanKick(KaitaiStruct):
        """Field sequence from handler at 0x0822a9cb in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanLeave(KaitaiStruct):
        """Field sequence from handler at 0x0822a514 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanListRecruiting(KaitaiStruct):
        """Recruiting clans — u8 status + bag list."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanListRecruiting, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcClanQuestAccept(KaitaiStruct):
        """Field sequence from handler at 0x0822d2ab in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanQuestAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestCredentials(KaitaiStruct):
        """Tabular response: list of (cid, name, tag, emblem) for the
        requested clans (typically 1, but recruiting list returns many).
        Confirmed against captures of varying sizes (44B count=1,
        274B count=7).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanRequestCredentials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u4be()
            self.clans = []
            for i in range(self.count):
                self.clans.append(StarConflictPackageServer.AcClanRequestCredentials.ClanCredential(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.clans)):
                pass
                self.clans[i]._fetch_instances()


        class ClanCredential(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageServer.AcClanRequestCredentials.ClanCredential, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.cid = self._io.read_u8be()
                self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self.tag = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                self.emblem = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


            def _fetch_instances(self):
                pass



    class AcClanRequestDesc(KaitaiStruct):
        """Full clan description (0x009f). Field names and types match the Lua
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
        """

        class Role(IntEnum):
            ceo = 0
            member = 1
            officer = 2
            vice_president = 3
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanRequestDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.cid = self._io.read_u8be()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self.tag = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self.motd = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self.desc = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self.emblem = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self.current_clan_ship = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self.creation_date = self._io.read_u8be()
            self.unknown_a = self._io.read_u4be()
            self.counter_target = self._io.read_u4be()
            self.counter_progress = self._io.read_u4be()
            self.clan_quest_id = self._io.read_s4be()
            self.clan_quest_progress = self._io.read_u2be()
            self.recruiting = self._io.read_u1()
            self.member_count = self._io.read_u4be()
            self.members = []
            for i in range(self.member_count):
                self.members.append(StarConflictPackageServer.AcClanRequestDesc.Member(self._io, self, self._root))

            self.invites_count = self._io.read_u4be()
            self.invites = []
            for i in range(self.invites_count):
                self.invites.append(self._io.read_u8be())

            self.joinreqs_count = self._io.read_u4be()
            self.joinreqs = []
            for i in range(self.joinreqs_count):
                self.joinreqs.append(self._io.read_u8be())

            self.upgrade_a = self._io.read_u1()
            self.upgrade_b = self._io.read_u1()
            self.resources = []
            for i in range(4):
                self.resources.append(self._io.read_u4be())

            self.fed_design_tgp_stream_flags = self._io.read_u4be()
            self._raw_fed_design_tgp_stream = self._io.read_bytes_full()
            _io__raw_fed_design_tgp_stream = KaitaiStream(BytesIO(self._raw_fed_design_tgp_stream))
            self.fed_design_tgp_stream = fed_design_tgp_stream.FedDesignTgpStream(_io__raw_fed_design_tgp_stream)


        def _fetch_instances(self):
            pass
            for i in range(len(self.members)):
                pass
                self.members[i]._fetch_instances()

            for i in range(len(self.invites)):
                pass

            for i in range(len(self.joinreqs)):
                pass

            for i in range(len(self.resources)):
                pass

            self.fed_design_tgp_stream._fetch_instances()

        class Member(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageServer.AcClanRequestDesc.Member, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.uid = self._io.read_u8be()
                self.role = KaitaiStream.resolve_enum(StarConflictPackageServer.AcClanRequestDesc.Role, self._io.read_u1())


            def _fetch_instances(self):
                pass



    class AcClanRequestProfile(KaitaiStruct):
        """Clan profile for a player; uid is the queried player."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanRequestProfile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.uid = self._io.read_u8be()
            self.unknown = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcClanResourceConvert(KaitaiStruct):
        """Field sequence from handler at 0x0822a987 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanResourceConvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanReviveInWar(KaitaiStruct):
        """Field sequence from handler at 0x0822d2e7 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanReviveInWar, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanSetCivilianZone(KaitaiStruct):
        """Field sequence from handler at 0x0822c7d2 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanSetCivilianZone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanSetRole(KaitaiStruct):
        """Field sequence from handler at 0x0822aa0f in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanSetRole, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBoostBuilding(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipBoostBuilding, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcClanShipBoostRepairing(KaitaiStruct):
        """Field sequence from handler at 0x0822a856 in OnRecieve dispatch.
        Reads: u8 cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipBoostRepairing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcClanShipBuild(KaitaiStruct):
        """Field sequence from handler at 0x0822a68b in OnRecieve dispatch.
        Reads: u8 cstrN cstrN cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipBuild, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.text1 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.text2 = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcClanShipFit(KaitaiStruct):
        """Field sequence from handler at 0x0822a558 in OnRecieve dispatch.
        Reads: u8 cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipFit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcClanShipRepair(KaitaiStruct):
        """Field sequence from handler at 0x0822a4d0 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipRepair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipSetCurrent(KaitaiStruct):
        """Field sequence from handler at 0x0822a448 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipSetCurrent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanUniverseMove(KaitaiStruct):
        """Clan universe-zone move ACK. 5B FIXED.
        u1 status + u2be zone_id (observed values vary by 1).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanUniverseMove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.zone_id = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcClanUpgrade(KaitaiStruct):
        """Field sequence from handler at 0x0822e328 in OnRecieve dispatch.
        Reads: u8 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanUpgrade, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanWarStart(KaitaiStruct):
        """Field sequence from handler at 0x0822d25e in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanWarStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCraftUpgradeItem(KaitaiStruct):
        """Field sequence from handler at 0x0822d32b in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcCraftUpgradeItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcDisassembleItem(KaitaiStruct):
        """Field sequence from handler at 0x0822ee0b in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcDisassembleItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcEmmChangeReady(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcEmmChangeReady, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcEnchantItem(KaitaiStruct):
        """Field sequence from handler at 0x08234d86 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcEnchantItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcEnterMmQueue(KaitaiStruct):
        """Matchmaking queue update; flags=0x80 means queued."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcEnterMmQueue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.flags = self._io.read_u1()
            self.queue_id = self._io.read_u4be()
            self.slot = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnterTournament(KaitaiStruct):
        """Tournament entry ACK — u8 status + bag of state."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcEnterTournament, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcExchangeGold(KaitaiStruct):
        """Exchange gold for credits."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcExchangeGold, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.credits = self._io.read_u4be()
            self.gold = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcFactionRepReset(KaitaiStruct):
        """Field sequence from handler at 0x0822cd72 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFactionRepReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFinalizeSteamMtxn(KaitaiStruct):
        """Field sequence from handler at 0x0822b52b in OnRecieve dispatch.
        Reads: u8 cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFinalizeSteamMtxn, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcFindAutogenItem(KaitaiStruct):
        """Field sequence from handler at 0x08234001 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFindAutogenItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsAcceptRequest(KaitaiStruct):
        """Result of accepting a friend request; uid is the new friend."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsAcceptRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcFriendsList(KaitaiStruct):
        """Field sequence from handler at 0x08232d20 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcFriendsRejectRequest(KaitaiStruct):
        """Field sequence from handler at 0x0822ff6c in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsRejectRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcFriendsRemove(KaitaiStruct):
        """Field sequence from handler at 0x08232dfc in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcFriendsSendRequest(KaitaiStruct):
        """Despite the AC name, the response carries the player's full social
        state. Handler 0x082338d8 → FUN_08901240 reads, byte-aligned:
        
          u1 num_friends,        num_friends × u8be UID
          u1 num_requests_in,    num × u8be UID
          u1 num_requests_out,   num × u8be UID
          u1 num_ignored,        num × u8be UID
          u1 num_watched,        num × u8be UID
          u1 num_pairs_a,        num × {u8be uid, u8be uid}
          u1 num_pairs_b,        num × {u8be uid, u8be uid}
        
        Surfaced through ac_unknown_bodies.AcFriendsSendRequestBody.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsSendRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_friends_send_request_body.AcFriendsSendRequestBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcGamesInfo(KaitaiStruct):
        """Field sequence from handler at 0x0822c20a in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGamesInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetBlueprints(KaitaiStruct):
        """Player blueprint inventory. Handler 0x0822d434 reads a u1 flag
        first (negated and stored as an internal "loaded" state) then the
        bag, so the body is `u1 + bag`. See `prefixed_bag_payload`.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetBlueprints, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = prefixed_bag_payload.PrefixedBagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcGetCraftResources(KaitaiStruct):
        """Craft-resource balances — a bag of u64 amounts."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetCraftResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcGetFbToken(KaitaiStruct):
        """Facebook token (18-byte blob, all-zero when not linked)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetFbToken, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.token = self._io.read_bytes(18)


        def _fetch_instances(self):
            pass


    class AcGetFreeSpaceSaveData(KaitaiStruct):
        """Free-space save data — a bag."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetFreeSpaceSaveData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcGetNicknames(KaitaiStruct):
        """Return list of nicknames."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetNicknames, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_u2be()
            self.num_nicks = self._io.read_u2be()
            self.nicks = []
            for i in range(self.num_nicks):
                self.nicks.append(StarConflictPackageServer.AcGetNicknames.Nick(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.nicks)):
                pass
                self.nicks[i]._fetch_instances()


        class Nick(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageServer.AcGetNicknames.Nick, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.uid = self._io.read_u8be()
                self.nickname = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")


            def _fetch_instances(self):
                pass



    class AcGetPunishments(KaitaiStruct):
        """Field sequence from handler at 0x0822eed9 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetPunishments, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetUids(KaitaiStruct):
        """Field sequence from handler at 0x08232521 in OnRecieve dispatch.
        Reads: u16
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetUids, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.value = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcGetUserdata(KaitaiStruct):
        """User-data dict (UI layout, preferences) — bag."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetUserdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcGetVisitedFreeSpaceZones(KaitaiStruct):
        """Visited-zones bitmap — a bag."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetVisitedFreeSpaceZones, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcInvExtBuy(KaitaiStruct):
        """Inventory expansion purchase. 15B FIXED.
        u1 status + u4be cost + u4be capacity + u4be timestamp.
        Verified against capture (cost=1500, capacity=2_000_000).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcInvExtBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.cost = self._io.read_u4be()
            self.capacity = self._io.read_u4be()
            self.timestamp = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcKarmaReset(KaitaiStruct):
        """Field sequence from handler at 0x0822cdb6 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcKarmaReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaderboardGet(KaitaiStruct):
        """Leaderboard — u8 status + bag of entries."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeaderboardGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcLeaderboardGetDescs(KaitaiStruct):
        """Leaderboard descriptors — u4be header + bag list."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeaderboardGetDescs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.header = self._io.read_u4be()
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcLeagueTeamCreate(KaitaiStruct):
        """Field sequence from handler at 0x082306bf in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInfo(KaitaiStruct):
        """Field sequence from handler at 0x08232b6c in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteAccept(KaitaiStruct):
        """Field sequence from handler at 0x08232aa0 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteCancel(KaitaiStruct):
        """Field sequence from handler at 0x082329b1 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteDecline(KaitaiStruct):
        """Field sequence from handler at 0x08232b28 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInviteDecline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteSend(KaitaiStruct):
        """Field sequence from handler at 0x08232a28 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamKick(KaitaiStruct):
        """Field sequence from handler at 0x0822e295 in OnRecieve dispatch.
        Reads: u8 u64 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.u64_1 = self._io.read_u8be()
            self.u64_2 = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamLeave(KaitaiStruct):
        """Field sequence from handler at 0x08232c98 in OnRecieve dispatch.
        Reads: u8 u64 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.u64_1 = self._io.read_u8be()
            self.u64_2 = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamRequestNames(KaitaiStruct):
        """Field sequence from handler at 0x08232bb0 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamRequestNames, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLearnBlueprint(KaitaiStruct):
        """ACK for learning a blueprint. status=0 success.
        Confirmed against capture ac_00e7_unknown.bin (33B): blueprint name
        "BP_Module_AdvancedHeal_T5_Rel".
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLearnBlueprint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.blueprint_def_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcLeaveMmQueue(KaitaiStruct):
        """2B echo + 2B status. Observed: 0xc240 (normal leave), 0x8000 (queue closed).
        The status is a bit-packed field; exact bit layout not reversed.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeaveMmQueue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcLeaveTournament(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeaveTournament, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcLoadInitialPlayerData(KaitaiStruct):
        """Initial player snapshot on login. Body is a single bit-stream the
        handler at 0x0823103b walks as 22 fields (16 byte-aligned scalars
        + 6 nested property bags interleaved). Sizes range from 2B
        (echo-only) and 8B (truncated short form — handler tolerates
        short reads via its lastReadOK flag) up to ~240 kB full state.
        Decoded by the ac_load_initial_player_data_body opaque type
        which mirrors the binary's read sequence and stops cleanly on
        EOFError when bodies are truncated.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLoadInitialPlayerData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.data = ac_load_initial_player_data_body.AcLoadInitialPlayerDataBody(self._io)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcLobbyCreate(KaitaiStruct):
        """Newly-created lobby info. Layout from 88-114B captures:
          u8be lobby_id (zero before creation completes) + cstring name +
          u4be reserved + cstring level_def_name + opaque settings tail.
        Tail contains mode + slot caps + flags but exact layout varies.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.lobby_id = self._io.read_u8be()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self.reserved = self._io.read_u4be()
            self.level_def_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.settings_payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupCreate(KaitaiStruct):
        """Field sequence from handler at 0x0822ac9c in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupDelete(KaitaiStruct):
        """Field sequence from handler at 0x0822ac58 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqCancel(KaitaiStruct):
        """Field sequence from handler at 0x0822ab17 in OnRecieve dispatch.
        Reads: u8 u32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupJoinreqCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.value = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqCreate(KaitaiStruct):
        """Field sequence from handler at 0x0822abb8 in OnRecieve dispatch.
        Reads: u8 u32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupJoinreqCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.value = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqReject(KaitaiStruct):
        """Field sequence from handler at 0x0822c55e in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupJoinreqReject, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupList(KaitaiStruct):
        """List of joinable lobby groups. 4B captures show empty list (count=0).
        Per-entry layout for non-empty lists not yet documented.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupModify(KaitaiStruct):
        """Field sequence from handler at 0x0822bfa4 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupModify, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyInfo(KaitaiStruct):
        """Lobby state — handler 0x0822b1c7 → FUN_088f1690. Inline reader:
        u8 lobby_id, cstring name, u4 unknown, cstring desc, plus a long
        tail (u8/u8/u8/6×u1/2×f32/u2/u4/u1/u8 + member array + 4 strings).
        Surfaced through ac_unknown_bodies.AcLobbyInfoBody (header
        decoded, tail kept opaque).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_lobby_info_body.AcLobbyInfoBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcLobbyInvite(KaitaiStruct):
        """Field sequence from handler at 0x0822b466 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyInvite, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyJoin(KaitaiStruct):
        """Field sequence from handler at 0x0822b264 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyJoin, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyKick(KaitaiStruct):
        """Field sequence from handler at 0x0822b42a in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyLeave(KaitaiStruct):
        """Lobby-leave ACK. 3B captures: echo + u1 status (0x00 = success).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcLobbyModify(KaitaiStruct):
        """Lobby modification ACK. 5B FIXED — observed identical bytes
        (0xd0, 0x80, 0x52) across captures, suggesting bit-packed flags
        or reserved status. Layout not yet fully reversed.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyModify, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.opaque_status = self._io.read_bytes(3)


        def _fetch_instances(self):
            pass


    class AcLobbyStartGame(KaitaiStruct):
        """Field sequence from handler at 0x0822b069 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyStartGame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLogFbEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLogFbEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcMailAcknowledgeExpiration(KaitaiStruct):
        """Acknowledge expired mail; mail_id=0xffffffff means all."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailAcknowledgeExpiration, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.mail_id = self._io.read_u4be()
            self.timestamp = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcMailDeliver(KaitaiStruct):
        """16 bytes. Push from server when mail arrives.
        Layout: echo(2) + u32be(0) + u32be(mail_id) + u32be(expiry_or_ts) + u16be(flags).
        Observed: mail_id=0x00656ca9, expiry=0x77000000, flags=0x0100.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailDeliver, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.padding = self._io.read_u4be()
            self.mail_id = self._io.read_u4be()
            self.expiry_ts = self._io.read_u4be()
            self.flags = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcMailGet(KaitaiStruct):
        """Mailbox listing. Handler at 0x0822e030 reads u8 status. Body is
        either 6B empty (`00 d0 00 00 00 00`) or 100B+ full mailbox with
        bit-packed mail records the linear handler walk doesn't capture.
        Status + opaque tail until per-mail layout is reversed.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcMailRemove(KaitaiStruct):
        """Field sequence from handler at 0x0822e184 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcMailSend(KaitaiStruct):
        """Result of sending mail; status + assigned mail ID."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.unknown = self._io.read_u1()
            self.mail_id = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcMmInfo(KaitaiStruct):
        """Matchmaking queue state. Body is a single property bag."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMmInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcMotd(KaitaiStruct):
        """Server MOTD notification; status indicates MOTD type/availability."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMotd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMottosSetActive(KaitaiStruct):
        """Currently-active motto plus the list of acquired motto / taunt names.
        Confirmed via two capture variants:
          62B: status=0 + empty active_motto + count=6 + 6 entries.
          70B: status=0 + active_motto="Taunt_68" + count=6 + 6 entries.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMottosSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.active_motto = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.count = self._io.read_u2be()
            self.taunts = []
            for i in range(self.count):
                self.taunts.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))



        def _fetch_instances(self):
            pass
            for i in range(len(self.taunts)):
                pass



    class AcObtainReferralKey(KaitaiStruct):
        """Referral / promotion key. 36B FIXED. Body is a cs0-shifted
        string (each byte = (char>>1) | (carry<<7)) encoding the
        promo code; layout opaque.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcObtainReferralKey, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.cs0_key = self._io.read_bytes(34)


        def _fetch_instances(self):
            pass


    class AcPlayerArcBalance(KaitaiStruct):
        """Field sequence from handler at 0x08232318 in OnRecieve dispatch.
        Reads: i32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerArcBalance, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.value = self._io.read_s4be()


        def _fetch_instances(self):
            pass


    class AcPlayerAutogenInventory(KaitaiStruct):
        """Field sequence from handler at 0x082342e0 in OnRecieve dispatch.
        Reads: u32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerAutogenInventory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.value = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcPlayerCredentials(KaitaiStruct):
        """Player nickname and session credentials."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerCredentials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.nickname = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcPlayerCredits(KaitaiStruct):
        """Player wallet snapshot. Handler 0x08231c56 → FUN_088e9ec0 reads
        a u16 flag word then byte-aligned per-bit currency balances:
        bit 1 → credits, bit 2 → goldCredits, bit 3 → tokenCredits,
        bit 4 → loyalty + loyalty_time, bit 5 → vid, bit 6 → premium,
        bit 7 → 5 × craft resources. All fields are byte-sized so the
        layout maps cleanly to native kaitai.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerCredits, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.flags = self._io.read_u2be()
            if self.flags & 2 != 0:
                pass
                self.credits = self._io.read_u8be()

            if self.flags & 4 != 0:
                pass
                self.gold_credits = self._io.read_u8be()

            if self.flags & 8 != 0:
                pass
                self.token_credits = self._io.read_u8be()

            if self.flags & 16 != 0:
                pass
                self.loyalty = self._io.read_u8be()

            if self.flags & 16 != 0:
                pass
                self.loyalty_time = self._io.read_u8be()

            if self.flags & 32 != 0:
                pass
                self.vid = self._io.read_u8be()

            if self.flags & 64 != 0:
                pass
                self.premium = self._io.read_u4be()

            if self.flags & 128 != 0:
                pass
                self.craft_resources = []
                for i in range(5):
                    self.craft_resources.append(self._io.read_u4be())




        def _fetch_instances(self):
            pass
            if self.flags & 2 != 0:
                pass

            if self.flags & 4 != 0:
                pass

            if self.flags & 8 != 0:
                pass

            if self.flags & 16 != 0:
                pass

            if self.flags & 16 != 0:
                pass

            if self.flags & 32 != 0:
                pass

            if self.flags & 64 != 0:
                pass

            if self.flags & 128 != 0:
                pass
                for i in range(len(self.craft_resources)):
                    pass




    class AcPlayerInventory(KaitaiStruct):
        """Inventory dump. Handler at 0x08233968 reads, bit-packed:
        
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
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerInventory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_player_inventory_body.AcPlayerInventoryBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcPlayerStats(KaitaiStruct):
        """92B FIXED. Player stat record encoded as a bag."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerStats, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcPlayerVessels(KaitaiStruct):
        """Field sequence from handler at 0x0822e436 in OnRecieve dispatch.
        Reads: u16 f32 f32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerVessels, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.u16_0 = self._io.read_u2be()
            self.value = self._io.read_f4be()
            self.value1 = self._io.read_f4be()


        def _fetch_instances(self):
            pass


    class AcPremiumBuy(KaitaiStruct):
        """Field sequence from handler at 0x0822f442 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPremiumBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPremiumInfo(KaitaiStruct):
        """Premium account expiry timestamp in milliseconds."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPremiumInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.expiry_ms = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcQuestAccept(KaitaiStruct):
        """19 bytes. Same shape as ac_quest_change (just shorter opaque tail):
        echo + u8(status=0) + u16be(quest_id_echo) + 14B opaque payload.
        Confirmed against capture ac_0019_unknown.bin (quest_id=0x035a).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuestAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.quest_id = self._io.read_u2be()
            self.opaque = self._io.read_bytes(14)


        def _fetch_instances(self):
            pass


    class AcQuestChange(KaitaiStruct):
        """21 bytes. Request: echo + u16be(quest_id).
        Response: echo + u8(status=0) + u16be(quest_id_echo) + u16be(new_state) + 12B opaque.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuestChange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.quest_id = self._io.read_u2be()
            self.new_state = self._io.read_u2be()
            self.opaque = self._io.read_bytes(14)


        def _fetch_instances(self):
            pass


    class AcQuestComplete(KaitaiStruct):
        """41 or 53 bytes. Request: echo + u16be(quest_id).
        Response: echo + u8(status=0) + u16be(quest_id_echo) + bit-packed reward/stat data.
        Shorter form (41B) omits the extra reward block present in the 53B form.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuestComplete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.quest_id = self._io.read_u2be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcQuestCompleteAll(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuestCompleteAll, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcQuests(KaitaiStruct):
        """Active and template quest list. Handler 0x0822d960 has a multi-section
        inline reader: 3×u4 totals + 4×u1 flags, then a u4+u1 dailies array,
        a per-quest array (FUN_088f8e20 prelude + u2 id + u1 status + u4
        progress + 2 optional u8s), then a quest-desc array, two u2-prefixed
        quest-id arrays, and a flag-byte/i32-pair stream terminated by 0xff.
        Surfaced through ac_unknown_bodies.AcQuestsBody (top fields only).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuests, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_quests_body.AcQuestsBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcReactOnAbandonedGame(KaitaiStruct):
        """Field sequence from handler at 0x08233b19 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcReactOnAbandonedGame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReferrals(KaitaiStruct):
        """Referral program info; flags=0x80 when no active referrer."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcReferrals, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.flags = self._io.read_u1()
            self.uid = self._io.read_u8be()
            self.reserved = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRelatedQuestEnable(KaitaiStruct):
        """Field sequence from handler at 0x0822d3f8 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcRelatedQuestEnable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReportPlayer(KaitaiStruct):
        """Field sequence from handler at 0x082324e5 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcReportPlayer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRewardTutorial(KaitaiStruct):
        """Field sequence from handler at 0x0823444a in OnRecieve dispatch.
        Reads: u8 u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcRewardTutorial, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()
            self.u64_2 = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcRewardedTutorials(KaitaiStruct):
        """List of tutorial IDs that have been completed and rewarded."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcRewardedTutorials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u1()
            self.tutorial_ids = []
            for i in range(self.count):
                self.tutorial_ids.append(self._io.read_u1())



        def _fetch_instances(self):
            pass
            for i in range(len(self.tutorial_ids)):
                pass



    class AcSalvageItem(KaitaiStruct):
        """Field sequence from handler at 0x08234a1b in OnRecieve dispatch.
        Reads: u64 u8 u32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSalvageItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.u64_0 = self._io.read_u8be()
            self.field_1 = self._io.read_u1()
            self.u32_2 = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcSalvageItems(KaitaiStruct):
        """Field sequence from handler at 0x0822fa48 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSalvageItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellCraftResource(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellCraftResource, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcSellCraftResources(KaitaiStruct):
        """Field sequence from handler at 0x0822c816 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellCraftResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcSellItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcSellVessel(KaitaiStruct):
        """Field sequence from handler at 0x08234b30 in OnRecieve dispatch.
        Reads: u64 u8 u32 f32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.u64_0 = self._io.read_u8be()
            self.field_1 = self._io.read_u1()
            self.u32_2 = self._io.read_u4be()
            self.value = self._io.read_f4be()


        def _fetch_instances(self):
            pass


    class AcSendEarlyPlayerLog(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSendEarlyPlayerLog, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcServerInfo(KaitaiStruct):
        """Server metadata. The 20-byte canonical form is memcpy'd verbatim
        into a singleton struct at 0x096285b4 from which Lua binding
        MasterServer_GetServerInfo (fn at 0x086ff780) reads field-by-field.
        Unlike most AC packets on this channel the scalar fields are
        LITTLE-ENDIAN — the client reads them with native x86 loads
        (fldl/mov), so the wire bytes are whatever the server had in memory.
        
        Short-form variants also appear on this type code (e.g. 14-byte and
        6-byte bodies) which look like periodic status updates with a
        different shape; the fields below are gated on remaining bytes so
        those don't fail to parse.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcServerInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            if self._io.size() - self._io.pos() >= 8:
                pass
                self.server_time_ms = self._io.read_f8le()

            if self._io.size() - self._io.pos() >= 4:
                pass
                self.unknown_8 = self._io.read_bytes(4)

            if self._io.size() - self._io.pos() >= 4:
                pass
                self.sandbox_access = self._io.read_u4le()

            if self._io.size() - self._io.pos() >= 1:
                pass
                self.mm_disabled = self._io.read_u1()

            if self._io.size() - self._io.pos() >= 1:
                pass
                self.mm_enable_pve_raids = self._io.read_u1()

            if self._io.size() - self._io.pos() >= 1:
                pass
                self.mm_enable_league = self._io.read_u1()

            if self._io.size() - self._io.pos() >= 1:
                pass
                self.mm_enable_coop_vs_ai = self._io.read_u1()

            self.tail = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass
            if self._io.size() - self._io.pos() >= 8:
                pass

            if self._io.size() - self._io.pos() >= 4:
                pass

            if self._io.size() - self._io.pos() >= 4:
                pass

            if self._io.size() - self._io.pos() >= 1:
                pass

            if self._io.size() - self._io.pos() >= 1:
                pass

            if self._io.size() - self._io.pos() >= 1:
                pass

            if self._io.size() - self._io.pos() >= 1:
                pass



    class AcSetFbToken(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSetFbToken, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcSetReferrer(KaitaiStruct):
        """Field sequence from handler at 0x0822b4e7 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSetReferrer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetUserdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSetUserdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_u2be()
            self.value = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcSetVisitedZone(KaitaiStruct):
        """Field sequence from handler at 0x0822cec6 in OnRecieve dispatch.
        Reads: u16
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSetVisitedZone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.value = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcShipQuestChange(KaitaiStruct):
        """Field sequence from handler at 0x082340b4 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcShipQuestChange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestEnd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcShipQuestEnd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcShipQuestStart(KaitaiStruct):
        """Field sequence from handler at 0x082340f8 in OnRecieve dispatch.
        Reads: u8 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcShipQuestStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuests(KaitaiStruct):
        """Per-ship quest list. Handler 0x0822bdf8 reads u1 flag + u1 num_records,
        then num_records × {FUN_088f9340 prelude, u1, u1, u4, u8, 8×u8be}.
        Surfaced through ac_unknown_bodies.AcShipQuestsBody.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcShipQuests, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_ship_quests_body.AcShipQuestsBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcSocialIgnoreAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialIgnoreAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSocialIgnoreRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialIgnoreRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestFb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialSuggestFb, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestSteam(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialSuggestSteam, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestVk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialSuggestVk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcSocialWatchAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialWatchAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSocialWatchRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialWatchRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSpaceStationsPopulation(KaitaiStruct):
        """Per-station population dict — a bag."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSpaceStationsPopulation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bag = bag_payload.BagPayload(self._io)


        def _fetch_instances(self):
            pass
            self.bag._fetch_instances()


    class AcSquadConvertToWing(KaitaiStruct):
        """Field sequence from handler at 0x08232ae4 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadConvertToWing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInfo(KaitaiStruct):
        """Current squad state; zero fields when not in a squad."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.squad_id = self._io.read_u8be()
            self.leader_uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSquadInviteAccept(KaitaiStruct):
        """Field sequence from handler at 0x08233ad5 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteCancel(KaitaiStruct):
        """ACK for cancelling an outbound squad-invite. 11 bytes: status + invitee uid.
        Confirmed against capture ac_0060_unknown.bin (status=0 = success).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSquadInviteDecline(KaitaiStruct):
        """Field sequence from handler at 0x0822f486 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInviteDecline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSquadInviteSend(KaitaiStruct):
        """ACK for outbound squad-invite. 11 bytes: status + invitee uid.
        Confirmed against capture ac_005f_unknown.bin.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSquadKick(KaitaiStruct):
        """Field sequence from handler at 0x0822c328 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcSquadLeave(KaitaiStruct):
        """Field sequence from handler at 0x08230f38 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadReady(KaitaiStruct):
        """Field sequence from handler at 0x08232bf4 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadReady, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSteamUserInfo(KaitaiStruct):
        """Field sequence from handler at 0x0822eb94 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSteamUserInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyGetNew(KaitaiStruct):
        """Response to survey poll; all-zero when no surveys available."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSurveyGetNew, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.reserved = self._io.read_u4be()
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyResults(KaitaiStruct):
        """Survey result data; all-zero when no surveys active."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSurveyResults, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.reserved = self._io.read_u4be()
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyVote(KaitaiStruct):
        """Field sequence from handler at 0x0822efcd in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSurveyVote, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTaStatsSendTutorialEntter(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTaStatsSendTutorialEntter, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcTaStatsSendTutorialExit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTaStatsSendTutorialExit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcTalentsAcquire(KaitaiStruct):
        """Field sequence from handler at 0x082302a0 in OnRecieve dispatch.
        Reads: u8 u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTalentsAcquire, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()
            self.u64_2 = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcTalentsAssignSets(KaitaiStruct):
        """Confirmed talent set assignments for 4 role slots."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTalentsAssignSets, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.set_ids = []
            for i in range(4):
                self.set_ids.append(self._io.read_u1())



        def _fetch_instances(self):
            pass
            for i in range(len(self.set_ids)):
                pass



    class AcTalentsReset(KaitaiStruct):
        """Field sequence from handler at 0x082303a7 in OnRecieve dispatch.
        Reads: u8 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTalentsReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsUpdate(KaitaiStruct):
        """Field sequence from handler at 0x082304ad in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTalentsUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingAccept(KaitaiStruct):
        """Field sequence from handler at 0x0822bb58 in OnRecieve dispatch.
        Reads: u8 u64 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.u64_1 = self._io.read_u8be()
            self.field_2 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingAllow(KaitaiStruct):
        """Field sequence from handler at 0x0822b852 in OnRecieve dispatch.
        Reads: u8 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingAllow, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingCheck(KaitaiStruct):
        """Field sequence from handler at 0x0822b97f in OnRecieve dispatch.
        Reads: u8 u64 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingCheck, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.u64_1 = self._io.read_u8be()
            self.field_2 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingList(KaitaiStruct):
        """Teach/learn relationship state. Handler 0x0822bf58 → FUN_08917c10
        calls a u4be-count + u8be-UID list reader six times, then reads two
        u1 flag bits. Empty teaching state shows up as 6×0-count lists +
        both flags=true (25-byte body). Surfaced through
        ac_unknown_bodies.AcTeachingListBody.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_teaching_list_body.AcTeachingListBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcTeachingReject(KaitaiStruct):
        """Field sequence from handler at 0x0822b9c6 in OnRecieve dispatch.
        Reads: u8 u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingReject, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()
            self.u64_2 = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcTeachingRequestToStudent(KaitaiStruct):
        """Field sequence from handler at 0x082309f6 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingRequestToStudent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcTeachingRequestToTeacher(KaitaiStruct):
        """Field sequence from handler at 0x0822be79 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingRequestToTeacher, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcTitlesSetActive(KaitaiStruct):
        """Field sequence from handler at 0x0822c6ed in OnRecieve dispatch.
        Reads: u8 u16
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTitlesSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.value = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcUndockSpaceStation(KaitaiStruct):
        """Undock result; status 0 = success."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUndockSpaceStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUniverseCounters(KaitaiStruct):
        """Field sequence from handler at 0x0822e0f3 in OnRecieve dispatch.
        Reads: u8 u64 f32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUniverseCounters, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.u64_1 = self._io.read_u8be()
            self.value = self._io.read_f4be()


        def _fetch_instances(self):
            pass


    class AcUniverseGet(KaitaiStruct):
        """Sector-control snapshot — what `MasterServer.UniverseGet` returns
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
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUniverseGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_universe_get_body.AcUniverseGetBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcUnlimPveDisablePlayerBuffs(KaitaiStruct):
        """Field sequence from handler at 0x08233d48 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUnlimPveDisablePlayerBuffs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUnlimPveUpgradePlayerLevel(KaitaiStruct):
        """Field sequence from handler at 0x08233710 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUnlimPveUpgradePlayerLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpdateDlcOwnership(KaitaiStruct):
        """Field sequence from handler at 0x08233924 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUpdateDlcOwnership, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpdateYupPurchases(KaitaiStruct):
        """Server-pushed Yuplay (Gaijin storefront) purchase state. Sent
        unsolicited shortly after connect to seed the cache.
        Body format (handler 0x082327ae): u8 status + bag yupPurchases +
        u8 N + N × cstring(<=60). Surfaced through
        `ac_update_yup_purchases_body`."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUpdateYupPurchases, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_update_yup_purchases_body.AcUpdateYupPurchasesBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcUpgradeAutogenItem(KaitaiStruct):
        """Field sequence from handler at 0x082348e0 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUpgradeAutogenItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpgradeItems(KaitaiStruct):
        """Field sequence from handler at 0x08232ed8 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUpgradeItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUseBlueprint(KaitaiStruct):
        """ACK for using a blueprint. Handler 0x0822c85a reads, when
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
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUseBlueprint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_use_blueprint_response_body.AcUseBlueprintResponseBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcUserNotes(KaitaiStruct):
        """Field sequence from handler at 0x0822f662 in OnRecieve dispatch.
        Reads: u32
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUserNotes, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.value = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class AcUserNotesAdd(KaitaiStruct):
        """Confirmation of user note added; echoes uid and note text."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUserNotesAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()
            self.note = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")


        def _fetch_instances(self):
            pass


    class AcUserNotesDelete(KaitaiStruct):
        """Confirmation of user note deletion."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUserNotesDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.flags = self._io.read_u2be()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcUserProfileGet(KaitaiStruct):
        """Bulk player-profile dump. Handler 0x0822ed43 reads u2 num_records
        then `num_records` × per-profile records via FUN_08922e60 (init) +
        FUN_08924e60 (the heavy reader). Each record is bit-packed and
        flag-driven: the inner reader exposes u8 uid, then a u32 flags
        word, then optional fields per bit (clan, alliance, rating, big
        ship-stats arrays at offsets +0x4ee and +0x26b4 of the in-memory
        struct, leaderboard entries, achievements). Surfaced through
        `ac_user_profile_get_response_body`; only the leading u2 count is
        currently exposed cleanly.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUserProfileGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_user_profile_get_response_body.AcUserProfileGetResponseBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcVesselActivateNode(KaitaiStruct):
        """Activate / unlock vessel skill node. 34B captures show:
        u4be status + u8be vessel_id + opaque node-state tail.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselActivateNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.vessel_id = self._io.read_u8be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcVesselAutogenDestroy(KaitaiStruct):
        """Autogen module destroy ACK. Variable size (10B / 274B observed).
        Header u4be status + bit-packed per-item payload listing
        destroyed items + refunds. Layout not fully reversed.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselAutogenDestroy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcVesselAutogenDismantle(KaitaiStruct):
        """Autogen module dismantle ACK. 64B captures.
        Header u4be status + bit-packed payload. Layout not fully reversed.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselAutogenDismantle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcVesselBudgetActivate(KaitaiStruct):
        """Budget vessel activation confirmation."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselBudgetActivate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.vessel_id = self._io.read_u4be()
            self.unknown = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselBudgetLevelup(KaitaiStruct):
        """Field sequence from handler at 0x08233ea8 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselBudgetLevelup, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeEquip(KaitaiStruct):
        """Server response to a vessel-equip change. Handler 0x082352c8 reads,
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
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselChangeEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_vessel_change_equip_response_body.AcVesselChangeEquipResponseBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcVesselChangeEquipMulti(KaitaiStruct):
        """Multi-equip response. Shares handler 0x082352c8 with the single
        variant for the prefix (status + vessel_id + 35 slot_module_ids)
        but the multi case has a much longer tail with per-change cleartext
        records (item_name + 2 flag bytes) and an inventory delta.
        Surfaced through ac_vessel_change_equip_multi_response_body.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselChangeEquipMulti, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = ac_vessel_change_equip_multi_response_body.AcVesselChangeEquipMultiResponseBody(_io__raw_data)


        def _fetch_instances(self):
            pass
            self.data._fetch_instances()


    class AcVesselChangeMunition(KaitaiStruct):
        """Field sequence from handler at 0x08234924 in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselChangeMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcVesselCheatChangeEquip(KaitaiStruct):
        """Field sequence from handler at 0x0823010c in OnRecieve dispatch.
        Reads: u8 u64 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselCheatChangeEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.u64_1 = self._io.read_u8be()
            self.field_2 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCraft(KaitaiStruct):
        """Field sequence from handler at 0x08233f81 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselCraft, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCustomElementsAcknowledgeExpiration(KaitaiStruct):
        """Field sequence from handler at 0x08230779 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselCustomElementsAcknowledgeExpiration, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCustomElementsBuy(KaitaiStruct):
        """Field sequence from handler at 0x0823080e in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselCustomElementsBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselEquipment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselEquipment, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcVesselExtractExp(KaitaiStruct):
        """Server response after a vessel-XP extraction. Handler 0x0822f3ad
        reads u1 status; on success, follows with a u4 extracted_amount,
        a u4 count, and `count` × {u8 vessel_id, u4 new_xp_value} records.
        Fully byte-aligned.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselExtractExp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            if self.status == 0:
                pass
                self.extracted_amount = self._io.read_u4be()

            if self.status == 0:
                pass
                self.num_vessels = self._io.read_u4be()

            if self.status == 0:
                pass
                self.vessels = []
                for i in range(self.num_vessels):
                    self.vessels.append(StarConflictPackageServer.AcVesselExtractExp.VesselXpUpdate(self._io, self, self._root))




        def _fetch_instances(self):
            pass
            if self.status == 0:
                pass

            if self.status == 0:
                pass

            if self.status == 0:
                pass
                for i in range(len(self.vessels)):
                    pass
                    self.vessels[i]._fetch_instances()



        class VesselXpUpdate(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageServer.AcVesselExtractExp.VesselXpUpdate, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.vessel_id = self._io.read_u8be()
                self.new_xp = self._io.read_u4be()


            def _fetch_instances(self):
                pass



    class AcVesselFreeCustomElements(KaitaiStruct):
        """Field sequence from handler at 0x082308a3 in OnRecieve dispatch.
        Reads: u32 cstrN
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselFreeCustomElements, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.value = self._io.read_u4be()
            self.text = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcVesselLevelup(KaitaiStruct):
        """Vessel level-up confirmation. 29B FIXED:
        u4be status + u8be vessel_id + opaque level/xp/credit data.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselLevelup, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.vessel_id = self._io.read_u8be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcVesselRecraft(KaitaiStruct):
        """Field sequence from handler at 0x08233a55 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRecraft, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRefillBattle(KaitaiStruct):
        """Field sequence from handler at 0x08233754 in OnRecieve dispatch.
        Reads: u8 u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRefillBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.field_1 = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRefillMunition(KaitaiStruct):
        """Munition refill confirmation; count = munitions restored."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRefillMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.unknown = self._io.read_u1()
            self.vessel_id = self._io.read_u4be()
            self.count = self._io.read_u2be()
            self.reserved = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRepair(KaitaiStruct):
        """Repair confirmation; vessel_id identifies the repaired vessel."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRepair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_u4be()
            self.vessel_id = self._io.read_u4be()
            self.status = self._io.read_u2be()


        def _fetch_instances(self):
            pass


    class AcVesselRepairBattle(KaitaiStruct):
        """Field sequence from handler at 0x08230d28 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRepairBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselStripEquip(KaitaiStruct):
        """Field sequence from handler at 0x0823353e in OnRecieve dispatch.
        Reads: u8 u64
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselStripEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.uid = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcVesselStripImproperBattle(KaitaiStruct):
        """8B FIXED. Handler at 0x08233d8c reads only u8 status. Remaining
        5B varies between captures (count-style values that don't fit a
        simple count + u1 array layout) — kept opaque pending RE.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselStripImproperBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcVesselTransferEquip(KaitaiStruct):
        """Transfer equipment between vessels. Confirmed against 38B captures:
        u4be status + u8be vessel_id_from + u8be vessel_id_to + opaque
        module-list tail.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselTransferEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.vessel_id_from = self._io.read_u8be()
            self.vessel_id_to = self._io.read_u8be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcVesselTransferMunition(KaitaiStruct):
        """Transfer munition between vessels. 22B FIXED:
        u4be status + u8be vessel_id_from + u8be vessel_id_to.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselTransferMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u4be()
            self.vessel_id_from = self._io.read_u8be()
            self.vessel_id_to = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcVesselUnlockNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselUnlockNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcWarmapGet(KaitaiStruct):
        """Sector ownership map. Handler at 0x0822e0a7 → FUN_08929b80; per-sector
        reader is FUN_08927420. All fields are byte-aligned (u4be/u8be/f4be),
        so the layout maps cleanly to native kaitai. The requesting clan's
        home sector (0x5fe = GD3F) appears with real coordinates and ~11
        links; off-map sectors arrive with y=10000.0 / radius=0.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcWarmapGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.num_sectors = self._io.read_u4be()
            self.sectors = []
            for i in range(self.num_sectors):
                self.sectors.append(StarConflictPackageServer.AcWarmapGet.WarmapSector(self._io, self, self._root))

            self.num_locations = self._io.read_u4be()
            self.locations = []
            for i in range(self.num_locations):
                self.locations.append(StarConflictPackageServer.AcWarmapGet.WarmapLocation(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.sectors)):
                pass
                self.sectors[i]._fetch_instances()

            for i in range(len(self.locations)):
                pass
                self.locations[i]._fetch_instances()


        class WarmapLink(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageServer.AcWarmapGet.WarmapLink, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.linked_id = self._io.read_u8be()
                self.weight = self._io.read_f4be()


            def _fetch_instances(self):
                pass


        class WarmapLocation(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageServer.AcWarmapGet.WarmapLocation, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.id = self._io.read_u8be()
                self.x = self._io.read_f4be()
                self.y = self._io.read_f4be()


            def _fetch_instances(self):
                pass


        class WarmapSector(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageServer.AcWarmapGet.WarmapSector, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.sector_id = self._io.read_u8be()
                self.x = self._io.read_f4be()
                self.y = self._io.read_f4be()
                self.radius = self._io.read_f4be()
                self.num_links = self._io.read_u4be()
                self.links = []
                for i in range(self.num_links):
                    self.links.append(StarConflictPackageServer.AcWarmapGet.WarmapLink(self._io, self, self._root))



            def _fetch_instances(self):
                pass
                for i in range(len(self.links)):
                    pass
                    self.links[i]._fetch_instances()




    class AcWelcomeMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcWelcomeMsg, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_u1()
            self.msg = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")


        def _fetch_instances(self):
            pass


    class AcZoneCoordinatorGmCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcZoneCoordinatorGmCommand, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcZoneInstancesInfo(KaitaiStruct):
        """Field sequence from handler at 0x0822ef89 in OnRecieve dispatch.
        Reads: u8
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcZoneInstancesInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcZonesLuaActiveEventsUpdate(KaitaiStruct):
        """Active Lua event status for zones."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcZonesLuaActiveEventsUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.status = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class ZoneInstanceJoin(KaitaiStruct):
        """Zone instance notification. Two forms:
        Short (9B): echo + u24be(0) + u32be(instance_id) — join confirmation.
        Long (1097B): echo + u32be(0) + 3B(uid) + list of avatar names + player data.
        The long form is pushed once when a zone fills with players.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZoneInstanceJoin, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class ZoneKvData(KaitaiStruct):
        """Open-space zone K-V data (376B). cs0-encoded key-value stream.
        Header: u16be(0) + u8(count=3).
        Known keys: "tier" (zone tier/rank), "auras" (active auras), "bundles".
        Values follow each key; type encoding unknown.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZoneKvData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.header = self._io.read_bytes(2)
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class ZoneMembership(KaitaiStruct):
        """Zone membership event (26B). Contains two 3-byte player IDs.
        Constant bytes: u48be(0) + u16be(0x074b=1867) + u48be(0) + 3B(player_uid_low)
        + u48be(0) + u8(0x32=50) + u8(0x00).
        Appears when players enter/leave a zone.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZoneMembership, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.payload = self._io.read_bytes(24)


        def _fetch_instances(self):
            pass


    class ZoneMilitaryRank(KaitaiStruct):
        """Player military rank updates (49B). count=3 at byte 4, then
        3 cs0-keyed entries starting at byte 5. First key = "militaryRank".
        Values are bit-packed after each cs0 key (format not fully reversed).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZoneMilitaryRank, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.header = self._io.read_bytes(3)
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class ZonePlayerData(KaitaiStruct):
        """Player presence data. Two forms:
        Short (10B): echo + u24be(1) + 3B(player_uid_low) + u8(flags=0x03)
          — player online/join indicator.
        Long (78B): echo + u24be(0) + 3B(player_uid_low) + credits(u32be)
          + 64B bit-packed zone stats (damage dealt, kills, etc.) — full stats push.
        Appears after 0x0a00 (join) and 0x0900 (update) for the same player.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZonePlayerData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class ZonePlayerHealth(KaitaiStruct):
        """Zone player health/shield status (70B). Contains float32 values
        for each player in the zone. 0x3f800000 = 1.0 (full health/shield).
        Repeating entries: 3B player_id + float32 health + more fields.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZonePlayerHealth, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.padding = self._io.read_u4be()
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class ZonePlayerJoin(KaitaiStruct):
        """Player join notification in zone (13B).
        Layout: echo(2) + u24be(1) + 3B(player_uid_low) + 4B(flags/status).
        Flags: 0x3f800000 = float 1.0 = player is fully online/active.
        Preceded by 0x8000 (player stats dump) and followed by 0x0700 (presence).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZonePlayerJoin, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown_prefix = self._io.read_u4be()
            self.player_uid_low = self._io.read_bytes(3)
            self.status_flags = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class ZonePlayerList(KaitaiStruct):
        """Zone player list (283B). Structure not fully reversed."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZonePlayerList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class ZonePlayerStatus(KaitaiStruct):
        """Brief player status update in zone (19B).
        Layout: echo(2) + u24be(1) + 3B(constant=0x3b34b2) + u8(0) + u8(1)
        + u48be(0) + 4B(varying value).
        The varying 4B at the end changes with player activity (credits? HP?).
        All examples share the same 3B constant, suggesting this is tied to a
        specific player or zone instance.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZonePlayerStatus, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.prefix = self._io.read_u4be()
            self.player_uid_or_constant = self._io.read_bytes(3)
            self.padding = self._io.read_bytes(6)
            self.value = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class ZonePlayerUpdate(KaitaiStruct):
        """Player credits/status update in zone (13B).
        Layout: echo(2) + u24be(1) + 3B(player_uid_low) + 4B(value).
        The 3-byte player UID is the low 3 bytes of the player's full UID.
        Observed alongside zone_player_join for the same player.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZonePlayerUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown_prefix = self._io.read_u4be()
            self.player_uid_low = self._io.read_bytes(3)
            self.value = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class ZoneServer23(KaitaiStruct):
        """Server address notification for 23.x.x.x servers (30B).
        The type code 0x3233 = "23" ARE the first two bytes of the IP string,
        so the body starts mid-string at ".111.211.207\0".
        Layout: echo("23") + partial_ip(\0-terminated) + port(u16be)
                + field_a(u32be) + field_b(u32be) + field_c(u32be) + pad(u8).
        When in an active instance: field_a=0, field_b=instance_id, field_c=0.
        When idle: field_a=player_count, field_b=zone_id, field_c=capacity.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZoneServer23, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.ip_suffix = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.port = self._io.read_u2be()
            self.field_a = self._io.read_u4be()
            self.field_b = self._io.read_u4be()
            self.field_c = self._io.read_u4be()
            self.pad = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class ZoneServer89(KaitaiStruct):
        """Server address notification for 89.x.x.x servers (29B). Same
        structure as zone_server_23. Type 0x3839 = "89" = IP prefix.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZoneServer89, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.ip_suffix = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.port = self._io.read_u2be()
            self.field_a = self._io.read_u4be()
            self.field_b = self._io.read_u4be()
            self.field_c = self._io.read_u4be()


        def _fetch_instances(self):
            pass


    class ZoneStatsList(KaitaiStruct):
        """Zone session stat counters (119B). 5 bytes header + 6 cs0-keyed entries.
        Header: u16be(0) + u8(0) + u16be(count=6).
        Entries (cs0-encoded key + u16be value + 3B padding each):
          munitionTransfered, munitionPurchased, credits,
          and 3 more (names still cs-encoded; values bit-packed).
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.ZoneStatsList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.header = self._io.read_bytes(3)
            self.payload = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass



