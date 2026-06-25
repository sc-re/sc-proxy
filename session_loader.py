"""Load older capture sessions back into PacketRecords.

The live proxy writes every packet body to disk under
`<base>/<session>/<idx>_<dir>_..._pkt<tt>_..._len<n>.bin` (see
proxy_util.log_packet). This module reverses that: it enumerates the
session directories that previous runs left behind and reconstructs a
list of packet_bus.PacketRecord from the `.bin` files so the Qt
inspector can browse a finished session offline.

Only the body bytes are persisted on disk, so a few header fields the
live capture knew (send_counter / echo_send_counter / checksum) cannot
be recovered and are reported as 0. Everything else — packet type,
direction, uid, sub-id/name, the decoded payload and its ok flag — is
re-derived from the filename plus a fresh scmd_decoders.decode_packet()
on the body, exactly as the live path did.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass

import packet_bus
import scmd_decoders
from notification import _RESET


# Base directories that may hold session subdirectories. The live proxy
# writes into one of these depending on prod- vs local-server mode; for
# loading we look in all of them (and honour SC_CAPTURE_DIR's parent if
# it points somewhere custom).
def _base_dirs() -> list[str]:
    bases = ["captures", "captures_debug"]
    env = os.environ.get("SC_CAPTURE_DIR")
    if env:
        env = env.rstrip("/")
        if env and env not in bases:
            bases.append(env)
    return bases


# <idx>_<S_to_C|C_to_S>[_uid<uid>]_pkt<tt>_<name…>_len<n>.bin
_FNAME_RE = re.compile(
    r"^(?P<idx>\d+)_(?P<dir>S_to_C|C_to_S)"
    r"(?:_uid(?P<uid>\d+))?"
    r"_pkt(?P<pkt>[0-9a-fA-F]{2})_.*_len(?P<len>\d+)\.bin$"
)

_ANSI = re.compile(r"\x1b\[[0-9;]*m")


@dataclass
class SessionInfo:
    """One on-disk capture session the UI can offer to load."""
    name: str          # session directory name, e.g. "20260510_081912"
    path: str          # full path to the session directory
    base: str          # which base dir it lives under ("captures", …)
    count: int         # number of *.bin capture files in it

    @property
    def label(self) -> str:
        return f"{self.name}  ({self.base}, {self.count} pkts)"


def list_sessions() -> list[SessionInfo]:
    """Enumerate capture sessions found under the known base dirs,
    newest first (session dirs are named with a sortable timestamp)."""
    out: list[SessionInfo] = []
    for base in _base_dirs():
        if not os.path.isdir(base):
            continue
        for name in os.listdir(base):
            path = os.path.join(base, name)
            if not os.path.isdir(path):
                continue
            count = sum(1 for f in os.listdir(path) if f.endswith(".bin"))
            if count:
                out.append(SessionInfo(name=name, path=path,
                                       base=base, count=count))
    # Newest first; the timestamp naming makes a string sort chronological.
    out.sort(key=lambda s: s.name, reverse=True)
    return out


def load_session(path: str) -> list[packet_bus.PacketRecord]:
    """Reconstruct the PacketRecords saved in session directory `path`,
    ordered by their capture index. Files whose names don't match the
    capture convention are skipped."""
    records: list[packet_bus.PacketRecord] = []
    try:
        names = os.listdir(path)
    except OSError:
        return records

    for fname in names:
        m = _FNAME_RE.match(fname)
        if not m:
            continue
        fpath = os.path.join(path, fname)
        try:
            with open(fpath, "rb") as f:
                body = f.read()
            ts = os.path.getmtime(fpath)
        except OSError:
            continue

        idx = int(m.group("idx"))
        direction = "S→C" if m.group("dir") == "S_to_C" else "C→S"
        pkt_type = int(m.group("pkt"), 16)
        uid = int(m.group("uid")) if m.group("uid") else None

        decoded = scmd_decoders.decode_packet(pkt_type, body, direction)
        # Mirror the live capture's one-line summary closely enough that
        # the UI's text filter and payload-fallback leaf behave the same.
        decoded_line = (
            f"[{direction}] pkt=0x{pkt_type:02x}({decoded.pkt_name}) "
            f"body_len={len(body)}{decoded.detail}"
        )

        records.append(packet_bus.PacketRecord(
            idx=idx,
            ts=ts,
            tag=direction,
            direction=direction,
            pkt_type=pkt_type,
            pkt_name=decoded.pkt_name,
            sub_id=decoded.sub_id,
            sub_name=decoded.sub_name,
            uid=uid,
            body=body,
            send_counter=0,        # not persisted on disk
            echo_send_counter=0,   # not persisted on disk
            checksum=0,            # not persisted on disk
            body_len=len(body),
            decoded_line=_ANSI.sub("", decoded_line),
            ok=decoded.ok,
        ))

    records.sort(key=lambda r: r.idx)
    return records
