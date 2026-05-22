"""Bit-stream parser for `ac_talents_update` (AC 0x56).

Sent S->C with the player's talent-preset state. Handler 0x082304ad reads
(in order, on the bit-stream):

    u8  × 4        set_ids       preset ids, observed [0, 1, 2, 3]
                                 (stored at obj+0xb565c..+0xb565f)
    bool × 4       set_active    per-preset active flag — 4 bits
                                 (stored at obj+0xb5660..+0xb5663)
    for each of 4 sets:
        48 bits    talent_mask   read via 8b1d7c0(buf, 6); bits 0..44 are
                                 acquired-talent flags (one bool per talent,
                                 45 talents per preset), bits 45..47 are
                                 always read but never inspected (the inner
                                 loop only iterates eax=0..0x2c=45). The
                                 acquired flags land at
                                 obj+0xb5664 + set*45 + talent.

Total = 32 + 4 + 4*48 = 228 bits, so the 29-byte body ends with 4
padding bits. Verified against all 106 captures: every body parses with
slack=4b, set_ids=[0,1,2,3], all flags True, talent counts in the low
double digits.

The handler uses these arrays as one flat `talent_acquired[180]` table
(four blocks of 45). We surface them as 4 preset records each with a
list of 45 booleans, plus the 3-bit padding tail per block so the
bit_ranges line up in the UI tree.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field


_SETS = 4
_TALENTS_PER_SET = 45
_BITS_PER_SET = 48  # 45 talent bits + 3 bits ignored/padding (handler reads 6 bytes)


def _read_set(br: BitReader) -> dict:
    """One preset record: 45 talent_acquired bools followed by 3 unused
    padding bits (so each block consumes a whole 48-bit/6-byte chunk to
    match the handler's ReadBytes(6) call)."""
    start = br.pos
    out: dict[str, object] = {}
    talents_start = br.pos
    talents = [read_field(br, "bool", br.read_bool())
               for _ in range(_TALENTS_PER_SET)]
    br.last_read_start = talents_start
    out["talents"] = Variant("list", talents, 0xff,
                             (talents_start, br.pos))
    # 3 bits of intra-block padding — surfaced so the bit ranges align.
    pad_start = br.pos
    pad_bits = [br.read_bool() for _ in range(_BITS_PER_SET - _TALENTS_PER_SET)]
    br.last_read_start = pad_start
    out["padding"] = Variant("bits", pad_bits, 0xff, (pad_start, br.pos))
    br.last_read_start = start
    return out


class AcTalentsUpdateBody:
    """Parsed body of `ac_talents_update`. Mirrors the binary's bit-level
    wire sequence — see module docstring."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            ids_start = br.pos
            set_ids = [read_field(br, "u8", br.read_u8())
                       for _ in range(_SETS)]
            br.last_read_start = ids_start
            self.set_ids = Variant("list", set_ids, 0xff,
                                   (ids_start, br.pos))

            flags_start = br.pos
            set_active = [read_field(br, "bool", br.read_bool())
                          for _ in range(_SETS)]
            br.last_read_start = flags_start
            self.set_active = Variant("list", set_active, 0xff,
                                      (flags_start, br.pos))

            sets_start = br.pos
            sets: List[dict] = [_read_set(br) for _ in range(_SETS)]
            br.last_read_start = sets_start
            self.sets = Variant("list", sets, 0xff, (sets_start, br.pos))

            self.bits_consumed = br.pos
        except EOFError:
            self.ok = False
            self.bits_consumed = br.pos
        except Exception as e:
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"
            self.bits_consumed = br.pos

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcTalentsUpdateBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "set_ids"):
            return (f"AcTalentsUpdateBody({len(self._raw)}B{suffix} "
                    f"slack={slack}b)")
        ids = [v.value for v in self.set_ids.value]
        actives = [v.value for v in self.set_active.value]
        counts = [sum(1 for t in s["talents"].value if t.value)
                  for s in self.sets.value]
        parts = [f"{len(self._raw)}B{suffix}",
                 f"set_ids={ids}",
                 f"active={actives}",
                 f"acquired_per_set={counts}",
                 f"slack={slack}b"]
        return "AcTalentsUpdateBody(" + ", ".join(parts) + ")"
