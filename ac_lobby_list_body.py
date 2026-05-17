"""Bit-stream parser for `ac_lobby_list` (AC 0x8d).

S→C response carrying the current list of open custom lobbies, in
exactly the same per-lobby wire shape as `ac_lobby_info` — just
repeated `count` times after a u32 prefix:

    u32  count
    count × LobbyInfo   (see ac_lobby_info_body._read_lobby_info)

Empty-list bodies (C→S request + S→C "no lobbies" reply) decode as
count=0 cleanly.
"""
from __future__ import annotations
from typing import List, Optional

from notification import BitReader, Variant, read_field
from ac_lobby_info_body import _read_lobby_info


class AcLobbyListBody:
    """Decoded body of an `ac_lobby_list` async-request.

    `lobbies` is a Variant whose `.value` is a list of dicts (each dict
    keyed by field-name → Variant), so every lobby's children land in
    the Qt tree with their bit ranges intact.
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.count = read_field(br, "u32", br.read_u32())
            lobbies_start = br.pos
            lobbies: List[dict] = [
                _read_lobby_info(br) for _ in range(self.count.value)
            ]
            br.last_read_start = lobbies_start
            self.lobbies = Variant("list", lobbies, 0xff,
                                   (lobbies_start, br.pos))
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
            return f"AcLobbyListBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "count"):
            return f"AcLobbyListBody({len(self._raw)}B{suffix} slack={slack}b)"
        lobbies = self.lobbies.value if hasattr(self, "lobbies") else []
        # Single-line summary per lobby — id + name + level + member count.
        summaries = []
        for lb in lobbies:
            summaries.append(
                f"  id=0x{lb['lobby_id'].value:x} "
                f"name={lb['name'].value!r} "
                f"level={lb['level_def'].value!r} "
                f"members={len(lb['members'].value)} "
                f"bot_preset={lb['bot_preset'].value!r}"
            )
        body = "\n" + "\n".join(summaries) if summaries else ""
        return (f"AcLobbyListBody({len(self._raw)}B{suffix}, "
                f"count={self.count.value}, slack={slack}b){body}")
