"""Bit-stream parser for `ac_player_credentials` (AC 0x09).

Sent S->C with the player's nickname and session credentials. Handler
0x082305c7 reads the fields below off the same MSB-first bit-stream the
other AC bodies use. Most fields are byte-sized, but `flag2` is a true
1-bit bool (BitStream_ReadBool @8b1b6d0) — so the trailing property bag
starts bit-misaligned (shifted 1 bit), with up to 7 padding bits at the
end. That single bit is why this message can't be modelled with native
byte-aligned kaitai once flag2/bag are non-trivial; hence this
hand-written BitReader body.

Wire layout (in handler read order):

    cstrN  nick         NUL-terminated display name  (ReadCStringLen @8b1d880)
    u8     flag1        bool, always 0x01 observed   (ReadU8  @8b1b6e0 -> obj+0xad928)
    u64    steam_id64   SteamID64, 0 if not Steam    (ReadU64v2 @8b1c360 -> obj+0x624)
    u64    account_id   stable 64-bit account id     (ReadU64v2 @8b1c360 -> obj+0x62c)
    i32    level        small account-progress level (ReadI32 @8b1c230 -> obj+0x28d8d4)
    u1     flag2        bool, always 0 observed       (ReadBool @8b1b6d0 -> obj+0x28d8d0)
    BAG    extra        property bag, empty in all    (Bag_Deserialize @8b1ed60 -> obj+0xad9b8)
                        captures (bit-packed: starts 1 bit after `level`).

flag1 is a full byte; flag2 is a single bit. steam_id64 carries the
Steam universe-1 prefix (0x0110000100000000 | accountID) and is 0 for
dev-login accounts. Verified against all 96 captures (flag1=1, flag2=0,
bag empty, <8 bits trailing slack).
"""
from __future__ import annotations
from typing import Optional

from notification import BitReader, Variant, read_field, _read_bag


_NICK_MAX = 128  # handler reads into a 0x80-byte buffer (obj+0xad8a8)


class AcPlayerCredentialsBody:
    """Parsed body of `ac_player_credentials`. Mirrors the binary's bit
    -level wire sequence — see module docstring. `flag2` is a 1-bit bool,
    so `extra` (the bag) is read from a bit-misaligned cursor."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.nickname   = read_field(br, "str",
                                         br.read_cstring(max_len=_NICK_MAX))
            self.flag1      = read_field(br, "u8",   br.read_u8())
            self.steam_id64 = read_field(br, "u64",  br.read_u64())
            self.account_id = read_field(br, "u64",  br.read_u64())
            self.level      = read_field(br, "i32",  br.read_i32())
            self.flag2      = read_field(br, "bool", br.read_bool())
            # Bag starts 1 bit after `level` (flag2 consumed a single bit).
            self.extra      = read_field(br, "bag",  _read_bag(br))
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
            return f"AcPlayerCredentialsBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "nickname"):
            return (f"AcPlayerCredentialsBody({len(self._raw)}B{suffix} "
                    f"slack={slack}b)")
        parts = [f"{len(self._raw)}B{suffix}",
                 f"nick={self.nickname.value!r}",
                 f"steam_id64={self.steam_id64.value:#018x}",
                 f"account_id={self.account_id.value:#x}",
                 f"level={self.level.value}",
                 f"flag1={self.flag1.value}",
                 f"flag2={self.flag2.value}",
                 f"slack={slack}b"]
        return "AcPlayerCredentialsBody(" + ", ".join(parts) + ")"
