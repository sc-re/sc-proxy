"""Bit-stream parser for `ac_ship_quests` (AC 0x1d).

Sent S->C with the player's per-ship quest record(s). Handler 0x0822bdf8
(decompiled in Ghidra) first clears the existing record array (the count
lives at profile+0xb5600, records at profile+0xb4a80, each 0x5c=92 B),
then reads (bit-stream order):

    u1   loaded         single-bit flag, stored at profile+0xb5610
    u8   num_records    number of records that follow; always 1 in our
                        captures (one record per ship)
    for each record (FUN_088f9340 zero-inits the 92-byte slot first):
        u8   field_00       (-> rec+0x00; small int)
        u8   field_04       (-> rec+0x04; small int)
        u32  field_08       (-> rec+0x08; observed 0x118 / 0x128 / 0x224)
        u64  primary_iid    (-> rec+0x0c; ReadU64; 0 when no active quest)
        // rec+0x14 is filled from a global double clock (NOT a wire read)
        u64 x 8  iids       (-> rec+0x1c, +0x24, ... ; ReadU64v2;
                             quest objective / reward instance ids;
                             all 0 when no active quest)

Per-record bit cost = 8+8+32+64 + 8*64 = 624 bits. With the 1+8-bit
header that's 633 bits in a 640-bit (80-byte) body, so every capture
ends with exactly 7 bits of padding - verified across all 106 captures.

The old body only read `loaded + num_records` and stopped, so 78 bytes
per record (the actual quest payload) went unparsed.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field


_IIDS_PER_RECORD = 8


def _read_record(br: BitReader) -> dict:
    """One per-ship quest record. Field names use rec+<offset> suffixes
    where the exact semantics aren't pinned down yet (these correspond
    to the 92-byte record struct the binary writes them into)."""
    start = br.pos
    out: dict[str, object] = {}
    out["field_00"]    = read_field(br, "u8",  br.read_u8())
    out["field_04"]    = read_field(br, "u8",  br.read_u8())
    out["field_08"]    = read_field(br, "u32", br.read_u32())
    out["primary_iid"] = read_field(br, "u64", br.read_u64())
    iids_start = br.pos
    iids = [read_field(br, "u64", br.read_u64())
            for _ in range(_IIDS_PER_RECORD)]
    br.last_read_start = iids_start
    out["iids"] = Variant("list", iids, 0xff, (iids_start, br.pos))
    br.last_read_start = start
    return out


class AcShipQuestsBody:
    """Parsed body of `ac_ship_quests`. Mirrors the binary's wire
    sequence - see module docstring. The 1-bit `loaded` flag means the
    rest of the body follows immediately bit-misaligned."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.loaded      = read_field(br, "bool", br.read_bool())
            self.num_records = read_field(br, "u8",   br.read_u8())

            recs_start = br.pos
            records: List[dict] = [_read_record(br)
                                   for _ in range(self.num_records.value)]
            br.last_read_start = recs_start
            self.records = Variant("list", records, 0xff,
                                   (recs_start, br.pos))
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
            return f"AcShipQuestsBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "num_records"):
            return (f"AcShipQuestsBody({len(self._raw)}B{suffix} "
                    f"slack={slack}b)")
        parts = [f"{len(self._raw)}B{suffix}",
                 f"loaded={self.loaded.value}",
                 f"num_records={self.num_records.value}"]
        if hasattr(self, "records"):
            actives = sum(1 for r in self.records.value
                          if r["primary_iid"].value)
            parts.append(f"active={actives}")
        parts.append(f"slack={slack}b")
        return "AcShipQuestsBody(" + ", ".join(parts) + ")"
