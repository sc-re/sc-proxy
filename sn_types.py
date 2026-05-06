"""ServerNotification (SN_*) id → name lookup.

Source: `proxy/ServerNotifications.by_id`, generated from the enum dump
`proxy/ServerNotifications` sorted by numeric id. Used to decode the first
byte of an SCMD_NOTIFICATION body, which is the SN_ type.
"""
import os
import re

_SN_PATH = os.path.join(os.path.dirname(__file__), "ServerNotifications.by_id")

SN_NAMES: dict[int, str] = {}
SN_INDEX: dict[str, int] = {}


def _load():
    pattern = re.compile(r'^\s*(\d+)\s*=\s*(SN_[A-Z0-9_]+)\s*$')
    with open(_SN_PATH) as f:
        for line in f:
            m = pattern.match(line)
            if m:
                idx = int(m.group(1))
                name = m.group(2)
                SN_NAMES[idx] = name
                SN_INDEX[name] = idx


_load()


def sn_name(type_id: int) -> str:
    """Return SN_ name for a type_id, or a hex string if unknown."""
    return SN_NAMES.get(type_id, f"0x{type_id:02x}")
