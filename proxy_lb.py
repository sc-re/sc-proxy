"""MITM proxy for the load balancer (port 3801).

Forwards the client's LB connection to the real server, parses every
packet, and REWRITES the shard-address response body so the client
connects back to our shard/chat proxies (127.0.0.1:19803 / 3815)
instead of talking to the real shard directly. The real shard/chat
address is extracted and stashed in proxy_util so proxy_shard and
proxy_chat know where to forward.

The shard address packet body is bit-packed (see loadbalancer.py
_BitWriter): [bool][u8][string ip][u16 port][bool][string ip][u16 port].
"""
import socket
import struct
import threading
import logging

from protocol import make_packet, read_packet
import proxy_util

log = logging.getLogger("proxy.lb")

LISTEN_PORT = 3801

# scmd_pkt_type values pushed by the LB.
_PKT_LB_CVARS       = 2  # SCMD_LB_CVARS
_PKT_ASSIGNED_SHARD = 0  # SCMD_ASSIGNED_SHARD


class _BitReader:
    """Mirror of loadbalancer._BitWriter — reads bits MSB-first."""
    def __init__(self, data: bytes):
        self._buf = data
        self._bit = 0  # total bit offset from start of buffer

    def _read_bit(self) -> int:
        byte_idx = self._bit >> 3
        bit_idx  = self._bit & 7
        if byte_idx >= len(self._buf):
            raise EOFError("bit reader past end")
        b = (self._buf[byte_idx] >> (7 - bit_idx)) & 1
        self._bit += 1
        return b

    def bool(self) -> bool:
        return bool(self._read_bit())

    def uint(self, n: int) -> int:
        v = 0
        for _ in range(n):
            v = (v << 1) | self._read_bit()
        return v

    def uint8(self) -> int:
        return self.uint(8)

    def uint16(self) -> int:
        return self.uint(16)

    def string(self) -> str:
        out = bytearray()
        while True:
            c = self.uint8()
            if c == 0:
                break
            out.append(c)
        return out.decode(errors="replace")


def _parse_shard_body(body: bytes):
    """Real server layout: [bool][u8 count][count × (string ip, u16 port)]
    [bool][string chat_ip][u16 chat_port]. Returns (shards, (chat_ip,
    chat_port)) where shards is a list of (ip, port)."""
    br = _BitReader(body)
    _ = br.bool()
    count = br.uint8()
    shards = []
    for _ in range(count):
        ip = br.string()
        port = br.uint16()
        shards.append((ip, port))
    _ = br.bool()
    chat_ip = br.string()
    chat_port = br.uint16()
    return shards, (chat_ip, chat_port)


class _BitWriter:
    def __init__(self):
        self._buf = bytearray()
        self._bit = 0

    def _write_bit(self, b):
        if self._bit == 0:
            self._buf.append(0)
        if b:
            self._buf[-1] |= 1 << (7 - self._bit)
        self._bit = (self._bit + 1) % 8

    def bool(self, v):
        self._write_bit(1 if v else 0)

    def uint8(self, v):
        for i in range(7, -1, -1):
            self._write_bit((v >> i) & 1)

    def uint16(self, v):
        for i in range(15, -1, -1):
            self._write_bit((v >> i) & 1)

    def string(self, s):
        for ch in s:
            self.uint8(ord(ch))
        self.uint8(0)

    def bytes(self):
        return bytes(self._buf)


def _build_shard_body(shards: list, chat_ip: str, chat_port: int) -> bytes:
    bw = _BitWriter()
    bw.bool(True)
    bw.uint8(len(shards))
    for ip, port in shards:
        bw.string(ip)
        bw.uint16(port)
    bw.bool(True)
    bw.string(chat_ip)
    bw.uint16(chat_port)
    return bw.bytes()


def _rewrite_shard_addr(pkt: dict, fake_shard: tuple[str, int],
                        fake_chat: tuple[str, int]) -> dict:
    try:
        shards, chat = _parse_shard_body(pkt["body"])
        log.info(f"[LB] real shards={shards} chat={chat[0]}:{chat[1]}")
        if shards:
            proxy_util.set_real_shard(shards[0][0], shards[0][1])
        proxy_util.set_real_chat(chat[0], chat[1])
    except Exception as e:
        log.warning(f"[LB] could not parse shard body, forwarding as-is: {e}")
        return pkt
    new_body = _build_shard_body([fake_shard], fake_chat[0], fake_chat[1])
    log.info(f"[LB] rewritten → shard={fake_shard[0]}:{fake_shard[1]} "
             f"chat={fake_chat[0]}:{fake_chat[1]}")
    pkt["body"] = new_body
    pkt["body_len"] = len(new_body)
    return pkt


def _handle(client: socket.socket, addr):
    log.info(f"[LB] connection from {addr}")
    try:
        upstream = proxy_util.connect_upstream(*proxy_util.DEFAULT_REAL_LB)
    except Exception as e:
        log.error(f"[LB] upstream connect failed: {e}")
        client.close()
        return
    log.info(f"[LB] upstream → {proxy_util.DEFAULT_REAL_LB}")

    # The LB protocol is one-shot: the server pushes cvars first, then
    # shard_addr, then closes. Identify packets by position — the real
    # server's msg_type values vary per connection (observed 0x8ff4,
    # 0x9020, 0x7dfb etc.), so type-based matching is unreliable.
    fake_shard = ("127.0.0.1", 19803)
    fake_chat  = ("127.0.0.1", 3815)
    s2c_idx = [0]  # list for closure mutation

    def on_s2c(pkt):
        if pkt.get("special"):
            return pkt
        s2c_idx[0] += 1
        if s2c_idx[0] == 2:
            return _rewrite_shard_addr(pkt, fake_shard, fake_chat)
        return pkt

    t1 = threading.Thread(
        target=proxy_util.relay_loop,
        args=(upstream, client, "LB S→C"),
        kwargs={"on_packet": on_s2c},
        daemon=True,
    )
    t2 = threading.Thread(
        target=proxy_util.relay_loop,
        args=(client, upstream, "LB C→S"),
        daemon=True,
    )
    t1.start(); t2.start()
    t1.join(); t2.join()
    try: client.close()
    except: pass
    try: upstream.close()
    except: pass
    log.info(f"[LB] connection from {addr} closed")


def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", LISTEN_PORT))
    s.listen(8)
    log.info(f"[LB] listening on port {LISTEN_PORT}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=_handle, args=(conn, addr), daemon=True).start()
