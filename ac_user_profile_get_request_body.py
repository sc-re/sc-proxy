"""Bit-stream parser for `ac_user_profile_get` C→S request (AC 0xc2).

The same handler (0x0822ed43 → UserProfile_DeserializeRecord at
0x08924e60) is dispatched on both sides, but the wire payload is
asymmetric. The C→S request carries only the *header* of each profile
record:

    u32   count             (BE — `BitStream_ReadU16v2` in the handler,
                             but the high u16 is always zero so the
                             effective field is u32)
    count × {
        u64  uid              (BitStream_ReadU64v2)
        varuint flags         (BitStream_ReadVarUInt: 1+8 / 2+16 / 2+32
                               bit encoding. Bit i set ⇒ the client
                               wants UPF_<bit_i> back in the response.)
    }

No per-flag-bit payload follows — those slots only appear in the
*response* (the server fills them in based on the requested flags).
The body is bit-packed, so when every flag varuint is the common
1+8 = 9-bit form, each record is exactly 73 bits and successive
records' byte-alignment shifts by 1 bit per record. That shifted
alignment is the `0x80, 0x40, 0x20, 0x10, ...` pattern visible in hex
dumps of count=7 captures.

UPF bit meanings (same as the response — see
`ac_user_profile_get_response_body`):
    bit 0  UPF_STATE
    bit 1  UPF_CLAN_ID
    bit 2  UPF_GENERAL_STATS
    bit 3  UPF_VESSELS_RANK_STATS
    bit 4  UPF_ACHIEVEMENTS
    bit 5  UPF_MEDALS
    bit 6  UPF_TITLES
    bit 7  UPF_AVATARS
    bit 8  UPF_MOTTOS
    bit 9  UPF_ATLAS
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from notification import BitReader, Variant, read_field
from ac_user_profile_get_response_body import _read_var_uint, UPF_NAMES


@dataclass
class _RequestEntry:
    uid: Variant
    flags: Variant

    def fields_requested(self) -> List[str]:
        f = self.flags.value
        return [UPF_NAMES.get(i, f"bit{i}")
                for i in range(10) if (f >> i) & 1]


def _read_entry(br: BitReader) -> _RequestEntry:
    start = br.pos
    uid = read_field(br, "u64", br.read_u64())
    flags = read_field(br, "varuint", _read_var_uint(br))
    br.last_read_start = start
    return _RequestEntry(uid=uid, flags=flags)


class AcUserProfileGetRequestBody:
    """Decoded C→S request body — list of {uid, requested-flags} entries.

    Public attributes are Variants so each carries its own `bit_range`
    for the Qt UI's hex highlighting.
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.num_records: Optional[Variant] = None
        self.records: List[_RequestEntry] = []
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            n = br.read_u32()
            self.num_records = read_field(br, "u32", n)
            self.records = [_read_entry(br) for _ in range(n)]
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcUserProfileGetRequestBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        n = self.num_records.value if self.num_records else "?"
        entries = [(r.uid.value, hex(r.flags.value)) for r in self.records]
        return (f"AcUserProfileGetRequestBody({len(self._raw)}B, "
                f"count={n}, records={entries}, slack={slack}b)")
