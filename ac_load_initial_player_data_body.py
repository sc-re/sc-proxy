"""Opaque kaitai type — body of `ac_load_initial_player_data` (AC 0).

WIRE FORMAT — head of the bit-stream the handler at 0x0823103b walks:

  pos   tag      addr        stored at        notes
  ---   ------   ----------  ---------------  ------------------------
   0    u64      0x08231044
   1    u32      0x08231050  endpoint+0x5f8
   2    u1       0x08231064                   early-return error gate
   3    u32      0x0823108e  endpoint+0x28e77c
   4    u1       0x082310a8  endpoint+0xb632c
   5    u64      0x082310bc  endpoint+0xb6324  (NOT the player's uid in
                                               real captures — empirically
                                               zero in 240 kB bodies)
   6    cstr60   0x082310ee                   60-byte length-bound buffer
                                               (NOT the player's nickname —
                                               empirically empty in 240 kB
                                               bodies; the nickname lives in
                                               SCMD_AUTH_ACK / ac_player_
                                               credentials instead)

…then 22 more reads (u32, BAG, i32, u8, etc.) which we no longer
attempt to enumerate, because between every pair of visible reader
CALLs the handler invokes deep sub-readers that *also consume bits*:

  FUN_088fc1e0 — reads 3×cstr256 + 5×u32 + 3×f32 + 2×u1 + u64 +
                 four count-prefixed lists, in a single call.
  FUN_088fcea0, FUN_088fe1c0, FUN_088fe450 — similar shapes.

So a linear walk past field 6 immediately drifts off the real cursor
position; values past that point are garbage. Properly modelling those
sub-readers is a multi-session RE task (each is hundreds of lines of
dense pcode and several layers deep). Until then this opaque type only
exposes the first 7 fields and stops.

The handler tolerates short bodies via its m_lastReadOK flag — each
reader returns 0 on overflow rather than throwing. We mirror that by
catching EOFError on every field and stopping. Sizes range from 2 B
(echo-only) and 8 B (only first u64 read succeeds) to ~240 kB full-
state responses.
"""
from __future__ import annotations
from typing import Any

from notification import BitReader, _read_bag, format_bag, Variant

# Field-read sequence — only the prefix that's known reliable. Past field
# `text_6` the handler invokes deep sub-readers that consume bits we
# don't model, so any read past that point would yield misaligned junk.
# (See the module docstring for the full 29-step list and why we stop.)
_FIELD_SEQUENCE = [
    ("field_0",  "u64"),     # 0x08231044  ReadU64
    ("field_1",  "u32"),     # 0x08231050  ReadU32           → endpoint+0x5f8
    ("flag_2",   "u1"),      # 0x08231064  ReadBit           early-error gate
    ("field_3",  "u32"),     # 0x0823108e  ReadU32           → endpoint+0x28e77c
    ("flag_4",   "u1"),      # 0x082310a8  ReadBit           → endpoint+0xb632c
    ("field_5",  "u64"),     # 0x082310bc  ReadU64           → endpoint+0xb6324
    ("text_6",   "cstr60"),  # 0x082310ee  ReadCStringLen(60)
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
        if not self.raw:
            return "AcLoadInitialPlayerDataBody(empty body)"
        if self.consumed_fields == 0:
            return f"AcLoadInitialPlayerDataBody({len(self.raw)}B, header too short)"
        head = f"AcLoadInitialPlayerDataBody({len(self.raw)}B"
        if self.consumed_fields < len(_FIELD_SEQUENCE):
            head += f", head={self.consumed_fields}/{len(_FIELD_SEQUENCE)}"
        for name, _ in _FIELD_SEQUENCE[: self.consumed_fields]:
            head += f" {name}={getattr(self, name)!r}"
        # Be honest about what we don't decode, in one phrase rather than 22 None= lines.
        if len(self.raw) > 256:
            head += " <body+remainder not decoded; sub-readers consume bits>"
        head += ")"
        return head
