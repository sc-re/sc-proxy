"""Opaque kaitai type — body of `ac_load_initial_player_data` (AC 0).

WIRE FORMAT — 29-step bit-stream the handler at 0x0823103b walks:

  pos   tag    addr        notes
  ---   ----   ----------  ----------------------------------
   0    u64    0x08231044
   1    u32    0x08231050  → stored at endpoint+0x5f8
   2    u1     0x08231064  early-return error gate
   3    u32    0x0823108e
   4    u1     0x082310a8
   5    u64    0x082310bc
   6    cstr60 0x082310ee  60-byte length-bound buffer
   7    u32    0x082311f5
   8    u32    0x08231362
   9    u32    0x082314c9
  10    BAG    0x082315bb
  11    BAG    0x08231648
  12    u32    0x082316c5
  13    u1     0x08231703
  14    u8     0x08231717
  15    u8     0x08231736
  16    i32    0x08231747
  17    u1     0x08231755
  18    BAG    0x0823177b
  19    BAG    0x082317a7
  20    i32    0x082317af
  21    i32    0x082317bd
  22    u1     0x082317cb
  23    i32    0x082317d9
  24    u64    0x0823181c
  25    i32    0x08231a01
  26    u1     0x08231a15
  27    BAG    0x08231a2d
  28    u8     0x08231a91

KNOWN LIMITATIONS:
* Between the visible reader CALLs the handler invokes per-section
  helpers (FUN_0824c9f0, FUN_08249a80, FUN_088fc1e0, FUN_088fcea0,
  FUN_088fe1c0, FUN_088fe450) that *also consume bits from the same
  stream*. Without recursively reverse-engineering each, our linear
  walk drifts after the first BAG — 240 kB captures parse cleanly up
  through field 9 (the third u32) and then diverge from the binary's
  cursor, so bag_10 onward show garbage.
* The handler tolerates short bodies via its m_lastReadOK flag — each
  reader returns 0 on overflow rather than throwing. We mirror that by
  catching EOFError on every field and stopping.
* Sizes range from 2 B (echo-only) and 8 B (only first u64 read
  succeeds) to ~240 kB full-state responses.
"""
from __future__ import annotations
from typing import Any

from notification import BitReader, _read_bag, format_bag, Variant

# Field-read sequence per the binary's handler at 0x0823103b. Re-extracted
# after discovering 0x08b1b6d0 is a 2nd ReadBit alias the earlier walker
# missed; the bit reads are critical because the bit-stream cursor would
# otherwise drift and break every subsequent read.
_FIELD_SEQUENCE = [
    ("field_0",   "u64"),    # 0x08231044  ReadU64
    ("field_1",   "u32"),    # 0x08231050  ReadU32
    ("flag_2",    "u1"),     # 0x08231064  ReadBit
    ("field_3",   "u32"),    # 0x0823108e  ReadU32
    ("flag_4",    "u1"),     # 0x082310a8  ReadBit
    ("uid",       "u64"),    # 0x082310bc  ReadU64
    ("nickname",  "cstr60"), # 0x082310ee  ReadCStringLen(60)
    ("field_7",   "u32"),    # 0x082311f5  ReadU32
    ("field_8",   "u32"),    # 0x08231362  ReadU32
    ("field_9",   "u32"),    # 0x082314c9  ReadU32
    ("bag_10",    "bag"),    # 0x082315bb  Bag_Deserialize
    ("bag_11",    "bag"),    # 0x08231648  Bag_Deserialize
    ("field_12",  "u32"),    # 0x082316c5  ReadU32
    ("flag_13",   "u1"),     # 0x08231703  ReadBit
    ("field_14",  "u8"),     # 0x08231717  ReadU8
    ("field_15",  "u8"),     # 0x08231736  ReadU8
    ("field_16",  "i32"),    # 0x08231747  ReadI32
    ("flag_17",   "u1"),     # 0x08231755  ReadBit
    ("bag_18",    "bag"),    # 0x0823177b  Bag_Deserialize
    ("bag_19",    "bag"),    # 0x082317a7  Bag_Deserialize
    ("field_20",  "i32"),    # 0x082317af  ReadI32
    ("field_21",  "i32"),    # 0x082317bd  ReadI32
    ("flag_22",   "u1"),     # 0x082317cb  ReadBit
    ("field_23",  "i32"),    # 0x082317d9  ReadI32
    ("field_24",  "u64"),    # 0x0823181c  ReadU64
    ("field_25",  "i32"),    # 0x08231a01  ReadI32
    ("flag_26",   "u1"),     # 0x08231a15  ReadBit
    ("bag_27",    "bag"),    # 0x08231a2d  Bag_Deserialize
    ("field_28",  "u8"),     # 0x08231a91  ReadU8
]


class AcLoadInitialPlayerDataBody:
    """Bit-stream parse of AC_LOAD_INITIAL_PLAYER_DATA's body.

    Public attributes:
        raw                 : raw bytes the kaitai stream handed us
        ok                  : True if every field decoded without EOFError
        consumed_fields     : number of fields successfully parsed
        bits_remaining      : trailing bits left after the parse
        error               : exception text if anything else broke
        + one attribute per documented field name (None when truncated)
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self.raw: bytes = _io.read_bytes_full()
        # Don't pre-init fields — only the ones we actually parse should
        # appear as attributes, so getattr(obj, 'fieldN') raises
        # AttributeError when truncated rather than yielding None garbage.
        self.ok = True
        self.error: str | None = None
        self.consumed_fields = 0
        self.bits_remaining = 0

        if not self.raw:
            return  # 2B echo-only response — no body

        br = BitReader(self.raw)
        try:
            for name, tag in _FIELD_SEQUENCE:
                if tag == "u1":
                    val = br.read_bool()
                elif tag == "u8":
                    val = br.read_u8()
                elif tag == "u32":
                    val = br.read_u32()
                elif tag == "i32":
                    val = br.read_i32()
                elif tag == "u64":
                    val = br.read_u64()
                elif tag.startswith("cstr"):
                    # cstrN means up-to-N-byte length-bounded read. The
                    # handler's BitStream_ReadCStringLen reads byte-by-
                    # byte and stops at the FIRST of: NUL, the byte cap,
                    # or end-of-stream. Match that semantics here so the
                    # cursor advances by min(len(string)+1, cap) bytes.
                    cap = int(tag[4:]) if tag != "cstr" else 2048
                    val = br.read_cstring(max_len=cap)
                elif tag == "bag":
                    val = _read_bag(br)
                else:
                    raise ValueError(f"unhandled tag {tag!r} for {name!r}")
                setattr(self, name, val)
                self.consumed_fields += 1
        except EOFError:
            # Short body — handler in the binary tolerates this silently
            # via its m_lastReadOK flag.
            self.ok = False
        except Exception as e:
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"
        self.bits_remaining = br.remaining()

    def _fetch_instances(self):
        pass  # No lazy instances.

    def __repr__(self) -> str:
        # The big captures' linear field walk diverges after field 9
        # (handler dispatches into per-section sub-readers we don't model).
        # Showing the bogus values past that point is misleading — instead,
        # just summarise truncation and only print fully-consumed fields.
        if self.consumed_fields == 0 and not self.error:
            if not self.raw:
                return "AcLoadInitialPlayerDataBody(empty body)"
            return f"AcLoadInitialPlayerDataBody(too short: {len(self.raw)}B body, no fields parsed)"
        # Truncation summary; never print fields beyond consumed_fields.
        # We also stop at the first BAG since past that the cursor is
        # known-unreliable for big captures.
        first_bag = next(
            (i for i, (n, t) in enumerate(_FIELD_SEQUENCE) if t == "bag"),
            len(_FIELD_SEQUENCE),
        )
        safe = min(self.consumed_fields, first_bag)
        head = f"AcLoadInitialPlayerDataBody({len(self.raw)}B"
        if safe < self.consumed_fields:
            head += f", parsed_fields={safe} (cursor unreliable past first BAG)"
        elif self.consumed_fields < len(_FIELD_SEQUENCE):
            head += f", truncated at field {self.consumed_fields}/{len(_FIELD_SEQUENCE)}"
        for name, tag in _FIELD_SEQUENCE[:safe]:
            v = getattr(self, name, None)
            if tag == "bag" and isinstance(v, dict):
                head += f" {name}=bag({len(v)})"
            else:
                head += f" {name}={v!r}"
        head += ")"
        return head
