"""TGPChannel packet framing and checksum."""
import struct
import socket

_M    = 0x5bd1e995
_SEED = 0x1337533d


def checksum(body_len: int, msg_type: int, seq: int, body: bytes) -> int:
    """MurmurHash2-based 16-bit checksum used by TGPChannel."""
    hdr = struct.pack("<IHHHxx", body_len, msg_type, (seq >> 16) & 0xffff, seq & 0xffff)
    h = (12 ^ _SEED) & 0xffffffff
    for data in (hdr, body):
        i = 0
        while i + 4 <= len(data):
            k = data[i] | (data[i+1]<<8) | (data[i+2]<<16) | (data[i+3]<<24)
            k = (k * _M) & 0xffffffff; k ^= k >> 24; k = (k * _M) & 0xffffffff
            h = ((h * _M) ^ k) & 0xffffffff
            i += 4
        rem = len(data) - i
        if rem >= 3: h ^= data[i+2] << 16
        if rem >= 2: h ^= data[i+1] << 8
        if rem >= 1: h = ((h ^ data[i]) * _M) & 0xffffffff
    h ^= h >> 13; h = (h * _M) & 0xffffffff; h ^= h >> 15
    return h & 0xffff


def make_packet(msg_type: int, seq: int, body: bytes) -> bytes:
    cs = checksum(len(body), msg_type, seq, body)
    return struct.pack(">IHIH", len(body), msg_type, seq, cs) + body


def read_packet(sock: socket.socket) -> dict | None:
    """Read one framed packet from sock. Returns None on EOF/error."""
    def recv_exact(n):
        buf = b""
        while len(buf) < n:
            chunk = sock.recv(n - len(buf))
            if not chunk:
                return None
            buf += chunk
        return buf

    hdr = recv_exact(12)
    if hdr is None:
        return None
    if hdr[:4] == b"\xff\xff\xff\xfe":
        # Special packet is exactly 12 bytes on the wire (ff ff ff fe +
        # 8 bytes of data). The whole thing is already in `hdr`; do NOT
        # read 8 more — that would over-read into the next packet and
        # leave recv_exact blocked forever trying to satisfy a garbage
        # body_len pulled from misaligned bytes.
        return {"special": True, "data": hdr[4:12]}
    body_len, msg_type, seq, req_id = struct.unpack(">IHIH", hdr)
    body = recv_exact(body_len)
    if body is None:
        return None
    return {"body_len": body_len, "type": msg_type, "seq": seq, "req_id": req_id, "body": body}
