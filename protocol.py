"""TGPChannel packet framing and checksum.

Header layout (big-endian, 12 bytes total):

    [4B body_len][2B send_counter][2B echo_send_counter][2B scmd_pkt_type][2B checksum]

Field meanings:
- body_len:           length of the following body in bytes
- send_counter:       per-direction monotonic counter (client starts 0x0001;
                      real server starts ~0xe2ed). NOT a packet type.
- echo_send_counter:  for responses, echoes the request's send_counter so the
                      Lua client can match the response back to its request.
                      Server-pushed packets leave this 0.
- scmd_pkt_type:      the SCMD type small-index 0..38 (table at VMA 0x08fe7ac0
                      in the binary). 0x000d = CSCMD_ASYNC_REQ, the wrapper
                      for everything that carries an AC_* opcode in body[0:2].
- checksum:           16-bit truncated MurmurHash2 (seed 0x1337533d).

read_packet() returns both the new explicit names and legacy aliases
(`type`, `seq`, `req_id`) so older callers keep working during the rename.
"""
import struct
import socket

_M    = 0x5bd1e995
_SEED = 0x1337533d


def checksum(body_len: int, send_counter: int, echo_send_counter: int,
             scmd_pkt_type: int, body: bytes) -> int:
    """MurmurHash2-based 16-bit checksum used by TGPChannel.

    Note the hashed-header layout is little-endian — the on-wire bytes are
    big-endian but the original C++ code feeds the parsed header to murmur2
    in native (LE) byte order, so we mirror that here.
    """
    hdr = struct.pack("<IHHHxx", body_len, send_counter,
                      echo_send_counter, scmd_pkt_type)
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


def make_packet(send_counter: int, echo_send_counter: int,
                scmd_pkt_type: int, body: bytes) -> bytes:
    """Build a TGP-framed packet with the four-field header."""
    cs = checksum(len(body), send_counter, echo_send_counter,
                  scmd_pkt_type, body)
    return struct.pack(">IHHHH", len(body), send_counter,
                       echo_send_counter, scmd_pkt_type, cs) + body


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
    body_len, send_counter, echo, pkt_type, cs = struct.unpack(">IHHHH", hdr)
    body = recv_exact(body_len)
    if body is None:
        return None
    return {
        "body_len": body_len,
        "send_counter": send_counter,
        "echo_send_counter": echo,
        "scmd_pkt_type": pkt_type,
        "checksum": cs,
        "body": body,
        # Legacy aliases — older callers still use these names.
        "type":    send_counter,
        "seq":     (echo << 16) | pkt_type,
        "req_id":  cs,
    }
