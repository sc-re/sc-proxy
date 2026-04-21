#!/usr/bin/env python3
"""StarConflict load-balancer proxy.

Proxies the real upstream LB on port 3801, intercepts the shard-address
packet (0x8109), and rewrites shard/chat IPs to 127.0.0.1 so the game
connects to local servers.  No iptables needed — after the rewrite the
game dials localhost:19803 (shard) and localhost:3815 (chat) directly,
which masterserver.py serves.

Set SC_REAL_HOST / SC_REAL_LB_PORT env vars to override the upstream
(defaults in proxy_util.DEFAULT_REAL_LB).

Usage:
    python3 proxy_main.py
"""
import threading
import time
import logging

import proxy_util
import proxy_lb
import proxy_shard
import proxy_chat


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-5s %(name)-12s | %(message)s",
)
log = logging.getLogger("main")

if __name__ == "__main__":
    log.info(f"upstream LB: {proxy_util.DEFAULT_REAL_LB[0]}:{proxy_util.DEFAULT_REAL_LB[1]}")
    try:
        threading.Thread(target=proxy_lb.run, daemon=True).start()
        threading.Thread(target=proxy_shard.run, daemon=True).start()
        threading.Thread(target=proxy_chat.run,  daemon=True).start()

        log.info("Proxy running. Press Ctrl-C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        log.info("Stopped.")
