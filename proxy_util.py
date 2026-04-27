"""Shared utilities for MITM proxy modules.

Parses framed TGP packets (same format as protocol.py), logs them with
hex + text dumps and a decoded header line so we can read back real
server responses as a reference for our stub server.
"""
import socket
import struct
import threading
import time
import logging
import os

from protocol import read_packet
from ac_types import pkt_type_name
from star_conflict_package_client import StarConflictPackageClient
from star_conflict_package_server import StarConflictPackageServer
from kaitaistruct import KaitaiStream, BytesIO

# scmd_pkt_type → name (mirrors the binary's table at VMA 0x08fe7ac0).
# See Documentation/SCMD-protocol.md for the full mapping and how this is
# different from the wire send_counter.
_SCMD_NAMES = [
    "SCMD_ASSIGNED_SHARD", "SCMD_LB_QUEUE_INFO", "SCMD_LB_CVARS",
    "SCMD_AUTH_REQ", "CCMD_AUTH_REQUEST", "SCMD_AUTH_ACK",
    "SCMD_STEAM_NOT_ATTACHED", "SCMD_ARC_NOT_ATTACHED", "CCMD_STORE",
    "SCMD_STORE", "SCMD_STORE_SPOILED", "SCMD_CONNECT_DEDICATED_SERVER",
    "SCMD_GAME_ENDED", "CSCMD_ASYNC_REQ", "SCMD_NOTIFICATION",
    "SCMD_SQUAD_NOTIFICATION", "SCMD_SOCIAL_NOTIFICATION",
    "SCMD_TEACH_NOTIFICATION", "SCMD_CLAN_NOTIFICATION",
    "SCMD_USER_PROFILE_NOTIFICATION", "SCMD_QUEST_NOTIFICATION",
    "SCMD_LEAGUE_NOTIFICATION", "SCMD_VESSEL_NOTIFICATION",
    "SCMD_LOBBY_NOTIFICATION", "SCMD_KEEP_ALIVE", "SCMD_BAN_INFO",
    "SCMD_WELCOME_MSG", "SCMD_DOCK_SPACE_STATION",
    "SCMD_FREE_SPACE_DEBRIEFING", "SCMD_NEW_MOTD",
    "SCMD_TOURNAMENT_TEAMS_INFO", "SCMD_BRAWL_SCHEDULE",
    "SCMD_REWARD_SCHEDULE", "SCMD_PVE_SCHEDULE",
    "SCMD_LEAGUE_FORBIDDEN_EQUIPMENT", "SCMD_BATTLE_PASS_ACTIVATION",
    "SCMD_ZONES_WITH_DISABLED_QUESTS", "SCMD_ADVENTURE_NOTIFICATION",
    "SCMD_REPLACE_CHAT_MSG",
]

log = logging.getLogger("proxy")

# Shared state: the LB's response to the client contains the shard and chat
# addresses. The LB proxy stores the real values here after parsing the real
# LB's response so the shard/chat proxies know where to forward. If the LB
# proxy doesn't run (or hasn't seen a handshake yet), the fallback defaults
# are used.
_state_lock = threading.Lock()
_state = {
    "real_shard": None,  # (host, port)
    "real_chat":  None,  # (host, port)
}

# Fallback destinations if the LB proxy hasn't populated the state yet.
# Override via env to test against a specific server.
DEFAULT_REAL_LB    = (os.environ.get("SC_REAL_HOST", "185.253.20.238"),
                      int(os.environ.get("SC_REAL_LB_PORT", "3801")))
DEFAULT_REAL_SHARD = (os.environ.get("SC_REAL_HOST", "185.253.20.238"),
                      int(os.environ.get("SC_REAL_SHARD_PORT", "3802")))
DEFAULT_REAL_CHAT  = (os.environ.get("SC_REAL_HOST", "185.253.20.238"),
                      int(os.environ.get("SC_REAL_CHAT_PORT", "3815")))


def set_real_shard(host: str, port: int):
    with _state_lock:
        _state["real_shard"] = (host, port)
    log.info(f"[proxy] real shard updated → {host}:{port}")


def set_real_chat(host: str, port: int):
    with _state_lock:
        _state["real_chat"] = (host, port)
    log.info(f"[proxy] real chat updated → {host}:{port}")


def get_real_shard() -> tuple[str, int]:
    with _state_lock:
        return _state["real_shard"] or DEFAULT_REAL_SHARD


def get_real_chat() -> tuple[str, int]:
    with _state_lock:
        return _state["real_chat"] or DEFAULT_REAL_CHAT


def _kaitai_repr(obj) -> str:
    """Render non-private, non-dummy fields of a KaitaiStruct as key=value pairs."""
    if not hasattr(obj, '__dict__'):
        return repr(obj)
    fields = {k: v for k, v in obj.__dict__.items()
              if not k.startswith('_') and k != 'dummy'}
    if not fields:
        return ""
    parts = []
    for k, v in fields.items():
        if isinstance(v, (bytes, bytearray)):
            parts.append(f"{k}={v.hex()}")
        elif isinstance(v, list):
            parts.append(f"{k}=[{', '.join(_kaitai_repr(i) for i in v)}]")
        elif hasattr(v, '__dict__') and hasattr(v, '_io'):
            parts.append(f"{k}=({_kaitai_repr(v)})")
        else:
            parts.append(f"{k}={v!r}")
    return " ".join(parts)


_GREEN = "\033[32m"
_RED   = "\033[31m"
_RESET = "\033[0m"


def _colorize(text: str, ok: bool) -> str:
    return f"{_GREEN if ok else _RED}{text}{_RESET}"


def _parse_kaitai(body: bytes, tag: str) -> tuple[str, bool]:
    """Try to parse body; return (description, success)."""
    try:
        if "C→S" in tag:
            parsed = StarConflictPackageClient(KaitaiStream(BytesIO(body)))
        else:
            parsed = StarConflictPackageServer(KaitaiStream(BytesIO(body)))
        name = type(parsed.body).__name__
        detail = _kaitai_repr(parsed.body)
        return f" [{name}{': ' + detail if detail else ''}]", True if detail else False
    except Exception as e:
        return f" [{e}]", False


def hexdump(data: bytes, width: int = 16, prefix: str = "    ") -> str:
    lines = []
    for i in range(0, len(data), width):
        chunk = data[i:i + width]
        hx = " ".join(f"{b:02x}" for b in chunk)
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        lines.append(f"{prefix}{i:04x}: {hx:<{width*3}}  {asc}")
    return "\n".join(lines)


# Full bodies go here so they can be recovered as exact bytes; the log
# still only holds a preview so it doesn't become unreadable.
_capture_base = os.environ.get("SC_CAPTURE_DIR", "captures/")
_session_ts = time.strftime("%Y%m%d_%H%M%S")
CAPTURE_DIR = os.path.join(_capture_base, _session_ts)
_capture_idx = [0]
_capture_lock = threading.Lock()


def log_packet(tag: str, pkt: dict, extra: str = ""):
    if pkt.get("special"):
        log.info(f"[{tag}] SPECIAL (ff ff ff fe + 8 bytes) {extra}")
        return
    body = pkt.get("body", b"")
    kaitai_str, ok = _parse_kaitai(body, tag)
    ac_idx = int.from_bytes(body[:2], "big") if len(body) >= 2 else 0xffff
    pkt_t = pkt['scmd_pkt_type']
    pkt_name = _SCMD_NAMES[pkt_t] if pkt_t < len(_SCMD_NAMES) else f"?{pkt_t}"
    hdr = (f"[{tag}] send=0x{pkt['send_counter']:04x} "
           f"echo=0x{pkt['echo_send_counter']:04x} "
           f"pkt=0x{pkt_t:04x}({pkt_name}) "
           f"cs=0x{pkt['checksum']:04x} body_len={pkt['body_len']}"
           f"{kaitai_str}")
    # Save the full body to disk for offline extraction — the log hexdump
    # is still truncated to keep the log readable.
    if body:
        with _capture_lock:
            idx = _capture_idx[0]
            _capture_idx[0] = idx + 1
        try:
            os.makedirs(CAPTURE_DIR, exist_ok=True)
            direction = tag.split()[-1].replace("→", "_to_")
            fname = f"{idx:04d}_{direction}_ac{ac_idx:04x}_{pkt_type_name(ac_idx).lower()}_len{len(body)}.bin"
            with open(os.path.join(CAPTURE_DIR, fname), "wb") as f:
                f.write(body)
            hdr += f" saved={fname}"
        except Exception as e:
            hdr += f" save_error={e}"
    if extra:
        hdr += f" {extra}"
    log.info(_colorize(hdr, ok))
    if body and not ok:
        body_preview = body[:128]
        log.info(_colorize(f"    body[0:{len(body_preview)}]:\n{hexdump(body_preview)}", False))


def relay_loop(src: socket.socket, dst: socket.socket, tag: str,
               on_packet=None):
    """Read framed packets from src, log them, optionally mutate via
    on_packet(pkt) -> pkt (return the packet to forward, or None to drop),
    then write to dst. Falls back to raw forwarding if framing fails."""
    try:
        while True:
            pkt = read_packet(src)
            if pkt is None:
                break
            log_packet(tag, pkt)
            if on_packet is not None:
                pkt = on_packet(pkt)
                if pkt is None:
                    continue
            if pkt.get("special"):
                # special packets are ff ff ff fe + 8 bytes (12 total)
                dst.sendall(b"\xff\xff\xff\xfe" + b"\x00" * 8)
            else:
                from protocol import make_packet
                dst.sendall(make_packet(
                    send_counter=pkt["send_counter"],
                    echo_send_counter=pkt["echo_send_counter"],
                    scmd_pkt_type=pkt["scmd_pkt_type"],
                    body=pkt["body"]))
    except Exception as e:
        log.warning(f"[{tag}] relay error: {e}")
    finally:
        # Shut down both sockets so the opposite-direction relay also
        # exits — otherwise one-shot streams (e.g. LB server closes after
        # sending cvars+shard_addr) leave the reverse relay blocked.
        try: src.shutdown(socket.SHUT_RDWR)
        except: pass
        try: dst.shutdown(socket.SHUT_RDWR)
        except: pass


def connect_upstream(host: str, port: int) -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((host, port))
    s.settimeout(None)
    return s
