#!/usr/bin/env python3
"""Decode a standalone property-bag .bin file.

For files that are *just* a bit-packed property bag — no TGP frame, no
SCMD/SN prefix. The wire format is the one notification._read_bag reads:

    u32 num_entries
    if num_entries > 0:
        u1  use_indexed_keys
        repeat num_entries:
            if !use_indexed_keys: cstring key
            variant value                  ; tag(8) + per-tag payload

`--prefixed` handles the PrefixedBagPayload variant: a leading u1 that,
when 0, means "no bag present" (the rest of the body is empty).

Examples:
    read_bag.py bag.bin
    read_bag.py --prefixed some_prefixed_bag.bin
    read_bag.py *.bin
"""
from __future__ import annotations
import argparse
import sys

from notification import BitReader, _read_bag, format_bag


def decode_bag_file(path: str, prefixed: bool) -> str:
    with open(path, "rb") as f:
        raw = f.read()
    br = BitReader(raw)
    if prefixed:
        present = br.read_bool()
        if not present:
            return "<no bag> (prefix bit 0)"
        bag = _read_bag(br)
    else:
        bag = _read_bag(br)
    slack = len(raw) * 8 - br.pos
    return f"{format_bag(bag)}  ({len(bag)} entries, slack={slack}b)"


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Decode a standalone property-bag .bin file.",
        epilog="Use --prefixed for bodies with a leading u1 'bag present' bit "
               "(the PrefixedBagPayload variant).",
    )
    ap.add_argument("paths", nargs="+", metavar="FILE",
                    help="raw property-bag .bin file(s)")
    ap.add_argument("--prefixed", action="store_true",
                    help="body starts with a u1 'bag present' bit")
    args = ap.parse_args()

    rc = 0
    multi = len(args.paths) > 1
    for path in args.paths:
        try:
            out = decode_bag_file(path, args.prefixed)
        except Exception as e:
            out = f"DECODE FAILED — {type(e).__name__}: {e}"
            rc = 1
        print(f"{path}: {out}" if multi else out)
    return rc


if __name__ == "__main__":
    sys.exit(main())
