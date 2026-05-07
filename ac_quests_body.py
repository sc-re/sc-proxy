"""Bit-stream parsers for AC response bodies that aren't pure bags but
were left as `unknown: size-eos: true` placeholders.

Each class is a kaitai opaque type — kaitai-struct-compiler with
`--opaque-types true` produces `AcXxx(self._io)` calls that this module
satisfies. Field names come from reverse-engineering the corresponding
client-side reader in the binary (handler addresses noted on the class).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Tuple

from notification import BitReader


def _read_cstring(br: BitReader, max_len: int = 256) -> str:
    out = bytearray()
    for _ in range(max_len):
        if br.remaining() < 8:
            break
        b = br.read_u8()
        if b == 0:
            return out.decode("utf-8", errors="replace")
        out.append(b)
    return out.decode("utf-8", errors="replace")


def _read_uid_list(br: BitReader) -> List[int]:
    """u4be count + count × u8be UID."""
    n = br.read_u32()
    return [br.read_u64() for _ in range(n)]


# ── ac_quests (handler 0x0822d960) ───────────────────────────────────────────
class AcQuestsBody:
    """Active and template quest list. Multi-section inline layout:
       u4 a + u4 b + u4 c + u1 d + u1 e + u1 f + u1 g
       + u1 num_dailies, num_dailies entries of {u4 + u1}
       + u1 num_quests, num_quests records (per-record reader FUN_088f8e20,
         then u2 quest_id, u1 status, u4 progress, optional u8 + optional u8)
       + u1 num_quest_descs, num_quest_descs entries (FUN_088f8ea0 + u2 + u1)
       + u2 num_quest_ids_a, num_quest_ids_a × u2
       + u4 misc
       + u2 num_quest_ids_b, num_quest_ids_b × u2
       + (u8 idx, i4 value)* terminated by 0xff
       Surfaced as the top three u4 values; rest opaque."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: str | None = None
        self.a: int | None = None
        self.b: int | None = None
        self.c: int | None = None
        try:
            br = BitReader(self._raw)
            self.a = br.read_u32()
            self.b = br.read_u32()
            self.c = br.read_u32()
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcQuestsBody(<error: {self.error}>)"
        return (f"AcQuestsBody({len(self._raw)}B, a={self.a}, b={self.b}, "
                f"c={self.c}, …)")
