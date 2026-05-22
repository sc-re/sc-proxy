"""Opaque kaitai type — `u1 + u1 + bag` body shape for ac_mm_info.

ac_mm_info (AC 0x04) reports matchmaking-queue state. Handler 0x08231dbc
reads two 1-bit bools, then a property bag (reader sequence
`ReadBool, ReadBool, Bag_Deserialize`). Because the two leading bits
leave the cursor sub-byte aligned, the bag is bit-misaligned — the plain
byte-aligned `bag_payload` mis-reads it (its u32 num_entries swallows the
prefix bits, giving a garbage count and a bogus variant tag downstream).

The bag carries keys like `clientsInQueue`, `averageTimeInQueue`,
`maxTimeInQueue`, `playersByMMValue`. Verified against all 63 S->C
captures: every body parses as flag1 + flag2 + bag with <8 bits trailing
slack. The two flags are always present and the bag is read
unconditionally (matching the handler's linear read sequence).

Decoding delegates to `notification._read_bag` so we don't duplicate the
variant-tag table here.
"""
from __future__ import annotations

from notification import BitReader, _read_bag, format_bag, Variant


class AcMmInfoBody:
    __slots__ = ("_io", "raw", "flag1", "flag2", "bag", "ok", "error")

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self.raw: bytes = _io.read_bytes_full()
        self.flag1: bool = False
        self.flag2: bool = False
        self.bag: dict[str, Variant] = {}
        try:
            br = BitReader(self.raw)
            self.flag1 = br.read_bool()
            self.flag2 = br.read_bool()
            self.bag = _read_bag(br)
            self.ok = True
            self.error: str | None = None
        except Exception as e:
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if not self.ok:
            return (f"AcMmInfoBody(<error: {self.error}> "
                    f"flag1={self.flag1} flag2={self.flag2} "
                    f"raw={self.raw[:8].hex()}…)")
        return (f"AcMmInfoBody(flag1={self.flag1}, flag2={self.flag2}, "
                f"{format_bag(self.bag)})")
