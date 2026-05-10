"""Bit-stream parser for ac_user_profile_get server-to-client response.

Handler 0x0822ed43 reads `u2 num_records` then `num_records` × per-profile
records via the per-record reader at FUN_08924e60. The per-record reader
populates a profile struct that the lua side accesses via
`MasterServer_UserProfileGet(uid)` — the field names below come from
star-conflict-lua-decompiled/ui/scripts/work/gameobjects/profile.lua and
match the lua callback `MasterServer_OnUserProfileUpdate(result,
requestId, uid, field)` where `field` is `MasterServer.UserProfileField`.

Per-record layout:

    u8be uid                            (read first via FUN_08b1c360)
    u4   present_field_mask             (LEB-style u4 via FUN_08b1bbd0;
                                         observed values fit in 32 bits —
                                         each bit selects a UPF_* field)

Then per bit set in present_field_mask, in this order:

    bit 0  UPF_STATE              u8 state + u64 sub_id
                                  (state = MasterServer.UserState value)
    bit 1  UPF_CLAN_ID            u64 clan_id
    bit 2  UPF_GENERAL_STATS      33 × u64 indexed by
                                  MasterServer.UserProfileGeneralStat
                                  (UPGS_KARMA=0 … UPGS_FACTION_REP_CYBER_2=32)
    bit 3  UPF_VESSELS_RANK_STATS 18 × 33 × u64 (per-vessel rank stat
                                  matrix; the inner stride matches the
                                  33-key general-stats table)
    bit 4  UPF_ACHIEVEMENTS       length-prefixed array of records of
                                  shape `{value: u64, ranks: [u64,...]}`
                                  (matches profile.achievements lua use)
    bit 5  UPF_MEDALS             u32-terminated array of fixed-size records
    bit 6  UPF_TITLES             FUN_08918870 sub-reader (titles list)
    bit 7  UPF_AVATARS            FUN_08919100 sub-reader (avatars list)
    bit 8  UPF_MOTTOS             FUN_08919b50 sub-reader (mottos list)
    bit 9  UPF_ATLAS              property bag via FUN_088c0ce0
                                  (atlas: blueprints/research)

The reads in FUN_08924e60 are byte-aligned u64s/u8s/u32s on the wire-side
class, but the AC body's bit-stream may have different byte-alignment
slack from the SCMD framing — we surface the per-flag-bit decode for
bits 0-3 (simple shapes) and stop at bit 4 to avoid desync, since the
sub-readers for bits 4-9 are too involved to model without per-flag
captures.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from notification import BitReader

# UserProfileField bit-mapping (mirrored from masterserver.lua line 613).
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


@dataclass
class _ProfileRecord:
    uid: int
    flags: int
    state: Optional[int] = None
    state_sub_id: Optional[int] = None
    clan_id: Optional[int] = None
    general_stats: Optional[List[int]] = None      # 33 entries, key = UPGS_*
    vessels_rank_stats: Optional[List[List[int]]] = None  # 18×33
    bits_after_simple: int = 0  # consumed bits after bit-3 (or wherever we stopped)

    def fields_present(self) -> List[str]:
        return [UPF_NAMES.get(i, f"bit{i}")
                for i in range(10) if (self.flags >> i) & 1]


class AcUserProfileGetResponseBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.num_records: int = 0
        self.records: List[_ProfileRecord] = []
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.num_records = br.read_u16()
            for _ in range(self.num_records):
                if br.remaining() < 64 + 32:
                    break
                rec = _ProfileRecord(uid=br.read_u64(), flags=br.read_u32())

                # UPF_STATE: u8 state + u64 sub_id
                if rec.flags & (1 << UPF_STATE):
                    if br.remaining() < 8 + 64:
                        self.records.append(rec); break
                    rec.state        = br.read_u8()
                    rec.state_sub_id = br.read_u64()

                # UPF_CLAN_ID: u64
                if rec.flags & (1 << UPF_CLAN_ID):
                    if br.remaining() < 64:
                        self.records.append(rec); break
                    rec.clan_id = br.read_u64()

                # UPF_GENERAL_STATS: 33 × u64
                if rec.flags & (1 << UPF_GENERAL_STATS):
                    if br.remaining() < 33 * 64:
                        self.records.append(rec); break
                    rec.general_stats = [br.read_u64() for _ in range(33)]

                # UPF_VESSELS_RANK_STATS: 18 × 33 × u64
                if rec.flags & (1 << UPF_VESSELS_RANK_STATS):
                    need = 18 * 33 * 64
                    if br.remaining() < need:
                        self.records.append(rec); break
                    rec.vessels_rank_stats = [
                        [br.read_u64() for _ in range(33)]
                        for _ in range(18)
                    ]

                rec.bits_after_simple = br.pos
                self.records.append(rec)

                # Stop walking as soon as a record needs a sub-reader we
                # don't model — we'd otherwise desync the bit-stream and
                # mis-parse the next uid.
                if rec.flags & ~((1 << UPF_VESSELS_RANK_STATS) |
                                  (1 << UPF_GENERAL_STATS) |
                                  (1 << UPF_CLAN_ID) |
                                  (1 << UPF_STATE)):
                    break
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcUserProfileGetResponseBody(<error: {self.error}>)"
        n_records = len(self.records)
        slack = len(self._raw) * 8 - self.bits_consumed
        first = self.records[0] if self.records else None
        if first:
            first_repr = (f"uid=0x{first.uid:x}, flags=0x{first.flags:x}"
                          f"{{{','.join(first.fields_present())}}}")
            extras = []
            if first.state is not None:
                extras.append(f"state={first.state}")
            if first.clan_id is not None:
                extras.append(f"clan=0x{first.clan_id:x}")
            if first.general_stats is not None:
                extras.append(f"gstats={len(first.general_stats)}")
            if first.vessels_rank_stats is not None:
                extras.append(f"vrank={len(first.vessels_rank_stats)}×"
                              f"{len(first.vessels_rank_stats[0])}")
            if extras:
                first_repr += " " + " ".join(extras)
        else:
            first_repr = "—"
        return (f"AcUserProfileGetResponseBody({len(self._raw)}B, "
                f"num_records={self.num_records}, parsed={n_records}, "
                f"first=({first_repr}), slack={slack}b)")
