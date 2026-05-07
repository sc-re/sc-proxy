"""Opaque kaitai type for the AcPlayerInventory response body.

The handler at 0x08233968 reads:

  u4be num_items                                 (BitStream_ReadU32)
  num_items × {                                  (FUN_088ead70 inner read)
    u8be  item_id                                (BitStream_ReadU64v2)
    cstring  name (max 60 chars)                 (BitStream_ReadCStringLen)
    u4be  quantity                               (BitStream_ReadU32)
    u1   flag                                    (BitStream_ReadBit)
    u8be  misc                                   (BitStream_ReadU64)
  }
  u8 cur_size                                    (BitStream_ReadU8) — written
                                                 to *(state+0x94844)
  u4be max_size                                  (BitStream_ReadU32) — written
                                                 to *(state+0x94840)

Everything is bit-packed (cstrings inside the bag mean the cursor lands
at a non-byte-aligned position frequently). A trailing run of <8 padding
bits brings the body up to a byte boundary.

`item_id` looks like a server-side primary key (small dense u64,
typically < 2^28). `quantity` is 1 for unique gear and >1 for stacked
ammo / consumables. `flag` is set on a small subset of items — likely
"currently equipped on a vessel" or similar. `misc` is non-zero when
the item carries an expiry timestamp (in our captures it was 0 for all
items of two real players).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List

from notification import BitReader


@dataclass
class InventoryItem:
    item_id: int
    name: str
    quantity: int
    flag: bool
    misc: int

    def __repr__(self) -> str:
        extras = []
        if self.quantity != 1:
            extras.append(f"qty={self.quantity}")
        if self.flag:
            extras.append("flag")
        if self.misc:
            extras.append(f"misc=0x{self.misc:x}")
        suffix = (" " + " ".join(extras)) if extras else ""
        return f"#{self.item_id} {self.name!r}{suffix}"


def _read_cstring_max(br: BitReader, max_len: int) -> str:
    """Read up to max_len 8-bit chars terminated by NUL."""
    out = bytearray()
    for _ in range(max_len):
        b = br.read_u8()
        if b == 0:
            return out.decode("utf-8", errors="replace")
        out.append(b)
    return out.decode("utf-8", errors="replace")


class AcPlayerInventoryBody:
    """Kaitai-protocol opaque type for the inventory response body."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: str | None = None
        self.items: List[InventoryItem] = []
        self.cur_size: int | None = None
        self.max_size: int | None = None
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            n = br.read_u32()
            for _ in range(n):
                item_id = br.read_u64()
                name = _read_cstring_max(br, 60)
                quantity = br.read_u32()
                flag = br.read_bool()
                misc = br.read_u64()
                self.items.append(InventoryItem(item_id, name, quantity, flag, misc))
            self.cur_size = br.read_u8()
            self.max_size = br.read_u32()
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            head = (self._raw[:8].hex() if self._raw else "<empty>")
            return f"AcPlayerInventoryBody(<error: {self.error}> raw={head}…)"
        total_bits = len(self._raw) * 8
        slack = total_bits - self.bits_consumed
        n = len(self.items)
        # Show abridged item list — first 3, ellipsis, last 1, plus any
        # interesting flag/misc/qty>1 items so the response stays useful.
        unusual = [it for it in self.items[3:-1] if it.flag or it.misc or it.quantity != 1]
        sample = self.items[:3] + unusual[:5]
        if n > len(sample) + 1:
            sample.append("…")
        if n > 0:
            sample.append(self.items[-1])
        items_repr = ", ".join(s if isinstance(s, str) else repr(s) for s in sample)
        return (
            f"AcPlayerInventoryBody({len(self._raw)}B parsed, "
            f"{n} items, cur_size={self.cur_size}, max_size={self.max_size}, "
            f"slack={slack}b)\n  items=[{items_repr}]"
        )
