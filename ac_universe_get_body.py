"""Opaque kaitai type for the AcUniverseGet response body.

Names below are pulled from the Lua-binding code at FUN_0891de50
(zone → Lua table) and FUN_08921210 (top-level "zones"/"unid" wrapper),
which expose exactly the field set returned by `MasterServer.UniverseGet`.

Outer handler at 0x0822d533 → FUN_089214b0:

    u8  unid                                   (status; pushed as "unid")
    u2  num_zones                              (the loop bound)
    num_zones × {
      u2   zone_slot                           (outer index — used as
                                                array slot; equals zoneId
                                                in observed captures)
      -- FUN_0891e800 inner reader from here:
      u2   zoneId                              (pushed to Lua as "zoneId")
      u1   has_conflict                        ("hasConflict")
      u8   unknown_u64_at_offset_8             (read but not exposed by
                                                MasterServer.UniverseGet —
                                                possibly a legacy field)
      f32  retention_factor                    ("retentionFactor")
      u1   is_civilian                         ("isCivilian")
      u8   civilian_time                       ("civilianTime", u64
                                                Lua-userdata timestamp)
      i4   race                                ("race", −1 for empty)
      u1   enable_logic                        ("enableLogic")
      u8   owner                               ("owner", clan id u64)
      f32  owner_pressure_total                Lua: ownerPressureReal =
                                               owner_pressure_total − owner_pressure_virtual
      f32  owner_pressure_virtual              "ownerPressureVirtual"
      u4   num_rivals
      num_rivals × {                           ("rivals" entries)
        u8   cid                               ("cid")
        f32  pressure_total                    Lua: pressureReal =
                                               pressure_total − pressure_virtual
        f32  pressure_virtual                  "pressureVirtual"
      }
    }

`hasConflict`, `isCivilian`, `enableLogic` are stored as u1 bits in the
bit-stream (the layout is otherwise byte-aligned, but those three flags
make every per-zone record 387 + 97·N bits, breaking byte alignment).

The wire splits each "real" pressure into a (total, virtual) pair so the
client can render a per-clan virtual-pressure bar in addition to the
attributed-pressure number; Lua only exposes the difference and the
virtual fraction directly.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from notification import BitReader


@dataclass
class UniverseRival:
    cid: int
    pressure_real: float       # = wire_total - wire_virtual
    pressure_virtual: float

    def short(self) -> str:
        return (f"cid=0x{self.cid:x} R={self.pressure_real:.1f}/"
                f"V={self.pressure_virtual:.1f}")


@dataclass
class UniverseZone:
    zone_slot: int                  # outer u2 — array slot index
    zone_id: int                    # inner u2 — Lua "zoneId" field
    has_conflict: bool
    unknown_u64: int
    retention_factor: float
    is_civilian: bool
    civilian_time: int
    race: int
    enable_logic: bool
    owner: int
    owner_pressure_real: float          # = wire_total - wire_virtual
    owner_pressure_virtual: float
    rivals: List[UniverseRival] = field(default_factory=list)

    def short(self) -> str:
        flags = []
        if self.has_conflict: flags.append("conflict")
        if self.is_civilian: flags.append("civilian")
        if self.enable_logic: flags.append("logic")
        flag_str = ",".join(flags) if flags else "-"
        return (
            f"#{self.zone_id} race={self.race} {flag_str} "
            f"owner=0x{self.owner:x} retention={self.retention_factor:.3f} "
            f"R={self.owner_pressure_real:.1f}/V={self.owner_pressure_virtual:.1f} "
            f"+{len(self.rivals)} rivals"
        )


class AcUniverseGetBody:
    """Decoded AcUniverseGet response body, structured to match the field
    set returned by the Lua `MasterServer.UniverseGet` wrapper."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: str | None = None
        self.unid: int | None = None
        self.zones: List[UniverseZone] = []
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.unid = br.read_u8()
            num_zones = br.read_u16()
            for _ in range(num_zones):
                zone_slot = br.read_u16()
                zone_id = br.read_u16()
                has_conflict = br.read_bool()
                unknown_u64 = br.read_u64()
                retention_factor = br.read_f32()
                is_civilian = br.read_bool()
                civilian_time = br.read_u64()
                race = br.read_i32()
                enable_logic = br.read_bool()
                owner = br.read_u64()
                owner_pressure_total = br.read_f32()
                owner_pressure_virtual = br.read_f32()
                num_rivals = br.read_u32()
                rivals = []
                for _ in range(num_rivals):
                    cid = br.read_u64()
                    rp_total = br.read_f32()
                    rp_virtual = br.read_f32()
                    rivals.append(UniverseRival(cid, rp_total - rp_virtual, rp_virtual))
                self.zones.append(UniverseZone(
                    zone_slot, zone_id, has_conflict, unknown_u64,
                    retention_factor, is_civilian, civilian_time, race,
                    enable_logic, owner,
                    owner_pressure_total - owner_pressure_virtual,
                    owner_pressure_virtual, rivals,
                ))
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcUniverseGetBody(<error: {self.error}> raw={self._raw[:8].hex()}…)"
        slack = len(self._raw) * 8 - self.bits_consumed
        head = (f"AcUniverseGetBody({len(self._raw)}B, unid={self.unid}, "
                f"{len(self.zones)} zones, slack={slack}b)")
        body = "\n    ".join(z.short() for z in self.zones[:6])
        if len(self.zones) > 6:
            body += f"\n    … {len(self.zones) - 6} more"
        return f"{head}\n    {body}"
