# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


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
        elif _on == 139:
            pass
            self.body = StarConflictPackageServer.AcAttachYupAccount(self._io, self, self._root)
        elif _on == 14:
            pass
            self.body = StarConflictPackageServer.AcAvatarsSetActive(self._io, self, self._root)
        elif _on == 140:
            pass
            self.body = StarConflictPackageServer.AcAttachEmail(self._io, self, self._root)
        elif _on == 141:
            pass
            self.body = StarConflictPackageServer.AcLobbyList(self._io, self, self._root)
        elif _on == 142:
            pass
            self.body = StarConflictPackageServer.AcLobbyJoin(self._io, self, self._root)
        elif _on == 143:
            pass
            self.body = StarConflictPackageServer.AcLobbyCreate(self._io, self, self._root)
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
        elif _on == 251:
            pass
            self.body = StarConflictPackageServer.AcAdventures(self._io, self, self._root)
        elif _on == 252:
            pass
            self.body = StarConflictPackageServer.AcAdventureCancel(self._io, self, self._root)
        elif _on == 26:
            pass
            self.body = StarConflictPackageServer.AcQuestChange(self._io, self, self._root)
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
        elif _on == 139:
            pass
            self.body._fetch_instances()
        elif _on == 14:
            pass
            self.body._fetch_instances()
        elif _on == 140:
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
        elif _on == 251:
            pass
            self.body._fetch_instances()
        elif _on == 252:
            pass
            self.body._fetch_instances()
        elif _on == 26:
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
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAccountAuras, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAchievements(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAchievements, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcActivateResourceVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcActivateResourceVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAddAccountAura(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAddAccountAura, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAddThumbUp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAddThumbUp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdminCmd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdminCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdventureCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdventureCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdventures(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdventures, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdvertCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertDelete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdvertDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdvertGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertHeaderGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAdvertHeaderGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachEmail(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAttachEmail, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachSteamAccount(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAttachSteamAccount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachYupAccount(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAttachYupAccount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAutoPilotSpaceStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAutoPilotSpaceStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAutogenInvExtBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAutogenInvExtBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAvatarsSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcAvatarsSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattlePassUnlockLevel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattlePassUnlockLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotChangeVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattleSlotChangeVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotCheatChangeVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattleSlotCheatChangeVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotSwapVessels(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattleSlotSwapVessels, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlots(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBattleSlots, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyArcDlc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyArcDlc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyGold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyGold, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyProductFromAdvert(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyProductFromAdvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyTalentSet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcBuyTalentSet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCancelAccountAura(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcCancelAccountAura, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcChangePlayerNickname(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcChangePlayerNickname, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCheckYupPurchases(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcCheckYupPurchases, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcChooseStartingStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcChooseStartingStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanAssignEmblem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanAssignEmblem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanBankTransfer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanBankTransfer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeMotd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeMotd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeName(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeName, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeRecruiting(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeRecruiting, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeTag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanChangeTag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanHistoryGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanHistoryGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanJoinreqAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanJoinreqCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanJoinreqCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanListRecruiting(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanListRecruiting, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanQuestAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanQuestAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestCredentials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanRequestCredentials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanRequestDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanRequestProfile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanResourceConvert(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanResourceConvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanReviveInWar(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanReviveInWar, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanSetCivilianZone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanSetCivilianZone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanSetRole(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanSetRole, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBoostBuilding(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipBoostBuilding, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBoostRepairing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipBoostRepairing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBuild(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipBuild, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipFit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipFit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipRepair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipRepair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipSetCurrent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanShipSetCurrent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanUniverseMove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanUniverseMove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanUpgrade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanUpgrade, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanWarStart(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcClanWarStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCraftUpgradeItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcCraftUpgradeItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcDisassembleItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcDisassembleItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEmmChangeReady(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcEmmChangeReady, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnchantItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcEnchantItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnterMmQueue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcEnterMmQueue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnterTournament(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcEnterTournament, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcExchangeGold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcExchangeGold, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFactionRepReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFactionRepReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFinalizeSteamMtxn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFinalizeSteamMtxn, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFindAutogenItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFindAutogenItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsAcceptRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsAcceptRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsRejectRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsRejectRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsSendRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcFriendsSendRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGamesInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGamesInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetBlueprints(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetBlueprints, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetCraftResources(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetCraftResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetFbToken(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetFbToken, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetFreeSpaceSaveData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetFreeSpaceSaveData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


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
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetPunishments, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetUids(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetUids, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetUserdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetUserdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetVisitedFreeSpaceZones(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcGetVisitedFreeSpaceZones, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcInvExtBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcInvExtBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcKarmaReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcKarmaReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaderboardGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeaderboardGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaderboardGetDescs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeaderboardGetDescs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteDecline(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInviteDecline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamRequestNames(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeagueTeamRequestNames, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLearnBlueprint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLearnBlueprint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaveMmQueue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeaveMmQueue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaveTournament(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLeaveTournament, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLoadInitialPlayerData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLoadInitialPlayerData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupDelete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupJoinreqCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupJoinreqCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqReject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupJoinreqReject, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupModify(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyGroupModify, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyInvite(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyInvite, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyJoin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyJoin, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyModify(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyModify, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyStartGame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLobbyStartGame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLogFbEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcLogFbEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailAcknowledgeExpiration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailAcknowledgeExpiration, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailDeliver(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailDeliver, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMailSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMmInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMmInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMotd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMotd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMottosSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcMottosSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcObtainReferralKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcObtainReferralKey, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerArcBalance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerArcBalance, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerAutogenInventory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerAutogenInventory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerCredentials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerCredentials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerCredits(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerCredits, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerInventory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerInventory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerStats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerStats, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerVessels(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPlayerVessels, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPremiumBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPremiumBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPremiumInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcPremiumInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuestAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuestChange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestComplete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuestComplete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestCompleteAll(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuestCompleteAll, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuests(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcQuests, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReactOnAbandonedGame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcReactOnAbandonedGame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReferrals(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcReferrals, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRelatedQuestEnable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcRelatedQuestEnable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReportPlayer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcReportPlayer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRewardTutorial(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcRewardTutorial, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRewardedTutorials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcRewardedTutorials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSalvageItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSalvageItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSalvageItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSalvageItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellCraftResource(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellCraftResource, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellCraftResources(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellCraftResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSellVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSendEarlyPlayerLog(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSendEarlyPlayerLog, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcServerInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcServerInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetFbToken(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSetFbToken, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetReferrer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSetReferrer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetUserdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSetUserdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetVisitedZone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSetVisitedZone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcShipQuestChange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestEnd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcShipQuestEnd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestStart(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcShipQuestStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuests(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcShipQuests, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialIgnoreAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialIgnoreAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialIgnoreRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialIgnoreRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestFb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialSuggestFb, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestSteam(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialSuggestSteam, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestVk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialSuggestVk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialWatchAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialWatchAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialWatchRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSocialWatchRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSpaceStationsPopulation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSpaceStationsPopulation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadConvertToWing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadConvertToWing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteCancel(KaitaiStruct):
        """Cancel Squad invite."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteDecline(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInviteDecline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadReady(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSquadReady, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSteamUserInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSteamUserInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyGetNew(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSurveyGetNew, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyResults(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSurveyResults, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyVote(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcSurveyVote, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTaStatsSendTutorialEntter(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTaStatsSendTutorialEntter, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTaStatsSendTutorialExit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTaStatsSendTutorialExit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsAcquire(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTalentsAcquire, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsAssignSets(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTalentsAssignSets, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTalentsReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsUpdate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTalentsUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingAllow(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingAllow, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingCheck(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingCheck, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingReject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingReject, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingRequestToStudent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingRequestToStudent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingRequestToTeacher(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTeachingRequestToTeacher, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTitlesSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcTitlesSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUndockSpaceStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUndockSpaceStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUniverseCounters(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUniverseCounters, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUniverseGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUniverseGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUnlimPveDisablePlayerBuffs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUnlimPveDisablePlayerBuffs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUnlimPveUpgradePlayerLevel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUnlimPveUpgradePlayerLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpdateDlcOwnership(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUpdateDlcOwnership, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpdateYupPurchases(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUpdateYupPurchases, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpgradeAutogenItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUpgradeAutogenItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpgradeItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUpgradeItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUseBlueprint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUseBlueprint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserNotes(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUserNotes, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserNotesAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUserNotesAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_u1()
            self.uid = self._io.read_u8be()
            self.note = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")


        def _fetch_instances(self):
            pass


    class AcUserNotesDelete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUserNotesDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserProfileGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcUserProfileGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselActivateNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselActivateNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselAutogenDestroy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselAutogenDestroy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselAutogenDismantle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselAutogenDismantle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselBudgetActivate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselBudgetActivate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselBudgetLevelup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselBudgetLevelup, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselChangeEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeEquipMulti(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselChangeEquipMulti, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselChangeMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCheatChangeEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselCheatChangeEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCraft(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselCraft, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCustomElementsAcknowledgeExpiration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselCustomElementsAcknowledgeExpiration, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCustomElementsBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselCustomElementsBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselEquipment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselEquipment, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselExtractExp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselExtractExp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselFreeCustomElements(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselFreeCustomElements, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselLevelup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselLevelup, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRecraft(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRecraft, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRefillBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRefillBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRefillMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRefillMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRepair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRepair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRepairBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselRepairBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselStripEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselStripEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselStripImproperBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselStripImproperBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselTransferEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselTransferEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselTransferMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselTransferMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselUnlockNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcVesselUnlockNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcWarmapGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcWarmapGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


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
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcZoneInstancesInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcZoneInstancesInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcZonesLuaActiveEventsUpdate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageServer.AcZonesLuaActiveEventsUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass



