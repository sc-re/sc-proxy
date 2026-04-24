"""MITM proxy for the chat server (port 3815).

Layers:
  1. Raw byte relay (unchanged) — still forwards bytes verbatim so the
     real server's checksums survive.
  2. _save_raw — still dumps each chunk under proxy_util.CAPTURE_DIR.
  3. Frame parser + body decoder — decodes TGP chat frames alongside
     the relay so the log shows what each packet *means*.

Chat frame format (reverse-engineered from captures, see chat.py):
    [4B body_len LE][4B signature LE][2B ctr LE][1B flag][body]

Body format by (ctr, flag):
  (0, 0xff)  AUTH        C→S 32B  — token_a, token_b
             AUTHRES     S→C 52B  — echoed tokens + session key
  (2, 0xff)  SECONDARY1  both  6B  — server's PeerID (IP+port BE)
  (3, 0xff)  SECONDARY2  both  6B  — client's PeerID enforced by server
  (4, 0xff)  PING        both  0B
  (5, 0xff)  PONG        both  0B
  (1, 0x00)  CHAN_REQ    req/ack for channel list
  (2, 0x00)  CHAN_DATA   C-initiated channel request (join by name)
  (3, 0x00)  CHAN_RESP   S-initiated channel response
  (5, 0x00)  CHAN_PUSH   server push — room chat message
  (6, 0x00)  PM_SEND     C→S private message
  (7, 0x00)  PM_ACK      S→C private message ack

All flag=0x00 bodies use a bit-packed layout:
    bit  0..  1  2-bit alignment prefix (constant 00)
    bit  2.. 49  48-bit destination PeerID (IP+port BE)
    bit 50..     type-specific fields

PM_SEND (30-byte body) fields after the peer:
    bit  50..73   24 zero bits (alignment pad before uid field)
    bit  74..137  64-bit recipient uid BE (shift-2 bytes 9..16;
                  matches the rest of the TGP family. Identical wire
                  bytes to an older "56 zeros + 24b uid" reading when
                  the uid fits in 24 bits, which is true for every
                  observed capture.)
    bit 138..      null-terminated ASCII message (byte-aligned in the
                  shift-2 view, i.e. reading 8-bit chunks from bit 138
                  gives the message chars directly: 'w','t','f',0x00)
    bit ...       zeros until:
    bit (-14)..(-7) 8-bit session PM counter (0, 1, 2, …)
    bit (-6)..end 6 pad bits

Other flag=0x00 bodies carry null-terminated UTF-8 channel names
(prefixed with '#') and nicknames + message text; those are extracted
on a best-effort basis by scanning for printable runs in the shift-2
(byte-realigned) view.
"""
import os
import socket
import struct
import threading
import logging

import proxy_util

log = logging.getLogger("proxy.chat")

LISTEN_PORT = 3815
FRAME_HEADER_LEN = 11

CTR_AUTH      = 0
CTR_CHAN_REQ  = 1
CTR_CHAN_DATA = 2
CTR_CHAN_RESP = 3
CTR_PING      = 4
CTR_PONG      = 5
CTR_PM_SEND   = 6
CTR_PM_ACK    = 7

_chat_idx = [0]
_chat_lock = threading.Lock()


def _save_raw(tag: str, data: bytes):
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


# ---------------------------------------------------------------------------
# Frame layer
# ---------------------------------------------------------------------------

def _frame_name(ctr: int, flag: int, direction: str) -> str:
    if flag == 0xff:
        return {
            CTR_AUTH: "AUTHRES" if direction == "S→C" else "AUTH",
            CTR_CHAN_DATA: "SECONDARY1",
            CTR_CHAN_RESP: "SECONDARY2",
            CTR_PING: "PING",
            CTR_PONG: "PONG",
        }.get(ctr, f"HS_CTR{ctr}")
    return {
        CTR_CHAN_REQ: "CHAN_REQ",
        CTR_CHAN_DATA: "CHAN_DATA",
        CTR_CHAN_RESP: "CHAN_RESP",
        CTR_PONG: "CHAN_PUSH",
        CTR_PM_SEND: "PM_SEND",
        CTR_PM_ACK: "PM_ACK",
    }.get(ctr, f"DATA_CTR{ctr}")


class FrameBuffer:
    """Per-direction rolling buffer that yields complete TGP chat frames
    as they arrive. A single recv() may deliver multiple frames or a
    partial frame — feed() handles both."""

    def __init__(self):
        self._buf = bytearray()

    def feed(self, data: bytes):
        self._buf.extend(data)
        while True:
            if len(self._buf) < FRAME_HEADER_LEN:
                return
            body_len = struct.unpack_from('<I', self._buf, 0)[0]
            if body_len > 1 << 20:
                log.warning(f"implausible body_len={body_len}; dropping buffer")
                self._buf.clear()
                return
            total = FRAME_HEADER_LEN + body_len
            if len(self._buf) < total:
                return
            frame = bytes(self._buf[:total])
            del self._buf[:total]
            yield frame


def parse_frame(frame: bytes) -> dict:
    body_len = struct.unpack_from('<I', frame, 0)[0]
    sig      = struct.unpack_from('<I', frame, 4)[0]
    ctr      = struct.unpack_from('<H', frame, 8)[0]
    flag     = frame[10]
    body     = frame[FRAME_HEADER_LEN:FRAME_HEADER_LEN + body_len]
    return {"body_len": body_len, "signature": sig, "ctr": ctr,
            "flag": flag, "body": body}


# ---------------------------------------------------------------------------
# Bitstream / body decoders
# ---------------------------------------------------------------------------

class BitReader:
    def __init__(self, data: bytes):
        self._bits = ''.join(f'{b:08b}' for b in data)
        self.off = 0

    def read(self, n: int) -> int:
        if self.off + n > len(self._bits):
            raise ValueError(f"read {n}b past end (off={self.off}, len={len(self._bits)})")
        v = int(self._bits[self.off:self.off + n], 2) if n else 0
        self.off += n
        return v

    def read_bytes(self, n_bits: int) -> bytes:
        v = self.read(n_bits)
        return v.to_bytes((n_bits + 7) // 8, 'big')

    def remaining(self) -> int:
        return len(self._bits) - self.off


def _decode_peer6(raw: bytes) -> str:
    if len(raw) != 6 or raw == b"\x00" * 6:
        return "0.0.0.0:0"
    return f"{socket.inet_ntoa(raw[:4])}:{struct.unpack('>H', raw[4:6])[0]}"


def _shift2_bytes(body: bytes) -> bytes:
    """Return the body re-aligned so bit 2 of the original becomes bit 0 —
    this is the natural byte-aligned view for flag=0x00 bodies."""
    bits = ''.join(f'{b:08b}' for b in body)
    realigned = bits[2:]
    realigned += '0' * ((8 - len(realigned) % 8) % 8)
    return bytes(int(realigned[i:i+8], 2) for i in range(0, len(realigned), 8))


def _extract_strings(data: bytes, min_len: int = 3) -> list[str]:
    """Pull out printable UTF-8 runs (ASCII + 2-byte UTF-8) of >= min_len chars.
    Used to surface channel names, nicks and message text inside bodies we
    don't fully parse yet."""
    out, cur = [], bytearray()
    i = 0
    while i < len(data):
        b = data[i]
        if 0x20 <= b < 0x7f or b == 0x23:  # printable ASCII + '#'
            cur.append(b); i += 1
        elif 0xC0 <= b <= 0xDF and i + 1 < len(data) and 0x80 <= data[i+1] <= 0xBF:
            cur.append(b); cur.append(data[i+1]); i += 2
        else:
            if len(cur) >= min_len:
                try:
                    out.append(cur.decode('utf-8'))
                except UnicodeDecodeError:
                    pass
            cur = bytearray(); i += 1
    if len(cur) >= min_len:
        try:
            out.append(cur.decode('utf-8'))
        except UnicodeDecodeError:
            pass
    return out


def decode_auth(body: bytes) -> dict:
    """AUTH body = two protocol-registration TLVs.
    body[8:16]  = PROTO_CL  (ChatProtoCL m3d::net::proto class hash)
    body[20:28] = PROTO_SV  (ChatProtoSV m3d::net::proto class hash)
    These are NOT credentials — see memory/project_chat_proto_ids.md."""
    if len(body) != 32:
        return {"raw": body.hex()}
    return {"proto_cl": body[8:16].hex(), "proto_sv": body[20:28].hex()}


def decode_authres(body: bytes) -> dict:
    """AUTHRES body = server echo of AUTH's two TLVs, each paired with the
    chat session_key. Note AUTHRES lists PROTO_SV first, then PROTO_CL."""
    if len(body) != 52:
        return {"raw": body.hex()}
    return {
        "proto_sv":    body[8:16].hex(),
        "session_key": body[16:24].hex(),
        "proto_cl":    body[28:36].hex(),
    }


def decode_peer_body(body: bytes) -> dict:
    return {"peer": _decode_peer6(body)} if len(body) == 6 else {"raw": body.hex()}


def decode_pm_send(body: bytes) -> dict:
    """PM_SEND layout (ctr=6, flag=0x00):
        2b prefix | 48b dest_peer | 24b zero pad | 64b recv_uid (BE) |
        null-terminated ASCII message (byte-aligned) |
        zero padding | 8b counter | 6b pad
    """
    br = BitReader(body)
    prefix    = br.read(2)
    peer_raw  = br.read_bytes(48)
    _         = br.read(24)
    recv_uid  = br.read(64)

    # Read the message: successive 8-bit chunks starting at bit 138,
    # up to (but not including) the 14 trailing bits (8 counter + 6 pad)
    # or the first null byte.
    text = bytearray()
    text_end = len(body) * 8 - 14
    while br.off + 8 <= text_end:
        ch = br.read(8)
        if ch == 0:
            break
        text.append(ch)

    counter = int(''.join(f'{b:08b}' for b in body)[-14:-6], 2)

    return {
        "prefix":    prefix,
        "dest_peer": _decode_peer6(peer_raw),
        "recv_uid":  recv_uid,
        "text":      text.decode('utf-8', errors='replace'),
        "counter":   counter,
    }


def decode_pm_ack(body: bytes) -> dict:
    """PM_ACK (ctr=7, flag=0x00, 19B body). Same general shape as PM_SEND
    but echoes only the peer + counter — the 2-bit counter lives at
    bits 136-137 of the body (top 2 bits of byte 17)."""
    br = BitReader(body)
    prefix   = br.read(2)
    peer_raw = br.read_bytes(48)
    # The ack has a fixed tail; extract the counter from its known
    # position at bit 136-137 regardless of other layout.
    all_bits = ''.join(f'{b:08b}' for b in body)
    counter = int(all_bits[136:138], 2) if len(all_bits) >= 138 else -1
    return {
        "prefix":    prefix,
        "dest_peer": _decode_peer6(peer_raw),
        "counter":   counter,
    }


def decode_chan_push(body: bytes) -> dict:
    """CHAN_PUSH (ctr=5, flag=0x00) — server-forwarded room message.
    Shift-2 layout (reversed from captures):
        peer(6)
        + 00×3                           (pad)
        + '#' + channel + \\0            (null-terminated channel name)
        + sender_uid(8, BE)              (upper 5 bytes are zero in
                                          practice because uids are <
                                          2^24; the low 3 bytes can
                                          coincidentally look like
                                          printable ASCII and be
                                          misread as part of the nick
                                          by a naïve extractor — e.g.
                                          `tDJohnnynator` = u64 ending
                                          in `74 44` followed by nick
                                          `Johnnynator`)
        + nick + \\0\\0                  (null-terminated nick)
        + text + \\0\\0                  (null-terminated UTF-8 text)

    The 3-byte sender field is mandatory and causes a nick of length
    N to start at a fixed offset regardless of whether those bytes are
    printable ASCII. A `_extract_strings` heuristic would glue the
    printable ones into the nick (e.g. `:qTStason1974` for `Stason1974`,
    `tDJohnnynator` for `Johnnynator`); parsing by structure avoids this.
    """
    if len(body) * 8 < 50:
        return {"raw": body.hex()}
    br = BitReader(body)
    prefix   = br.read(2)
    peer_raw = br.read_bytes(48)
    aligned  = _shift2_bytes(body)[6:]   # everything after the peer

    out = {"prefix": prefix, "dest_peer": _decode_peer6(peer_raw)}

    # Find "#channel\0" — the first '#' and the NUL after it.
    hash_idx = aligned.find(b'#')
    if hash_idx < 0:
        out["tail_hex"] = aligned.hex()
        return out
    nul_after_chan = aligned.find(b'\x00', hash_idx)
    if nul_after_chan < 0:
        out["tail_hex"] = aligned.hex()
        return out
    out["channel"] = aligned[hash_idx:nul_after_chan].decode('utf-8', errors='replace')

    # 8-byte BE sender uid follows the channel's NUL.
    uid_start = nul_after_chan + 1
    nick_start = uid_start + 8
    if nick_start >= len(aligned):
        out["tail_hex"] = aligned[nul_after_chan:].hex()
        return out
    out["sender_uid"] = int.from_bytes(aligned[uid_start:nick_start], 'big')

    # Null-terminated nick.
    nul_after_nick = aligned.find(b'\x00', nick_start)
    if nul_after_nick < 0:
        out["nick_raw_hex"] = aligned[nick_start:].hex()
        return out
    out["nick"] = aligned[nick_start:nul_after_nick].decode('utf-8', errors='replace')

    # Text: skip 1 extra NUL pad (observed), then null-terminate.
    text_start = nul_after_nick + 2
    nul_after_text = aligned.find(b'\x00', text_start)
    if nul_after_text < 0:
        out["text"] = aligned[text_start:].decode('utf-8', errors='replace')
    else:
        out["text"] = aligned[text_start:nul_after_text].decode('utf-8', errors='replace')
    return out


def decode_chat_data(body: bytes) -> dict:
    """Generic fallback for flag=0x00 bodies we don't have a bespoke
    parser for yet. Extracts the destination peer and lifts any
    printable strings out of the shift-2 view."""
    if len(body) * 8 < 50:
        return {"raw": body.hex()}
    br = BitReader(body)
    prefix   = br.read(2)
    peer_raw = br.read_bytes(48)
    aligned  = _shift2_bytes(body)[6:]
    out = {
        "prefix":    prefix,
        "dest_peer": _decode_peer6(peer_raw),
        "tail_hex":  aligned.hex(),
    }
    strs = _extract_strings(aligned)
    if strs:
        out["strings"] = strs
    return out


def decode_body(direction: str, ctr: int, flag: int, body: bytes) -> dict:
    if flag == 0xff:
        if ctr == CTR_AUTH:
            return decode_authres(body) if direction == "S→C" else decode_auth(body)
        if ctr in (CTR_CHAN_DATA, CTR_CHAN_RESP):
            return decode_peer_body(body)
        if ctr in (CTR_PING, CTR_PONG):
            return {} if not body else {"raw": body.hex()}
        return {"raw": body.hex()}
    # flag == 0x00
    if ctr == CTR_PM_SEND:
        return decode_pm_send(body)
    if ctr == CTR_PM_ACK:
        return decode_pm_ack(body)
    # ctr=5 flag=0x00 direction=S→C is the server-pushed room message;
    # use structural parser so printable hash bytes don't glue onto nick.
    if ctr == CTR_PONG and direction == "S→C":
        return decode_chan_push(body)
    return decode_chat_data(body)


# ---------------------------------------------------------------------------
# Relay + logging
# ---------------------------------------------------------------------------

def _format_decoded(d: dict) -> str:
    return " ".join(
        f"{k}={v!r}" if isinstance(v, (bytes, bytearray, list)) or (isinstance(v, str) and " " in v)
        else f"{k}={v}"
        for k, v in d.items()
    )


def _log_frame(tag: str, direction: str, frame: bytes):
    hdr = parse_frame(frame)
    name = _frame_name(hdr["ctr"], hdr["flag"], direction)
    try:
        decoded = decode_body(direction, hdr["ctr"], hdr["flag"], hdr["body"])
    except Exception as e:
        decoded = {"decode_error": str(e), "raw": hdr["body"].hex()}
    log.info(
        f"[{tag}] {name} body_len={hdr['body_len']} "
        f"sig=0x{hdr['signature']:08x} ctr={hdr['ctr']} flag=0x{hdr['flag']:02x} "
        f"| {_format_decoded(decoded)}"
    )


def _raw_relay(src: socket.socket, dst: socket.socket, tag: str, direction: str):
    buf = FrameBuffer()
    try:
        while True:
            data = src.recv(4096)
            if not data:
                log.info(f"[{tag}] EOF")
                break
            _save_raw(tag, data)
            for frame in buf.feed(data):
                _log_frame(tag, direction, frame)
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

    t1 = threading.Thread(target=_raw_relay, args=(upstream, client, "CHAT S→C", "S→C"), daemon=True)
    t2 = threading.Thread(target=_raw_relay, args=(client, upstream, "CHAT C→S", "C→S"), daemon=True)
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
