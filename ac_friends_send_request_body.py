"""Bit-stream parser for ac_friends_send_request response.

Despite the AC name, the response carries the player's full social state.
Reader is FUN_08901240 (called from handler 0x082338d8). Each list is a
u8 count followed by `count` × u8be UID; the last two are pair lists.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Tuple

from notification import BitReader


@dataclass
class FriendsState:
    friends: List[int] = field(default_factory=list)
    requests_in: List[int] = field(default_factory=list)
    requests_out: List[int] = field(default_factory=list)
    ignored: List[int] = field(default_factory=list)
    watched: List[int] = field(default_factory=list)
    pairs_a: List[Tuple[int, int]] = field(default_factory=list)
    pairs_b: List[Tuple[int, int]] = field(default_factory=list)


class AcFriendsSendRequestBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: str | None = None
        self.state = FriendsState()
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            for label in ("friends", "requests_in", "requests_out",
                          "ignored", "watched"):
                n = br.read_u8()
                getattr(self.state, label).extend(br.read_u64() for _ in range(n))
            for label in ("pairs_a", "pairs_b"):
                n = br.read_u8()
                lst = getattr(self.state, label)
                for _ in range(n):
                    lst.append((br.read_u64(), br.read_u64()))
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcFriendsSendRequestBody(<error: {self.error}>)"
        s = self.state
        slack = len(self._raw) * 8 - self.bits_consumed
        return (f"AcFriendsSendRequestBody({len(self._raw)}B, "
                f"friends={len(s.friends)}, in={len(s.requests_in)}, "
                f"out={len(s.requests_out)}, ignored={len(s.ignored)}, "
                f"watched={len(s.watched)}, pairs_a={len(s.pairs_a)}, "
                f"pairs_b={len(s.pairs_b)}, slack={slack}b)")
