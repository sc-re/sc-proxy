"""Bit-stream parser for ac_vessel_change_equip_multi client-to-server request.

The single-equip variant (AC 0x33) is fully byte-aligned:
    u8be vessel_id + u8 slot_idx + u8be module_id

The multi variant (AC 0x34) is bit-packed and carries a list of changes
referenced by slot category name + item def-name. Decoded prefix:

    u8be vessel_id
    u4be num_changes
    u1   padding/flag
    -- per-change records follow, format varies by entry —
       observed cs0 strings include slot categories ("ammo") and
       module def-names ("WeaponMod_RailPerfect_Mk1",
       "SpaceMissile_AAMSlow_T5_Mk3"). Inter-string gaps are not yet
       fully reverse-engineered (the C→S sender lives in the client
       binary but isn't in the response-handler dispatch we already
       mapped).

We surface the prefix and any cs0/cleartext strings we can decode,
leaving the inter-string binary as opaque hex.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from notification import BitReader


def _cs0_decode_at(buf: bytes, start_bit: int) -> Tuple[str, int]:
    """Read 8-bit chars from a bit-stream starting at start_bit, until NUL.
    Returns (decoded text, end bit position)."""
    br = BitReader(buf)
    br.pos = start_bit
    out = bytearray()
    while br.remaining() >= 8:
        b = br.read_u8()
        if b == 0:
            break
        out.append(b)
        if len(out) > 80:
            break
    try:
        text = out.decode("utf-8")
    except UnicodeDecodeError:
        text = out.decode("latin-1", errors="replace")
    return text, br.pos


class AcVesselChangeEquipMultiRequestBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.vessel_id: int = 0
        self.num_changes: int = 0
        self.strings: List[Tuple[int, str]] = []  # (bit_offset, text)
        try:
            br = BitReader(self._raw)
            self.vessel_id = br.read_u64()
            self.num_changes = br.read_u32()
            # Scan the rest for printable cstring-shaped runs at any bit
            # alignment. Take the longest non-overlapping hits, then keep
            # only ones long enough or that match game-data conventions
            # (start with a letter, contain only [A-Za-z0-9_]).
            import re
            ident_re = re.compile(r'^[A-Za-z][A-Za-z0-9_]{3,}$')
            candidates: List[Tuple[int, int, str]] = []
            n_bits = len(self._raw) * 8
            bit = br.pos
            while bit < n_bits - 8 * 4:
                text, end = _cs0_decode_at(self._raw, bit)
                if ident_re.match(text):
                    candidates.append((bit, end, text))
                bit += 1
            # Keep only outermost ranges
            candidates.sort(key=lambda r: (-len(r[2]), r[0]))
            kept: List[Tuple[int, int, str]] = []
            for s, e, t in candidates:
                if not any(ks <= s < ke for ks, ke, _ in kept):
                    kept.append((s, e, t))
            kept.sort(key=lambda r: r[0])
            self.strings = [(s, t) for s, _, t in kept]
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcVesselChangeEquipMultiRequestBody(<error: {self.error}>)"
        names = [t for _, t in self.strings]
        return (f"AcVesselChangeEquipMultiRequestBody({len(self._raw)}B, "
                f"vessel=0x{self.vessel_id:x}, num_changes={self.num_changes}, "
                f"strings={names})")
