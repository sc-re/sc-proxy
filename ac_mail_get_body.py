"""Bit-stream parser for `ac_mail_get` (AC 0xd0).

Sent S→C with the player's mailbox. Handler at 0x0822e030 reads:

    u8 status
    u1 keep_existing      (0 ⇒ FUN_088f6fe0 wipes mailbox first; either
                           branch then falls through to FUN_088f6480)

Then FUN_088f6480 (mailbox-list reader):

    u16v2 num_mails
    num_mails × MailRecord  (FUN_088f43a0)

MailRecord (FUN_088f43a0):

    u64v2 mail_id
    u8    flags            (param_1[2]; 1=unread / 5=deleted / etc.)
    u64v2 from_uid
    u64v2 to_uid
    u64   send_time        (plain u64, BE)
    u64   read_time        (plain u64, BE)
    u1    flag_a           (param_1+0x3c)
    u8    flag_b           (param_1+0x20 / +8 word)
    u8    num_attachments
    num_attachments × {
        u8  attach_type
        bag attach_data    (Bag_Deserialize — key/value pairs)
    }
    u32   price_gs         (param_1+0x44; GS cost to claim the
                            attachments — 0 for free system mail)

Empty mailbox (`u16 num_mails == 0`) ends the body — typical 6-byte
response is `ac_id(0x00d0) status(0) bit(0) num_mails(0)` plus padding.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field, _read_bag


def _read_mail(br: BitReader) -> dict:
    """Read one MailRecord from `br`. Returns a dict of Variants /
    sub-records so the GUI tree can render the per-mail layout with
    bit-range highlighting. Restores `last_read_start` to the record's
    entry position so a wrapping `read_field` covers the whole record.
    """
    start = br.pos
    out: dict[str, object] = {}
    out["mail_id"]    = read_field(br, "u64", br.read_u64())
    out["flags"]      = read_field(br, "u8",  br.read_u8())
    out["from_uid"]   = read_field(br, "u64", br.read_u64())
    out["to_uid"]     = read_field(br, "u64", br.read_u64())
    out["send_time"]  = read_field(br, "u64", br.read_u64())
    out["read_time"]  = read_field(br, "u64", br.read_u64())
    out["flag_a"]     = read_field(br, "u1",  br.read_bool())
    out["flag_b"]     = read_field(br, "u8",  br.read_u8())
    n = br.read_u8()
    out["num_attachments"] = read_field(br, "u8", n)
    atts: list[dict] = []
    for _ in range(n):
        att_start = br.pos
        attach_type = read_field(br, "u8", br.read_u8())
        bag = read_field(br, "bag", _read_bag(br))
        br.last_read_start = att_start  # widen for the wrapping Variant
        atts.append({"type": attach_type, "data": bag})
    out["attachments"] = atts
    out["price_gs"]   = read_field(br, "u32", br.read_u32())
    br.last_read_start = start
    return out


class AcMailGetBody:
    """Decoded body of an `ac_mail_get` async-request response.

    Public attributes are Variants (from `read_field`) so each carries
    its own `bit_range` for the Qt UI's hex highlighting. The `mails`
    list holds per-record dicts of Variants (same shape used by the
    lobby_info parser).
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.status: Optional[Variant] = None
        self.keep_existing: Optional[Variant] = None
        self.num_mails: Optional[Variant] = None
        self.mails: List[dict] = []
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.status = read_field(br, "u8", br.read_u8())
            self.keep_existing = read_field(br, "u1", br.read_bool())
            n = br.read_u16()
            self.num_mails = read_field(br, "u16", n)
            self.mails = [_read_mail(br) for _ in range(n)]
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcMailGetBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        if self.num_mails is None:
            return f"AcMailGetBody({len(self._raw)}B, <unparsed>)"
        return (f"AcMailGetBody({len(self._raw)}B, "
                f"status={self.status.value}, "
                f"keep={self.keep_existing.value}, "
                f"num_mails={self.num_mails.value}, slack={slack}b)")
