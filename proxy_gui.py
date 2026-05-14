#!/usr/bin/env python3
"""StarConflict proxy with the Qt packet inspector.

Same three sub-proxies as `proxy.py` (LB / shard / chat) running on
daemon threads, plus a PySide6 main window that subscribes to
packet_bus to render every captured packet in a Wireshark-style
table. The console logger keeps running unchanged.

Closing the window stops the process.

Usage:
    python3 proxy_gui.py
"""
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


if __name__ == "__main__":
    log.info(
        f"upstream LB: {proxy_util.DEFAULT_REAL_LB[0]}:"
        f"{proxy_util.DEFAULT_REAL_LB[1]}"
    )
    threading.Thread(target=proxy_lb.run,    daemon=True).start()
    threading.Thread(target=proxy_shard.run, daemon=True).start()
    threading.Thread(target=proxy_chat.run,  daemon=True).start()
    log.info("Proxy running. Close window to stop.")
    raise SystemExit(proxy_ui.run())
