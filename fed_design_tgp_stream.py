"""Opaque kaitai type for the FedDesign TGP stream carried in
ac_clan_request_desc (and similar clan packets).

The stream is a recursive tree of typed values. Strings are encoded in
three different schemes and most container-headers have a u32be count.
The format is documented in detail in server.ksy alongside ac_clan_request_desc
where we discovered it; this module implements a best-effort parser.

Encodings
---------
cs0 (carry-shifted, type tags 0x02 / 0x15 / 0x82):
    encode: byte[i] = (char[i] >> 1) | ((char[i-1] & 1) << 7)   char[-1] := 0
    decode: char[i] = ((byte[i] & 0x7F) << 1) | (byte[i+1] >> 7)
    terminator: a byte in {0x00, 0x80} (decoded char == 0)

x2 (multiply-by-two, type tag 0x0a):
    encode: byte = char << 1   (low bit always 0)
    decode: char = byte >> 1
    terminator: byte == 0x00

cleartext (type tag 0x05):
    NUL-terminated raw ASCII

Type tags
---------
    0x02  cs0 string                      (subsequent array element)
    0x03  map (u32be count, then entries) — internal layout still partially opaque
    0x04  u64be
    0x05  cleartext string
    0x06  array (u32be count, then values)
    0x0a  x2 string
    0x0c  struct (u32be count, then `count` × (cleartext-key + tagged-value))
    0x15  cs0 string (rarer; dialect of 0x02)
    0x18  u32be
    0x82  cs0 string with "first array element" flag

Naked keys inside containers
----------------------------
    struct (0x0c) keys are cleartext-NUL-terminated, no leading tag.
    arrays (0x06) hold tagged values, no keys.
    maps (0x03) carry typed keys followed by typed values.

What we don't yet model
-----------------------
The very first ~0x80 bytes of an outer top-level stream have a binary
hash-table header that we leave opaque. Likewise an arbitrary 0x30 tag is
treated as opaque-with-best-effort. Where the walker encounters bytes it
cannot identify, it emits a hex run rather than failing the parse.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Tuple, Union


# ---------- string decoders ---------------------------------------------------

def _printable(c: int) -> str:
    if 0x20 <= c < 0x7F:
        return chr(c)
    if c == 0:
        return ""
    return f"\\x{c:02x}"


def cs0_decode(buf: bytes, off: int) -> Tuple[str, int]:
    """Decode a cs0 (carry-shifted) NUL-terminated string. Returns
    (text, new_off) where new_off points just past the terminator byte."""
    out = []
    while off < len(buf):
        b = buf[off]
        # terminator: a byte in {0x00, 0x80} encodes char == 0
        if b in (0x00, 0x80):
            return "".join(out), off + 1
        nxt = buf[off + 1] if off + 1 < len(buf) else 0
        c = ((b & 0x7F) << 1) | (nxt >> 7)
        out.append(_printable(c))
        off += 1
    return "".join(out), off


def x2_decode(buf: bytes, off: int) -> Tuple[str, int]:
    """Decode an x2 (char<<1) NUL-terminated string."""
    out = []
    while off < len(buf):
        b = buf[off]
        off += 1
        if b == 0x00:
            return "".join(out), off
        out.append(_printable(b >> 1))
    return "".join(out), off


def cleartext_decode(buf: bytes, off: int) -> Tuple[str, int]:
    """Decode a NUL-terminated raw ASCII string."""
    end = buf.find(b"\x00", off)
    if end < 0:
        return buf[off:].decode("latin-1"), len(buf)
    return buf[off:end].decode("latin-1", errors="replace"), end + 1


def _looks_printable(s: str) -> bool:
    """True if a decoded string is mostly printable ASCII (a key heuristic)."""
    if not s:
        return False
    return all(0x20 <= ord(c) < 0x7F for c in s)


def smart_key_decode(buf: bytes, off: int) -> Tuple[str, str, int]:
    """Decode a struct/map key by trying cs0, x2, and cleartext and picking the
    most plausible printable result. Returns (encoding, text, new_off)."""
    # cleartext: no decoding
    cl_text, cl_end = cleartext_decode(buf, off)
    if _looks_printable(cl_text) and cl_end > off + 1:
        return "cleartext", cl_text, cl_end
    # cs0: high-density, every byte is a char
    cs_text, cs_end = cs0_decode(buf, off)
    if _looks_printable(cs_text) and cs_end > off + 1:
        return "cs0", cs_text, cs_end
    # x2: every byte should have low bit clear; bail early if not
    if all((b & 1) == 0 for b in buf[off:off + 32]) or buf[off] == 0:
        x2_text, x2_end = x2_decode(buf, off)
        if _looks_printable(x2_text) and x2_end > off + 1:
            return "x2", x2_text, x2_end
    # fallback: cleartext, possibly garbled
    return "cleartext", cl_text, cl_end


# ---------- AST ---------------------------------------------------------------

@dataclass
class Node:
    """One decoded element of the stream."""
    kind: str            # 'cs0', 'x2', 'cleartext', 'u32', 'u64', 'array',
                         # 'struct', 'map', 'opaque', 'unknown_tag'
    value: object = None
    off: int = 0
    end: int = 0
    extra: object = None  # tag byte / count / etc.

    def render(self, indent: int = 0) -> str:
        pad = "  " * indent
        if self.kind in ("cs0", "x2", "cleartext"):
            return f"{pad}{self.kind}={self.value!r}"
        if self.kind in ("u32", "u64"):
            return f"{pad}{self.kind}={self.value} (0x{self.value:x})"
        if self.kind == "array":
            head = f"{pad}array[{len(self.value)}]:"
            return "\n".join([head] + [n.render(indent + 1) for n in self.value])
        if self.kind == "struct":
            head = f"{pad}struct[{len(self.value)}]:"
            lines = [head]
            for k, v in self.value:
                lines.append(f"{pad}  {k!r}:")
                lines.append(v.render(indent + 2))
            return "\n".join(lines)
        if self.kind == "map":
            head = f"{pad}map[{len(self.value)}]:"
            lines = [head]
            for k, v in self.value:
                lines.append(f"{pad}  key=")
                lines.append(k.render(indent + 2))
                lines.append(f"{pad}  val=")
                lines.append(v.render(indent + 2))
            return "\n".join(lines)
        if self.kind == "opaque":
            hex_ = self.value.hex()
            if len(hex_) > 64:
                hex_ = hex_[:64] + "…"
            return f"{pad}opaque[{len(self.value)}B]={hex_}"
        if self.kind == "unknown_tag":
            return f"{pad}<unknown tag 0x{self.extra:02x}@{self.off:#x}>"
        return f"{pad}{self.kind}={self.value!r}"


# ---------- recursive walker --------------------------------------------------

class FedDesignTgpStream:
    """Opaque kaitai type. `_io` is a kaitai stream; we read everything
    eagerly into bytes and parse with our own walker."""

    def __init__(self, _io, _parent=None, _root=None):
        # kaitai gives us the stream positioned at the start of our blob;
        # consume the rest.
        self._raw = _io.read_bytes_full()
        self.nodes, self.tail_off = walk_top_level(self._raw)

    @classmethod
    def from_bytes(cls, blob: bytes) -> "FedDesignTgpStream":
        # convenience for ad-hoc testing without a kaitai stream
        from kaitaistruct import KaitaiStream
        import io
        return cls(KaitaiStream(io.BytesIO(blob)))

    def _fetch_instances(self):
        # Kaitai walks lazy `instances:` here; we have none.
        pass

    def __repr__(self) -> str:
        bytes_total = len(self._raw)
        consumed = self.tail_off
        head_lines = [
            f"FedDesignTgpStream({bytes_total}B, parsed={consumed}B"
            + (", complete" if consumed == bytes_total else f", trailing={bytes_total - consumed}B")
            + ")"
        ]
        for n in self.nodes:
            head_lines.append(n.render(indent=1))
        return "\n".join(head_lines)


def parse_value(buf: bytes, off: int) -> Tuple[Node, int]:
    """Parse a single typed value starting at `off`. Returns (node, new_off).
    On unrecognized tag we return an opaque single-byte node and let the
    caller decide how to continue."""
    if off >= len(buf):
        return Node(kind="opaque", value=b"", off=off, end=off), off
    tag = buf[off]
    start = off
    off += 1

    if tag in (0x02, 0x15, 0x82):
        s, off = cs0_decode(buf, off)
        return Node(kind="cs0", value=s, off=start, end=off, extra=tag), off

    if tag == 0x05:
        s, off = cleartext_decode(buf, off)
        return Node(kind="cleartext", value=s, off=start, end=off), off

    if tag == 0x0a:
        s, off = x2_decode(buf, off)
        return Node(kind="x2", value=s, off=start, end=off), off

    if tag == 0x18:
        if off + 4 > len(buf):
            return Node(kind="opaque", value=buf[start:], off=start, end=len(buf)), len(buf)
        v = int.from_bytes(buf[off:off + 4], "big")
        return Node(kind="u32", value=v, off=start, end=off + 4), off + 4

    if tag == 0x04:
        if off + 8 > len(buf):
            return Node(kind="opaque", value=buf[start:], off=start, end=len(buf)), len(buf)
        v = int.from_bytes(buf[off:off + 8], "big")
        return Node(kind="u64", value=v, off=start, end=off + 8), off + 8

    if tag == 0x06:
        if off + 4 > len(buf):
            return Node(kind="opaque", value=buf[start:], off=start, end=len(buf)), len(buf)
        count = int.from_bytes(buf[off:off + 4], "big")
        off += 4
        if count > 1024 * 1024:
            # almost certainly a misparse; bail
            return Node(kind="opaque", value=buf[start:start + 5], off=start, end=start + 5), start + 5
        items = []
        for _ in range(count):
            child, off = parse_value(buf, off)
            items.append(child)
        return Node(kind="array", value=items, off=start, end=off), off

    if tag == 0x0c:
        if off + 4 > len(buf):
            return Node(kind="opaque", value=buf[start:], off=start, end=len(buf)), len(buf)
        count = int.from_bytes(buf[off:off + 4], "big")
        off += 4
        if count > 1024 * 1024:
            return Node(kind="opaque", value=buf[start:start + 5], off=start, end=start + 5), start + 5
        entries = []
        for _ in range(count):
            enc, key, off = smart_key_decode(buf, off)
            child, off = parse_value(buf, off)
            entries.append((key, child))
        return Node(kind="struct", value=entries, off=start, end=off), off

    if tag == 0x03:
        if off + 4 > len(buf):
            return Node(kind="opaque", value=buf[start:], off=start, end=len(buf)), len(buf)
        count = int.from_bytes(buf[off:off + 4], "big")
        off += 4
        if count > 1024 * 1024:
            return Node(kind="opaque", value=buf[start:start + 5], off=start, end=start + 5), start + 5
        entries = []
        for _ in range(count):
            key, off = parse_value(buf, off)
            child, off = parse_value(buf, off)
            entries.append((key, child))
        return Node(kind="map", value=entries, off=start, end=off), off

    return Node(kind="unknown_tag", value=None, off=start, end=off, extra=tag), off


def walk_top_level(buf: bytes) -> Tuple[List[Node], int]:
    """Walk the stream from the start, collecting every value we can parse.

    The very first portion of an outer FedDesign stream is a binary header we
    don't yet model — we pass through it as an `opaque` node up to the first
    recognizable type tag.
    """
    nodes: List[Node] = []
    off = 0

    # find first plausible tag for an "outer header" opaque region
    KNOWN_TAGS = {0x02, 0x03, 0x04, 0x05, 0x06, 0x0a, 0x0c, 0x15, 0x18, 0x82}
    first_tag = None
    for i in range(len(buf)):
        if buf[i] not in KNOWN_TAGS:
            continue
        # heuristic: be confident only if the tag looks like it's followed by
        # a sensible length/value. Cheap probe: try to parse a value and see
        # whether it consumes a reasonable amount of data without overrunning.
        try:
            node, end = parse_value(buf, i)
            if end <= len(buf) and node.kind != "unknown_tag":
                first_tag = i
                break
        except Exception:
            continue
    if first_tag is None:
        nodes.append(Node(kind="opaque", value=buf, off=0, end=len(buf)))
        return nodes, len(buf)

    if first_tag > 0:
        nodes.append(Node(kind="opaque", value=buf[:first_tag], off=0, end=first_tag))
        off = first_tag

    # walk all remaining values, tolerating unknown bytes as opaque runs
    while off < len(buf):
        node, new_off = parse_value(buf, off)
        if node.kind == "unknown_tag" or new_off == off:
            # gather a hex run of unrecognized bytes until we can resync
            run_start = off
            off += 1
            while off < len(buf) and buf[off] not in KNOWN_TAGS:
                off += 1
            nodes.append(Node(kind="opaque", value=buf[run_start:off], off=run_start, end=off))
        else:
            nodes.append(node)
            off = new_off
    return nodes, off


# ---------- ad-hoc CLI for testing -------------------------------------------

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("usage: fed_design_tgp_stream.py <stream.bin>")
        sys.exit(1)
    blob = open(sys.argv[1], "rb").read()
    parsed = FedDesignTgpStream.from_bytes(blob)
    print(parsed)
