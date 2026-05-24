"""Bit-stream parser for `ac_buy_item` C->S request (AC 0x27).

Sent by the client when the player presses "Buy" in any shop UI. The
encoder is FUN_082576a0 (called by the Lua binding `GameStore_Buy`
@FUN_082640a0), which writes the bitstream:

    u32  store_item_id            (32 bits)
    u32  amount                   (32 bits; encoder clamps to 1..0x3fff)
    u8   credits_type             (8 bits; CT_INVALID/CREDITS/GOLD/...)
    u1   has_discount             (1 bit; client-computed from
                                   FUN_08257360 -- 1 if a discount aura's
                                   `discounted_def` / `alt_discounted_defs`
                                   covers this store_item_id)
    u32  mode                     (32 bits; the 4th Lua arg to
                                   GameStore_Buy(); 0xffffffff when
                                   omitted, otherwise an enum/flag --
                                   observed values 0x00000001 from the
                                   item-craft windows and 0x00000002 from
                                   the ships-tree buy flow)

Total = 32+32+8+1+32 = 105 bits; bodies are 14 B (112 bits), so every
capture ends with 7 bits of padding. The 1-bit `has_discount` makes the
trailing u32 bit-misaligned, so native kaitai can't model this cleanly
-- hence a hand-written BitReader body, like the other bit-packed
messages.

credits_type values (CT_* enum, per
`jump_to_zone_price_type should be: CT_INVALID, CT_CREDITS, CT_GOLD,
CT_TOKENS, CT_EVENT, CT_GOLD_BUYING_PTS, CT_VESSEL_EXP` string in the
binary):
    0 = CT_INVALID
    1 = CT_CREDITS        (in-game credits)
    2 = CT_GOLD           (GS)
    3 = CT_TOKENS         (iridium)
    4 = CT_EVENT          (event credits)
    5 = CT_GOLD_BUYING_PTS
    6 = CT_VESSEL_EXP

Verified against all 3 C->S captures with 0/0/0 errors and 7 bits
trailing padding each.
"""
from __future__ import annotations
from typing import Optional

from notification import BitReader, Variant, read_field


_CREDITS_TYPE_NAMES = {
    0: "CT_INVALID",
    1: "CT_CREDITS",
    2: "CT_GOLD",
    3: "CT_TOKENS",
    4: "CT_EVENT",
    5: "CT_GOLD_BUYING_PTS",
    6: "CT_VESSEL_EXP",
}


class AcBuyItemRequestBody:
    """Parsed body of the C->S `ac_buy_item` request. See module docstring."""

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.store_item_id = read_field(br, "u32", br.read_u32())
            self.amount        = read_field(br, "u32", br.read_u32())
            ct = br.read_u8()
            self.credits_type  = read_field(
                br, "u8", ct,
                display=f"{ct} ({_CREDITS_TYPE_NAMES.get(ct, '?')})")
            self.has_discount  = read_field(br, "bool", br.read_bool())
            self.mode          = read_field(br, "u32", br.read_u32())
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
            return f"AcBuyItemRequestBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "store_item_id"):
            return (f"AcBuyItemRequestBody({len(self._raw)}B{suffix} "
                    f"slack={slack}b)")
        ct = self.credits_type.value
        mode = self.mode.value
        mode_str = "default(-1)" if mode == 0xFFFFFFFF else str(mode)
        parts = [
            f"{len(self._raw)}B{suffix}",
            f"store_item_id={self.store_item_id.value:#x}",
            f"amount={self.amount.value}",
            f"credits_type={_CREDITS_TYPE_NAMES.get(ct, ct)}",
            f"has_discount={self.has_discount.value}",
            f"mode={mode_str}",
            f"slack={slack}b",
        ]
        return "AcBuyItemRequestBody(" + ", ".join(parts) + ")"
