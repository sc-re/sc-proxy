"""Bit-stream parser for `ac_league_team_info` (AC 0x64).

Sent S→C with the player's league-team state. Handler entry is at
0x08232b6c — that function reads a `u8 status` and, when status == 0,
calls FUN_088ee800 (the body reader) for the rest of the payload.
Empty/no-team responses still carry the full record with every field
zeroed (and a default rating of 1000.0); only the field VALUES change,
not the structure.

Wire format (in read order):

    u8     status            (0 = success — the rest is present)
    u64v2  team_id
    cstrN  name              (≤ 20 chars, no nul if exactly 20)
    cstrN  short_name        (≤ 20 chars, no nul if exactly 20)
    u64v2  captain_uid       (uid of the team owner)
    u8     num_members
    num_members × u64v2 member_uid
    u8     num_other
    num_other × u64v2 other_uid     (invitations / requests / past members?)
    f32    rating            (default 1000.0 for fresh teams)
    u32    a
    u32    b
    u32    c
    u64    big_a
    u64    big_b
    u1     flag

When `status != 0` the handler skips FUN_088ee800; we report `status`
and stop reading.

Public attributes are Variants (from `read_field`) so each carries its
own `bit_range` for the Qt UI's hex highlighting. Member-uid arrays are
lists of Variants for the same reason.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field


_CSTR_MAX = 21  # matches BitStream_ReadCStringLen(buf, 0x15) in FUN_088ee800


class AcLeagueTeamInfoBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.status: Optional[Variant] = None
        self.team_id: Optional[Variant] = None
        self.name: Optional[Variant] = None
        self.short_name: Optional[Variant] = None
        self.captain_uid: Optional[Variant] = None
        self.num_members: Optional[Variant] = None
        self.members: List[Variant] = []
        self.num_other: Optional[Variant] = None
        self.others: List[Variant] = []
        self.rating: Optional[Variant] = None
        self.a: Optional[Variant] = None
        self.b: Optional[Variant] = None
        self.c: Optional[Variant] = None
        self.big_a: Optional[Variant] = None
        self.big_b: Optional[Variant] = None
        self.flag: Optional[Variant] = None
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.status = read_field(br, "u8", br.read_u8())
            if self.status.value == 0:
                self.team_id = read_field(br, "u64", br.read_u64())
                self.name = read_field(br, "str",
                                       br.read_cstring(max_len=_CSTR_MAX))
                self.short_name = read_field(
                    br, "str", br.read_cstring(max_len=_CSTR_MAX))
                self.captain_uid = read_field(br, "u64", br.read_u64())
                nm = br.read_u8()
                self.num_members = read_field(br, "u8", nm)
                self.members = [read_field(br, "u64", br.read_u64())
                                for _ in range(nm)]
                no = br.read_u8()
                self.num_other = read_field(br, "u8", no)
                self.others = [read_field(br, "u64", br.read_u64())
                               for _ in range(no)]
                self.rating = read_field(br, "f32", br.read_f32())
                self.a = read_field(br, "u32", br.read_u32())
                self.b = read_field(br, "u32", br.read_u32())
                self.c = read_field(br, "u32", br.read_u32())
                self.big_a = read_field(br, "u64", br.read_u64())
                self.big_b = read_field(br, "u64", br.read_u64())
                self.flag = read_field(br, "bool", br.read_bool())
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcLeagueTeamInfoBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        if self.status is None or self.status.value != 0:
            s = self.status.value if self.status else "?"
            return (f"AcLeagueTeamInfoBody({len(self._raw)}B, "
                    f"status={s}, slack={slack}b)")
        members = [m.value for m in self.members]
        others = [o.value for o in self.others]
        return (f"AcLeagueTeamInfoBody({len(self._raw)}B, "
                f"team_id={self.team_id.value}, name={self.name.value!r}, "
                f"short={self.short_name.value!r}, "
                f"captain={self.captain_uid.value}, "
                f"members={members}, others={others}, "
                f"rating={self.rating.value:.1f}, "
                f"a={self.a.value}, b={self.b.value}, c={self.c.value}, "
                f"big_a={self.big_a.value}, big_b={self.big_b.value}, "
                f"flag={self.flag.value}, slack={slack}b)")
