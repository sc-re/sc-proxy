"""Opaque kaitai type — body of `ac_load_initial_player_data` (AC 0).

The handler at 0x0823103b inside the AC dispatcher reads 22 fields from
the bit-stream:

  pos   tag   purpose (best-guess)
  ---   ---   ----------------------------------
   0    u64   field_0   (timestamp / session token)
   1    u32   field_1
   2    u32   field_2
   3    u64   uid
   4    cstr  nickname            (length-bounded ≤ ~60)
   5    u32   field_5
   6    u32   field_6
   7    u32   field_7
   8    BAG   bag_8                (factions / auras?)
   9    BAG   bag_9                (achievements?)
  10    u32   field_10
  11    u8    field_11
  12    u8    field_12
  13    i32   field_13
  14    BAG   bag_14               (player vessels?)
  15    BAG   bag_15               (inventory?)
  16    i32   field_16
  17    i32   field_17
  18    i32   field_18
  19    u64   field_19
  20    i32   field_20
  21    BAG   bag_21               (mail / leaderboards?)

The handler tolerates short bodies: each BitStream reader returns 0 and
sets a "lastReadOK=false" flag rather than throwing. We mirror that
here — on EOFError we stop, leaving subsequent fields as None and
recording how far we got in `.consumed_fields`.

Captured sizes range from 2B (echo-only) and 8B (~6 body bytes — only
the first read succeeds) all the way to 240 kB full-state responses.
"""
from __future__ import annotations
from typing import Any

from notification import BitReader, _read_bag, format_bag, Variant

# Field-read sequence per the binary's handler at 0x0823103b
_FIELD_SEQUENCE = [
    ("field_0",  "u64"),
    ("field_1",  "u32"),
    ("field_2",  "u32"),
    ("uid",      "u64"),
    ("nickname", "cstr"),
    ("field_5",  "u32"),
    ("field_6",  "u32"),
    ("field_7",  "u32"),
    ("bag_8",    "bag"),
    ("bag_9",    "bag"),
    ("field_10", "u32"),
    ("field_11", "u8"),
    ("field_12", "u8"),
    ("field_13", "i32"),
    ("bag_14",   "bag"),
    ("bag_15",   "bag"),
    ("field_16", "i32"),
    ("field_17", "i32"),
    ("field_18", "i32"),
    ("field_19", "u64"),
    ("field_20", "i32"),
    ("bag_21",   "bag"),
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
        # Pre-init every field so they exist regardless of how far we get.
        for name, _ in _FIELD_SEQUENCE:
            setattr(self, name, None)

        self.ok = True
        self.error: str | None = None
        self.consumed_fields = 0
        self.bits_remaining = 0

        if not self.raw:
            return  # 2B echo-only response — no body

        br = BitReader(self.raw)
        try:
            for name, tag in _FIELD_SEQUENCE:
                if tag == "u8":
                    val = br.read_u8()
                elif tag == "u32":
                    val = br.read_u32()
                elif tag == "i32":
                    val = br.read_i32()
                elif tag == "u64":
                    val = br.read_u64()
                elif tag == "cstr":
                    val = br.read_cstring(max_len=2048)
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
        if self.consumed_fields == 0 and not self.error:
            return "AcLoadInitialPlayerDataBody(empty)"
        head = f"AcLoadInitialPlayerDataBody(fields={self.consumed_fields}/{len(_FIELD_SEQUENCE)}"
        if self.error:
            head += f", err={self.error}"
        if not self.ok:
            head += ", truncated"
        # Only show the cheap scalar fields; bags can be huge.
        for name, tag in _FIELD_SEQUENCE:
            v = getattr(self, name, None)
            if v is None: continue
            if tag == "bag" and isinstance(v, dict):
                head += f", {name}=bag({len(v)})"
            else:
                head += f", {name}={v!r}"
        head += ")"
        return head
