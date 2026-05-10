"""Bit-stream parser for ac_user_profile_get server-to-client response.

Handler 0x0822ed43 reads `u2 num_records` then `num_records` × per-profile
records via UserProfile_DeserializeRecord (FUN_08924e60). Each record is:

    u8be uid                            (BitStream_ReadU64v2)
    varuint flags                       (BitStream_ReadVarUInt; encoding:
                                         1+8 / 2+16 / 2+32 bits)

Then per bit set in `flags`, in this order, with the wire format derived
from FUN_08924e60 + the named UserProfile_Deserialize* helpers:

    bit 0 (UPF_STATE)
        u8  state                       (UserState enum)
        u64 stateLastChange             (timestamp / token)

    bit 1 (UPF_CLAN_ID)
        u64 clan_id

    bit 2 (UPF_GENERAL_STATS)
        33 × u64                        (UPGS_KARMA=0..UPGS_FACTION_REP_CYBER_2=32)

    bit 3 (UPF_VESSELS_RANK_STATS)
        18 × 33 × u64                   (594 u64s — per-vessel × per-stat)

    bit 4 (UPF_ACHIEVEMENTS)
        261 × {
            u32 value
            u8  num_ranks               (≤16)
            0..num_ranks × u64 rank_data
            (loop early-exits on the first all-zero u64 — i.e. unranked
             entries don't have to write num_ranks zeros, the wire just
             truncates them)
        }

    bit 5 (UPF_MEDALS)
        62 × {
            1..8 × u32                  (early-exits on first 0)
        }

    bit 6 (UPF_TITLES) — UserProfile_DeserializeTitles
        u16 active_title_id
        loop i = 0..383:
            u1 present
            if present: u64 title_data  (likely unlock timestamp)

    bit 7 (UPF_AVATARS) — UserProfile_DeserializeAvatars
        cstring current_avatar          (≤60)
        u16 count
        count × cstring                 (≤60)

    bit 8 (UPF_MOTTOS) — UserProfile_DeserializeMottos
        cstring current_motto           (≤60)
        u16 count
        count × cstring                 (≤60)

    bit 9 (UPF_ATLAS) — Atlas_Deserialize
        i32 accountExpPool              (lua: profile.atlas.accountExpPool)
        u1  modules_present
        if modules_present: bag         (sparse; key=tier-group index,
                                          value=u64 packing 21 × 3-bit
                                          module ranks)
        u1  vesselsProgress_present
        if vesselsProgress_present: bag (per-vessel research)

The captured `flags` values like 0x80f13fff or 0x027fffff have bits set
above bit 9. UserProfile_DeserializeRecord ignores those higher bits on
the wire — they appear to be runtime-only flags (e.g. "loaded from
disk", "request pending"), set elsewhere — so the wire reader stops
after bit 9.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from notification import BitReader, _read_bag

UPF_STATE              = 0
UPF_CLAN_ID            = 1
UPF_GENERAL_STATS      = 2
UPF_VESSELS_RANK_STATS = 3
UPF_ACHIEVEMENTS       = 4
UPF_MEDALS             = 5
UPF_TITLES             = 6
UPF_AVATARS            = 7
UPF_MOTTOS             = 8
UPF_ATLAS              = 9

UPF_NAMES = {
    0: "UPF_STATE",
    1: "UPF_CLAN_ID",
    2: "UPF_GENERAL_STATS",
    3: "UPF_VESSELS_RANK_STATS",
    4: "UPF_ACHIEVEMENTS",
    5: "UPF_MEDALS",
    6: "UPF_TITLES",
    7: "UPF_AVATARS",
    8: "UPF_MOTTOS",
    9: "UPF_ATLAS",
}


def _read_var_uint(br: BitReader) -> int:
    """BitStream_ReadVarUInt (FUN_08b1bbd0): 1+8 / 2+16 / 2+32 encoding."""
    if br.read_bool() == 0:
        return br.read_u8()
    if br.read_bool() == 0:
        return br.read_u16()
    return br.read_u32()


def _read_titles(br: BitReader) -> dict:
    """UserProfile_DeserializeTitles (FUN_08918870)."""
    out = {"active_title_id": br.read_u16(), "titles": {}}
    for i in range(0x180):
        if br.read_bool():
            out["titles"][i] = br.read_u64()
    return out


def _read_avatars_or_mottos(br: BitReader) -> dict:
    """UserProfile_DeserializeAvatars (08919100) /
    UserProfile_DeserializeMottos (08919b50). Same wire format."""
    current = br.read_cstring(max_len=60)
    n = br.read_u16()
    items = [br.read_cstring(max_len=60) for _ in range(n)]
    return {"current": current, "count": n, "items": items}


def _read_atlas(br: BitReader) -> dict:
    """Atlas_Deserialize (FUN_088c0ce0)."""
    out = {"accountExpPool": br.read_i32()}
    if br.read_bool() == 0:
        out["modules"] = _read_bag(br)
    if br.remaining() >= 1 and br.read_bool() == 0:
        out["vesselsProgress"] = _read_bag(br)
    return out


@dataclass
class _ProfileRecord:
    uid: int
    flags: int
    # bit 0
    state: Optional[int] = None
    state_last_change: Optional[int] = None
    # bit 1
    clan_id: Optional[int] = None
    # bit 2
    general_stats: Optional[List[int]] = None      # 33 entries
    # bit 3
    vessels_rank_stats: Optional[List[List[int]]] = None  # 18 × 33
    # bit 4
    achievements: Optional[List[Tuple[int, List[int]]]] = None
    # bit 5
    medals: Optional[List[List[int]]] = None
    # bit 6
    titles: Optional[dict] = None
    # bit 7
    avatars: Optional[dict] = None
    # bit 8
    mottos: Optional[dict] = None
    # bit 9
    atlas: Optional[dict] = None
    bits_consumed: int = 0

    def fields_present(self) -> List[str]:
        return [UPF_NAMES.get(i, f"bit{i}")
                for i in range(10) if (self.flags >> i) & 1]


def _read_record(br: BitReader) -> _ProfileRecord:
    rec = _ProfileRecord(uid=br.read_u64(), flags=_read_var_uint(br))

    if rec.flags & (1 << UPF_STATE):
        rec.state             = br.read_u8()
        rec.state_last_change = br.read_u64()

    if rec.flags & (1 << UPF_CLAN_ID):
        rec.clan_id = br.read_u64()

    if rec.flags & (1 << UPF_GENERAL_STATS):
        rec.general_stats = [br.read_u64() for _ in range(33)]

    if rec.flags & (1 << UPF_VESSELS_RANK_STATS):
        rec.vessels_rank_stats = [
            [br.read_u64() for _ in range(33)] for _ in range(18)
        ]

    if rec.flags & (1 << UPF_ACHIEVEMENTS):
        ach = []
        for _ in range(261):
            value = br.read_u32()
            num_ranks = br.read_u8()
            ranks: List[int] = []
            for _ in range(num_ranks):
                rd = br.read_u64()
                ranks.append(rd)
                if rd == 0:
                    break
            ach.append((value, ranks))
        rec.achievements = ach

    if rec.flags & (1 << UPF_MEDALS):
        med = []
        for _ in range(62):
            entry: List[int] = []
            for _ in range(8):
                v = br.read_u32()
                entry.append(v)
                if v == 0:
                    break
            med.append(entry)
        rec.medals = med

    if rec.flags & (1 << UPF_TITLES):
        rec.titles = _read_titles(br)

    if rec.flags & (1 << UPF_AVATARS):
        rec.avatars = _read_avatars_or_mottos(br)

    if rec.flags & (1 << UPF_MOTTOS):
        rec.mottos = _read_avatars_or_mottos(br)

    if rec.flags & (1 << UPF_ATLAS):
        rec.atlas = _read_atlas(br)

    rec.bits_consumed = br.pos
    return rec


class AcUserProfileGetResponseBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.num_records: int = 0
        self.records: List[_ProfileRecord] = []
        self.bits_consumed: int = 0
        self.partial: bool = False
        try:
            br = BitReader(self._raw)
            self.num_records = br.read_u16()
            for _ in range(self.num_records):
                start = br.pos
                try:
                    rec = _read_record(br)
                    self.records.append(rec)
                except Exception as e:
                    self.error = (f"record {len(self.records)}: "
                                  f"{type(e).__name__}: {e} (bit {start})")
                    self.partial = True
                    break
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = f" ERROR: {self.error}" if self.error else ""
        if not self.records:
            return (f"AcUserProfileGetResponseBody({len(self._raw)}B, "
                    f"records=0/{self.num_records}, slack={slack}b{suffix})")
        # Every record shows its decoded values (state, clan, atlas
        # summary, etc.). Records are typically small (state-only) so
        # one line per record stays readable even for 96-record
        # friends-list lookups.
        lines = [_format_record_long(r) for r in self.records]
        body = "\n  ".join(lines)
        return (f"AcUserProfileGetResponseBody({len(self._raw)}B, "
                f"records={len(self.records)}/{self.num_records}, "
                f"slack={slack}b{suffix}):\n  {body}")


def _format_record_long(r: _ProfileRecord) -> str:
    parts = [f"uid=0x{r.uid:x}"]
    if r.state is not None:
        parts.append(f"state={r.state}@{r.state_last_change}")
    if r.clan_id is not None:
        parts.append(f"clan=0x{r.clan_id:x}")
    if r.general_stats is not None:
        nz = sum(1 for v in r.general_stats if v != 0)
        parts.append(f"gstats={nz}/33nz")
    if r.vessels_rank_stats is not None:
        nz = sum(1 for row in r.vessels_rank_stats for v in row if v != 0)
        parts.append(f"vrank={nz}/594nz")
    if r.achievements is not None:
        nz = sum(1 for v, _ in r.achievements if v != 0)
        parts.append(f"ach={nz}/261touched")
    if r.medals is not None:
        nz = sum(1 for entry in r.medals if any(entry))
        parts.append(f"medals={nz}/62nz")
    if r.titles is not None:
        active = r.titles["active_title_id"]
        unlocked = len(r.titles["titles"])
        parts.append(f"titles(active={active},n={unlocked})")
    if r.avatars is not None:
        cur = r.avatars["current"]
        parts.append(f"avatar={cur!r}(n={r.avatars['count']})")
    if r.mottos is not None:
        cur = r.mottos["current"]
        parts.append(f"motto={cur!r}(n={r.mottos['count']})")
    if r.atlas is not None:
        ap = r.atlas["accountExpPool"]
        mods = r.atlas.get("modules", {})
        vp = r.atlas.get("vesselsProgress", {})
        nz_modules = 0
        for v in mods.values():
            val = v.value if hasattr(v, "value") else v
            for i in range(21):
                if (val >> (61 - 3 * i)) & 7:
                    nz_modules += 1
        parts.append(
            f"atlas(clearance={ap},"
            f"modules={nz_modules}nz/{len(mods)}tiers,"
            f"vp={len(vp)})")
    # If only the leading uid is set (no UPF bits decoded), show flags.
    if len(parts) == 1:
        parts.append(f"flags=0x{r.flags:x}")
    return " ".join(parts)
