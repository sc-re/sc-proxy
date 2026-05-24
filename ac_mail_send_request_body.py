"""Bit-stream parser for `ac_mail_send` C→S request (AC 0xd2).

Wire format (in read order):

    u64v2 recipient_uid       (target player)
    cstr  subject             (≤ ~30 chars in practice)
    cstr  body                (mail body text, nul-terminated)
    bag   attachments         (Bag_Deserialize — usually empty when the
                               client just sends text; structured the
                               same way as the attachments seen in
                               `ac_mail_get` mail records)

The server's ACK uses opcode 210 with `u8 status (+ u1 has_data)`; see
the `AcMailSend` body class in star_conflict_package_server.py for the
response side.
"""
from __future__ import annotations
from typing import Optional

from notification import BitReader, Variant, read_field, _read_bag


_CSTR_MAX = 256


class AcMailSendRequestBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.recipient_uid: Optional[Variant] = None
        self.subject: Optional[Variant] = None
        self.body: Optional[Variant] = None
        self.attachments: Optional[Variant] = None
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.recipient_uid = read_field(br, "u64", br.read_u64())
            self.subject = read_field(
                br, "str", br.read_cstring(max_len=_CSTR_MAX))
            self.body = read_field(
                br, "str", br.read_cstring(max_len=_CSTR_MAX))
            self.attachments = read_field(br, "bag", _read_bag(br))
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcMailSendRequestBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        return (f"AcMailSendRequestBody({len(self._raw)}B, "
                f"to={self.recipient_uid.value}, "
                f"subject={self.subject.value!r}, "
                f"body={self.body.value!r}, "
                f"attachments={self.attachments.value!r}, slack={slack}b)")
