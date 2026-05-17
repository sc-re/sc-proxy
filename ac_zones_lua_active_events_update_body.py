"""Bit-stream parser for `ac_zones_lua_active_events_update` (AC 0xfa).

S→C push carrying the current scripted-event state for every zone.
The lua side reads it via `MasterServer_ZonesLuaActiveEventsGet()`
and stores it as `UI.serverData.zoneEvents = {[zone_id] = {[event_id]
= seconds_or_sentinel}}` — see `UI.UpdateZoneEvents` in
`ui/scripts/work/uigamefuncs.lua` and the callback chain
`MasterServer_OnZonesLuaActiveEventsUpdate` → `UpdateZoneEvents`.

Wire format:

    u1   has_data
    if has_data:
        bag    zone_events       (outer key: zone_id, value: bag
                                   { inner key: event_id,
                                     value: f32 seconds-remaining
                                     OR an ai.ScriptsServer sentinel })

ai.ScriptsServer sentinels (from `scripts/general/constants.lua`):

    DISABLE_EVENT   = -100500
    TIMEOUT_EVENT   = -100501
    COMPLETED_EVENT = -100502
    FAILED_EVENT    = -100503
    REMOVED_EVENT   = -100504

Positive values are "seconds remaining" — the lua handler converts
them to absolute server-time deadlines (`currentTime + secs*1000`)
for any event whose visual map declares `showTimer = true`.

This is the same nested-bag shape as `bag_27` in
`ac_load_initial_player_data` (which initial-load embeds for the same
purpose — both write to the same master-server cache member).

Tested against all observed captures (3 B "no data" and 3017 B "79
zones" — both decode with 7-bit sub-byte slack).
"""
from __future__ import annotations
from typing import Optional

from notification import BitReader, _read_bag, format_bag, read_field


# ai.ScriptsServer sentinels — used to label values in the repr.
_SENTINELS = {
    -100500.0: "DISABLE_EVENT",
    -100501.0: "TIMEOUT_EVENT",
    -100502.0: "COMPLETED_EVENT",
    -100503.0: "FAILED_EVENT",
    -100504.0: "REMOVED_EVENT",
}


def decode_event_state(value: float) -> str:
    """Render a leaf event-state value with its sentinel name when known."""
    name = _SENTINELS.get(value)
    if name is not None:
        return f"{value:g} ({name})"
    if value > 0:
        return f"{value:g}s remaining"
    return f"{value:g}"


class AcZonesLuaActiveEventsUpdateBody:
    """Decoded body of an `ac_zones_lua_active_events_update` push.

    Public attributes:
        has_data: Variant[u1] — set when a payload follows.
        zone_events: Variant[bag] — outer key is the zone_id, the value
            is a nested bag keyed by event_id with f32 leaves (seconds
            remaining, or one of the ai.ScriptsServer sentinels).
        ok / error / bits_consumed — standard tolerance fields.
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.ok: bool = True
        self.error: Optional[str] = None
        self.bits_consumed: int = 0
        if not self._raw:
            return

        br = BitReader(self._raw)
        try:
            self.has_data = read_field(br, "bool", br.read_bool())
            if self.has_data.value:
                # _read_bag restores last_read_start to bag start so the
                # outer Variant's range covers the u32 num_entries and
                # the u1 indexed-keys flag too.
                self.zone_events = read_field(
                    br, "bag", _read_bag(br))
            self.bits_consumed = br.pos
        except EOFError:
            self.ok = False
            self.bits_consumed = br.pos
        except Exception as e:
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"
            self.bits_consumed = br.pos

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcZonesLuaActiveEventsUpdateBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        suffix = " TRUNCATED" if not self.ok else ""
        if not hasattr(self, "has_data"):
            return (f"AcZonesLuaActiveEventsUpdateBody("
                    f"{len(self._raw)}B{suffix} slack={slack}b)")
        if not self.has_data.value or not hasattr(self, "zone_events"):
            return (f"AcZonesLuaActiveEventsUpdateBody({len(self._raw)}B"
                    f"{suffix}, has_data=False, slack={slack}b)")
        bag = self.zone_events.value
        # Count event leaves for the summary line.
        leaves = sum(
            len(v.value) if hasattr(v, "value") and isinstance(v.value, dict)
            else 0 for v in bag.values())
        return (f"AcZonesLuaActiveEventsUpdateBody({len(self._raw)}B{suffix}, "
                f"zones={len(bag)}, events={leaves}, "
                f"slack={slack}b)\n  zone_events={format_bag(bag)}")
