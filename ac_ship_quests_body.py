"""Bit-stream parsers for AC response bodies that aren't pure bags but
were left as `unknown: size-eos: true` placeholders.

Each class is a kaitai opaque type — kaitai-struct-compiler with
`--opaque-types true` produces `AcXxx(self._io)` calls that this module
satisfies. Field names come from reverse-engineering the corresponding
client-side reader in the binary (handler addresses noted on the class).
"""
from __future__ import annotations
from typing import List

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


# ── ac_ship_quests (handler 0x0822bdf8) ──────────────────────────────────────
class AcShipQuestsBody:
    """Per-ship quest list. Inline reader:
       u1 a + u1 num_records + num_records × {
         FUN_088f9340 (small prelude), u1 b, u1 c, u4 d, u8 e, u8be × 8
       }.
       Modelled minimally — the FUN_088f9340 prelude is ~32 bits we don't
       fully name yet."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: str | None = None
        self.flag: bool = False
        self.num_records: int = 0
        try:
            br = BitReader(self._raw)
            self.flag = br.read_bool()
            self.num_records = br.read_u8()
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcShipQuestsBody(<error: {self.error}>)"
        return (f"AcShipQuestsBody({len(self._raw)}B, flag={self.flag}, "
                f"records={self.num_records}, raw={self._raw[:32].hex()}…)")
