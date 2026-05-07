"""Bit-stream parser for ac_vessel_change_equip_multi server-to-client response.

The multi-change response shares handler 0x082352c8 with the single-equip
variant but, after the standard prefix, includes a per-change list and a
much longer tail (sometimes the entire inventory at ~65 KB).

Confirmed prefix (same as single-equip):
    u8   status                 (0 = success)
    u8be vessel_id
    35 × u8be slot_module_id    (full vessel loadout after the changes)

Trailing region observed in 64967-byte capture:
    Byte 289 onwards: pairs of `cstring item_name + u1 + u1`, e.g.
        "WeaponMod_RailPerfect_Mk1\0\x01\x01"
        "SpaceMissile_AAMSlow_T5_Mk3\0\x01\x01"
    Then a binary trailer with cs0-encoded module ids and a long
    inventory delta.

Without a count field for the cstring list, we just scan forward
extracting any clean cstring at the byte cursor while we can; once we
hit non-printable bytes we stop and report the rest as opaque.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from notification import BitReader


@dataclass
class _ChangeRecord:
    item_name: str
    flag_a: int
    flag_b: int


class AcVesselChangeEquipMultiResponseBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.status: int = 0
        self.vessel_id: int = 0
        self.slots: List[int] = []
        self.changes: List[_ChangeRecord] = []
        self.tail_bytes: bytes = b""
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.status = br.read_u8()
            self.vessel_id = br.read_u64()
            if self.status == 0:
                self.slots = [br.read_u64() for _ in range(35)]
                # the rest is byte-aligned; switch to byte indexing
                byte_off = br.pos // 8
                # scan for cstring entries while bytes look like printable ASCII
                while byte_off < len(self._raw):
                    end = self._raw.find(b"\x00", byte_off)
                    if end < 0 or end == byte_off:
                        break
                    name = self._raw[byte_off:end]
                    if not all(0x20 <= b < 0x7F for b in name):
                        break
                    if end + 2 >= len(self._raw):
                        break
                    flag_a = self._raw[end + 1]
                    flag_b = self._raw[end + 2]
                    self.changes.append(
                        _ChangeRecord(name.decode("ascii"), flag_a, flag_b))
                    byte_off = end + 3
                self.tail_bytes = self._raw[byte_off:]
            self.bits_consumed = br.pos + (len(self._raw) - br.pos // 8) * 8 - len(self.tail_bytes) * 8
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcVesselChangeEquipMultiResponseBody(<error: {self.error}>)"
        nonzero = sum(1 for s in self.slots if s)
        names = [c.item_name for c in self.changes]
        return (f"AcVesselChangeEquipMultiResponseBody({len(self._raw)}B, "
                f"status={self.status}, vessel=0x{self.vessel_id:x}, "
                f"slots={nonzero}/{len(self.slots)} fitted, "
                f"changes={names}, tail={len(self.tail_bytes)}B)")
