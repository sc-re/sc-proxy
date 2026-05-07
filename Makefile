.PHONY: all
all: star_conflict_package_client.py star_conflict_package_server.py

# --opaque-types true so .ksy files can reference user-provided Python
# classes (currently bag_payload.BagPayload) for fields that aren't
# byte-aligned and can't be modelled in static kaitai.
KSC_FLAGS := -t python --opaque-types true

star_conflict_package_client.py: client.ksy
	kaitai-struct-compiler $(KSC_FLAGS) client.ksy

star_conflict_package_server.py: server.ksy
	kaitai-struct-compiler $(KSC_FLAGS) server.ksy
