"""Parse AC_ptrs (Ghidra listing) and expose packet-type lookups.

The file contains 252 entries in a pointer array starting at base 0x08fe75e0.
Each 4-byte slot holds a pointer to an "AC_*" string.  The slot offset / 4
gives the AC index, which we assume equals the packet type_id used on the wire.

This assumption will be confirmed once we capture post-login packet type IDs.
"""
import os
import re

_AC_PTRS_PATH = os.path.join(os.path.dirname(__file__), "AC_ptrs")
_BASE_ADDR = 0x08FE75E0

# {index: name}
AC_NAMES: dict[int, str] = {}
# {name: index}
AC_INDEX: dict[str, int] = {}


def _load():
    pattern = re.compile(r'^\s+([\da-f]{8})\s+(?:[\da-f]{2}\s+){4}addr\s+\S+\s*=\s*"(AC_[^"\n]+)', re.IGNORECASE)
    with open(_AC_PTRS_PATH) as f:
        for line in f:
            m = pattern.match(line)
            if m:
                addr = int(m.group(1), 16)
                name = m.group(2)
                index = (addr - _BASE_ADDR) // 4
                AC_NAMES[index] = name
                AC_INDEX[name] = index


_load()


def pkt_type_name(type_id: int) -> str:
    """Return AC_ name for a type_id, or a hex string if unknown."""
    return AC_NAMES.get(type_id, f"0x{type_id:04x}")
