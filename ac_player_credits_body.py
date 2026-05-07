"""Bit-stream parser for ac_player_credits server-to-client response.

Handler 0x08231c56 → FUN_088e9ec0. The body is a u16 flag word followed
by selectively-present scalars (one bit per currency type), then one
final variable-length "5 × u32 craft resources" array if bit 7 is set.

  u2 flags
  if flags & 0x02: u8 credits             (main currency, observed ~2.5M)
  if flags & 0x04: u8 gold_credits
  if flags & 0x08: u8 token_credits
  if flags & 0x10: u8 loyalty + u8 loyalty_time   (timestamp partner)
  if flags & 0x20: u8 vid                  (some account/version id, u8v2)
  if flags & 0x40: u4 premium              (status / time flag)
  if flags & 0x80: 5 × u4 craft_resources  (e.g. 3.8M, 3.8M, 720K, 2.3M, 48K)

Field names are best guesses based on bit ordering and observed values;
the binary dispatches into game state offsets rather than Lua-named
fields, so the names aren't directly recoverable. Confirmed: 0 bits of
slack on every captured 66-byte body (flags=0x00de = bits 1,2,3,4,6,7).
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader


class AcPlayerCreditsBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.flags: int = 0
        self.credits: Optional[int] = None
        self.gold_credits: Optional[int] = None
        self.token_credits: Optional[int] = None
        self.loyalty: Optional[int] = None
        self.loyalty_time: Optional[int] = None
        self.vid: Optional[int] = None
        self.premium: Optional[int] = None
        self.craft_resources: Optional[List[int]] = None
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.flags = br.read_u16()
            if self.flags & 0x02: self.credits = br.read_u64()
            if self.flags & 0x04: self.gold_credits = br.read_u64()
            if self.flags & 0x08: self.token_credits = br.read_u64()
            if self.flags & 0x10:
                self.loyalty = br.read_u64()
                self.loyalty_time = br.read_u64()
            if self.flags & 0x20: self.vid = br.read_u64()
            if self.flags & 0x40: self.premium = br.read_u32()
            if self.flags & 0x80:
                self.craft_resources = [br.read_u32() for _ in range(5)]
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcPlayerCreditsBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        parts = [f"flags=0x{self.flags:04x}"]
        if self.credits is not None: parts.append(f"credits={self.credits}")
        if self.gold_credits is not None: parts.append(f"gold={self.gold_credits}")
        if self.token_credits is not None: parts.append(f"tokens={self.token_credits}")
        if self.loyalty is not None: parts.append(f"loyalty={self.loyalty}")
        if self.loyalty_time is not None: parts.append(f"loyalty_time={self.loyalty_time}")
        if self.vid is not None: parts.append(f"vid={self.vid}")
        if self.premium is not None: parts.append(f"premium={self.premium}")
        if self.craft_resources is not None:
            parts.append(f"resources={self.craft_resources}")
        return f"AcPlayerCreditsBody({len(self._raw)}B, {', '.join(parts)}, slack={slack}b)"
