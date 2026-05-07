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


# ── ac_teaching_list (handler 0x0822bf58 → FUN_08917c10) ─────────────────────
class AcTeachingListBody:
    """Six UID lists + two u1 flags. The six lists likely correspond to
    the teach/learn state slots (in_progress/teacher/student/etc.). The
    trailing pair of bits are accept/recruit toggles. Reader: FUN_08917c10
    which calls FUN_08917a90 (a u4be count + u8be UID array reader)
    six times with offsets 0, 0x14, 0x3c, 0x28, 0x64, 0x50."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: str | None = None
        self.lists: List[List[int]] = []
        self.flag_a: bool = False
        self.flag_b: bool = False
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            for _ in range(6):
                self.lists.append(_read_uid_list(br))
            self.flag_a = br.read_bool()
            self.flag_b = br.read_bool()
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcTeachingListBody(<error: {self.error}>)"
        sizes = [len(l) for l in self.lists]
        return (f"AcTeachingListBody({len(self._raw)}B, lists={sizes}, "
                f"flag_a={self.flag_a}, flag_b={self.flag_b})")
