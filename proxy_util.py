"""Transport, logging and capture for the MITM proxy modules.

Reads framed TGP packets (same format as protocol.py), hands each one to
scmd_decoders.decode_packet for interpretation, then logs a one-line
summary, saves the full body under CAPTURE_DIR, and publishes it on the
packet bus. All decode logic lives in scmd_decoders / notification — this
module is purely the relay.
"""
import socket
import threading
import time
import logging
import os

from protocol import read_packet, make_packet
from notification import _GREEN, _RED, _RESET
import scmd_decoders
import packet_bus

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


def _detect_lan_ip() -> str:
    """Best-effort primary outbound IPv4 of this host.

    Opens a UDP socket "toward" a public address (no packet is actually
    sent) so the OS picks the default-route interface, then reads back
    its local address. Falls back to loopback if that fails.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()


# Host advertised to the game inside the rewritten shard/chat address
# (proxy_lb._rewrite_shard_addr). The game must be able to reach the
# proxy's shard/chat listeners at this address from wherever it runs, so
# it defaults to this machine's primary LAN IP (auto-detected). Pin it
# via SC_PROXY_HOST for unusual layouts (e.g. NAT, or a fixed LAN IP).
# Previously this was a hardcoded literal that silently went stale when
# the host's DHCP lease changed, leaving the game unable to reach the
# shard.
ADVERTISE_HOST = os.environ.get("SC_PROXY_HOST") or _detect_lan_ip()

# Ports the proxy listens on. Each sub-proxy reads these at start() so a
# late call to set_local_server_mode() before the threads launch takes
# effect. Defaults match the upstream prod values (so the game's
# unchanged configuration finds the proxy first).
LB_LISTEN_PORT    = 3801
SHARD_LISTEN_PORT = 19803
CHAT_LISTEN_PORT  = 3815


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


def _colorize(text: str, ok: bool) -> str:
    return f"{_GREEN if ok else _RED}{text}{_RESET}"


def hexdump(data: bytes, width: int = 16, prefix: str = "    ") -> str:
    lines = []
    for i in range(0, len(data), width):
        chunk = data[i:i + width]
        hx = " ".join(f"{b:02x}" for b in chunk)
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        lines.append(f"{prefix}{i:04x}: {hx:<{width*3}}  {asc}")
    return "\n".join(lines)


# Full bodies go here so they can be recovered as exact bytes; the log
# still only holds a preview so it doesn't become unreadable. The base
# directory can be flipped at runtime via set_local_server_mode() so the
# --local-server flag lands its captures in captures_debug/ instead.
_capture_base = os.environ.get("SC_CAPTURE_DIR", "captures/")
_session_ts = time.strftime("%Y%m%d_%H%M%S")
CAPTURE_DIR = os.path.join(_capture_base, _session_ts)
_capture_idx = [0]
_capture_lock = threading.Lock()


def set_local_server_mode(host: str) -> None:
    """Switch the proxy to point at the local dev server at `host`.

    Effects, all applied to the module globals so the sub-proxies pick
    them up when they next read these names:

      * Upstream LB / shard / chat → `host`:3801 / :3802 / :3815
        (the local dev server uses the same standard ports as prod).
      * Listen ports → 4801 / 4802 / 4815 (shifted by +1000 so a
        prod-mode proxy can run side-by-side without conflict).
      * Capture directory base → `captures_debug/` (new session
        subdirectory under it, matching the prod-mode layout).

    Call this BEFORE the sub-proxy run() threads start. Listen ports
    are only consumed at bind() time, and CAPTURE_DIR is consulted
    per-packet, so a one-shot call at startup is enough.
    """
    global DEFAULT_REAL_LB, DEFAULT_REAL_SHARD, DEFAULT_REAL_CHAT
    global LB_LISTEN_PORT, SHARD_LISTEN_PORT, CHAT_LISTEN_PORT
    global CAPTURE_DIR
    DEFAULT_REAL_LB    = (host, 3801)
    DEFAULT_REAL_SHARD = (host, 3802)
    DEFAULT_REAL_CHAT  = (host, 3815)
    LB_LISTEN_PORT    = 4801
    SHARD_LISTEN_PORT = 4802
    CHAT_LISTEN_PORT  = 4815
    CAPTURE_DIR = os.path.join("captures_debug", _session_ts)
    log.info(
        f"[proxy] local-server mode: upstream={host}, "
        f"listen=({LB_LISTEN_PORT}/{SHARD_LISTEN_PORT}/{CHAT_LISTEN_PORT}), "
        f"captures={CAPTURE_DIR}"
    )


def log_packet(tag: str, pkt: dict, extra: str = "", state: dict | None = None):
    """Log + capture one framed packet.

    `state`, when given, is a per-connection dict that the proxy uses to
    accumulate session info (currently just the local user's `uid`).
    The shard proxy passes one shared dict between its S→C and C→S relay
    threads; the LB and chat proxies don't pass one. When `state["uid"]`
    becomes known it is appended to capture filenames so per-user runs
    are easy to grep.
    """
    if pkt.get("special"):
        log.info(f"[{tag}] SPECIAL (ff ff ff fe + 8 bytes) {extra}")
        return
    body = pkt.get("body", b"")
    pkt_t = pkt['scmd_pkt_type']
    direction = "S→C" if "S→C" in tag else "C→S" if "C→S" in tag else ""

    # Single decode dispatch — async-req kaitai, notification bag and the
    # per-SCMD struct decoders all live behind scmd_decoders.decode_packet.
    decoded = scmd_decoders.decode_packet(pkt_t, body, direction)

    hdr = (f"[{tag}] send=0x{pkt['send_counter']:04x} "
           f"echo=0x{pkt['echo_send_counter']:04x} "
           f"pkt=0x{pkt_t:04x}({decoded.pkt_name}) "
           f"cs=0x{pkt['checksum']:04x} body_len={pkt['body_len']}"
           f"{decoded.detail}")

    # SCMD_AUTH_ACK (pkt 0x05) is the server's response to a successful
    # authentication and carries `u64 uid` at body offset 0 — that's the
    # local user, sent exactly once per connection well before any
    # gameplay traffic. Latch it into the per-connection state so
    # subsequent captures can be tagged with the uid.
    if state is not None and pkt_t == 0x05 and len(body) >= 8 \
            and state.get("uid") is None:
        try:
            state["uid"] = int.from_bytes(body[:8], "big")
        except Exception:
            pass

    # Save the full body to disk for offline extraction — the log hexdump
    # is still truncated to keep the log readable.
    if body:
        with _capture_lock:
            idx = _capture_idx[0]
            _capture_idx[0] = idx + 1
        try:
            os.makedirs(CAPTURE_DIR, exist_ok=True)
            # The "ac<idx>"/"sn<idx>" suffix comes straight from the
            # decode dispatch — sub_id is only set for CSCMD_ASYNC_REQ
            # (AC opcode) and SCMD_NOTIFICATION (SN id).
            sub_suffix = ""
            if decoded.pkt_name == "CSCMD_ASYNC_REQ" and decoded.sub_id is not None:
                sub_suffix = f"_ac{decoded.sub_id:04x}_{decoded.sub_name.lower()}"
            elif decoded.pkt_name == "SCMD_NOTIFICATION" and decoded.sub_id is not None:
                sub_suffix = f"_sn{decoded.sub_id:02x}_{decoded.sub_name.lower()}"
            uid_suffix = (f"_uid{state['uid']}"
                          if state is not None and state.get("uid") is not None
                          else "")
            fname = (f"{idx:04d}_{direction.replace('→', '_to_')}{uid_suffix}"
                     f"_pkt{pkt_t:02x}_{decoded.pkt_name.lower()}"
                     f"{sub_suffix}_len{len(body)}.bin")
            with open(os.path.join(CAPTURE_DIR, fname), "wb") as f:
                f.write(body)
            hdr += f" saved={fname}"
        except Exception as e:
            hdr += f" save_error={e}"
    if extra:
        hdr += f" {extra}"
    log.info(_colorize(hdr, decoded.ok))
    if body and not decoded.ok:
        body_preview = body[:128]
        log.info(_colorize(f"    body[0:{len(body_preview)}]:\n{hexdump(body_preview)}", False))

    # Also push to the in-process packet bus so the Qt UI (and any other
    # subscriber) can see this packet. publish() is a no-op with no subscribers.
    packet_bus.publish(packet_bus.PacketRecord(
        idx=0,                          # overwritten by publish()
        ts=time.time(),
        tag=tag,
        direction=direction,
        pkt_type=pkt_t,
        pkt_name=decoded.pkt_name,
        sub_id=decoded.sub_id,
        sub_name=decoded.sub_name,
        uid=(state["uid"] if state is not None else None),
        body=body or b"",
        send_counter=pkt.get("send_counter", 0),
        echo_send_counter=pkt.get("echo_send_counter", 0),
        checksum=pkt.get("checksum", 0),
        body_len=pkt.get("body_len", len(body) if body else 0),
        decoded_line=hdr,
        ok=decoded.ok,
    ))


def relay_loop(src: socket.socket, dst: socket.socket, tag: str,
               on_packet=None, state: dict | None = None):
    """Read framed packets from src, log them, optionally mutate via
    on_packet(pkt) -> pkt (return the packet to forward, or None to drop),
    then write to dst. Falls back to raw forwarding if framing fails.

    `state`, when given, is a per-connection dict shared between the two
    relay threads (S→C and C→S) of the same connection; see log_packet.
    """
    try:
        while True:
            pkt = read_packet(src)
            if pkt is None:
                break
            log_packet(tag, pkt, state=state)
            if on_packet is not None:
                pkt = on_packet(pkt)
                if pkt is None:
                    continue
            if pkt.get("special"):
                # special packets are ff ff ff fe + 8 bytes (12 total)
                dst.sendall(b"\xff\xff\xff\xfe" + b"\x00" * 8)
            else:
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
