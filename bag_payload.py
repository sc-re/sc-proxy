"""Opaque kaitai type — bit-packed property bag tail.

Used as `type: bag_payload` in server.ksy / client.ksy when the AC body
ends with a bit-stream-encoded property bag rather than a discrete
struct. The kaitai compiler invoked with `--opaque-types true` produces
calls like `BagPayload(self._io)` that this module satisfies.

Wire format is the same as SCMD_NOTIFICATION's bag:

    u32 num_entries                 ; 32 bits BE
    if num_entries > 0:
        u1  use_indexed_keys        ; 1 bit
        repeat num_entries:
            if !use_indexed_keys:
                cstring key         ; 8-bit chars NUL-terminated
            variant value           ; tag(8) + per-tag payload

Decoding delegates to `notification._read_bag` (already battle-tested
against ~88 K SCMD_NOTIFICATION captures) so we don't duplicate the
variant-tag table here.
"""
from __future__ import annotations
from typing import Any

from notification import BitReader, _read_bag, format_bag, Variant


class BagPayload:
    """Kaitai-protocol opaque type that decodes a property bag tail."""

    __slots__ = ("_io", "raw", "bag", "ok", "error")

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        # Slurp every remaining byte — bag is always the body's tail.
        self.raw: bytes = _io.read_bytes_full()
        try:
            br = BitReader(self.raw)
            self.bag: dict[str, Variant] = _read_bag(br)
            self.ok: bool = True
            self.error: str | None = None
        except Exception as e:
            self.bag = {}
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        # Kaitai calls this on every parsed type to walk lazy `instances:`
        # blocks. We have none — no-op.
        pass

    def __repr__(self) -> str:
        if not self.ok:
            return f"BagPayload(<error: {self.error}> raw={self.raw[:8].hex()}…)"
        return f"BagPayload({format_bag(self.bag)})"
