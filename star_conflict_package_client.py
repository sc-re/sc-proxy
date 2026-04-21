# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class StarConflictPackageClient(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(StarConflictPackageClient, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.packet_type = self._io.read_s2be()
        _on = self.packet_type
        if _on == 0:
            pass
            self.body = StarConflictPackageClient.AcLoadInitialPlayerData(self._io, self, self._root)
        elif _on == 1:
            pass
            self.body = StarConflictPackageClient.AcServerInfo(self._io, self, self._root)
        elif _on == 10:
            pass
            self.body = StarConflictPackageClient.AcPlayerCredits(self._io, self, self._root)
        elif _on == 100:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamInfo(self._io, self, self._root)
        elif _on == 101:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamCreate(self._io, self, self._root)
        elif _on == 102:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamInviteSend(self._io, self, self._root)
        elif _on == 103:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamInviteCancel(self._io, self, self._root)
        elif _on == 104:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamInviteAccept(self._io, self, self._root)
        elif _on == 105:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamKick(self._io, self, self._root)
        elif _on == 106:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamLeave(self._io, self, self._root)
        elif _on == 107:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamInviteDecline(self._io, self, self._root)
        elif _on == 108:
            pass
            self.body = StarConflictPackageClient.AcLeagueTeamRequestNames(self._io, self, self._root)
        elif _on == 109:
            pass
            self.body = StarConflictPackageClient.AcGetNicknames(self._io, self, self._root)
        elif _on == 11:
            pass
            self.body = StarConflictPackageClient.AcPlayerStats(self._io, self, self._root)
        elif _on == 110:
            pass
            self.body = StarConflictPackageClient.AcGetUids(self._io, self, self._root)
        elif _on == 111:
            pass
            self.body = StarConflictPackageClient.AcReportPlayer(self._io, self, self._root)
        elif _on == 112:
            pass
            self.body = StarConflictPackageClient.AcUpdateYupPurchases(self._io, self, self._root)
        elif _on == 113:
            pass
            self.body = StarConflictPackageClient.AcCheckYupPurchases(self._io, self, self._root)
        elif _on == 114:
            pass
            self.body = StarConflictPackageClient.AcUpdateDlcOwnership(self._io, self, self._root)
        elif _on == 115:
            pass
            self.body = StarConflictPackageClient.AcFriendsSendRequest(self._io, self, self._root)
        elif _on == 116:
            pass
            self.body = StarConflictPackageClient.AcFriendsAcceptRequest(self._io, self, self._root)
        elif _on == 117:
            pass
            self.body = StarConflictPackageClient.AcFriendsRejectRequest(self._io, self, self._root)
        elif _on == 118:
            pass
            self.body = StarConflictPackageClient.AcFriendsRemove(self._io, self, self._root)
        elif _on == 119:
            pass
            self.body = StarConflictPackageClient.AcFriendsList(self._io, self, self._root)
        elif _on == 12:
            pass
            self.body = StarConflictPackageClient.AcPlayerArcBalance(self._io, self, self._root)
        elif _on == 120:
            pass
            self.body = StarConflictPackageClient.AcSocialIgnoreAdd(self._io, self, self._root)
        elif _on == 121:
            pass
            self.body = StarConflictPackageClient.AcSocialIgnoreRemove(self._io, self, self._root)
        elif _on == 122:
            pass
            self.body = StarConflictPackageClient.AcSocialWatchAdd(self._io, self, self._root)
        elif _on == 123:
            pass
            self.body = StarConflictPackageClient.AcSocialWatchRemove(self._io, self, self._root)
        elif _on == 124:
            pass
            self.body = StarConflictPackageClient.AcSocialSuggestSteam(self._io, self, self._root)
        elif _on == 125:
            pass
            self.body = StarConflictPackageClient.AcSocialSuggestFb(self._io, self, self._root)
        elif _on == 126:
            pass
            self.body = StarConflictPackageClient.AcSocialSuggestVk(self._io, self, self._root)
        elif _on == 127:
            pass
            self.body = StarConflictPackageClient.AcTeachingList(self._io, self, self._root)
        elif _on == 128:
            pass
            self.body = StarConflictPackageClient.AcTeachingRequestToTeacher(self._io, self, self._root)
        elif _on == 129:
            pass
            self.body = StarConflictPackageClient.AcTeachingRequestToStudent(self._io, self, self._root)
        elif _on == 13:
            pass
            self.body = StarConflictPackageClient.AcTitlesSetActive(self._io, self, self._root)
        elif _on == 130:
            pass
            self.body = StarConflictPackageClient.AcTeachingAccept(self._io, self, self._root)
        elif _on == 131:
            pass
            self.body = StarConflictPackageClient.AcTeachingReject(self._io, self, self._root)
        elif _on == 132:
            pass
            self.body = StarConflictPackageClient.AcTeachingCheck(self._io, self, self._root)
        elif _on == 133:
            pass
            self.body = StarConflictPackageClient.AcTeachingAllow(self._io, self, self._root)
        elif _on == 134:
            pass
            self.body = StarConflictPackageClient.AcReferrals(self._io, self, self._root)
        elif _on == 135:
            pass
            self.body = StarConflictPackageClient.AcSetReferrer(self._io, self, self._root)
        elif _on == 136:
            pass
            self.body = StarConflictPackageClient.AcObtainReferralKey(self._io, self, self._root)
        elif _on == 137:
            pass
            self.body = StarConflictPackageClient.AcAttachSteamAccount(self._io, self, self._root)
        elif _on == 138:
            pass
            self.body = StarConflictPackageClient.AcFinalizeSteamMtxn(self._io, self, self._root)
        elif _on == 139:
            pass
            self.body = StarConflictPackageClient.AcAttachYupAccount(self._io, self, self._root)
        elif _on == 14:
            pass
            self.body = StarConflictPackageClient.AcAvatarsSetActive(self._io, self, self._root)
        elif _on == 140:
            pass
            self.body = StarConflictPackageClient.AcAttachEmail(self._io, self, self._root)
        elif _on == 141:
            pass
            self.body = StarConflictPackageClient.AcLobbyList(self._io, self, self._root)
        elif _on == 142:
            pass
            self.body = StarConflictPackageClient.AcLobbyJoin(self._io, self, self._root)
        elif _on == 143:
            pass
            self.body = StarConflictPackageClient.AcLobbyCreate(self._io, self, self._root)
        elif _on == 144:
            pass
            self.body = StarConflictPackageClient.AcLobbyInfo(self._io, self, self._root)
        elif _on == 145:
            pass
            self.body = StarConflictPackageClient.AcLobbyKick(self._io, self, self._root)
        elif _on == 146:
            pass
            self.body = StarConflictPackageClient.AcLobbyLeave(self._io, self, self._root)
        elif _on == 147:
            pass
            self.body = StarConflictPackageClient.AcLobbyInvite(self._io, self, self._root)
        elif _on == 148:
            pass
            self.body = StarConflictPackageClient.AcLobbyModify(self._io, self, self._root)
        elif _on == 149:
            pass
            self.body = StarConflictPackageClient.AcLobbyStartGame(self._io, self, self._root)
        elif _on == 15:
            pass
            self.body = StarConflictPackageClient.AcMottosSetActive(self._io, self, self._root)
        elif _on == 150:
            pass
            self.body = StarConflictPackageClient.AcLobbyGroupList(self._io, self, self._root)
        elif _on == 151:
            pass
            self.body = StarConflictPackageClient.AcLobbyGroupInfo(self._io, self, self._root)
        elif _on == 152:
            pass
            self.body = StarConflictPackageClient.AcLobbyGroupCreate(self._io, self, self._root)
        elif _on == 153:
            pass
            self.body = StarConflictPackageClient.AcLobbyGroupModify(self._io, self, self._root)
        elif _on == 154:
            pass
            self.body = StarConflictPackageClient.AcLobbyGroupDelete(self._io, self, self._root)
        elif _on == 155:
            pass
            self.body = StarConflictPackageClient.AcLobbyGroupJoinreqCreate(self._io, self, self._root)
        elif _on == 156:
            pass
            self.body = StarConflictPackageClient.AcLobbyGroupJoinreqCancel(self._io, self, self._root)
        elif _on == 157:
            pass
            self.body = StarConflictPackageClient.AcLobbyGroupJoinreqReject(self._io, self, self._root)
        elif _on == 158:
            pass
            self.body = StarConflictPackageClient.AcClanRequestCredentials(self._io, self, self._root)
        elif _on == 159:
            pass
            self.body = StarConflictPackageClient.AcClanRequestDesc(self._io, self, self._root)
        elif _on == 16:
            pass
            self.body = StarConflictPackageClient.AcChooseStartingStation(self._io, self, self._root)
        elif _on == 160:
            pass
            self.body = StarConflictPackageClient.AcClanRequestProfile(self._io, self, self._root)
        elif _on == 161:
            pass
            self.body = StarConflictPackageClient.AcClanJoinreqCreate(self._io, self, self._root)
        elif _on == 162:
            pass
            self.body = StarConflictPackageClient.AcClanJoinreqCancel(self._io, self, self._root)
        elif _on == 163:
            pass
            self.body = StarConflictPackageClient.AcClanJoinreqAccept(self._io, self, self._root)
        elif _on == 164:
            pass
            self.body = StarConflictPackageClient.AcClanInviteSend(self._io, self, self._root)
        elif _on == 165:
            pass
            self.body = StarConflictPackageClient.AcClanInviteAccept(self._io, self, self._root)
        elif _on == 166:
            pass
            self.body = StarConflictPackageClient.AcClanInviteCancel(self._io, self, self._root)
        elif _on == 167:
            pass
            self.body = StarConflictPackageClient.AcClanKick(self._io, self, self._root)
        elif _on == 168:
            pass
            self.body = StarConflictPackageClient.AcClanLeave(self._io, self, self._root)
        elif _on == 169:
            pass
            self.body = StarConflictPackageClient.AcClanSetRole(self._io, self, self._root)
        elif _on == 17:
            pass
            self.body = StarConflictPackageClient.AcChangePlayerNickname(self._io, self, self._root)
        elif _on == 170:
            pass
            self.body = StarConflictPackageClient.AcClanChangeMotd(self._io, self, self._root)
        elif _on == 171:
            pass
            self.body = StarConflictPackageClient.AcClanChangeDesc(self._io, self, self._root)
        elif _on == 172:
            pass
            self.body = StarConflictPackageClient.AcClanChangeRecruiting(self._io, self, self._root)
        elif _on == 173:
            pass
            self.body = StarConflictPackageClient.AcClanResourceConvert(self._io, self, self._root)
        elif _on == 174:
            pass
            self.body = StarConflictPackageClient.AcClanShipBuild(self._io, self, self._root)
        elif _on == 175:
            pass
            self.body = StarConflictPackageClient.AcClanShipBoostBuilding(self._io, self, self._root)
        elif _on == 176:
            pass
            self.body = StarConflictPackageClient.AcClanShipRepair(self._io, self, self._root)
        elif _on == 177:
            pass
            self.body = StarConflictPackageClient.AcClanShipBoostRepairing(self._io, self, self._root)
        elif _on == 178:
            pass
            self.body = StarConflictPackageClient.AcClanShipFit(self._io, self, self._root)
        elif _on == 179:
            pass
            self.body = StarConflictPackageClient.AcClanShipSetCurrent(self._io, self, self._root)
        elif _on == 18:
            pass
            self.body = StarConflictPackageClient.AcSteamUserInfo(self._io, self, self._root)
        elif _on == 180:
            pass
            self.body = StarConflictPackageClient.AcClanUniverseMove(self._io, self, self._root)
        elif _on == 181:
            pass
            self.body = StarConflictPackageClient.AcClanSetCivilianZone(self._io, self, self._root)
        elif _on == 182:
            pass
            self.body = StarConflictPackageClient.AcClanReviveInWar(self._io, self, self._root)
        elif _on == 183:
            pass
            self.body = StarConflictPackageClient.AcClanWarStart(self._io, self, self._root)
        elif _on == 184:
            pass
            self.body = StarConflictPackageClient.AcClanQuestAccept(self._io, self, self._root)
        elif _on == 185:
            pass
            self.body = StarConflictPackageClient.AcClanCreate(self._io, self, self._root)
        elif _on == 186:
            pass
            self.body = StarConflictPackageClient.AcClanUpgrade(self._io, self, self._root)
        elif _on == 187:
            pass
            self.body = StarConflictPackageClient.AcClanChangeName(self._io, self, self._root)
        elif _on == 188:
            pass
            self.body = StarConflictPackageClient.AcClanChangeTag(self._io, self, self._root)
        elif _on == 189:
            pass
            self.body = StarConflictPackageClient.AcClanAssignEmblem(self._io, self, self._root)
        elif _on == 19:
            pass
            self.body = StarConflictPackageClient.AcPremiumInfo(self._io, self, self._root)
        elif _on == 190:
            pass
            self.body = StarConflictPackageClient.AcClanBankTransfer(self._io, self, self._root)
        elif _on == 191:
            pass
            self.body = StarConflictPackageClient.AcClanListRecruiting(self._io, self, self._root)
        elif _on == 192:
            pass
            self.body = StarConflictPackageClient.AcClanHistoryGet(self._io, self, self._root)
        elif _on == 193:
            pass
            self.body = StarConflictPackageClient.AcRelatedQuestEnable(self._io, self, self._root)
        elif _on == 194:
            pass
            self.body = StarConflictPackageClient.AcUserProfileGet(self._io, self, self._root)
        elif _on == 195:
            pass
            self.body = StarConflictPackageClient.AcAchievements(self._io, self, self._root)
        elif _on == 196:
            pass
            self.body = StarConflictPackageClient.AcAdminCmd(self._io, self, self._root)
        elif _on == 197:
            pass
            self.body = StarConflictPackageClient.AcGamesInfo(self._io, self, self._root)
        elif _on == 198:
            pass
            self.body = StarConflictPackageClient.AcZoneInstancesInfo(self._io, self, self._root)
        elif _on == 199:
            pass
            self.body = StarConflictPackageClient.AcGetPunishments(self._io, self, self._root)
        elif _on == 2:
            pass
            self.body = StarConflictPackageClient.AcEnterMmQueue(self._io, self, self._root)
        elif _on == 20:
            pass
            self.body = StarConflictPackageClient.AcPremiumBuy(self._io, self, self._root)
        elif _on == 200:
            pass
            self.body = StarConflictPackageClient.AcWelcomeMsg(self._io, self, self._root)
        elif _on == 201:
            pass
            self.body = StarConflictPackageClient.AcMotd(self._io, self, self._root)
        elif _on == 202:
            pass
            self.body = StarConflictPackageClient.AcSurveyGetNew(self._io, self, self._root)
        elif _on == 203:
            pass
            self.body = StarConflictPackageClient.AcSurveyVote(self._io, self, self._root)
        elif _on == 204:
            pass
            self.body = StarConflictPackageClient.AcSurveyResults(self._io, self, self._root)
        elif _on == 205:
            pass
            self.body = StarConflictPackageClient.AcUniverseGet(self._io, self, self._root)
        elif _on == 206:
            pass
            self.body = StarConflictPackageClient.AcUniverseCounters(self._io, self, self._root)
        elif _on == 207:
            pass
            self.body = StarConflictPackageClient.AcWarmapGet(self._io, self, self._root)
        elif _on == 208:
            pass
            self.body = StarConflictPackageClient.AcMailGet(self._io, self, self._root)
        elif _on == 209:
            pass
            self.body = StarConflictPackageClient.AcMailDeliver(self._io, self, self._root)
        elif _on == 21:
            pass
            self.body = StarConflictPackageClient.AcAccountAuras(self._io, self, self._root)
        elif _on == 210:
            pass
            self.body = StarConflictPackageClient.AcMailSend(self._io, self, self._root)
        elif _on == 211:
            pass
            self.body = StarConflictPackageClient.AcMailRemove(self._io, self, self._root)
        elif _on == 212:
            pass
            self.body = StarConflictPackageClient.AcMailAcknowledgeExpiration(self._io, self, self._root)
        elif _on == 213:
            pass
            self.body = StarConflictPackageClient.AcSendEarlyPlayerLog(self._io, self, self._root)
        elif _on == 214:
            pass
            self.body = StarConflictPackageClient.AcAutoPilotSpaceStation(self._io, self, self._root)
        elif _on == 215:
            pass
            self.body = StarConflictPackageClient.AcUndockSpaceStation(self._io, self, self._root)
        elif _on == 216:
            pass
            self.body = StarConflictPackageClient.AcSetVisitedZone(self._io, self, self._root)
        elif _on == 217:
            pass
            self.body = StarConflictPackageClient.AcZoneCoordinatorGmCommand(self._io, self, self._root)
        elif _on == 218:
            pass
            self.body = StarConflictPackageClient.AcSpaceStationsPopulation(self._io, self, self._root)
        elif _on == 219:
            pass
            self.body = StarConflictPackageClient.AcKarmaReset(self._io, self, self._root)
        elif _on == 22:
            pass
            self.body = StarConflictPackageClient.AcAddAccountAura(self._io, self, self._root)
        elif _on == 220:
            pass
            self.body = StarConflictPackageClient.AcFactionRepReset(self._io, self, self._root)
        elif _on == 221:
            pass
            self.body = StarConflictPackageClient.AcLeaderboardGet(self._io, self, self._root)
        elif _on == 222:
            pass
            self.body = StarConflictPackageClient.AcLeaderboardGetDescs(self._io, self, self._root)
        elif _on == 223:
            pass
            self.body = StarConflictPackageClient.AcSetFbToken(self._io, self, self._root)
        elif _on == 224:
            pass
            self.body = StarConflictPackageClient.AcGetFbToken(self._io, self, self._root)
        elif _on == 225:
            pass
            self.body = StarConflictPackageClient.AcLogFbEvent(self._io, self, self._root)
        elif _on == 226:
            pass
            self.body = StarConflictPackageClient.AcGetCraftResources(self._io, self, self._root)
        elif _on == 227:
            pass
            self.body = StarConflictPackageClient.AcUseBlueprint(self._io, self, self._root)
        elif _on == 228:
            pass
            self.body = StarConflictPackageClient.AcSellCraftResource(self._io, self, self._root)
        elif _on == 229:
            pass
            self.body = StarConflictPackageClient.AcSellCraftResources(self._io, self, self._root)
        elif _on == 23:
            pass
            self.body = StarConflictPackageClient.AcCancelAccountAura(self._io, self, self._root)
        elif _on == 230:
            pass
            self.body = StarConflictPackageClient.AcGetBlueprints(self._io, self, self._root)
        elif _on == 231:
            pass
            self.body = StarConflictPackageClient.AcLearnBlueprint(self._io, self, self._root)
        elif _on == 232:
            pass
            self.body = StarConflictPackageClient.AcGetFreeSpaceSaveData(self._io, self, self._root)
        elif _on == 233:
            pass
            self.body = StarConflictPackageClient.AcDisassembleItem(self._io, self, self._root)
        elif _on == 234:
            pass
            self.body = StarConflictPackageClient.AcAddThumbUp(self._io, self, self._root)
        elif _on == 235:
            pass
            self.body = StarConflictPackageClient.AcGetVisitedFreeSpaceZones(self._io, self, self._root)
        elif _on == 236:
            pass
            self.body = StarConflictPackageClient.AcAdvertCreate(self._io, self, self._root)
        elif _on == 237:
            pass
            self.body = StarConflictPackageClient.AcAdvertDelete(self._io, self, self._root)
        elif _on == 238:
            pass
            self.body = StarConflictPackageClient.AcAdvertHeaderGet(self._io, self, self._root)
        elif _on == 239:
            pass
            self.body = StarConflictPackageClient.AcAdvertGet(self._io, self, self._root)
        elif _on == 24:
            pass
            self.body = StarConflictPackageClient.AcQuests(self._io, self, self._root)
        elif _on == 240:
            pass
            self.body = StarConflictPackageClient.AcBuyProductFromAdvert(self._io, self, self._root)
        elif _on == 241:
            pass
            self.body = StarConflictPackageClient.AcEmmChangeReady(self._io, self, self._root)
        elif _on == 242:
            pass
            self.body = StarConflictPackageClient.AcUnlimPveUpgradePlayerLevel(self._io, self, self._root)
        elif _on == 243:
            pass
            self.body = StarConflictPackageClient.AcUnlimPveDisablePlayerBuffs(self._io, self, self._root)
        elif _on == 244:
            pass
            self.body = StarConflictPackageClient.AcTaStatsSendTutorialEntter(self._io, self, self._root)
        elif _on == 245:
            pass
            self.body = StarConflictPackageClient.AcTaStatsSendTutorialExit(self._io, self, self._root)
        elif _on == 246:
            pass
            self.body = StarConflictPackageClient.AcUserNotes(self._io, self, self._root)
        elif _on == 247:
            pass
            self.body = StarConflictPackageClient.AcUserNotesAdd(self._io, self, self._root)
        elif _on == 248:
            pass
            self.body = StarConflictPackageClient.AcUserNotesDelete(self._io, self, self._root)
        elif _on == 249:
            pass
            self.body = StarConflictPackageClient.AcBattlePassUnlockLevel(self._io, self, self._root)
        elif _on == 25:
            pass
            self.body = StarConflictPackageClient.AcQuestAccept(self._io, self, self._root)
        elif _on == 250:
            pass
            self.body = StarConflictPackageClient.AcZonesLuaActiveEventsUpdate(self._io, self, self._root)
        elif _on == 251:
            pass
            self.body = StarConflictPackageClient.AcAdventures(self._io, self, self._root)
        elif _on == 252:
            pass
            self.body = StarConflictPackageClient.AcAdventureCancel(self._io, self, self._root)
        elif _on == 26:
            pass
            self.body = StarConflictPackageClient.AcQuestChange(self._io, self, self._root)
        elif _on == 27:
            pass
            self.body = StarConflictPackageClient.AcQuestComplete(self._io, self, self._root)
        elif _on == 28:
            pass
            self.body = StarConflictPackageClient.AcQuestCompleteAll(self._io, self, self._root)
        elif _on == 29:
            pass
            self.body = StarConflictPackageClient.AcShipQuests(self._io, self, self._root)
        elif _on == 3:
            pass
            self.body = StarConflictPackageClient.AcLeaveMmQueue(self._io, self, self._root)
        elif _on == 30:
            pass
            self.body = StarConflictPackageClient.AcShipQuestStart(self._io, self, self._root)
        elif _on == 31:
            pass
            self.body = StarConflictPackageClient.AcShipQuestChange(self._io, self, self._root)
        elif _on == 32:
            pass
            self.body = StarConflictPackageClient.AcShipQuestEnd(self._io, self, self._root)
        elif _on == 33:
            pass
            self.body = StarConflictPackageClient.AcRewardedTutorials(self._io, self, self._root)
        elif _on == 34:
            pass
            self.body = StarConflictPackageClient.AcRewardTutorial(self._io, self, self._root)
        elif _on == 35:
            pass
            self.body = StarConflictPackageClient.AcPlayerInventory(self._io, self, self._root)
        elif _on == 36:
            pass
            self.body = StarConflictPackageClient.AcPlayerAutogenInventory(self._io, self, self._root)
        elif _on == 37:
            pass
            self.body = StarConflictPackageClient.AcPlayerVessels(self._io, self, self._root)
        elif _on == 38:
            pass
            self.body = StarConflictPackageClient.AcVesselEquipment(self._io, self, self._root)
        elif _on == 39:
            pass
            self.body = StarConflictPackageClient.AcBuyItem(self._io, self, self._root)
        elif _on == 4:
            pass
            self.body = StarConflictPackageClient.AcMmInfo(self._io, self, self._root)
        elif _on == 40:
            pass
            self.body = StarConflictPackageClient.AcSellItem(self._io, self, self._root)
        elif _on == 41:
            pass
            self.body = StarConflictPackageClient.AcSellItems(self._io, self, self._root)
        elif _on == 42:
            pass
            self.body = StarConflictPackageClient.AcEnchantItem(self._io, self, self._root)
        elif _on == 43:
            pass
            self.body = StarConflictPackageClient.AcSalvageItem(self._io, self, self._root)
        elif _on == 44:
            pass
            self.body = StarConflictPackageClient.AcSalvageItems(self._io, self, self._root)
        elif _on == 45:
            pass
            self.body = StarConflictPackageClient.AcUpgradeItems(self._io, self, self._root)
        elif _on == 46:
            pass
            self.body = StarConflictPackageClient.AcUpgradeAutogenItem(self._io, self, self._root)
        elif _on == 47:
            pass
            self.body = StarConflictPackageClient.AcCraftUpgradeItem(self._io, self, self._root)
        elif _on == 48:
            pass
            self.body = StarConflictPackageClient.AcFindAutogenItem(self._io, self, self._root)
        elif _on == 49:
            pass
            self.body = StarConflictPackageClient.AcActivateResourceVessel(self._io, self, self._root)
        elif _on == 5:
            pass
            self.body = StarConflictPackageClient.AcEnterTournament(self._io, self, self._root)
        elif _on == 50:
            pass
            self.body = StarConflictPackageClient.AcSellVessel(self._io, self, self._root)
        elif _on == 51:
            pass
            self.body = StarConflictPackageClient.AcVesselChangeEquip(self._io, self, self._root)
        elif _on == 52:
            pass
            self.body = StarConflictPackageClient.AcVesselChangeEquipMulti(self._io, self, self._root)
        elif _on == 53:
            pass
            self.body = StarConflictPackageClient.AcVesselCheatChangeEquip(self._io, self, self._root)
        elif _on == 54:
            pass
            self.body = StarConflictPackageClient.AcVesselTransferEquip(self._io, self, self._root)
        elif _on == 55:
            pass
            self.body = StarConflictPackageClient.AcVesselStripEquip(self._io, self, self._root)
        elif _on == 56:
            pass
            self.body = StarConflictPackageClient.AcVesselChangeMunition(self._io, self, self._root)
        elif _on == 57:
            pass
            self.body = StarConflictPackageClient.AcVesselRefillMunition(self._io, self, self._root)
        elif _on == 58:
            pass
            self.body = StarConflictPackageClient.AcVesselTransferMunition(self._io, self, self._root)
        elif _on == 59:
            pass
            self.body = StarConflictPackageClient.AcVesselAutogenDestroy(self._io, self, self._root)
        elif _on == 6:
            pass
            self.body = StarConflictPackageClient.AcLeaveTournament(self._io, self, self._root)
        elif _on == 60:
            pass
            self.body = StarConflictPackageClient.AcVesselAutogenDismantle(self._io, self, self._root)
        elif _on == 61:
            pass
            self.body = StarConflictPackageClient.AcVesselExtractExp(self._io, self, self._root)
        elif _on == 62:
            pass
            self.body = StarConflictPackageClient.AcVesselLevelup(self._io, self, self._root)
        elif _on == 63:
            pass
            self.body = StarConflictPackageClient.AcVesselRepair(self._io, self, self._root)
        elif _on == 64:
            pass
            self.body = StarConflictPackageClient.AcVesselRepairBattle(self._io, self, self._root)
        elif _on == 65:
            pass
            self.body = StarConflictPackageClient.AcVesselRefillBattle(self._io, self, self._root)
        elif _on == 66:
            pass
            self.body = StarConflictPackageClient.AcVesselStripImproperBattle(self._io, self, self._root)
        elif _on == 67:
            pass
            self.body = StarConflictPackageClient.AcVesselFreeCustomElements(self._io, self, self._root)
        elif _on == 68:
            pass
            self.body = StarConflictPackageClient.AcVesselCustomElementsBuy(self._io, self, self._root)
        elif _on == 69:
            pass
            self.body = StarConflictPackageClient.AcVesselCustomElementsAcknowledgeExpiration(self._io, self, self._root)
        elif _on == 7:
            pass
            self.body = StarConflictPackageClient.AcGetUserdata(self._io, self, self._root)
        elif _on == 70:
            pass
            self.body = StarConflictPackageClient.AcVesselCraft(self._io, self, self._root)
        elif _on == 71:
            pass
            self.body = StarConflictPackageClient.AcVesselRecraft(self._io, self, self._root)
        elif _on == 72:
            pass
            self.body = StarConflictPackageClient.AcVesselBudgetLevelup(self._io, self, self._root)
        elif _on == 73:
            pass
            self.body = StarConflictPackageClient.AcVesselBudgetActivate(self._io, self, self._root)
        elif _on == 74:
            pass
            self.body = StarConflictPackageClient.AcVesselUnlockNode(self._io, self, self._root)
        elif _on == 75:
            pass
            self.body = StarConflictPackageClient.AcVesselActivateNode(self._io, self, self._root)
        elif _on == 76:
            pass
            self.body = StarConflictPackageClient.AcBattleSlots(self._io, self, self._root)
        elif _on == 77:
            pass
            self.body = StarConflictPackageClient.AcBattleSlotChangeVessel(self._io, self, self._root)
        elif _on == 78:
            pass
            self.body = StarConflictPackageClient.AcBattleSlotSwapVessels(self._io, self, self._root)
        elif _on == 79:
            pass
            self.body = StarConflictPackageClient.AcBattleSlotCheatChangeVessel(self._io, self, self._root)
        elif _on == 8:
            pass
            self.body = StarConflictPackageClient.AcSetUserdata(self._io, self, self._root)
        elif _on == 80:
            pass
            self.body = StarConflictPackageClient.AcInvExtBuy(self._io, self, self._root)
        elif _on == 81:
            pass
            self.body = StarConflictPackageClient.AcAutogenInvExtBuy(self._io, self, self._root)
        elif _on == 82:
            pass
            self.body = StarConflictPackageClient.AcExchangeGold(self._io, self, self._root)
        elif _on == 83:
            pass
            self.body = StarConflictPackageClient.AcBuyGold(self._io, self, self._root)
        elif _on == 84:
            pass
            self.body = StarConflictPackageClient.AcBuyArcDlc(self._io, self, self._root)
        elif _on == 85:
            pass
            self.body = StarConflictPackageClient.AcTalentsAcquire(self._io, self, self._root)
        elif _on == 86:
            pass
            self.body = StarConflictPackageClient.AcTalentsUpdate(self._io, self, self._root)
        elif _on == 87:
            pass
            self.body = StarConflictPackageClient.AcTalentsReset(self._io, self, self._root)
        elif _on == 88:
            pass
            self.body = StarConflictPackageClient.AcTalentsAssignSets(self._io, self, self._root)
        elif _on == 89:
            pass
            self.body = StarConflictPackageClient.AcBuyTalentSet(self._io, self, self._root)
        elif _on == 9:
            pass
            self.body = StarConflictPackageClient.AcPlayerCredentials(self._io, self, self._root)
        elif _on == 90:
            pass
            self.body = StarConflictPackageClient.AcReactOnAbandonedGame(self._io, self, self._root)
        elif _on == 91:
            pass
            self.body = StarConflictPackageClient.AcSquadInfo(self._io, self, self._root)
        elif _on == 92:
            pass
            self.body = StarConflictPackageClient.AcSquadInviteAccept(self._io, self, self._root)
        elif _on == 93:
            pass
            self.body = StarConflictPackageClient.AcSquadInviteDecline(self._io, self, self._root)
        elif _on == 94:
            pass
            self.body = StarConflictPackageClient.AcSquadLeave(self._io, self, self._root)
        elif _on == 95:
            pass
            self.body = StarConflictPackageClient.AcSquadInviteSend(self._io, self, self._root)
        elif _on == 96:
            pass
            self.body = StarConflictPackageClient.AcSquadInviteCancel(self._io, self, self._root)
        elif _on == 97:
            pass
            self.body = StarConflictPackageClient.AcSquadKick(self._io, self, self._root)
        elif _on == 98:
            pass
            self.body = StarConflictPackageClient.AcSquadReady(self._io, self, self._root)
        elif _on == 99:
            pass
            self.body = StarConflictPackageClient.AcSquadConvertToWing(self._io, self, self._root)


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
            super(StarConflictPackageClient.AcAccountAuras, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAchievements(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAchievements, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcActivateResourceVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcActivateResourceVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAddAccountAura(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAddAccountAura, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAddThumbUp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAddThumbUp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdminCmd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAdminCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdventureCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAdventureCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdventures(KaitaiStruct):
        """Empty request, server responds with adventures list."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAdventures, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcAdvertCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAdvertCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertDelete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAdvertDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAdvertGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertHeaderGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAdvertHeaderGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachEmail(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAttachEmail, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachSteamAccount(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAttachSteamAccount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachYupAccount(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAttachYupAccount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAutoPilotSpaceStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAutoPilotSpaceStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAutogenInvExtBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAutogenInvExtBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAvatarsSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcAvatarsSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattlePassUnlockLevel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBattlePassUnlockLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotChangeVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBattleSlotChangeVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotCheatChangeVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBattleSlotCheatChangeVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotSwapVessels(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBattleSlotSwapVessels, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlots(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBattleSlots, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyArcDlc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBuyArcDlc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyGold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBuyGold, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBuyItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyProductFromAdvert(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBuyProductFromAdvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyTalentSet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcBuyTalentSet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCancelAccountAura(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcCancelAccountAura, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcChangePlayerNickname(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcChangePlayerNickname, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCheckYupPurchases(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcCheckYupPurchases, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcChooseStartingStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcChooseStartingStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanAssignEmblem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanAssignEmblem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanBankTransfer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanBankTransfer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanChangeDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeMotd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanChangeMotd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeName(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanChangeName, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeRecruiting(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanChangeRecruiting, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeTag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanChangeTag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanHistoryGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanHistoryGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanJoinreqAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanJoinreqCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanJoinreqCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanListRecruiting(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanListRecruiting, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanQuestAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanQuestAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestCredentials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanRequestCredentials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestDesc(KaitaiStruct):
        """Empty request, server responds with clan description."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanRequestDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcClanRequestProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanRequestProfile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanResourceConvert(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanResourceConvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanReviveInWar(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanReviveInWar, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanSetCivilianZone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanSetCivilianZone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanSetRole(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanSetRole, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBoostBuilding(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanShipBoostBuilding, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBoostRepairing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanShipBoostRepairing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBuild(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanShipBuild, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipFit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanShipFit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipRepair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanShipRepair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipSetCurrent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanShipSetCurrent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanUniverseMove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanUniverseMove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanUpgrade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanUpgrade, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanWarStart(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcClanWarStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCraftUpgradeItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcCraftUpgradeItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcDisassembleItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcDisassembleItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEmmChangeReady(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcEmmChangeReady, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnchantItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcEnchantItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnterMmQueue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcEnterMmQueue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnterTournament(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcEnterTournament, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcExchangeGold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcExchangeGold, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFactionRepReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcFactionRepReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFinalizeSteamMtxn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcFinalizeSteamMtxn, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFindAutogenItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcFindAutogenItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsAcceptRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcFriendsAcceptRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcFriendsList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsRejectRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcFriendsRejectRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcFriendsRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsSendRequest(KaitaiStruct):
        """Empty request, initiates friend request flow."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcFriendsSendRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcGamesInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGamesInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetBlueprints(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGetBlueprints, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetCraftResources(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGetCraftResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetFbToken(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGetFbToken, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetFreeSpaceSaveData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGetFreeSpaceSaveData, self).__init__(_io)
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
            super(StarConflictPackageClient.AcGetNicknames, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_u2be()
            self.num_uids = self._io.read_u2be()
            self.uids = []
            for i in range(self.num_uids):
                self.uids.append(StarConflictPackageClient.AcGetNicknames.Uid(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.uids)):
                pass
                self.uids[i]._fetch_instances()


        class Uid(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackageClient.AcGetNicknames.Uid, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.uid = self._io.read_u8be()


            def _fetch_instances(self):
                pass



    class AcGetPunishments(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGetPunishments, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetUids(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGetUids, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetUserdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGetUserdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetVisitedFreeSpaceZones(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcGetVisitedFreeSpaceZones, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcInvExtBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcInvExtBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcKarmaReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcKarmaReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaderboardGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeaderboardGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaderboardGetDescs(KaitaiStruct):
        """Empty request, server responds with leaderboard descriptors."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeaderboardGetDescs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcLeagueTeamCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInfo(KaitaiStruct):
        """Empty request, server responds with league team info."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteDecline(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamInviteDecline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamRequestNames(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeagueTeamRequestNames, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLearnBlueprint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLearnBlueprint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaveMmQueue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeaveMmQueue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaveTournament(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLeaveTournament, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLoadInitialPlayerData(KaitaiStruct):
        """Initial player data request; 6 bytes when sent with session credentials, empty for keepalive."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLoadInitialPlayerData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.session_data = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass


    class AcLobbyCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyGroupCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupDelete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyGroupDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyGroupInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyGroupJoinreqCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyGroupJoinreqCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqReject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyGroupJoinreqReject, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyGroupList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupModify(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyGroupModify, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyInfo(KaitaiStruct):
        """Empty request, server responds with lobby info."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcLobbyInvite(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyInvite, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyJoin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyJoin, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyModify(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyModify, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyStartGame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLobbyStartGame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLogFbEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcLogFbEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailAcknowledgeExpiration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcMailAcknowledgeExpiration, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailDeliver(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcMailDeliver, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailGet(KaitaiStruct):
        """Client requests mailbox contents in specified language."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcMailGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.lang = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcMailRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcMailRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcMailSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMmInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcMmInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMotd(KaitaiStruct):
        """Client requests MOTD in specified language."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcMotd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.lang = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcMottosSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcMottosSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcObtainReferralKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcObtainReferralKey, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerArcBalance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPlayerArcBalance, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerAutogenInventory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPlayerAutogenInventory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerCredentials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPlayerCredentials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerCredits(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPlayerCredits, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerInventory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPlayerInventory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerStats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPlayerStats, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerVessels(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPlayerVessels, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPremiumBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPremiumBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPremiumInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcPremiumInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcQuestAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcQuestChange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestComplete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcQuestComplete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestCompleteAll(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcQuestCompleteAll, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuests(KaitaiStruct):
        """Empty request, server responds with quest list."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcQuests, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcReactOnAbandonedGame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcReactOnAbandonedGame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReferrals(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcReferrals, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRelatedQuestEnable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcRelatedQuestEnable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReportPlayer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcReportPlayer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRewardTutorial(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcRewardTutorial, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRewardedTutorials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcRewardedTutorials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSalvageItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSalvageItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSalvageItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSalvageItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellCraftResource(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSellCraftResource, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellCraftResources(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSellCraftResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSellItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSellItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSellVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSendEarlyPlayerLog(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSendEarlyPlayerLog, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcServerInfo(KaitaiStruct):
        """Empty request, server responds with server info."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcServerInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcSetFbToken(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSetFbToken, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetReferrer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSetReferrer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetUserdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSetUserdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetVisitedZone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSetVisitedZone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcShipQuestChange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestEnd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcShipQuestEnd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestStart(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcShipQuestStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuests(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcShipQuests, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialIgnoreAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSocialIgnoreAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialIgnoreRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSocialIgnoreRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestFb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSocialSuggestFb, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestSteam(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSocialSuggestSteam, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestVk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSocialSuggestVk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialWatchAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSocialWatchAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialWatchRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSocialWatchRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSpaceStationsPopulation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSpaceStationsPopulation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadConvertToWing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSquadConvertToWing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInfo(KaitaiStruct):
        """Empty request, server responds with squad info."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSquadInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcSquadInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSquadInviteAccept, self).__init__(_io)
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
            super(StarConflictPackageClient.AcSquadInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteDecline(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSquadInviteDecline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSquadInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSquadKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSquadLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadReady(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSquadReady, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSteamUserInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSteamUserInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyGetNew(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSurveyGetNew, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyResults(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSurveyResults, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyVote(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcSurveyVote, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTaStatsSendTutorialEntter(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTaStatsSendTutorialEntter, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTaStatsSendTutorialExit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTaStatsSendTutorialExit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsAcquire(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTalentsAcquire, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsAssignSets(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTalentsAssignSets, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTalentsReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsUpdate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTalentsUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTeachingAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingAllow(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTeachingAllow, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingCheck(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTeachingCheck, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingList(KaitaiStruct):
        """Empty request, server responds with teaching list."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTeachingList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcTeachingReject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTeachingReject, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingRequestToStudent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTeachingRequestToStudent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingRequestToTeacher(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTeachingRequestToTeacher, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTitlesSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcTitlesSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUndockSpaceStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUndockSpaceStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUniverseCounters(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUniverseCounters, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUniverseGet(KaitaiStruct):
        """Empty request, server responds with universe data."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUniverseGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class AcUnlimPveDisablePlayerBuffs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUnlimPveDisablePlayerBuffs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUnlimPveUpgradePlayerLevel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUnlimPveUpgradePlayerLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpdateDlcOwnership(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUpdateDlcOwnership, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpdateYupPurchases(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUpdateYupPurchases, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpgradeAutogenItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUpgradeAutogenItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpgradeItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUpgradeItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUseBlueprint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUseBlueprint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserNotes(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUserNotes, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserNotesAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUserNotesAdd, self).__init__(_io)
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
            super(StarConflictPackageClient.AcUserNotesDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserProfileGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcUserProfileGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselActivateNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselActivateNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselAutogenDestroy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselAutogenDestroy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselAutogenDismantle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselAutogenDismantle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselBudgetActivate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselBudgetActivate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselBudgetLevelup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselBudgetLevelup, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselChangeEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeEquipMulti(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselChangeEquipMulti, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselChangeMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCheatChangeEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselCheatChangeEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCraft(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselCraft, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCustomElementsAcknowledgeExpiration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselCustomElementsAcknowledgeExpiration, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCustomElementsBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselCustomElementsBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselEquipment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselEquipment, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselExtractExp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselExtractExp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselFreeCustomElements(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselFreeCustomElements, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselLevelup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselLevelup, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRecraft(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselRecraft, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRefillBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselRefillBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRefillMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselRefillMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRepair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselRepair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRepairBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselRepairBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselStripEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselStripEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselStripImproperBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselStripImproperBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselTransferEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselTransferEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselTransferMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselTransferMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselUnlockNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcVesselUnlockNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcWarmapGet(KaitaiStruct):
        """Client requests war map data for a specific zone."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcWarmapGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.zone_id = self._io.read_u8be()


        def _fetch_instances(self):
            pass


    class AcWelcomeMsg(KaitaiStruct):
        """Client requests welcome message in specified language."""
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcWelcomeMsg, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.lang = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class AcZoneCoordinatorGmCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcZoneCoordinatorGmCommand, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcZoneInstancesInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcZoneInstancesInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcZonesLuaActiveEventsUpdate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackageClient.AcZonesLuaActiveEventsUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass



