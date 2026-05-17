"""MITM proxy for the shard (port 19803, same as shard.py).

Accepts connections that iptables has redirected from port 3802 and
forwards them to the real shard whose address was captured by the LB
proxy (or to the SC_REAL_HOST fallback). Every framed packet is parsed
and logged in both directions so the real server's responses can be
used as a reference for the stub shard implementation.

This is a pure relay — the shard protocol has heavy session state
(challenge/response, RSA signature, per-session message counters) so we
don't try to synthesize anything, we just eavesdrop.
"""
import socket
import threading
import logging

from ac_types import pkt_type_name
import proxy_util

log = logging.getLogger("proxy.shard")


def _tag_packet(pkt: dict, base: str) -> str:
    """Append a human-readable hint about what the packet is."""
    if pkt.get("special"):
        return base
    body = pkt["body"]
    if len(body) >= 2:
        ac_idx = int.from_bytes(body[:2], "big")
        name = pkt_type_name(ac_idx)
        if name != f"0x{ac_idx:04x}":
            return f"{base} ac=0x{ac_idx:04x} ({name})"
    return base


def _handle(client: socket.socket, addr):
    log.info(f"[SHARD] connection from {addr}")
    real = proxy_util.get_real_shard()
    try:
        upstream = proxy_util.connect_upstream(*real)
    except Exception as e:
        log.error(f"[SHARD] upstream connect failed ({real}): {e}")
        client.close()
        return
    log.info(f"[SHARD] upstream → {real}")

    # Per-connection state — shared between the two relay threads.
    # log_packet learns the uid from the first SCMD_USER_PROFILE_NOTIFICATION
    # and stamps it into subsequent capture filenames.
    conn_state: dict = {"uid": None}

    def on_s2c(pkt):
        if pkt.get("special"):
            log.info("[SHARD S→C] SPECIAL")
        return pkt

    def on_c2s(pkt):
        if not pkt.get("special") and pkt["body"]:
            tag = _tag_packet(pkt, "C→S")
            if tag:
                log.debug(f"[SHARD] {tag}")
        return pkt

    t1 = threading.Thread(
        target=proxy_util.relay_loop,
        args=(upstream, client, "SHARD S→C"),
        kwargs={"on_packet": on_s2c, "state": conn_state},
        daemon=True,
    )
    t2 = threading.Thread(
        target=proxy_util.relay_loop,
        args=(client, upstream, "SHARD C→S"),
        kwargs={"on_packet": on_c2s, "state": conn_state},
        daemon=True,
    )
    t1.start(); t2.start()
    t1.join(); t2.join()
    try: client.close()
    except: pass
    try: upstream.close()
    except: pass
    log.info(f"[SHARD] connection from {addr} closed (uid={conn_state['uid']})")


def run():
    port = proxy_util.SHARD_LISTEN_PORT
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", port))
    s.listen(8)
    log.info(f"[SHARD] listening on port {port}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=_handle, args=(conn, addr), daemon=True).start()
