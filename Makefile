.PHONY: all
all: star_conflict_package_client.py star_conflict_package_server.py

star_conflict_package_client.py: client.ksy
	kaitai-struct-compiler -t python client.ksy

star_conflict_package_server.py: server.ksy
	kaitai-struct-compiler -t python server.ksy
