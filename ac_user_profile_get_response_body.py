"""Bit-stream parser for ac_user_profile_get server-to-client response.

Handler 0x0822ed43 reads u2 num_records then `num_records` × per-profile
records via the per-record reader at FUN_08924e60. Each record has:

    u8be uid
    u4   flags                              (FUN_08b1bbd0 — width-prefix
                                             read returning a uint;
                                             observed values fit in 32 b)

Then per flag bit:
    bit 0  → u8 race + u8 clan_id           (with cross-check vs cached)
    bit 1  → u8 alliance_or_secondary_id
    bit 2  → 33 × u8 ship_stats_a
    bit 3  → 33 × 33 × u8 ship_stats_b      (1089 u64s — chunky)
    bit 4  → leaderboard array
              each entry: u4 + u8 num + num × u8 (sorted into best-so-far)
    bit 5  → u32-terminated array of fixed-size records
    bit 6  → FUN_08918870 sub-reader        (pvp scoreboard?)
    bit 7  → FUN_08919100 sub-reader        (achievements / titles)
    bit 8  → FUN_08919b50 sub-reader        (clan history)
    bit 9  → conditional FUN_088c0ce0       (admin/punishment data)

The structure is too involved to model fully without per-bit captures;
we only surface the leading num_records and the per-record (uid, flags)
header for now, and report the bytes consumed.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from notification import BitReader


@dataclass
class _ProfileHead:
    uid: int
    flags: int


class AcUserProfileGetResponseBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.num_records: int = 0
        self.heads: List[_ProfileHead] = []
        try:
            br = BitReader(self._raw)
            self.num_records = br.read_u16()
            # Just decode each profile's leading uid + flags so we at
            # least surface who was returned. The remainder is too
            # complex to model without verified captures per flag bit.
            for _ in range(self.num_records):
                if br.remaining() < 64 + 32:
                    break
                uid = br.read_u64()
                flags = br.read_u32()
                self.heads.append(_ProfileHead(uid, flags))
                # We can't safely advance through the per-bit blocks
                # without modelling each one — break after the first
                # head so we don't desync the reader.
                break
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcUserProfileGetResponseBody(<error: {self.error}>)"
        head = self.heads[0] if self.heads else None
        return (f"AcUserProfileGetResponseBody({len(self._raw)}B, "
                f"num_records={self.num_records}, "
                f"first_uid={hex(head.uid) if head else '?'}, "
                f"first_flags={hex(head.flags) if head else '?'})")
