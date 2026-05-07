"""Bit-stream parser for ac_vessel_change_equip_multi server-to-client response.

Shares handler 0x082352c8 with the single-equip variant; layout is
identical:
    u8   status
    u8be vessel_id
    if status == 0:
        35 × u8be slot_module_id
        cstring main_def_name (≤59) + u8 qty + u8 flag    (FUN_08926690 #1)
        cstring secondary_def_name + u8 qty + u8 flag      (FUN_08926690 #2)
        u1   has_inventory_update
        if has_inventory_update:
            u4 num_items
            num_items × inventory_item                     (same shape as
                                                            ac_player_inventory)

Across the four captures we have, the multi response is always
~64 KB — that's the inventory delta carrying the player's full
post-action inventory. Decoding the inventory delta works the same
way as in `ac_player_inventory_body`.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from notification import BitReader

from ac_vessel_change_equip_body import (
    _read_change_record, _read_inventory_item, _InventoryDelta,
)


class AcVesselChangeEquipMultiResponseBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.status: int = 0
        self.vessel_id: int = 0
        self.slots: List[int] = []
        self.main_change: Optional[Tuple[str, int, int]] = None
        self.secondary_change: Optional[Tuple[str, int, int]] = None
        self.has_inventory_update: bool = False
        self.inventory: Optional[_InventoryDelta] = None
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.status = br.read_u8()
            self.vessel_id = br.read_u64()
            if self.status == 0:
                self.slots = [br.read_u64() for _ in range(35)]
                self.main_change = _read_change_record(br)
                self.secondary_change = _read_change_record(br)
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
            return f"AcVesselChangeEquipMultiResponseBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        nonzero = sum(1 for s in self.slots if s != 0)
        inv_n = len(self.inventory.items) if self.inventory else 0
        chg = []
        if self.main_change and self.main_change[0]:
            chg.append(f"main={self.main_change[0]!r}")
        if self.secondary_change and self.secondary_change[0]:
            chg.append(f"secondary={self.secondary_change[0]!r}")
        chg_str = ", ".join(chg) if chg else "(no changes)"
        return (f"AcVesselChangeEquipMultiResponseBody({len(self._raw)}B, "
                f"status={self.status}, vessel=0x{self.vessel_id:x}, "
                f"slots={nonzero}/{len(self.slots)} fitted, "
                f"{chg_str}, inv_delta={inv_n}, slack={slack}b)")
