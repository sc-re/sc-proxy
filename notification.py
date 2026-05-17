#!/usr/bin/env python3
"""SCMD_NOTIFICATION (scmd_pkt_type=0x0e) body decoder.

Wire format (reversed from MasterServerEndpoint::OnRecieve, switch at
0x08243f74) is a tightly bit-packed BE bit-stream produced by Star
Conflict's BitStream/Bag library:

    sn_type    : u8                            # 8 bits — see SN_NAMES
    bag        : property_bag                  # named fields

    property_bag:
        num_entries : u32                      # 32 bits
        if num_entries > 0:
            use_indexed_keys : u1              # 1 bit
            for _ in range(num_entries):
                if not use_indexed_keys:
                    key : cstring              # 8-bit chars NUL-terminated
                value : variant

    variant:
        tag : u8                               # 8 bits
        switch tag:
            0x00 nil
            0x01 i32                           # 32 bits, two's complement
            0x02 u64    (setter v1)            # 64 bits
            0x03 u64    (setter v2)            # 64 bits
            0x04 f32                           # 32 bits IEEE-754
            0x05 cstring                       # NUL-terminated 8-bit chars
            0x06 nested property_bag           # recursive
            0x07 12-byte blob                  # 96 bits
            0x08 bool                          # 1 bit

Per-SN field names/types are documented in OnRecieve's case bodies; for
example SN_ATLAS_INIT (0x60) carries one field "atlasModulesNum" : i32.

Kaitai struct can't represent this cleanly: in bit-mode there's no f32,
no bool, no strz, so values come out as raw ints / int lists. A
hand-rolled bit reader is much cleaner and gives Python-native types.

Reverse-engineering anchors (StarConflict, x86, vmaddr 0x08048000):
    Bag::Deserialize          0x08b1ed60
    Bag::DeserializeEntries   0x08b1ec70
    Bag::ReadVariant          0x08b1c720
    BitStream::Read           0x08b20c00  (read N bits, BE/MSB-first)
    BitStream::ReadBit        0x08b1fc30
    BitStream::ReadU8         0x08b1b6e0
    BitStream::ReadU32        0x08b1baa0
    BitStream::ReadI32        0x08b1c230
    BitStream::ReadU64        0x08b1c4a0
    BitStream::ReadF32        0x08b1c5e0
    BitStream::ReadCString    0x08b19c80
"""
from __future__ import annotations

import struct
from dataclasses import dataclass
from typing import Any

from sn_types import sn_name


class BitReader:
    """Big-endian, MSB-first bit-stream reader (matches BitStream::Read).

    `last_read_start` records the bit offset where the most recent
    top-level read started, so callers can compute a (start, end) bit
    range for the value they just read. `_read_bag` / `_read_variant`
    restore `last_read_start` to their own entry-position before
    returning, so a `_kv("bag", _read_bag(br), br)` call gets the full
    bag span rather than the last inner read.
    """

    __slots__ = ("buf", "pos", "last_read_start")

    def __init__(self, buf: bytes):
        self.buf = buf
        self.pos = 0              # bit offset
        self.last_read_start = 0  # start of the most recent top-level read

    def remaining(self) -> int:
        return len(self.buf) * 8 - self.pos

    def read_bits(self, nbits: int) -> int:
        if self.pos + nbits > len(self.buf) * 8:
            raise EOFError(f"need {nbits} bits, have {self.remaining()}")
        val = 0
        for _ in range(nbits):
            byte = self.buf[self.pos >> 3]
            bit = (byte >> (7 - (self.pos & 7))) & 1
            val = (val << 1) | bit
            self.pos += 1
        return val

    def read_bool(self) -> bool:
        self.last_read_start = self.pos
        return self.read_bits(1) == 1

    def read_u8(self) -> int:
        self.last_read_start = self.pos
        return self.read_bits(8)

    def read_u16(self) -> int:
        self.last_read_start = self.pos
        return self.read_bits(16)

    def read_u32(self) -> int:
        self.last_read_start = self.pos
        return self.read_bits(32)

    def read_i32(self) -> int:
        self.last_read_start = self.pos
        v = self.read_bits(32)
        return v - (1 << 32) if v & (1 << 31) else v

    def read_u64(self) -> int:
        self.last_read_start = self.pos
        return self.read_bits(64)

    def read_f32(self) -> float:
        self.last_read_start = self.pos
        return struct.unpack(">f", self.read_bits(32).to_bytes(4, "big"))[0]

    def read_cstring(self, max_len: int = 2048) -> str:
        self.last_read_start = self.pos
        out = bytearray()
        for _ in range(max_len):
            b = self.read_bits(8)
            if b == 0:
                break
            out.append(b)
        return out.decode("utf-8", errors="replace")

    def read_blob(self, nbytes: int) -> bytes:
        self.last_read_start = self.pos
        return bytes(self.read_bits(8) for _ in range(nbytes))


# ── Variant tags (matches Bag_ReadVariant switch at 0x08b1c720) ───────────────

TAG_NIL    = 0x00
TAG_I32    = 0x01
TAG_U64_A  = 0x02
TAG_U64_B  = 0x03
TAG_F32    = 0x04
TAG_STR    = 0x05
TAG_BAG    = 0x06
TAG_BLOB12 = 0x07
TAG_BOOL   = 0x08


@dataclass(frozen=True)
class Variant:
    """A typed value plus its on-wire variant tag.

    Repr is `tag(value)` — e.g. `i32(42)`, `f32(3.14)`, `str('hi')` — so
    decoded bags display their on-wire types inline. Use `.value` to get
    the raw Python value.

    `bit_range` (when set) is the (start_bit, end_bit_exclusive) span of
    the wire bytes this Variant was parsed from — used by the Qt UI to
    map a tree node to a hex-pane highlight.

    `display` (when set) is a parser-supplied human-readable rendering
    of the value (e.g. an enum-name list for a bitmask). The tree
    renderer prefers it over `repr(value)` so the GUI mirrors what the
    CLI's custom `__repr__` already shows.
    """
    tag: str
    value: Any
    itag: int
    bit_range: tuple[int, int] | None = None
    display: str | None = None

    def __repr__(self) -> str:
        return f"{self.tag}[{self.itag:02x}]({self.value!r})"


def read_field(br: BitReader, tag: str, value: Any,
               display: str | None = None) -> Variant:
    """Wrap a freshly-read scalar in a Variant tagged with its on-wire
    type and the bit range it consumed.

    Idiom for hand-rolled parsers:

        out["foo"] = read_field(br, "u32", br.read_u32())

    The range comes from `br.last_read_start` (set by the read) and
    `br.pos` (after the read), so the call must come *immediately*
    after the read with no other read in between.

    For compound reads, `_read_bag` and `_read_variant` restore
    `last_read_start` to their own entry position, so
    `read_field(br, "bag", _read_bag(br))` Just Works and the range
    covers the whole bag (header + entries).

    Pass `display=` to override what the Qt tree shows in the value
    column — e.g. decoded enum/bitmask names alongside the raw int.
    """
    return Variant(tag, value, 0xff,
                   (br.last_read_start, br.pos),
                   display=display)


# ── ANSI colour rendering ─────────────────────────────────────────────────────
# Plain `repr()` stays uncoloured (useful for files & assertions). Use the
# format_* helpers below when emitting to a terminal.

_RESET   = "\033[0m"
_DIM     = "\033[2m"
_BOLD    = "\033[1m"
_RED     = "\033[31m"
_GREEN   = "\033[32m"
_YELLOW  = "\033[33m"
_BLUE    = "\033[34m"
_MAGENTA = "\033[35m"
_CYAN    = "\033[36m"
_BRRED   = "\033[91m"
_BRYEL   = "\033[93m"

_TAG_COLOURS: dict[str, str] = {
    # Bag variant tags
    "nil":    _DIM,
    "i32":    _CYAN,
    "u64a":   _BLUE,
    "u64b":   _BLUE,
    "f32":    _MAGENTA,
    "str":    _GREEN,
    "bag":    _YELLOW,
    "blob12": _MAGENTA,
    "bool":   _BRYEL,
    # Direct-read types used by non-notification SCMD decoders. Same hue
    # family as their bag-variant equivalents so eye-grep stays consistent.
    "u64":    _BLUE,
    "u32":    _CYAN,
    "u16":    _CYAN,
    "u8":     _CYAN,
    "u1":     _BRYEL,
}


def format_variant(v: Any) -> str:
    """Render a Variant (or anything else) as a colour-coded string."""
    if not isinstance(v, Variant):
        return repr(v)
    colour = _TAG_COLOURS.get(v.tag, "")
    head = f"{colour}{v.tag}[{v.itag:02x}]{_RESET}"
    if v.tag == "bag" and isinstance(v.value, dict):
        return f"{head}({format_bag(v.value)})"
    return f"{head}({colour}{v.value!r}{_RESET})"


def format_bag(bag: dict) -> str:
    """Render a bag dict with each value coloured by its variant tag."""
    if not bag:
        return "{}"
    parts = [f"{k!r}: {format_variant(v)}" for k, v in bag.items()]
    return "{" + ", ".join(parts) + "}"


def format_issues(issues: list[str]) -> str:
    """Render validate() issues in red. Empty list → empty string."""
    if not issues:
        return ""
    return f" {_BRRED}⚠ {'; '.join(issues)}{_RESET}"


def _read_variant(br: BitReader) -> Variant:
    """Read one wire variant. The returned Variant carries `bit_range`
    spanning its tag byte through the end of its payload, so callers
    can highlight the corresponding hex bytes in a UI."""
    start = br.pos
    tag = br.read_u8()
    if tag == TAG_NIL:
        v = Variant("nil", None, tag)
    elif tag == TAG_I32:
        v = Variant("i32", br.read_i32(), tag)
    elif tag == TAG_U64_A:
        v = Variant("u64a", br.read_u64(), tag)
    elif tag == TAG_U64_B:
        v = Variant("u64b", br.read_u64(), tag)
    elif tag == TAG_F32:
        v = Variant("f32", br.read_f32(), tag)
    elif tag == TAG_STR:
        v = Variant("str", br.read_cstring(), tag)
    elif tag == TAG_BAG:
        v = Variant("bag", _read_bag(br), tag)
    elif tag == TAG_BLOB12:
        v = Variant("blob12", br.read_blob(12), tag)
    elif tag == TAG_BOOL:
        v = Variant("bool", br.read_bool(), tag)
    else:
        raise ValueError(f"unknown variant tag 0x{tag:02x} at bit {br.pos - 8}")
    end = br.pos
    # last_read_start so a wrapping _kv(..., br=br) sees the variant's span.
    br.last_read_start = start
    return Variant(v.tag, v.value, v.itag, (start, end))


def _read_bag(br: BitReader) -> dict:
    """Returns a dict of {key: value}. Indexed bags use str(idx) as key.
    Each value Variant's `bit_range` is widened to cover its key bytes
    too, so the UI can highlight the whole entry on click."""
    bag_start = br.pos
    num_entries = br.read_u32()
    out: dict[str, Any] = {}
    if num_entries == 0:
        br.last_read_start = bag_start
        return out
    use_indexed_keys = br.read_bool()
    for i in range(num_entries):
        entry_start = br.pos
        key = str(i) if use_indexed_keys else br.read_cstring()
        v = _read_variant(br)
        # Widen the variant's range to cover the key too — the tree
        # shows "key: value" as one node, so highlighting the value
        # alone would leave the key bytes un-highlighted.
        out[key] = Variant(v.tag, v.value, v.itag, (entry_start, br.pos))
    br.last_read_start = bag_start
    return out


# ── Top-level decoder ─────────────────────────────────────────────────────────

@dataclass
class Notification:
    sn_id: int
    sn_name: str
    bag: dict

    def __repr__(self) -> str:
        return f"Notification({self.sn_name}, {self.bag!r})"

    def validate(self) -> list[str]:
        """Convenience — see module-level validate()."""
        return validate(self)


def decode(body: bytes) -> Notification:
    """Decode an SCMD_NOTIFICATION packet body."""
    br = BitReader(body)
    sn_id = br.read_u8()
    bag = _read_bag(br)
    return Notification(sn_id=sn_id, sn_name=sn_name(sn_id), bag=bag)


def expected_fields(sn_id: int) -> list[tuple[str, str]]:
    """Return the (variant_tag, field_name) list documented for this SN
    notification, merged from C++ + Lua sources. See SN_FIELDS comment.
    """
    return SN_FIELDS.get(sn_id, [])


# Tags treated as compatible with each documented type. Keeps validate()
# tolerant of:
#   * Lua "num" (any numeric variant on the wire)
#   * the dual u64a/u64b setter encoding (same payload, different setter)
_COMPAT: dict[str, set[str]] = {
    "i32":   {"i32"},
    "u64":   {"u64a", "u64b"},
    "f32":   {"f32"},
    "str":   {"str"},
    "bag":   {"bag"},
    "bool":  {"bool"},
    "nil":   {"nil"},
    "num":   {"i32", "u64a", "u64b", "f32"},
    "?":     {"nil", "i32", "u64a", "u64b", "f32", "str", "bag", "blob12", "bool"},
}


def validate(notif: Notification) -> list[str]:
    """Check a decoded Notification against SN_FIELDS.

    Returns a list of human-readable issue strings (empty list = OK):
      * "missing field 'X' (expected <tag>)" — documented field absent
      * "field 'X' wire-tag <got>, expected <want>" — type mismatch
      * "extra undocumented field 'X' (<tag>)" — bag carries fields the
        spec doesn't mention. May indicate (a) a server-only field the
        client ignores, or (b) a documentation gap.
      * "no spec for SN <name> (id=N) — N field(s) present" — when
        SN_FIELDS has no entry for this SN. Informational, not an error.

    Tolerances: u64a vs u64b are accepted interchangeably for `u64` specs;
    `num` accepts any numeric tag; `?` accepts any tag.
    """
    spec = SN_FIELDS.get(notif.sn_id)
    issues: list[str] = []
    if not spec:
        if notif.bag:
            issues.append(
                f"no spec for {notif.sn_name} (id={notif.sn_id}) — "
                f"{len(notif.bag)} field(s) present: {sorted(notif.bag)}")
        return issues

    expected_keys: set[str] = set()
    for want_tag, key in spec:
        expected_keys.add(key)
        if key not in notif.bag:
            issues.append(f"missing field {key!r} (expected {want_tag})")
            continue
        v = notif.bag[key]
        got_tag = v.tag if isinstance(v, Variant) else "?"
        compat = _COMPAT.get(want_tag, {want_tag})
        if got_tag not in compat:
            issues.append(f"field {key!r} wire-tag {got_tag}, expected {want_tag}")

    for key, v in notif.bag.items():
        if key not in expected_keys:
            got_tag = v.tag if isinstance(v, Variant) else "?"
            issues.append(f"extra undocumented field {key!r} ({got_tag})")

    return issues


# ── Per-SN field map ──────────────────────────────────────────────────────────
# Documents which bag fields each SN_* notification carries, merged from
# THREE sources (in order of confidence):
#
#   1. C++ client (authoritative): MasterServerEndpoint::OnRecieve switch at
#      0x08243f74. Each Bag::Get*(local_8dc, "key", default) call gives an
#      exact (variant_tag, field_name) pair.
#   2. Lua handlers (confirmed): UI.NotificationsSlotWnd.Update_SN_<NAME>(...)
#      in star-conflict-lua-decompiled/ui/scripts/windows/notificationsslotwnd.lua.
#      Each `params.<field>` access (and GetParam(params, "<field>")) is a
#      bag-field read; type is inferred from `type(...) == "..."` checks,
#      `for ... in pairs(...)` iteration, IsTrueEx, and sys.log error msgs.
#   3. Localisation strings (NOT included): unpacked-game/strings/english/
#      string.txt has ntf_SN_*\$placeholder\$ tokens, but many of those are
#      DERIVED in Lua (e.g. "ships" computed from `vessels`), not real bag
#      fields, so they're filtered out to avoid false positives in validate().
#
# Type tag legend:
#   i32 / u64 / f32 / str / bag / bool / nil — exact variant tag
#   num — Lua `number`, may be any of i32 / u64 / f32 on the wire
#   ?   — field referenced but no type evidence
#
# Each entry's trailing comment lists sources (cpp,lua) so you know how
# trustworthy a given row is.

SN_FIELDS: dict[int, list[tuple[str, str]]] = {
      0: [],  # SN_VESSELS_AUTO_REPAIRED — no C++ handler, no Lua handler
      1: [],  # SN_VESSELS_AUTO_REPAIR_FAILED — no C++ handler, no Lua handler
      2: [("i32", 'withModules'), ("u64", 'vid'), ("i32",'credits'), ("i32", 'goldCredits')],  # SN_VESSEL_REPAIRED — no C++ handler, no Lua handler
      3: [],  # SN_DURABILITY_RESTORED — no C++ handler, no Lua handler
      4: [],  # SN_FREE_REPAIR_USED — no C++ handler, no Lua handler
      5: [],  # SN_VESSELS_AUTO_REFILLED — no C++ handler, no Lua handler
      6: [],  # SN_VESSELS_AUTO_REFILL_FAILED — no C++ handler, no Lua handler
      7: [],  # SN_VESSEL_REFILLED — no C++ handler, no Lua handler
      8: [("str", "defName"), ("bag", "bundleContents"), ("?", "itemDefName"), ("?", "itemType"), ("?", "iid")],  # SN_ITEM_PURCHASED (cpp,lua)
      9: [("bag", "contents")],  # SN_ITEM_BURNED (lua)
     10: [],  # SN_CREDITS_PURCHASED — no C++ handler, no Lua handler
     11: [("?", "premiumSeconds")],  # SN_PREMIUM_TIME_PURCHASED (lua)
     12: [],  # SN_INVENTORY_EXT_PURCHASED — no C++ handler, no Lua handler
     13: [("?", "autogenItem"), ("?", "defName"), ("?", "itemDefName"), ("?", "itemType"), ("?", "iid"), ("?", "amount")],  # SN_ITEM_SOLD (lua)
     14: [("str", "defName"), ("num", "tokensRefund"), ("bag", "itemsRefund")],  # SN_ITEM_SALVAGED (lua)
     15: [("i32", "giver"), ("i32", "receiver")],  # SN_LIKE_ADDED (cpp)
     16: [],  # SN_UPDATE_DLC_OWNERSHIP — no C++ handler, no Lua handler
     17: [],  # SN_WAR_THUNDER_PROMO — no C++ handler, no Lua handler
     18: [],  # SN_VK_GROUP_REWARD_PROMO — no C++ handler, no Lua handler
     19: [("bag", "unlockedShips")],  # SN_VESSEL_LEVELUP (lua)
     20: [],  # SN_BATTLE_SLOT_AVAILABLE — no C++ handler, no Lua handler
     21: [],  # SN_SKILL_LEARNED — no C++ handler, no Lua handler
     22: [],  # SN_SKILL_RESET — no C++ handler, no Lua handler
     23: [],  # SN_MODULE_EQUIPPED — no C++ handler, no Lua handler
     24: [],  # SN_MODULE_UNEQUIPPED — no C++ handler, no Lua handler
     25: [("bag", "modules"), ("bag", "munition")],  # SN_MODULE_UNEQUIPPED_MULTI (lua)
     26: [("u64", "vid"), ("i32", "slot"), ("string", "defName")],  # SN_MUNITION_EQUIPPED — no C++ handler, no Lua handler
     27: [],  # SN_MUNITION_UNEQUIPPED — no C++ handler, no Lua handler
     28: [("?", "bBroken")],  # SN_BATTLE_SLOT_VESSEL_INSTALLED (lua)
     29: [],  # SN_BATTLE_SLOT_VESSEL_REMOVED — no C++ handler, no Lua handler
     30: [("i32", "gameMode"), ("i32", "isLooser"), ("bool", "incAntibotCounter"), ("i32", "unlimPveMissionLevel"), ("str", "pveMissionName"), ("bool", "isWinner"), ("bool", "isDraw"), ("bool", "isLeaver"), ("?", "levelName"), ("?", "createdAt"), ("?", "vessels")],  # SN_GAME_REWARDED (cpp,lua)
     31: [],  # SN_LEADERBOARD_SOMETHING — no C++ handler, no Lua handler
     32: [("num", "achievementId"), ("num", "rank")],  # SN_ACHIEVEMENT_UNLOCKED (lua)
     33: [],  # SN_SQUAD_NOTIFICATION — no C++ handler, no Lua handler
     34: [],  # SN_RACE_RANK — no C++ handler, no Lua handler
     35: [],  # SN_SOCIAL_NOTIFICATION — no C++ handler, no Lua handler
     36: [("num", "goldCredits"), ("u64", "premiumTime"), ("?", "goldBuyingPoints")],  # SN_YUP_PURCHASE (lua)
     37: [],  # SN_GOLD_REVOKE — no C++ handler, no Lua handler
     38: [],  # SN_GOLD_EMISSION — no C++ handler, no Lua handler
     39: [("num", "goldCredits"), ("u64", "premiumTime"), ("?", "goldBuyingPoints")],  # SN_STEAM_PURCHASE (lua)
     40: [],  # SN_BONUS_BUNDLE — no C++ handler, no Lua handler
     41: [],  # SN_STRIPPED_UNAVAILABLE_ITEMS — no C++ handler, no Lua handler
     42: [("i32", "minutesLeft")],  # SN_MAINTENANCE_COUNTDOWN (cpp)
     43: [],  # SN_MAINTENANCE_CANCELLED — no C++ handler, no Lua handler
     44: [],  # SN_STEAM_DLC_PURCHASED — no C++ handler, no Lua handler
     45: [("i32", "premiumAccess")],  # SN_PREMIUM_ACCESS (cpp)
     46: [],  # SN_VESSEL_CUSTOM_ELEMENTS_CHANGED — no C++ handler, no Lua handler
     47: [],  # SN_VESSEL_CUSTOM_ELEMENTS_EXPIRED — no C++ handler, no Lua handler
     48: [("bag", "defNames")],  # SN_VESSEL_CUSTOM_ELEMENTS_NEW_FREE (cpp)
     49: [("str", "msg")],  # SN_WELCOME_MSG (lua)
     50: [("str", "msg")],  # SN_MOTD (lua)
     51: [("?", "stringIdx"), ("?", "defName")],  # SN_ITEM_ADVERT (lua)
     52: [],  # SN_GOLD_POOL_ADVERT — no C++ handler, no Lua handler
     53: [],  # SN_LOBBY_NOTIFICATION — no C++ handler, no Lua handler
     54: [],  # SN_DAILY_LOGIN — no C++ handler, no Lua handler
     55: [("u64", "mailId")],  # SN_NEW_LETTER (cpp)
     56: [],  # SN_STEAM_GROUP_PROMO — no C++ handler, no Lua handler
     57: [("?", "questId")],  # SN_QUEST_ACCEPTED (lua)
     58: [],  # SN_QUEST_PROGRESS — no C++ handler, no Lua handler
     59: [("?", "questId"), ("?", "completionData")],  # SN_QUEST_COMPLETED (lua)
     60: [],  # SN_TITLE_ACQUIRED — no C++ handler, no Lua handler
     61: [],  # SN_AVATAR_ACQUIRED — no C++ handler, no Lua handler
     62: [],  # SN_MOTTO_ACQUIRED — no C++ handler, no Lua handler
     63: [("u64", "uid")],  # SN_REFEREE_ADDED (cpp)
     64: [("u64", "referee"), ("i32", "bonusGold")],  # SN_REFERRER_BONUS_GOLD (cpp)
     65: [],  # SN_STEAM_PRIVATE_PROFILE — no C++ handler, no Lua handler
     66: [("num", "prestige")],  # SN_PRESTIGE_CHANGED (lua)
     67: [],  # SN_RESOURCE_VESSEL_DEACTIVATE — no C++ handler, no Lua handler
     68: [],  # SN_ZONE_OWNAGE_REWARD — no C++ handler, no Lua handler
     69: [],  # SN_CLAN_NOTIFICATION — no C++ handler, no Lua handler
     70: [("str", "def"), ("u64", "uid"), ("str", "nickName")],  # SN_PLAYER_CRAFTED_VESSEL (cpp)
     71: [("str", "def"), ("u64", "uid"), ("str", "nickName")],  # SN_PLAYER_BOUGHT_PREMIUM_VESSEL (cpp)
     72: [("i32", "success")],  # SN_ADMIN_TASK_RESULT (cpp)
     73: [],  # SN_TEACHING_NOTIFICATION — no C++ handler, no Lua handler
     74: [("?", "defName"), ("?", "amount"), ("?", "blueprintDefName"), ("?", "numEnch")],  # SN_CRAFT_RESULT (lua)
     75: [("num", "goldCredits"), ("u64", "premiumTime"), ("?", "goldBuyingPoints")],  # SN_ARC_PURCHASE (lua)
     76: [],  # SN_TALENT_NOTIFICATION — no C++ handler, no Lua handler
     77: [],  # SN_GAME_REWARDED_PREMIUM — no C++ handler, no Lua handler
     78: [("?", "textId"), ("bag", "vids"), ("bag", "shipDefNames")],  # SN_SHIP_QUEST_STARTED (lua)
     79: [],  # SN_SHIP_QUEST_ENDED — no C++ handler, no Lua handler
     80: [("?", "goldCredits"), ("?", "eventCredits"), ("?", "tokenCredits")],  # SN_TOURNAMENT_REWARDS (lua)
     81: [("num", "zid"), ("bag", "new"), ("bag", "old")],  # SN_ZONE_OWNER_CHANGED (lua)
     82: [("str", "name"), ("str", "tag")],  # SN_CLANSHIP_BUILDING_FINISHED (lua)
     83: [],  # SN_NEW_LETTERS — no C++ handler, no Lua handler
     84: [],  # SN_ITEM_CONVERTED — no C++ handler, no Lua handler
     85: [("i32", "aid"), ("i32", "rank"), ("u64", "uid"), ("str", "nickName")],  # SN_PLAYER_UNLOCKED_ACHIEVEMENT (cpp)
     86: [("?", "modulesSold"), ("?", "munitionSold"), ("?", "refundCredits")],  # SN_MASSIVE_SALE (lua)
     87: [("?", "resourcesSold"), ("?", "refundCredits")],  # SN_MASSIVE_RESOURCE_SALE (lua)
     88: [("u64", "mailId"), ("u64", "newGold"), ("u64", "tradeMoneyNew"), ("bag", "items"), ("?", "goldCost"), ("?", "gold"), ("?", "tradeMoneyOld")],  # SN_LETTER_PAYMENT (cpp,lua)
     89: [("u64", "mailId"), ("i32", "dealsNum")],  # SN_LETTER_REJECTED (cpp)
     90: [],  # SN_LETTER_EXPIRED — no C++ handler, no Lua handler
     91: [],  # SN_ADMIN_LETTERS — no C++ handler, no Lua handler
     92: [],  # SN_LETTER_ITEMS — no C++ handler, no Lua handler
     93: [("num", "goldCost"), ("bag", "items")],  # SN_LETTER_GOODS (lua)
     94: [("?", "ench"), ("?", "creditsCost"), ("?", "goldCost"), ("?", "oldDefName"), ("?", "newDefName")],  # SN_UPGRADE_RESULT (lua)
     95: [("i32", "existOpponent")],  # SN_EMM_EXIST_OPPONENT (cpp)
     96: [("i32", "atlasModulesNum")],  # SN_ATLAS_INIT (cpp)
     97: [("i32", "accountRank"), ("i32", "accountExpPool")],  # SN_ACCOUNT_RANK_UP (cpp)
     98: [("i32", "militaryRank"), ("f32", "militaryExp"), ("bool", "rankUp")],  # SN_MILITARY_EXP_ADD (cpp)
     99: [],  # SN_ADVERT_DELETE — no C++ handler, no Lua handler
    100: [("bag", "letter"), ("i32", "dealsNum")],  # SN_SELL_PRODUCT_FROM_ADVERT (cpp)
    101: [],  # SN_UNLIM_PVE_UPGRADE_PLAYER_LEVEL — no C++ handler, no Lua handler
    102: [],  # SN_AUTOGEN_INVENTORY_EXT_PURCHASED — no C++ handler, no Lua handler
    103: [],  # SN_AUTOGEN_UPGRADE_RESULT — no C++ handler, no Lua handler
    104: [],  # SN_EQUIPMENT_CHANGE_MULTI — no C++ handler, no Lua handler
    105: [("bag", "battlePass")],  # SN_BATTLE_PASS_UNLOCK (cpp)
    106: [("?", "amount")],  # SN_IMAGINARY_QUEST_REWARD (lua)
    107: [],  # SN_LOBBY_GROUP_CREATED — no C++ handler, no Lua handler
    108: [("?", "autogenItem")],  # SN_AUTOGEN_DESTROYED (lua)
    109: [("?", "rollData"), ("?", "upgradeLevel")],  # SN_AUTOGEN_DISMANTLED (lua)
    110: [("i32", "questKey")],  # SN_QUEST_KEY_CHANGE (cpp)
    111: [("i32", "messageType"), ("str", "textId"), ("bag", "params")],  # SN_GAME_EVENT_STATE_CHANGED (cpp)
    112: [("i32", "amount"), ("str", "dlcName"), ("i32", "credits"), ("i32", "goldCredits"), ("i32", "premiumTime"), ("bag", "items"), ("bag", "auras"), ("bag", "bundles"), ("i32", "invExtLevel"), ("i32", "titleId"), ("bag", "vessels"), ("bag", "stickers"), ("bag", "battlePass"), ("?", "type"), ("str", "name"), ("bag", "bundle"), ("num", "stage"), ("str", "aura")],  # SN_DLC_PURCHASED (cpp,lua)
    113: [("?", "completionData")],  # SN_ADVENTURE_FINAL (lua)
    114: [],  # SN_ADVENTURE_PROGRESS — no C++ handler, no Lua handler
    115: [],  # SN_NUM — no C++ handler, no Lua handler
}
# ── Self-test ─────────────────────────────────────────────────────────────────

def _strip_bit_ranges(bag: dict) -> dict:
    """Helper for tests: drop bit_range from every Variant so synthesised
    Variant objects (constructed without ranges) compare equal."""
    out = {}
    for k, v in bag.items():
        if isinstance(v, Variant):
            inner = v.value
            if isinstance(inner, dict):
                inner = _strip_bit_ranges(inner)
            out[k] = Variant(v.tag, inner, v.itag)
        else:
            out[k] = v
    return out


def _selftest() -> None:
    """Synthesize SN_ATLAS_INIT { atlasModulesNum: 42 } and round-trip it."""
    bits: list[int] = []

    def w(val: int, n: int) -> None:
        for i in range(n - 1, -1, -1):
            bits.append((val >> i) & 1)

    w(0x60, 8)                                       # sn_type = SN_ATLAS_INIT
    w(1, 32)                                         # num_entries = 1
    w(0, 1)                                          # use_indexed_keys = false
    for c in b"atlasModulesNum\x00":
        w(c, 8)                                      # key
    w(TAG_I32, 8)                                    # variant tag
    w(42, 32)                                        # value

    while len(bits) % 8:
        bits.append(0)
    buf = bytes(int("".join(map(str, bits[i:i + 8])), 2)
                for i in range(0, len(bits), 8))

    n = decode(buf)
    assert n.sn_id == 0x60, n.sn_id
    assert n.sn_name == "SN_ATLAS_INIT", n.sn_name
    # Compare value/tag/itag — bit_range is set by the parser and differs
    # per buffer layout, so we ignore it here.
    assert _strip_bit_ranges(n.bag) == {
        "atlasModulesNum": Variant("i32", 42, TAG_I32)
    }, n.bag
    print(f"OK  {n}")

    # Indexed-keys bag with mixed types — synthetic but exercises the format.
    bits.clear()
    w(0x00, 8)                                       # sn_type = SN_VESSELS_AUTO_REPAIRED (no real fields)
    w(3, 32)                                         # num_entries = 3
    w(1, 1)                                          # use_indexed_keys = true
    w(TAG_BOOL, 8); w(1, 1)                          # entries[0] = true
    w(TAG_F32,  8); w(0x40490fdb, 32)                # entries[1] = 3.1415927 (pi)
    w(TAG_STR,  8)
    for c in b"hi\x00":
        w(c, 8)                                      # entries[2] = "hi"

    while len(bits) % 8:
        bits.append(0)
    buf = bytes(int("".join(map(str, bits[i:i + 8])), 2)
                for i in range(0, len(bits), 8))
    n = decode(buf)
    pi = struct.unpack(">f", b"\x40\x49\x0f\xdb")[0]
    assert _strip_bit_ranges(n.bag) == {
        "0": Variant("bool", True, TAG_BOOL),
        "1": Variant("f32", pi, TAG_F32),
        "2": Variant("str", "hi", TAG_STR),
    }, n.bag
    print(f"OK  indexed bag: {n.bag}")


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(
        description="Decode SCMD_NOTIFICATION .bin capture bodies.")
    ap.add_argument("paths", nargs="*", metavar="FILE",
                    help="capture .bin file(s); pass multiple to decode a list")
    ap.add_argument("--selftest", action="store_true",
                    help="run synthesised round-trip tests instead of decoding")
    args = ap.parse_args()

    if args.selftest or not args.paths:
        _selftest()
    else:
        for path in args.paths:
            with open(path, "rb") as f:
                body = f.read()
            try:
                n = decode(body)
                print(f"{path}: Notification({n.sn_name}, {format_bag(n.bag)})")
                for issue in n.validate():
                    print(f"  {_BRRED}⚠ {issue}{_RESET}")
            except Exception as e:
                print(f"{path}: {_BRRED}DECODE FAILED — {type(e).__name__}: {e}{_RESET}")
