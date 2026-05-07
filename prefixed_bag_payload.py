"""Opaque kaitai type — `u1 prefix + bag` body shape.

Several AC handlers begin their response with a 1-bit flag before the
property bag. Examples:

  * ac_clan_history_get (handler 0x0822f2da): reads u1 has_bag; if 1,
    deserialises the bag, otherwise emits a placeholder.
  * ac_get_blueprints  (handler 0x0822d434): reads u1 (stored as
    !is_loaded), unconditionally deserialises the bag.

The kaitai compiler invoked with `--opaque-types true` produces calls
like `PrefixedBagPayload(self._io)` that this module satisfies.

Decoding delegates to `notification._read_bag` so we don't duplicate the
variant-tag table here.
"""
from __future__ import annotations
from typing import Any

from notification import BitReader, _read_bag, format_bag, Variant


class PrefixedBagPayload:
    __slots__ = ("_io", "raw", "prefix", "bag", "ok", "error")

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self.raw: bytes = _io.read_bytes_full()
        self.prefix: bool = False
        self.bag: dict[str, Variant] = {}
        try:
            br = BitReader(self.raw)
            self.prefix = br.read_bool()
            if self.prefix:
                self.bag = _read_bag(br)
            self.ok = True
            self.error: str | None = None
        except Exception as e:
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if not self.ok:
            return (f"PrefixedBagPayload(<error: {self.error}> "
                    f"prefix={self.prefix} raw={self.raw[:8].hex()}…)")
        return f"PrefixedBagPayload(prefix={self.prefix}, {format_bag(self.bag)})"
