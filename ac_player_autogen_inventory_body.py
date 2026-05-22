"""Bit-stream parser for `ac_player_autogen_inventory` (AC 0x24).

Sent S→C with the player's catalogue of *autogen* items — the
procedurally-generated modular gear whose stats are rolled rather than
fixed. The handler is at 0x082342e0; it reads a u32 record count, then
constructs (FUN_088eb0f0) and deserializes (FUN_088eb190) one record per
entry, and finishes with the inventory's used/total capacity.

Per-record reader FUN_088eb190 reads, in wire order (all big-endian, on
the same MSB-first bit-stream the other AC bodies use, so reads are
frequently sub-byte-aligned):

    u64  iid              item instance id        (ReadU64v2 @8b1c360 -> obj+0x00)
    i32  unknown_0x08     small enum, 0..4, mostly 0 (ReadI32 @8b1c230 -> obj+0x08)
    i32  unknown_0x20     mostly 0; occasionally a few-hundred-to-1000+
                          magnitude on a subset of items (ReadI32 -> obj+0x20)
    BAG  rolls            indexed property bag of the item's rolled stat
                          parameters (Bag_Deserialize @8b1ed60 -> obj+0x0c);
                          entries are i32 stat ids/tiers interleaved with
                          f32 magnitudes (0.0-1.0 normalised rolls).

Tail, after the record loop:

    u8   cur_size         autogen items currently held
    u32  max_size         autogen-inventory capacity

Verified against all 98 captures: every body parses with <8 bits of
trailing slack (byte-alignment padding). The two i32 fields keep
`unknown_0x<offset>` names recording their record-struct offset, since
their meaning is not yet confirmed.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field, _read_bag


def _read_item_record(br: BitReader) -> dict:
    """One autogen-item record (FUN_088eb190). Every field is wrapped via
    read_field()/Variant so the GUI tree picks up its bit_range."""
    start = br.pos
    out: dict[str, object] = {}
    out["iid"]           = read_field(br, "u64", br.read_u64())
    out["unknown_0x08"]  = read_field(br, "i32", br.read_i32())
    out["unknown_0x20"]  = read_field(br, "i32", br.read_i32())
    # Indexed property bag of the rolled stat parameters. read_field picks
    # up the bag's full span because _read_bag restores last_read_start.
    out["rolls"]         = read_field(br, "bag", _read_bag(br))
    br.last_read_start = start
    return out


class AcPlayerAutogenInventoryBody:
    """Parsed body of `ac_player_autogen_inventory`. Mirrors the binary's
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
            self.count = read_field(br, "u32", br.read_u32())

            items_start = br.pos
            items: List[dict] = [
                _read_item_record(br) for _ in range(self.count.value)
            ]
            br.last_read_start = items_start
            self.items = Variant("list", items, 0xff, (items_start, br.pos))

            self.cur_size = read_field(br, "u8", br.read_u8())
            self.max_size = read_field(br, "u32", br.read_u32())
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
            return f"AcPlayerAutogenInventoryBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "count"):
            return (f"AcPlayerAutogenInventoryBody({len(self._raw)}B{suffix} "
                    f"slack={slack}b)")
        n = self.count.value
        parts = [f"{len(self._raw)}B{suffix}", f"count={n}"]
        if hasattr(self, "cur_size"):
            parts.append(f"cur_size={self.cur_size.value}")
        if hasattr(self, "max_size"):
            parts.append(f"max_size={self.max_size.value}")
        parts.append(f"slack={slack}b")
        return "AcPlayerAutogenInventoryBody(" + ", ".join(parts) + ")"
