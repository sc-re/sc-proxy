#!/usr/bin/env python3
"""Verify ksy definitions against all captured packets.

Reports:
  - Types never seen in any capture (per direction)
  - Non-dummy types where some captures have unconsumed bytes
  - Non-dummy types where some captures failed to parse
"""

import glob
import os
import sys
from collections import defaultdict

from ruamel.yaml import YAML as _YAML
yaml = _YAML()
yaml.preserve_quotes = True
from kaitaistruct import KaitaiStream, BytesIO

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from star_conflict_package_client import StarConflictPackageClient
from star_conflict_package_server import StarConflictPackageServer

CAPTURES_BASE = os.environ.get("SC_CAPTURE_DIR", "captures/")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_ksy(path):
    """Return (id_to_name, name_to_kind) where kind is 'empty'|'dummy'|'real'."""
    with open(path) as f:
        ksy = yaml.load(f)

    # id → name from the switch-on cases
    id_to_name = {}
    for field in ksy.get("seq", []):
        t = field.get("type", {})
        if isinstance(t, dict) and "cases" in t:
            id_to_name = {int(k): v for k, v in t["cases"].items()}
            break

    # name → kind
    name_to_kind = {}
    for name, defn in ksy.get("types", {}).items():
        if not defn or "seq" not in defn:
            name_to_kind[name] = "empty"
        else:
            seq = defn["seq"]
            if len(seq) == 1 and seq[0].get("id") == "dummy":
                name_to_kind[name] = "dummy"
            else:
                name_to_kind[name] = "real"

    return id_to_name, name_to_kind


def scan_captures():
    """Yield (path, direction, type_id) for every .bin file under CAPTURES_BASE."""
    base = os.path.join(SCRIPT_DIR, CAPTURES_BASE)
    for path in sorted(glob.glob(os.path.join(base, "**", "*.bin"), recursive=True)):
        fname = os.path.basename(path)
        if "S_to_C" in fname:
            direction = "S_to_C"
        elif "C_to_S" in fname:
            direction = "C_to_S"
        else:
            continue
        for part in fname.split("_"):
            if part.startswith("ac") and len(part) == 6:
                try:
                    yield path, direction, int(part[2:], 16)
                except ValueError:
                    pass
                break


def parse_file(path, direction):
    """Return (leftover_bytes, error_str).  One of them will be None."""
    with open(path, "rb") as f:
        data = f.read()
    stream = KaitaiStream(BytesIO(data))
    try:
        cls = StarConflictPackageClient if direction == "C_to_S" else StarConflictPackageServer
        cls(stream)
        return stream.size() - stream.pos(), None
    except Exception as e:
        return None, str(e)


def main():
    client_ids, client_kinds = load_ksy(os.path.join(SCRIPT_DIR, "client.ksy"))
    server_ids, server_kinds = load_ksy(os.path.join(SCRIPT_DIR, "server.ksy"))

    id_map   = {"C_to_S": client_ids,   "S_to_C": server_ids}
    kind_map = {"C_to_S": client_kinds, "S_to_C": server_kinds}

    # (direction, type_id) → list of (leftover|None, error|None, file_bytes)
    results  = defaultdict(list)
    seen     = defaultdict(set)   # direction → {type_id}

    for path, direction, type_id in scan_captures():
        seen[direction].add(type_id)
        lo, err = parse_file(path, direction)
        results[(direction, type_id)].append((lo, err, os.path.getsize(path)))

    total_files = sum(len(v) for v in results.values())

    # ── Never seen ───────────────────────────────────────────────────────────
    print("=" * 72)
    print("TYPES NEVER SEEN IN CAPTURES")
    print("=" * 72)
    for direction in ("C_to_S", "S_to_C"):
        ids = id_map[direction]
        kinds = kind_map[direction]
        missing = sorted(
            [(tid, ids[tid]) for tid in ids if tid not in seen[direction]],
            key=lambda x: x[0],
        )
        print(f"\n  {direction}: {len(missing)} / {len(ids)} types not seen")
        for tid, name in missing:
            print(f"    [{tid:3d}] {name}  ({kinds.get(name, '?')})")

    # ── Incomplete definitions ────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("INCOMPLETE DEFINITIONS  (non-dummy; has leftover bytes)")
    print("=" * 72)
    for direction in ("C_to_S", "S_to_C"):
        ids   = id_map[direction]
        kinds = kind_map[direction]
        issues = []
        for tid, name in sorted(ids.items()):
            if kinds.get(name, "?") in ("dummy", "empty"):
                continue
            entries = results.get((direction, tid), [])
            bad = [(lo, fs) for lo, err, fs in entries if lo is not None and lo > 0]
            if bad:
                unique_lo = sorted({lo for lo, _ in bad})
                issues.append((tid, name, len(entries), len(bad), unique_lo))
        print(f"\n  {direction}:")
        if issues:
            for tid, name, total, n_bad, lo_vals in issues:
                print(f"    [{tid:3d}] {name}  —  {n_bad}/{total} captures, leftover bytes: {lo_vals}")
        else:
            print("    (none)")

    # ── Parse errors ─────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("PARSE ERRORS  (non-dummy; failed to parse)")
    print("=" * 72)
    for direction in ("C_to_S", "S_to_C"):
        ids   = id_map[direction]
        kinds = kind_map[direction]
        errors = []
        for tid, name in sorted(ids.items()):
            if kinds.get(name, "?") in ("dummy", "empty"):
                continue
            entries = results.get((direction, tid), [])
            bad = [(err, fs) for lo, err, fs in entries if err is not None]
            if bad:
                unique_errs = list(dict.fromkeys(e for e, _ in bad))[:2]
                errors.append((tid, name, len(entries), len(bad), unique_errs))
        print(f"\n  {direction}:")
        if errors:
            for tid, name, total, n_bad, errs in errors:
                print(f"    [{tid:3d}] {name}  —  {n_bad}/{total} captures failed")
                for e in errs:
                    print(f"         {e}")
        else:
            print("    (none)")

    print()
    print(f"Scanned {total_files} capture files across {len(seen['C_to_S']) + len(seen['S_to_C'])} unique type IDs.")


if __name__ == "__main__":
    main()
