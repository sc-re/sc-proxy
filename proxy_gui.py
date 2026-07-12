#!/usr/bin/env python3
"""StarConflict proxy with the Qt packet inspector.

Same three sub-proxies as `proxy.py` (LB / shard / chat) running on
daemon threads, plus a PySide6 main window that subscribes to
packet_bus to render every captured packet in a Wireshark-style
table. The console logger keeps running unchanged.

Closing the window stops the process. Pass `--local-server` to point
at the LAN dev server (192.168.2.32) on the shifted port set; see
`proxy.py` for the full description of both modes.

Usage:
    python3 proxy_gui.py
    python3 proxy_gui.py --local-server
"""
import argparse
import logging
import threading

import proxy_util
import proxy_lb
import proxy_shard
import proxy_chat
import proxy_ui


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-5s %(name)-12s | %(message)s",
)
log = logging.getLogger("main")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--local-server", action="store_true",
                    help="point the proxy at the LAN dev server "
                         "(192.168.2.32), listen on the shifted port set "
                         "(4801/4802/4815), and save captures into "
                         "captures_debug/.")
    args = ap.parse_args()

    if args.local_server:
        proxy_util.set_local_server_mode()

    log.info(f"upstream LB: {proxy_util.DEFAULT_REAL_LB[0]}:"
             f"{proxy_util.DEFAULT_REAL_LB[1]}")
    log.info(f"advertising shard/chat to game at {proxy_util.ADVERTISE_HOST} "
             f"(override with SC_PROXY_HOST)")
    threading.Thread(target=proxy_lb.run,    daemon=True).start()
    threading.Thread(target=proxy_shard.run, daemon=True).start()
    threading.Thread(target=proxy_chat.run,  daemon=True).start()
    log.info("Proxy running. Close window to stop.")
    return proxy_ui.run()


if __name__ == "__main__":
    raise SystemExit(main())
