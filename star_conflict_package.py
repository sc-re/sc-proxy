# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class StarConflictPackage(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(StarConflictPackage, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.packet_type = self._io.read_s2be()
        _on = self.packet_type
        if _on == 0:
            pass
            self.body = StarConflictPackage.AcLoadInitialPlayerData(self._io, self, self._root)
        elif _on == 1:
            pass
            self.body = StarConflictPackage.AcServerInfo(self._io, self, self._root)
        elif _on == 10:
            pass
            self.body = StarConflictPackage.AcPlayerCredits(self._io, self, self._root)
        elif _on == 100:
            pass
            self.body = StarConflictPackage.AcLeagueTeamInfo(self._io, self, self._root)
        elif _on == 101:
            pass
            self.body = StarConflictPackage.AcLeagueTeamCreate(self._io, self, self._root)
        elif _on == 102:
            pass
            self.body = StarConflictPackage.AcLeagueTeamInviteSend(self._io, self, self._root)
        elif _on == 103:
            pass
            self.body = StarConflictPackage.AcLeagueTeamInviteCancel(self._io, self, self._root)
        elif _on == 104:
            pass
            self.body = StarConflictPackage.AcLeagueTeamInviteAccept(self._io, self, self._root)
        elif _on == 105:
            pass
            self.body = StarConflictPackage.AcLeagueTeamKick(self._io, self, self._root)
        elif _on == 106:
            pass
            self.body = StarConflictPackage.AcLeagueTeamLeave(self._io, self, self._root)
        elif _on == 107:
            pass
            self.body = StarConflictPackage.AcLeagueTeamInviteDecline(self._io, self, self._root)
        elif _on == 108:
            pass
            self.body = StarConflictPackage.AcLeagueTeamRequestNames(self._io, self, self._root)
        elif _on == 109:
            pass
            self.body = StarConflictPackage.AcGetNicknames(self._io, self, self._root)
        elif _on == 11:
            pass
            self.body = StarConflictPackage.AcPlayerStats(self._io, self, self._root)
        elif _on == 110:
            pass
            self.body = StarConflictPackage.AcGetUids(self._io, self, self._root)
        elif _on == 111:
            pass
            self.body = StarConflictPackage.AcReportPlayer(self._io, self, self._root)
        elif _on == 112:
            pass
            self.body = StarConflictPackage.AcUpdateYupPurchases(self._io, self, self._root)
        elif _on == 113:
            pass
            self.body = StarConflictPackage.AcCheckYupPurchases(self._io, self, self._root)
        elif _on == 114:
            pass
            self.body = StarConflictPackage.AcUpdateDlcOwnership(self._io, self, self._root)
        elif _on == 115:
            pass
            self.body = StarConflictPackage.AcFriendsSendRequest(self._io, self, self._root)
        elif _on == 116:
            pass
            self.body = StarConflictPackage.AcFriendsAcceptRequest(self._io, self, self._root)
        elif _on == 117:
            pass
            self.body = StarConflictPackage.AcFriendsRejectRequest(self._io, self, self._root)
        elif _on == 118:
            pass
            self.body = StarConflictPackage.AcFriendsRemove(self._io, self, self._root)
        elif _on == 119:
            pass
            self.body = StarConflictPackage.AcFriendsList(self._io, self, self._root)
        elif _on == 12:
            pass
            self.body = StarConflictPackage.AcPlayerArcBalance(self._io, self, self._root)
        elif _on == 120:
            pass
            self.body = StarConflictPackage.AcSocialIgnoreAdd(self._io, self, self._root)
        elif _on == 121:
            pass
            self.body = StarConflictPackage.AcSocialIgnoreRemove(self._io, self, self._root)
        elif _on == 122:
            pass
            self.body = StarConflictPackage.AcSocialWatchAdd(self._io, self, self._root)
        elif _on == 123:
            pass
            self.body = StarConflictPackage.AcSocialWatchRemove(self._io, self, self._root)
        elif _on == 124:
            pass
            self.body = StarConflictPackage.AcSocialSuggestSteam(self._io, self, self._root)
        elif _on == 125:
            pass
            self.body = StarConflictPackage.AcSocialSuggestFb(self._io, self, self._root)
        elif _on == 126:
            pass
            self.body = StarConflictPackage.AcSocialSuggestVk(self._io, self, self._root)
        elif _on == 127:
            pass
            self.body = StarConflictPackage.AcTeachingList(self._io, self, self._root)
        elif _on == 128:
            pass
            self.body = StarConflictPackage.AcTeachingRequestToTeacher(self._io, self, self._root)
        elif _on == 129:
            pass
            self.body = StarConflictPackage.AcTeachingRequestToStudent(self._io, self, self._root)
        elif _on == 13:
            pass
            self.body = StarConflictPackage.AcTitlesSetActive(self._io, self, self._root)
        elif _on == 130:
            pass
            self.body = StarConflictPackage.AcTeachingAccept(self._io, self, self._root)
        elif _on == 131:
            pass
            self.body = StarConflictPackage.AcTeachingReject(self._io, self, self._root)
        elif _on == 132:
            pass
            self.body = StarConflictPackage.AcTeachingCheck(self._io, self, self._root)
        elif _on == 133:
            pass
            self.body = StarConflictPackage.AcTeachingAllow(self._io, self, self._root)
        elif _on == 134:
            pass
            self.body = StarConflictPackage.AcReferrals(self._io, self, self._root)
        elif _on == 135:
            pass
            self.body = StarConflictPackage.AcSetReferrer(self._io, self, self._root)
        elif _on == 136:
            pass
            self.body = StarConflictPackage.AcObtainReferralKey(self._io, self, self._root)
        elif _on == 137:
            pass
            self.body = StarConflictPackage.AcAttachSteamAccount(self._io, self, self._root)
        elif _on == 138:
            pass
            self.body = StarConflictPackage.AcFinalizeSteamMtxn(self._io, self, self._root)
        elif _on == 139:
            pass
            self.body = StarConflictPackage.AcAttachYupAccount(self._io, self, self._root)
        elif _on == 14:
            pass
            self.body = StarConflictPackage.AcAvatarsSetActive(self._io, self, self._root)
        elif _on == 140:
            pass
            self.body = StarConflictPackage.AcAttachEmail(self._io, self, self._root)
        elif _on == 141:
            pass
            self.body = StarConflictPackage.AcLobbyList(self._io, self, self._root)
        elif _on == 142:
            pass
            self.body = StarConflictPackage.AcLobbyJoin(self._io, self, self._root)
        elif _on == 143:
            pass
            self.body = StarConflictPackage.AcLobbyCreate(self._io, self, self._root)
        elif _on == 144:
            pass
            self.body = StarConflictPackage.AcLobbyInfo(self._io, self, self._root)
        elif _on == 145:
            pass
            self.body = StarConflictPackage.AcLobbyKick(self._io, self, self._root)
        elif _on == 146:
            pass
            self.body = StarConflictPackage.AcLobbyLeave(self._io, self, self._root)
        elif _on == 147:
            pass
            self.body = StarConflictPackage.AcLobbyInvite(self._io, self, self._root)
        elif _on == 148:
            pass
            self.body = StarConflictPackage.AcLobbyModify(self._io, self, self._root)
        elif _on == 149:
            pass
            self.body = StarConflictPackage.AcLobbyStartGame(self._io, self, self._root)
        elif _on == 15:
            pass
            self.body = StarConflictPackage.AcMottosSetActive(self._io, self, self._root)
        elif _on == 150:
            pass
            self.body = StarConflictPackage.AcLobbyGroupList(self._io, self, self._root)
        elif _on == 151:
            pass
            self.body = StarConflictPackage.AcLobbyGroupInfo(self._io, self, self._root)
        elif _on == 152:
            pass
            self.body = StarConflictPackage.AcLobbyGroupCreate(self._io, self, self._root)
        elif _on == 153:
            pass
            self.body = StarConflictPackage.AcLobbyGroupModify(self._io, self, self._root)
        elif _on == 154:
            pass
            self.body = StarConflictPackage.AcLobbyGroupDelete(self._io, self, self._root)
        elif _on == 155:
            pass
            self.body = StarConflictPackage.AcLobbyGroupJoinreqCreate(self._io, self, self._root)
        elif _on == 156:
            pass
            self.body = StarConflictPackage.AcLobbyGroupJoinreqCancel(self._io, self, self._root)
        elif _on == 157:
            pass
            self.body = StarConflictPackage.AcLobbyGroupJoinreqReject(self._io, self, self._root)
        elif _on == 158:
            pass
            self.body = StarConflictPackage.AcClanRequestCredentials(self._io, self, self._root)
        elif _on == 159:
            pass
            self.body = StarConflictPackage.AcClanRequestDesc(self._io, self, self._root)
        elif _on == 16:
            pass
            self.body = StarConflictPackage.AcChooseStartingStation(self._io, self, self._root)
        elif _on == 160:
            pass
            self.body = StarConflictPackage.AcClanRequestProfile(self._io, self, self._root)
        elif _on == 161:
            pass
            self.body = StarConflictPackage.AcClanJoinreqCreate(self._io, self, self._root)
        elif _on == 162:
            pass
            self.body = StarConflictPackage.AcClanJoinreqCancel(self._io, self, self._root)
        elif _on == 163:
            pass
            self.body = StarConflictPackage.AcClanJoinreqAccept(self._io, self, self._root)
        elif _on == 164:
            pass
            self.body = StarConflictPackage.AcClanInviteSend(self._io, self, self._root)
        elif _on == 165:
            pass
            self.body = StarConflictPackage.AcClanInviteAccept(self._io, self, self._root)
        elif _on == 166:
            pass
            self.body = StarConflictPackage.AcClanInviteCancel(self._io, self, self._root)
        elif _on == 167:
            pass
            self.body = StarConflictPackage.AcClanKick(self._io, self, self._root)
        elif _on == 168:
            pass
            self.body = StarConflictPackage.AcClanLeave(self._io, self, self._root)
        elif _on == 169:
            pass
            self.body = StarConflictPackage.AcClanSetRole(self._io, self, self._root)
        elif _on == 17:
            pass
            self.body = StarConflictPackage.AcChangePlayerNickname(self._io, self, self._root)
        elif _on == 170:
            pass
            self.body = StarConflictPackage.AcClanChangeMotd(self._io, self, self._root)
        elif _on == 171:
            pass
            self.body = StarConflictPackage.AcClanChangeDesc(self._io, self, self._root)
        elif _on == 172:
            pass
            self.body = StarConflictPackage.AcClanChangeRecruiting(self._io, self, self._root)
        elif _on == 173:
            pass
            self.body = StarConflictPackage.AcClanResourceConvert(self._io, self, self._root)
        elif _on == 174:
            pass
            self.body = StarConflictPackage.AcClanShipBuild(self._io, self, self._root)
        elif _on == 175:
            pass
            self.body = StarConflictPackage.AcClanShipBoostBuilding(self._io, self, self._root)
        elif _on == 176:
            pass
            self.body = StarConflictPackage.AcClanShipRepair(self._io, self, self._root)
        elif _on == 177:
            pass
            self.body = StarConflictPackage.AcClanShipBoostRepairing(self._io, self, self._root)
        elif _on == 178:
            pass
            self.body = StarConflictPackage.AcClanShipFit(self._io, self, self._root)
        elif _on == 179:
            pass
            self.body = StarConflictPackage.AcClanShipSetCurrent(self._io, self, self._root)
        elif _on == 18:
            pass
            self.body = StarConflictPackage.AcSteamUserInfo(self._io, self, self._root)
        elif _on == 180:
            pass
            self.body = StarConflictPackage.AcClanUniverseMove(self._io, self, self._root)
        elif _on == 181:
            pass
            self.body = StarConflictPackage.AcClanSetCivilianZone(self._io, self, self._root)
        elif _on == 182:
            pass
            self.body = StarConflictPackage.AcClanReviveInWar(self._io, self, self._root)
        elif _on == 183:
            pass
            self.body = StarConflictPackage.AcClanWarStart(self._io, self, self._root)
        elif _on == 184:
            pass
            self.body = StarConflictPackage.AcClanQuestAccept(self._io, self, self._root)
        elif _on == 185:
            pass
            self.body = StarConflictPackage.AcClanCreate(self._io, self, self._root)
        elif _on == 186:
            pass
            self.body = StarConflictPackage.AcClanUpgrade(self._io, self, self._root)
        elif _on == 187:
            pass
            self.body = StarConflictPackage.AcClanChangeName(self._io, self, self._root)
        elif _on == 188:
            pass
            self.body = StarConflictPackage.AcClanChangeTag(self._io, self, self._root)
        elif _on == 189:
            pass
            self.body = StarConflictPackage.AcClanAssignEmblem(self._io, self, self._root)
        elif _on == 19:
            pass
            self.body = StarConflictPackage.AcPremiumInfo(self._io, self, self._root)
        elif _on == 190:
            pass
            self.body = StarConflictPackage.AcClanBankTransfer(self._io, self, self._root)
        elif _on == 191:
            pass
            self.body = StarConflictPackage.AcClanListRecruiting(self._io, self, self._root)
        elif _on == 192:
            pass
            self.body = StarConflictPackage.AcClanHistoryGet(self._io, self, self._root)
        elif _on == 193:
            pass
            self.body = StarConflictPackage.AcRelatedQuestEnable(self._io, self, self._root)
        elif _on == 194:
            pass
            self.body = StarConflictPackage.AcUserProfileGet(self._io, self, self._root)
        elif _on == 195:
            pass
            self.body = StarConflictPackage.AcAchievements(self._io, self, self._root)
        elif _on == 196:
            pass
            self.body = StarConflictPackage.AcAdminCmd(self._io, self, self._root)
        elif _on == 197:
            pass
            self.body = StarConflictPackage.AcGamesInfo(self._io, self, self._root)
        elif _on == 198:
            pass
            self.body = StarConflictPackage.AcZoneInstancesInfo(self._io, self, self._root)
        elif _on == 199:
            pass
            self.body = StarConflictPackage.AcGetPunishments(self._io, self, self._root)
        elif _on == 2:
            pass
            self.body = StarConflictPackage.AcEnterMmQueue(self._io, self, self._root)
        elif _on == 20:
            pass
            self.body = StarConflictPackage.AcPremiumBuy(self._io, self, self._root)
        elif _on == 200:
            pass
            self.body = StarConflictPackage.AcWelcomeMsg(self._io, self, self._root)
        elif _on == 201:
            pass
            self.body = StarConflictPackage.AcMotd(self._io, self, self._root)
        elif _on == 202:
            pass
            self.body = StarConflictPackage.AcSurveyGetNew(self._io, self, self._root)
        elif _on == 203:
            pass
            self.body = StarConflictPackage.AcSurveyVote(self._io, self, self._root)
        elif _on == 204:
            pass
            self.body = StarConflictPackage.AcSurveyResults(self._io, self, self._root)
        elif _on == 205:
            pass
            self.body = StarConflictPackage.AcUniverseGet(self._io, self, self._root)
        elif _on == 206:
            pass
            self.body = StarConflictPackage.AcUniverseCounters(self._io, self, self._root)
        elif _on == 207:
            pass
            self.body = StarConflictPackage.AcWarmapGet(self._io, self, self._root)
        elif _on == 208:
            pass
            self.body = StarConflictPackage.AcMailGet(self._io, self, self._root)
        elif _on == 209:
            pass
            self.body = StarConflictPackage.AcMailDeliver(self._io, self, self._root)
        elif _on == 21:
            pass
            self.body = StarConflictPackage.AcAccountAuras(self._io, self, self._root)
        elif _on == 210:
            pass
            self.body = StarConflictPackage.AcMailSend(self._io, self, self._root)
        elif _on == 211:
            pass
            self.body = StarConflictPackage.AcMailRemove(self._io, self, self._root)
        elif _on == 212:
            pass
            self.body = StarConflictPackage.AcMailAcknowledgeExpiration(self._io, self, self._root)
        elif _on == 213:
            pass
            self.body = StarConflictPackage.AcSendEarlyPlayerLog(self._io, self, self._root)
        elif _on == 214:
            pass
            self.body = StarConflictPackage.AcAutoPilotSpaceStation(self._io, self, self._root)
        elif _on == 215:
            pass
            self.body = StarConflictPackage.AcUndockSpaceStation(self._io, self, self._root)
        elif _on == 216:
            pass
            self.body = StarConflictPackage.AcSetVisitedZone(self._io, self, self._root)
        elif _on == 217:
            pass
            self.body = StarConflictPackage.AcZoneCoordinatorGmCommand(self._io, self, self._root)
        elif _on == 218:
            pass
            self.body = StarConflictPackage.AcSpaceStationsPopulation(self._io, self, self._root)
        elif _on == 219:
            pass
            self.body = StarConflictPackage.AcKarmaReset(self._io, self, self._root)
        elif _on == 22:
            pass
            self.body = StarConflictPackage.AcAddAccountAura(self._io, self, self._root)
        elif _on == 220:
            pass
            self.body = StarConflictPackage.AcFactionRepReset(self._io, self, self._root)
        elif _on == 221:
            pass
            self.body = StarConflictPackage.AcLeaderboardGet(self._io, self, self._root)
        elif _on == 222:
            pass
            self.body = StarConflictPackage.AcLeaderboardGetDescs(self._io, self, self._root)
        elif _on == 223:
            pass
            self.body = StarConflictPackage.AcSetFbToken(self._io, self, self._root)
        elif _on == 224:
            pass
            self.body = StarConflictPackage.AcGetFbToken(self._io, self, self._root)
        elif _on == 225:
            pass
            self.body = StarConflictPackage.AcLogFbEvent(self._io, self, self._root)
        elif _on == 226:
            pass
            self.body = StarConflictPackage.AcGetCraftResources(self._io, self, self._root)
        elif _on == 227:
            pass
            self.body = StarConflictPackage.AcUseBlueprint(self._io, self, self._root)
        elif _on == 228:
            pass
            self.body = StarConflictPackage.AcSellCraftResource(self._io, self, self._root)
        elif _on == 229:
            pass
            self.body = StarConflictPackage.AcSellCraftResources(self._io, self, self._root)
        elif _on == 23:
            pass
            self.body = StarConflictPackage.AcCancelAccountAura(self._io, self, self._root)
        elif _on == 230:
            pass
            self.body = StarConflictPackage.AcGetBlueprints(self._io, self, self._root)
        elif _on == 231:
            pass
            self.body = StarConflictPackage.AcLearnBlueprint(self._io, self, self._root)
        elif _on == 232:
            pass
            self.body = StarConflictPackage.AcGetFreeSpaceSaveData(self._io, self, self._root)
        elif _on == 233:
            pass
            self.body = StarConflictPackage.AcDisassembleItem(self._io, self, self._root)
        elif _on == 234:
            pass
            self.body = StarConflictPackage.AcAddThumbUp(self._io, self, self._root)
        elif _on == 235:
            pass
            self.body = StarConflictPackage.AcGetVisitedFreeSpaceZones(self._io, self, self._root)
        elif _on == 236:
            pass
            self.body = StarConflictPackage.AcAdvertCreate(self._io, self, self._root)
        elif _on == 237:
            pass
            self.body = StarConflictPackage.AcAdvertDelete(self._io, self, self._root)
        elif _on == 238:
            pass
            self.body = StarConflictPackage.AcAdvertHeaderGet(self._io, self, self._root)
        elif _on == 239:
            pass
            self.body = StarConflictPackage.AcAdvertGet(self._io, self, self._root)
        elif _on == 24:
            pass
            self.body = StarConflictPackage.AcQuests(self._io, self, self._root)
        elif _on == 240:
            pass
            self.body = StarConflictPackage.AcBuyProductFromAdvert(self._io, self, self._root)
        elif _on == 241:
            pass
            self.body = StarConflictPackage.AcEmmChangeReady(self._io, self, self._root)
        elif _on == 242:
            pass
            self.body = StarConflictPackage.AcUnlimPveUpgradePlayerLevel(self._io, self, self._root)
        elif _on == 243:
            pass
            self.body = StarConflictPackage.AcUnlimPveDisablePlayerBuffs(self._io, self, self._root)
        elif _on == 244:
            pass
            self.body = StarConflictPackage.AcTaStatsSendTutorialEntter(self._io, self, self._root)
        elif _on == 245:
            pass
            self.body = StarConflictPackage.AcTaStatsSendTutorialExit(self._io, self, self._root)
        elif _on == 246:
            pass
            self.body = StarConflictPackage.AcUserNotes(self._io, self, self._root)
        elif _on == 247:
            pass
            self.body = StarConflictPackage.AcUserNotesAdd(self._io, self, self._root)
        elif _on == 248:
            pass
            self.body = StarConflictPackage.AcUserNotesDelete(self._io, self, self._root)
        elif _on == 249:
            pass
            self.body = StarConflictPackage.AcBattlePassUnlockLevel(self._io, self, self._root)
        elif _on == 25:
            pass
            self.body = StarConflictPackage.AcQuestAccept(self._io, self, self._root)
        elif _on == 250:
            pass
            self.body = StarConflictPackage.AcZonesLuaActiveEventsUpdate(self._io, self, self._root)
        elif _on == 251:
            pass
            self.body = StarConflictPackage.AcAdventures(self._io, self, self._root)
        elif _on == 252:
            pass
            self.body = StarConflictPackage.AcAdventureCancel(self._io, self, self._root)
        elif _on == 26:
            pass
            self.body = StarConflictPackage.AcQuestChange(self._io, self, self._root)
        elif _on == 27:
            pass
            self.body = StarConflictPackage.AcQuestComplete(self._io, self, self._root)
        elif _on == 28:
            pass
            self.body = StarConflictPackage.AcQuestCompleteAll(self._io, self, self._root)
        elif _on == 29:
            pass
            self.body = StarConflictPackage.AcShipQuests(self._io, self, self._root)
        elif _on == 3:
            pass
            self.body = StarConflictPackage.AcLeaveMmQueue(self._io, self, self._root)
        elif _on == 30:
            pass
            self.body = StarConflictPackage.AcShipQuestStart(self._io, self, self._root)
        elif _on == 31:
            pass
            self.body = StarConflictPackage.AcShipQuestChange(self._io, self, self._root)
        elif _on == 32:
            pass
            self.body = StarConflictPackage.AcShipQuestEnd(self._io, self, self._root)
        elif _on == 33:
            pass
            self.body = StarConflictPackage.AcRewardedTutorials(self._io, self, self._root)
        elif _on == 34:
            pass
            self.body = StarConflictPackage.AcRewardTutorial(self._io, self, self._root)
        elif _on == 35:
            pass
            self.body = StarConflictPackage.AcPlayerInventory(self._io, self, self._root)
        elif _on == 36:
            pass
            self.body = StarConflictPackage.AcPlayerAutogenInventory(self._io, self, self._root)
        elif _on == 37:
            pass
            self.body = StarConflictPackage.AcPlayerVessels(self._io, self, self._root)
        elif _on == 38:
            pass
            self.body = StarConflictPackage.AcVesselEquipment(self._io, self, self._root)
        elif _on == 39:
            pass
            self.body = StarConflictPackage.AcBuyItem(self._io, self, self._root)
        elif _on == 4:
            pass
            self.body = StarConflictPackage.AcMmInfo(self._io, self, self._root)
        elif _on == 40:
            pass
            self.body = StarConflictPackage.AcSellItem(self._io, self, self._root)
        elif _on == 41:
            pass
            self.body = StarConflictPackage.AcSellItems(self._io, self, self._root)
        elif _on == 42:
            pass
            self.body = StarConflictPackage.AcEnchantItem(self._io, self, self._root)
        elif _on == 43:
            pass
            self.body = StarConflictPackage.AcSalvageItem(self._io, self, self._root)
        elif _on == 44:
            pass
            self.body = StarConflictPackage.AcSalvageItems(self._io, self, self._root)
        elif _on == 45:
            pass
            self.body = StarConflictPackage.AcUpgradeItems(self._io, self, self._root)
        elif _on == 46:
            pass
            self.body = StarConflictPackage.AcUpgradeAutogenItem(self._io, self, self._root)
        elif _on == 47:
            pass
            self.body = StarConflictPackage.AcCraftUpgradeItem(self._io, self, self._root)
        elif _on == 48:
            pass
            self.body = StarConflictPackage.AcFindAutogenItem(self._io, self, self._root)
        elif _on == 49:
            pass
            self.body = StarConflictPackage.AcActivateResourceVessel(self._io, self, self._root)
        elif _on == 5:
            pass
            self.body = StarConflictPackage.AcEnterTournament(self._io, self, self._root)
        elif _on == 50:
            pass
            self.body = StarConflictPackage.AcSellVessel(self._io, self, self._root)
        elif _on == 51:
            pass
            self.body = StarConflictPackage.AcVesselChangeEquip(self._io, self, self._root)
        elif _on == 52:
            pass
            self.body = StarConflictPackage.AcVesselChangeEquipMulti(self._io, self, self._root)
        elif _on == 53:
            pass
            self.body = StarConflictPackage.AcVesselCheatChangeEquip(self._io, self, self._root)
        elif _on == 54:
            pass
            self.body = StarConflictPackage.AcVesselTransferEquip(self._io, self, self._root)
        elif _on == 55:
            pass
            self.body = StarConflictPackage.AcVesselStripEquip(self._io, self, self._root)
        elif _on == 56:
            pass
            self.body = StarConflictPackage.AcVesselChangeMunition(self._io, self, self._root)
        elif _on == 57:
            pass
            self.body = StarConflictPackage.AcVesselRefillMunition(self._io, self, self._root)
        elif _on == 58:
            pass
            self.body = StarConflictPackage.AcVesselTransferMunition(self._io, self, self._root)
        elif _on == 59:
            pass
            self.body = StarConflictPackage.AcVesselAutogenDestroy(self._io, self, self._root)
        elif _on == 6:
            pass
            self.body = StarConflictPackage.AcLeaveTournament(self._io, self, self._root)
        elif _on == 60:
            pass
            self.body = StarConflictPackage.AcVesselAutogenDismantle(self._io, self, self._root)
        elif _on == 61:
            pass
            self.body = StarConflictPackage.AcVesselExtractExp(self._io, self, self._root)
        elif _on == 62:
            pass
            self.body = StarConflictPackage.AcVesselLevelup(self._io, self, self._root)
        elif _on == 63:
            pass
            self.body = StarConflictPackage.AcVesselRepair(self._io, self, self._root)
        elif _on == 64:
            pass
            self.body = StarConflictPackage.AcVesselRepairBattle(self._io, self, self._root)
        elif _on == 65:
            pass
            self.body = StarConflictPackage.AcVesselRefillBattle(self._io, self, self._root)
        elif _on == 66:
            pass
            self.body = StarConflictPackage.AcVesselStripImproperBattle(self._io, self, self._root)
        elif _on == 67:
            pass
            self.body = StarConflictPackage.AcVesselFreeCustomElements(self._io, self, self._root)
        elif _on == 68:
            pass
            self.body = StarConflictPackage.AcVesselCustomElementsBuy(self._io, self, self._root)
        elif _on == 69:
            pass
            self.body = StarConflictPackage.AcVesselCustomElementsAcknowledgeExpiration(self._io, self, self._root)
        elif _on == 7:
            pass
            self.body = StarConflictPackage.AcGetUserdata(self._io, self, self._root)
        elif _on == 70:
            pass
            self.body = StarConflictPackage.AcVesselCraft(self._io, self, self._root)
        elif _on == 71:
            pass
            self.body = StarConflictPackage.AcVesselRecraft(self._io, self, self._root)
        elif _on == 72:
            pass
            self.body = StarConflictPackage.AcVesselBudgetLevelup(self._io, self, self._root)
        elif _on == 73:
            pass
            self.body = StarConflictPackage.AcVesselBudgetActivate(self._io, self, self._root)
        elif _on == 74:
            pass
            self.body = StarConflictPackage.AcVesselUnlockNode(self._io, self, self._root)
        elif _on == 75:
            pass
            self.body = StarConflictPackage.AcVesselActivateNode(self._io, self, self._root)
        elif _on == 76:
            pass
            self.body = StarConflictPackage.AcBattleSlots(self._io, self, self._root)
        elif _on == 77:
            pass
            self.body = StarConflictPackage.AcBattleSlotChangeVessel(self._io, self, self._root)
        elif _on == 78:
            pass
            self.body = StarConflictPackage.AcBattleSlotSwapVessels(self._io, self, self._root)
        elif _on == 79:
            pass
            self.body = StarConflictPackage.AcBattleSlotCheatChangeVessel(self._io, self, self._root)
        elif _on == 8:
            pass
            self.body = StarConflictPackage.AcSetUserdata(self._io, self, self._root)
        elif _on == 80:
            pass
            self.body = StarConflictPackage.AcInvExtBuy(self._io, self, self._root)
        elif _on == 81:
            pass
            self.body = StarConflictPackage.AcAutogenInvExtBuy(self._io, self, self._root)
        elif _on == 82:
            pass
            self.body = StarConflictPackage.AcExchangeGold(self._io, self, self._root)
        elif _on == 83:
            pass
            self.body = StarConflictPackage.AcBuyGold(self._io, self, self._root)
        elif _on == 84:
            pass
            self.body = StarConflictPackage.AcBuyArcDlc(self._io, self, self._root)
        elif _on == 85:
            pass
            self.body = StarConflictPackage.AcTalentsAcquire(self._io, self, self._root)
        elif _on == 86:
            pass
            self.body = StarConflictPackage.AcTalentsUpdate(self._io, self, self._root)
        elif _on == 87:
            pass
            self.body = StarConflictPackage.AcTalentsReset(self._io, self, self._root)
        elif _on == 88:
            pass
            self.body = StarConflictPackage.AcTalentsAssignSets(self._io, self, self._root)
        elif _on == 89:
            pass
            self.body = StarConflictPackage.AcBuyTalentSet(self._io, self, self._root)
        elif _on == 9:
            pass
            self.body = StarConflictPackage.AcPlayerCredentials(self._io, self, self._root)
        elif _on == 90:
            pass
            self.body = StarConflictPackage.AcReactOnAbandonedGame(self._io, self, self._root)
        elif _on == 91:
            pass
            self.body = StarConflictPackage.AcSquadInfo(self._io, self, self._root)
        elif _on == 92:
            pass
            self.body = StarConflictPackage.AcSquadInviteAccept(self._io, self, self._root)
        elif _on == 93:
            pass
            self.body = StarConflictPackage.AcSquadInviteDecline(self._io, self, self._root)
        elif _on == 94:
            pass
            self.body = StarConflictPackage.AcSquadLeave(self._io, self, self._root)
        elif _on == 95:
            pass
            self.body = StarConflictPackage.AcSquadInviteSend(self._io, self, self._root)
        elif _on == 96:
            pass
            self.body = StarConflictPackage.AcSquadInviteCancel(self._io, self, self._root)
        elif _on == 97:
            pass
            self.body = StarConflictPackage.AcSquadKick(self._io, self, self._root)
        elif _on == 98:
            pass
            self.body = StarConflictPackage.AcSquadReady(self._io, self, self._root)
        elif _on == 99:
            pass
            self.body = StarConflictPackage.AcSquadConvertToWing(self._io, self, self._root)


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
            super(StarConflictPackage.AcAccountAuras, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAchievements(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAchievements, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcActivateResourceVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcActivateResourceVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAddAccountAura(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAddAccountAura, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAddThumbUp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAddThumbUp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdminCmd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAdminCmd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdventureCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAdventureCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdventures(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAdventures, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAdvertCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertDelete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAdvertDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAdvertGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAdvertHeaderGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAdvertHeaderGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachEmail(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAttachEmail, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachSteamAccount(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAttachSteamAccount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAttachYupAccount(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAttachYupAccount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAutoPilotSpaceStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAutoPilotSpaceStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAutogenInvExtBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAutogenInvExtBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcAvatarsSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcAvatarsSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattlePassUnlockLevel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBattlePassUnlockLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotChangeVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBattleSlotChangeVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotCheatChangeVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBattleSlotCheatChangeVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlotSwapVessels(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBattleSlotSwapVessels, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBattleSlots(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBattleSlots, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyArcDlc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBuyArcDlc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyGold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBuyGold, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBuyItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyProductFromAdvert(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBuyProductFromAdvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcBuyTalentSet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcBuyTalentSet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCancelAccountAura(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcCancelAccountAura, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcChangePlayerNickname(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcChangePlayerNickname, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCheckYupPurchases(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcCheckYupPurchases, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcChooseStartingStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcChooseStartingStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanAssignEmblem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanAssignEmblem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanBankTransfer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanBankTransfer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanChangeDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeMotd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanChangeMotd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeName(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanChangeName, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeRecruiting(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanChangeRecruiting, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanChangeTag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanChangeTag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanHistoryGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanHistoryGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanJoinreqAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanJoinreqCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanJoinreqCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanJoinreqCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanListRecruiting(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanListRecruiting, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanQuestAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanQuestAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestCredentials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanRequestCredentials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestDesc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanRequestDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanRequestProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanRequestProfile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanResourceConvert(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanResourceConvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanReviveInWar(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanReviveInWar, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanSetCivilianZone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanSetCivilianZone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanSetRole(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanSetRole, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBoostBuilding(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanShipBoostBuilding, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBoostRepairing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanShipBoostRepairing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipBuild(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanShipBuild, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipFit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanShipFit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipRepair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanShipRepair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanShipSetCurrent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanShipSetCurrent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanUniverseMove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanUniverseMove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanUpgrade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanUpgrade, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcClanWarStart(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcClanWarStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcCraftUpgradeItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcCraftUpgradeItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcDisassembleItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcDisassembleItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEmmChangeReady(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcEmmChangeReady, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnchantItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcEnchantItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnterMmQueue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcEnterMmQueue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcEnterTournament(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcEnterTournament, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcExchangeGold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcExchangeGold, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFactionRepReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcFactionRepReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFinalizeSteamMtxn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcFinalizeSteamMtxn, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFindAutogenItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcFindAutogenItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsAcceptRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcFriendsAcceptRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcFriendsList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsRejectRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcFriendsRejectRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcFriendsRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcFriendsSendRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcFriendsSendRequest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGamesInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGamesInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetBlueprints(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGetBlueprints, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetCraftResources(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGetCraftResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetFbToken(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGetFbToken, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetFreeSpaceSaveData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGetFreeSpaceSaveData, self).__init__(_io)
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
            super(StarConflictPackage.AcGetNicknames, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unknown = self._io.read_u2be()
            self.num_nicks = self._io.read_u2be()
            self.nicks = []
            for i in range(self.num_nicks):
                self.nicks.append(StarConflictPackage.AcGetNicknames.Nick(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.nicks)):
                pass
                self.nicks[i]._fetch_instances()


        class Nick(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                super(StarConflictPackage.AcGetNicknames.Nick, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.uid = self._io.read_u8be()
                self.nickname = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


            def _fetch_instances(self):
                pass



    class AcGetPunishments(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGetPunishments, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetUids(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGetUids, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetUserdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGetUserdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcGetVisitedFreeSpaceZones(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcGetVisitedFreeSpaceZones, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcInvExtBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcInvExtBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcKarmaReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcKarmaReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaderboardGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeaderboardGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaderboardGetDescs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeaderboardGetDescs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamInviteAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteDecline(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamInviteDecline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeagueTeamRequestNames(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeagueTeamRequestNames, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLearnBlueprint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLearnBlueprint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaveMmQueue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeaveMmQueue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLeaveTournament(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLeaveTournament, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLoadInitialPlayerData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLoadInitialPlayerData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyGroupCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupDelete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyGroupDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyGroupInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqCancel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyGroupJoinreqCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqCreate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyGroupJoinreqCreate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupJoinreqReject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyGroupJoinreqReject, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyGroupList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyGroupModify(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyGroupModify, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyInvite(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyInvite, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyJoin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyJoin, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyModify(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyModify, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLobbyStartGame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLobbyStartGame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcLogFbEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcLogFbEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailAcknowledgeExpiration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcMailAcknowledgeExpiration, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailDeliver(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcMailDeliver, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcMailGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcMailRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMailSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcMailSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMmInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcMmInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMotd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcMotd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcMottosSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcMottosSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcObtainReferralKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcObtainReferralKey, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerArcBalance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPlayerArcBalance, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerAutogenInventory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPlayerAutogenInventory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerCredentials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPlayerCredentials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerCredits(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPlayerCredits, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerInventory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPlayerInventory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerStats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPlayerStats, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPlayerVessels(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPlayerVessels, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPremiumBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPremiumBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcPremiumInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcPremiumInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcQuestAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcQuestChange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestComplete(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcQuestComplete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuestCompleteAll(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcQuestCompleteAll, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcQuests(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcQuests, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReactOnAbandonedGame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcReactOnAbandonedGame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReferrals(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcReferrals, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRelatedQuestEnable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcRelatedQuestEnable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcReportPlayer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcReportPlayer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRewardTutorial(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcRewardTutorial, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcRewardedTutorials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcRewardedTutorials, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSalvageItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSalvageItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSalvageItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSalvageItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellCraftResource(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSellCraftResource, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellCraftResources(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSellCraftResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSellItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSellItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSellVessel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSellVessel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSendEarlyPlayerLog(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSendEarlyPlayerLog, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcServerInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcServerInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetFbToken(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSetFbToken, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetReferrer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSetReferrer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetUserdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSetUserdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSetVisitedZone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSetVisitedZone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcShipQuestChange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestEnd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcShipQuestEnd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuestStart(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcShipQuestStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcShipQuests(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcShipQuests, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialIgnoreAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSocialIgnoreAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialIgnoreRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSocialIgnoreRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestFb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSocialSuggestFb, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestSteam(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSocialSuggestSteam, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialSuggestVk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSocialSuggestVk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialWatchAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSocialWatchAdd, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSocialWatchRemove(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSocialWatchRemove, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSpaceStationsPopulation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSpaceStationsPopulation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadConvertToWing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSquadConvertToWing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSquadInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSquadInviteAccept, self).__init__(_io)
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
            super(StarConflictPackage.AcSquadInviteCancel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteDecline(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSquadInviteDecline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadInviteSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSquadInviteSend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadKick(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSquadKick, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadLeave(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSquadLeave, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSquadReady(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSquadReady, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSteamUserInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSteamUserInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyGetNew(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSurveyGetNew, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyResults(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSurveyResults, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcSurveyVote(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcSurveyVote, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTaStatsSendTutorialEntter(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTaStatsSendTutorialEntter, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTaStatsSendTutorialExit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTaStatsSendTutorialExit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsAcquire(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTalentsAcquire, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsAssignSets(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTalentsAssignSets, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsReset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTalentsReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTalentsUpdate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTalentsUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTeachingAccept, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingAllow(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTeachingAllow, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingCheck(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTeachingCheck, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTeachingList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingReject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTeachingReject, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingRequestToStudent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTeachingRequestToStudent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTeachingRequestToTeacher(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTeachingRequestToTeacher, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcTitlesSetActive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcTitlesSetActive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUndockSpaceStation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUndockSpaceStation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUniverseCounters(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUniverseCounters, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUniverseGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUniverseGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUnlimPveDisablePlayerBuffs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUnlimPveDisablePlayerBuffs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUnlimPveUpgradePlayerLevel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUnlimPveUpgradePlayerLevel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpdateDlcOwnership(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUpdateDlcOwnership, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpdateYupPurchases(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUpdateYupPurchases, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpgradeAutogenItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUpgradeAutogenItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUpgradeItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUpgradeItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUseBlueprint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUseBlueprint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserNotes(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUserNotes, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserNotesAdd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUserNotesAdd, self).__init__(_io)
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
            super(StarConflictPackage.AcUserNotesDelete, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcUserProfileGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcUserProfileGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselActivateNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselActivateNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselAutogenDestroy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselAutogenDestroy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselAutogenDismantle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselAutogenDismantle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselBudgetActivate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselBudgetActivate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselBudgetLevelup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselBudgetLevelup, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselChangeEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeEquipMulti(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselChangeEquipMulti, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselChangeMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselChangeMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCheatChangeEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselCheatChangeEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCraft(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselCraft, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCustomElementsAcknowledgeExpiration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselCustomElementsAcknowledgeExpiration, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselCustomElementsBuy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselCustomElementsBuy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselEquipment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselEquipment, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselExtractExp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselExtractExp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselFreeCustomElements(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselFreeCustomElements, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselLevelup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselLevelup, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRecraft(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselRecraft, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRefillBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselRefillBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRefillMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselRefillMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRepair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselRepair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselRepairBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselRepairBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselStripEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselStripEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselStripImproperBattle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselStripImproperBattle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselTransferEquip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselTransferEquip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselTransferMunition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselTransferMunition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcVesselUnlockNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcVesselUnlockNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcWarmapGet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcWarmapGet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcWelcomeMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcWelcomeMsg, self).__init__(_io)
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
            super(StarConflictPackage.AcZoneCoordinatorGmCommand, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcZoneInstancesInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcZoneInstancesInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class AcZonesLuaActiveEventsUpdate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(StarConflictPackage.AcZonesLuaActiveEventsUpdate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.dummy = self._io.read_u1()


        def _fetch_instances(self):
            pass



