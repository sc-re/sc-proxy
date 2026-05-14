"""Bit-stream parser for ac_use_blueprint server-to-client response.

Handler 0x0822c85a reads, when status == 0:
    u1   status
    cstring blueprint_def_name              (e.g. "BP_Iridium_plate")
    u1   ui_flag                            (whether to fire UI toast)
    bag  result                             (notification.py-style bag)
    cstring secondary_name
    u1   misc_a
    u1   num_item_ids
    num_item_ids × u4 item_id
    u1   has_extra
    if has_extra: i4 a + u4 b + u8 c        (overflow / bonus payload)

The bag is bit-aligned so the trailing fields land at non-byte
boundaries — that's why this can't be expressed in native kaitai.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, _read_bag, format_bag


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


class AcUseBlueprintResponseBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.status: int = 0
        self.blueprint_def_name: str = ""
        self.ui_flag: bool = False
        self.result_bag: dict = {}
        self.secondary_name: str = ""
        self.misc_a: int = 0
        self.item_ids: List[int] = []
        self.has_extra: bool = False
        self.extra_a: Optional[int] = None
        self.extra_b: Optional[int] = None
        self.extra_c: Optional[int] = None
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.status = br.read_u8()
            if self.status == 0:
                self.blueprint_def_name = _read_cstring(br, 256)
                self.ui_flag = br.read_bool()
                self.result_bag = _read_bag(br)
                self.secondary_name = _read_cstring(br, 256)
                self.misc_a = br.read_u8()
                n = br.read_u8()
                for _ in range(n):
                    self.item_ids.append(br.read_u32())
                self.has_extra = br.read_bool()
                if self.has_extra:
                    self.extra_a = br.read_i32()
                    self.extra_b = br.read_u32()
                    self.extra_c = br.read_u64()
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcUseBlueprintResponseBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        bag_repr = format_bag(self.result_bag) if self.result_bag else "{}"
        if len(bag_repr) > 80:
            bag_repr = bag_repr[:80] + "…"
        extra = ""
        if self.has_extra:
            extra = f", extra=({self.extra_a}, {self.extra_b}, {self.extra_c})"
        return (f"AcUseBlueprintResponseBody({len(self._raw)}B, "
                f"status={self.status}, blueprint={self.blueprint_def_name!r}, "
                f"ui={self.ui_flag}, bag={bag_repr}, "
                f"secondary={self.secondary_name!r}, items={self.item_ids[:8]}"
                f"{extra}, slack={slack}b)")
