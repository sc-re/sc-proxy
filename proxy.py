#!/usr/bin/env python3
"""StarConflict load-balancer proxy.

Two operating modes (pick with the `--local-server` flag):

  * default              — proxy talks to the real upstream
                           (185.253.20.238:3801/3802/3815), listens on
                           the standard ports (3801/19803/3815),
                           captures into `captures/<session>/`.
  * `--local-server`     — proxy talks to the local dev server at
                           192.168.2.32 (same standard upstream ports),
                           listens on shifted ports (4801/4802/4815)
                           so a default-mode proxy can run alongside,
                           captures into `captures_debug/<session>/`.

Set `SC_REAL_HOST` / `SC_REAL_LB_PORT` env vars to override the
default-mode upstream (see proxy_util.DEFAULT_REAL_LB).

Usage:
    python3 proxy.py                  # default-mode console logger
    python3 proxy.py --local-server   # local-server console logger
    python3 proxy_gui.py              # default-mode + Qt inspector
    python3 proxy_gui.py --local-server
"""
import argparse
import logging
import threading
import time

import proxy_util
import proxy_lb
import proxy_shard
import proxy_chat


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-5s %(name)-12s | %(message)s",
)
log = logging.getLogger("main")


def main() -> None:
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


if __name__ == "__main__":
    main()
