"""Bit-stream parsers for ac_vessel_change_equip in both directions.

C→S request (handler-implicit, 17B observed):
    u8be vessel_id
    u8   slot_idx
    u8be module_id

S→C response (handler 0x082352c8, 296B observed):
    u8   status                         (0 = success)
    u8be vessel_id
    if status == 0:
        35 × u8be slot_module_id        (full vessel loadout after change)
        u1  has_inventory_update
        if has_inventory_update:
            u4  num_items
            num_items × {                (same record shape as ac_player_inventory)
                u8be item_id
                cstring  name (≤60 chars)
                u4   quantity
                u1   flag
                u8be misc
            }

The same handler is also bound to ac_vessel_change_equip_multi (AC ID 52);
both share the layout above.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from notification import BitReader


# ── shared helper ────────────────────────────────────────────────────────────
def _read_inventory_item(br: BitReader):
    item_id = br.read_u64()
    name = bytearray()
    for _ in range(60):
        b = br.read_u8()
        if b == 0:
            break
        name.append(b)
    quantity = br.read_u32()
    flag = br.read_bool()
    misc = br.read_u64()
    return (item_id, name.decode("utf-8", errors="replace"), quantity, flag, misc)


# ── C→S request body ────────────────────────────────────────────────────────
class AcVesselChangeEquipRequestBody:
    """Client request: equip a single module into a slot."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.vessel_id: int = 0
        self.slot_idx: int = 0
        self.module_id: int = 0
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.vessel_id = br.read_u64()
            self.slot_idx = br.read_u8()
            self.module_id = br.read_u64()
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcVesselChangeEquipRequestBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        return (f"AcVesselChangeEquipRequest(vessel=0x{self.vessel_id:x}, "
                f"slot={self.slot_idx}, module=0x{self.module_id:x}, "
                f"slack={slack}b)")


# ── S→C response body ───────────────────────────────────────────────────────
@dataclass
class _InventoryDelta:
    items: List[tuple] = field(default_factory=list)


class AcVesselChangeEquipResponseBody:
    """Server response: status + full vessel loadout (35 slots) + optional
    inventory delta. Same handler is reused for ac_vessel_change_equip_multi."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.status: int = 0
        self.vessel_id: int = 0
        self.slots: List[int] = []
        self.has_inventory_update: bool = False
        self.inventory: Optional[_InventoryDelta] = None
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.status = br.read_u8()
            self.vessel_id = br.read_u64()
            if self.status == 0:
                self.slots = [br.read_u64() for _ in range(35)]
                self.has_inventory_update = br.read_bool()
                if self.has_inventory_update:
                    n = br.read_u32()
                    inv = _InventoryDelta()
                    for _ in range(n):
                        inv.items.append(_read_inventory_item(br))
                    self.inventory = inv
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcVesselChangeEquipResponseBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        nonzero = sum(1 for s in self.slots if s != 0)
        inv_n = len(self.inventory.items) if self.inventory else 0
        return (f"AcVesselChangeEquipResponse({len(self._raw)}B, "
                f"status={self.status}, vessel=0x{self.vessel_id:x}, "
                f"slots={nonzero}/{len(self.slots)} fitted, "
                f"inv_delta={inv_n}, slack={slack}b)")
