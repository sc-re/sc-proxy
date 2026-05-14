"""Bit-stream parser for ac_vessel_strip_improper_battle (AC 0x42).

S→C notification that one or more vessel modules were stripped because
the player brought an "improper" loadout into battle (e.g. equipment
the league/queue doesn't allow). The handler at 0x08233d8c reads:

    u8  status                      (0 = OK; non-zero exits early
                                     into FUN_0822a308 event-pump
                                     wrapper, no further wire data)
    if status == 0:
        u1  has_vessel              (branch flag at 0x0823beb3)
        if has_vessel:
            u32 vessel_id           (stored at struct+0x28d8dc, then
                                     fed to FUN_086e42a0 and
                                     FUN_0832ed00 to invalidate the
                                     profile-cache vessel slot)
        u32 account_exp_pool        (always read at 0x0823bf05 —
                                     the player's current clearance
                                     score, the same number that comes
                                     through SCMD_USER_PROFILE_NOTIFICATION
                                     sub=6 and Atlas.accountExpPool;
                                     this tells the client what tier
                                     the player has been knocked back
                                     to / is still cleared for)

Observed: 49 captures across sessions, all status=0 has_vessel=0.
Values seen for the clearance field: 745, 750, 810, 1480, 26620 —
matching the same uids' Atlas clearance scores. The has_vessel=1
path is never observed in captures.
"""
from __future__ import annotations
from typing import Optional

from notification import BitReader


class AcVesselStripImproperBattleBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.status: int = 0
        self.has_vessel: Optional[bool] = None
        self.vessel_id: Optional[int] = None
        self.account_exp_pool: Optional[int] = None
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.status = br.read_u8()
            if self.status == 0:
                self.has_vessel = br.read_bool()
                if self.has_vessel:
                    self.vessel_id = br.read_u32()
                self.account_exp_pool = br.read_u32()
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = f" ERROR: {self.error}" if self.error else ""
        if self.status != 0:
            return (f"AcVesselStripImproperBattleBody({len(self._raw)}B, "
                    f"status={self.status} (failure), "
                    f"slack={slack}b{suffix})")
        parts = ["status=0", f"has_vessel={self.has_vessel}"]
        if self.vessel_id is not None:
            parts.append(f"vessel_id={self.vessel_id}")
        if self.account_exp_pool is not None:
            parts.append(f"clearance={self.account_exp_pool}")
        return (f"AcVesselStripImproperBattleBody({len(self._raw)}B, "
                f"{', '.join(parts)}, slack={slack}b{suffix})")
