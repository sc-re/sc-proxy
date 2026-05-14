"""Thread-safe pub/sub for captured packets.

The proxy still writes to the console logger as before; this module is
an *additional* sink that the Qt UI subscribes to. The bus has no
required dependency on Qt — it's just a list + a list of callbacks —
so importing it from `proxy_util` doesn't drag PySide6 into headless
runs of `proxy.py`.

Threading: `publish()` is called from whichever proxy thread received
the packet. Subscribers receive the record on that same thread, so
GUI subscribers must hop to the main thread themselves (the Qt UI
does this via a queued signal).
"""
from __future__ import annotations
import threading
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class PacketRecord:
    idx: int                            # monotonic in publish order
    ts: float                           # time.time() at capture
    tag: str                            # e.g. "shard S→C"
    direction: str                      # "S→C" or "C→S"
    pkt_type: int
    pkt_name: str
    sub_id: Optional[int] = None        # AC index or SN sub-id
    sub_name: Optional[str] = None
    uid: Optional[int] = None
    body: bytes = b""
    send_counter: int = 0
    echo_send_counter: int = 0
    checksum: int = 0
    body_len: int = 0
    decoded_line: str = ""              # exactly what was logged (incl. ANSI)
    ok: bool = True


# Cap retained history so a long session doesn't grow forever. The
# Qt model keeps its own copy; the history list is just for late
# subscribers (e.g. the UI starting after the proxy has been running).
_HISTORY_LIMIT = 10_000

_lock = threading.Lock()
_subscribers: list[Callable[[PacketRecord], None]] = []
_history: list[PacketRecord] = []
_next_idx = 0


def subscribe(cb: Callable[[PacketRecord], None]) -> None:
    with _lock:
        _subscribers.append(cb)


def publish(rec: PacketRecord) -> None:
    """Append to history + notify all subscribers. Safe to call with no
    subscribers attached."""
    global _next_idx
    with _lock:
        rec.idx = _next_idx
        _next_idx += 1
        _history.append(rec)
        if len(_history) > _HISTORY_LIMIT:
            del _history[: len(_history) - _HISTORY_LIMIT]
        subs = list(_subscribers)
    for s in subs:
        try:
            s(rec)
        except Exception:
            # A misbehaving subscriber must not break the proxy's
            # logging path. Swallow.
            pass


def history() -> list[PacketRecord]:
    """Snapshot of records captured so far. Used by the UI to backfill
    after a late subscribe."""
    with _lock:
        return list(_history)


def next_idx() -> int:
    """Index that the *next* publish() will assign. Useful for tests
    and for the UI's status bar."""
    with _lock:
        return _next_idx
