# Star Conflict Shard and Chat Proxy

Disclaimer: The python code in this repo is heavily vibe coded

This git repo is to document the packet types used by the game Star Conflict.
Initial goal is to document the format of all packet types with id 0 to 252.

## How to

Launch the proxy (`python3 proxy.py`) after installing needed dependencies.

Append `-test` to the launch parameters of `game.exe`
(in Steam Right Click on game -> Properties -> Launch Options)
outside of Steam, just launch game.exe directly with the mentioned parameter.

Choose `localhost` in the Server dropdown to connect through the proxy.

After logging in, the proxy will dump the bodies of recieved packets in `./captures`
or whatever directory the environment variable `SC_CAPTURE_DIR` points to.

Update the file `packet.ksy` with definitions of pacakges you understand.

## Dependencies
- python
- kaitaistruct (pip)
- kaitai-struct-compiler (https://kaitai.io/#download)

### Optional
- gnu-make
