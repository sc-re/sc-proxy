"""MITM proxy for the chat server (port 3815).

Uses a raw byte relay (no TGP parsing) because:
  1. The chat server may use a different checksum or framing than the shard.
  2. relay_loop re-encodes packets through make_packet which recalculates
     the checksum — if the chat server's checksum differs, the game gets a
     bad packet and immediately disconnects.
  3. Raw relay is sufficient to capture the full exchange for protocol analysis.
"""
import os
import socket
import threading
import logging

import proxy_util

log = logging.getLogger("proxy.chat")

LISTEN_PORT = 3815

_chat_idx = [0]
_chat_lock = threading.Lock()


def _save_raw(tag: str, data: bytes):
    """Dump each chat packet chunk to disk so we can diff what the real
    server sent vs. what our chat.py stub produces. Directory is
    proxy_util.CAPTURE_DIR, files named chat_<idx>_<dir>_<len>.bin."""
    with _chat_lock:
        idx = _chat_idx[0]
        _chat_idx[0] = idx + 1
    try:
        os.makedirs(proxy_util.CAPTURE_DIR, exist_ok=True)
        direction = tag.split()[-1].replace("→", "_to_")
        fname = f"chat_{idx:04d}_{direction}_len{len(data)}.bin"
        with open(os.path.join(proxy_util.CAPTURE_DIR, fname), "wb") as f:
            f.write(data)
    except Exception as e:
        log.warning(f"[{tag}] save_error={e}")


def _raw_relay(src: socket.socket, dst: socket.socket, tag: str):
    try:
        while True:
            data = src.recv(4096)
            if not data:
                log.info(f"[{tag}] EOF")
                break
            _save_raw(tag, data)
            log.info(f"[{tag}] {len(data)} bytes:\n{proxy_util.hexdump(data[:128])}")
            dst.sendall(data)
    except Exception as e:
        log.warning(f"[{tag}] {e}")
    finally:
        for sock in (src, dst):
            try:
                sock.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass


def _handle(client: socket.socket, addr):
    log.info(f"[CHAT] connection from {addr}")
    real = proxy_util.get_real_chat()
    log.info(f"[CHAT] connecting to real chat server {real[0]}:{real[1]}")
    try:
        upstream = proxy_util.connect_upstream(*real)
    except Exception as e:
        log.error(f"[CHAT] upstream connect failed ({real[0]}:{real[1]}): {e}")
        client.close()
        return
    log.info(f"[CHAT] upstream connected → {real[0]}:{real[1]}")

    t1 = threading.Thread(target=_raw_relay, args=(upstream, client, "CHAT S→C"), daemon=True)
    t2 = threading.Thread(target=_raw_relay, args=(client, upstream, "CHAT C→S"), daemon=True)
    t1.start(); t2.start()
    t1.join(); t2.join()
    try: client.close()
    except Exception: pass
    try: upstream.close()
    except Exception: pass
    log.info(f"[CHAT] connection from {addr} closed")


def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", LISTEN_PORT))
    s.listen(8)
    log.info(f"[CHAT] listening on port {LISTEN_PORT}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=_handle, args=(conn, addr), daemon=True).start()
