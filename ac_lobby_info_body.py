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


# ── ac_lobby_info (handler 0x0822b1c7 → FUN_088f1690) ────────────────────────
class AcLobbyInfoBody:
    """Lobby state — header decoded, body kept opaque.

    Layout per handler:
      u8 lobby_id, cstring name (max 256), u4 unknown, cstring desc,
      u8 a, u8 b, u8 c, u1 flag1..6, f32 x, f32 y, u2 d, u4 e,
      u1 flag7, u8 some_id, u1 num_members,
      num_members × FUN_088efe80 (per-member),
      cstring s1, cstring s2, u1 flag8, u1 flag9, cstring s3, cstring s4.
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: str | None = None
        self.lobby_id: int | None = None
        self.name: str | None = None
        self.unknown_u32: int | None = None
        self.desc: str | None = None
        try:
            br = BitReader(self._raw)
            self.lobby_id = br.read_u64()
            self.name = _read_cstring(br, 250)
            self.unknown_u32 = br.read_u32()
            self.desc = _read_cstring(br, 250)
            self.tail_bits = br.remaining()
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcLobbyInfoBody(<error: {self.error}>)"
        return (f"AcLobbyInfoBody({len(self._raw)}B, id=0x{self.lobby_id:x}, "
                f"name={self.name!r}, desc={self.desc!r}, "
                f"tail={self.tail_bits}b)")
