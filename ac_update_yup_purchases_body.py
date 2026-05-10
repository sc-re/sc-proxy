"""Bit-stream parser for ac_update_yup_purchases (AC 0x70).

S→C only. The server pushes the player's Yuplay (Gaijin's storefront)
purchase state — DLCs, premium account, etc. — unsolicited shortly
after connect, and again whenever the cache needs refreshing. The
client *can* request a refresh via lua's MasterServer_UpdateYupPurchases
but the server doesn't wait for that.

Handler (inline case at 0x082327ae inside OnRecieve):

    u8  status                  (0 on success)
    bag yupPurchases            (full new state — the bag is read via
                                 FUN_8b1ed60 = cleanup + standard bag
                                 deserializer; stored at struct +0xada4c)
    u8  num_invalidate
    num_invalidate × cstring (≤60)
                                (purchase IDs to drop from the cache —
                                 for an initial server-push when the
                                 cache is empty this list is empty too)

Cached purchases (the bag) are exposed to lua via
`MasterServer_GetCachedYupPurchases()`. The lua callback name
`MasterServer_OnUpdateYupPurchases` is registered on the C++ side but
the decompiled lua never defines a handler — the cache is just kept
warm for any later read.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from notification import BitReader, _read_bag


class AcUpdateYupPurchasesBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.status: int = 0
        self.purchases: dict = {}
        self.num_invalidate: int = 0
        self.invalidate_ids: List[str] = []
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.status = br.read_u8()
            self.purchases = _read_bag(br)
            self.num_invalidate = br.read_u8()
            for _ in range(self.num_invalidate):
                self.invalidate_ids.append(br.read_cstring(max_len=60))
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = f" ERROR: {self.error}" if self.error else ""
        # Show a compact summary of the bag: number of entries plus the
        # keys, since those are the purchase identifiers.
        keys = list(self.purchases.keys())
        kpreview = (", ".join(repr(k) for k in keys[:6])
                    + (f", ... +{len(keys)-6}" if len(keys) > 6 else ""))
        inv = (f", invalidate={self.invalidate_ids}"
               if self.invalidate_ids else "")
        return (f"AcUpdateYupPurchasesBody({len(self._raw)}B, "
                f"status={self.status}, "
                f"purchases={len(self.purchases)}={{{kpreview}}}{inv}, "
                f"slack={slack}b{suffix})")
