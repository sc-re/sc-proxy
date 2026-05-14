"""Bit-stream parser for ac_leaderboard_get_descs (AC 0xde).

S→C response to MasterServer_LeaderboardGetDescs. The body is:

    u32 count
    count × bag         ; one property bag per leaderboard descriptor

Each descriptor bag carries that leaderboard's config — observed keys:
name, entityType, dir, expiresAt, renewalInterval, expAction,
lastDecay, decayInterval, decayPower, rewards (a nested bag).

The previous schema modelled this as `u4be header + bag_payload`, which
read only the first of the `count` bags and left the rest of the body
unparsed; this opaque type reads every descriptor.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, _read_bag


class AcLeaderboardGetDescsBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.count: int = 0
        self.descs: List[dict] = []
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.count = br.read_u32()
            for _ in range(self.count):
                self.descs.append(_read_bag(br))
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = f" ERROR: {self.error}" if self.error else ""
        names = [d["name"].value for d in self.descs
                 if "name" in d and hasattr(d["name"], "value")]
        preview = ", ".join(names[:6])
        if len(names) > 6:
            preview += f", … +{len(names) - 6}"
        return (f"AcLeaderboardGetDescsBody({len(self._raw)}B, "
                f"count={self.count}, descs={len(self.descs)}={{{preview}}}, "
                f"slack={slack}b{suffix})")
