# Star Conflict Shard and Chat Proxy

Disclaimer: The python code in this repo is heavily vibe coded

This git repo is to document the packet types used by the game Star Conflict.
Initial goal is to document the format of all packet types with id 0 to 252.

## Setup

Requires Python 3. From the repo root:

```sh
# 1. create an isolated environment
python -m venv .venv

# 2. activate it
#    Windows (PowerShell):  .venv\Scripts\Activate.ps1
#    Windows (Git Bash):    source .venv/Scripts/activate
#    Linux / macOS:         source .venv/bin/activate

# 3. install dependencies
python -m pip install -r requirements.txt
```

`requirements.txt` pulls in `kaitaistruct` (core packet parsers), `PySide6`
(the Qt inspector used by `proxy_gui.py`), and `ruamel.yaml` (used by
`verify_ksy.py`). The kaitai-generated parsers
(`star_conflict_package_client.py` / `_server.py`) are committed, so the
`kaitai-struct-compiler` is **only** needed if you edit a `.ksy` schema and
want to regenerate them (see [Dependencies](#dependencies)).

Verify the install:

```sh
python proxy.py --help     # core proxy (console)
python verify_ksy.py       # lints the .ksy schemas against captures/
```

> Note: the repo also ships a `Pipfile` / `.envrc` (`layout pipenv`) for
> users who prefer pipenv + direnv. `pipenv install` is equivalent to the
> venv steps above.

## How to

Activate the environment (see [Setup](#setup)), then launch the proxy
(`python proxy.py`, or `python proxy_gui.py` for the Qt inspector).

Append `-test` to the launch parameters of `game.exe`
(in Steam Right Click on game -> Properties -> Launch Options)
outside of Steam, just launch game.exe directly with the mentioned parameter.

Choose `localhost` in the Server dropdown to connect through the proxy.

After logging in, the proxy will dump the bodies of recieved packets in `./captures`
or whatever directory the environment variable `SC_CAPTURE_DIR` points to.

### Browsing older sessions

The Qt inspector (`python3 proxy_gui.py`) has a **Session** dropdown in the
filter bar. It defaults to `● Live` (freshly captured traffic); selecting one
of the listed sessions reloads that session's saved packet bodies from disk and
shows them in the table, decoded exactly as the live view would. Use `⟳` to
rescan the capture directories, and pick `● Live` again to resume the live feed.

Update the files `server.ksy` and `client.ksy` with definitions of packages you understand.
- `client.ksy` is for packages flowing from Client to Server
- `server.ksy` is for packages flowing from Server to Client

Not all package types do get sent in both directions


## Dependencies

Installed by `requirements.txt` (see [Setup](#setup)):
- python 3
- kaitaistruct (pip) — runtime for the generated packet parsers
- PySide6 (pip) — Qt inspector, `proxy_gui.py` only
- ruamel.yaml (pip) — `.ksy` linting, `verify_ksy.py` only

### Optional (only for regenerating parsers from `.ksy`)
- kaitai-struct-compiler (https://kaitai.io/#download) — run `make` (or the
  `kaitai-struct-compiler` commands in the `Makefile`) to rebuild
  `star_conflict_package_client.py` / `_server.py` after editing the schemas
- gnu-make — drives the above
