"""Opaque kaitai type — body of `ac_load_initial_player_data` (AC 0).

Implements the bit-stream reader at handler 0x0823103b and every
sub-handler it dispatches into. The visible CALLs in the outer handler
are only a fraction of what reads from the stream; each "u32 count"
gates a loop whose body invokes a deep sub-reader (FUN_088fc1e0, etc.).
This file mirrors all of them.

Outer field order:

   0  u64                     0x08231044
   1  u32                     0x08231050
   2  u1                      0x08231064  early-error gate
   3  u32                     0x0823108e
   4  u1                      0x082310a8
   5  u64                     0x082310bc
   6  cstr60                  0x082310ee  ← end of "head" section

   section A: u32 + count×StructA  (StructA = FUN_088fc1e0)
   section B: u32 + count×StructA
   section C: u32 + count×StructA
              + FUN_088fcea0 (count + N×{u32+u32+cstr256})
              + FUN_088fe1c0 (count + N×{u32+u32} + cstr59)
              + FUN_088fe450 (28× FUN_088fe1c0)

   …then bag_11, u32, u1, u8×2, i32, u1, bag×2, i32×2, u1, i32, u64,
   i32, u1, bag, u8 — up through field_28 (29 outer reads total).

Each sub-reader is implemented as a Python function that returns the
parsed dict. Counts can be huge (some entries are hundreds of items),
so for the public repr we just summarise list lengths and string
fields rather than dumping every record.
"""
from __future__ import annotations
from typing import Any

from notification import BitReader, _read_bag


# ── Sub-readers (drop-in replacements for the binary's helpers) ───────────────

def _read_struct_088fc1e0(br: BitReader) -> dict:
    """FUN_088fc1e0 — reads one record. Used by sections A/B/C in a loop."""
    out: dict[str, Any] = {}
    out["s1"] = br.read_cstring(max_len=256)
    out["u_a"] = br.read_u32()
    out["s2"] = br.read_cstring(max_len=256)
    out["f0"] = br.read_f32()
    out["f1"] = br.read_f32()
    out["f2"] = br.read_f32()
    out["u_b"] = br.read_u32()
    out["u_c"] = br.read_u32()
    out["u_d"] = br.read_u32()
    out["u_e"] = br.read_u32()
    out["u_f"] = br.read_u32()
    out["u_g"] = br.read_u32()
    out["flag1"] = br.read_bool()
    out["flag2"] = br.read_bool()
    out["s3"] = br.read_cstring(max_len=256)

    n = br.read_u32()
    out["list1"] = [
        {"name": br.read_cstring(max_len=256),
         "f1": br.read_bool(),
         "f2": br.read_bool()} for _ in range(n)
    ]
    n = br.read_u32()
    out["list2"] = [br.read_cstring(max_len=256) for _ in range(n)]
    n = br.read_u32()
    out["list3"] = [br.read_cstring(max_len=256) for _ in range(n)]
    n = br.read_u32()
    out["list4"] = [
        {"name": br.read_cstring(max_len=256),
         "a": br.read_u32(),
         "b": br.read_u32()} for _ in range(n)
    ]
    n = br.read_u32()
    out["list5"] = [(br.read_i32(), br.read_i32()) for _ in range(n)]
    out["u64_end"] = br.read_u64()
    return out


def _read_struct_088fcea0(br: BitReader) -> list[dict]:
    """FUN_088fcea0 — u32 count + count×{u32 + u32 + cstr256}."""
    n = br.read_u32()
    return [{"a": br.read_u32(),
             "b": br.read_u32(),
             "name": br.read_cstring(max_len=256)} for _ in range(n)]


def _read_struct_088fe1c0(br: BitReader) -> dict:
    """FUN_088fe1c0 — u32 count + count×{u32 + u32} + cstr59."""
    n = br.read_u32()
    pairs = [(br.read_u32(), br.read_u32()) for _ in range(n)]
    name = br.read_cstring(max_len=59)
    return {"pairs": pairs, "name": name}


def _read_struct_088fe450(br: BitReader) -> list[dict]:
    """FUN_088fe450 — 28× FUN_088fe1c0."""
    return [_read_struct_088fe1c0(br) for _ in range(28)]


def _read_struct_082590e0(br: BitReader) -> dict:
    """FUN_082590e0 — wraps Bag_Deserialize (writes into a bag at
    endpoint+0x193878). Consumes one full property bag from the stream."""
    return _read_bag(br)


def _read_struct_088d9700(br: BitReader) -> dict:
    """FUN_088d9700 — BattlePass::ReadActivationFromBitStream.
    u64 token + u16 count + count×{u16 stage + u64 ts}.
    """
    token = br.read_u64()
    n = br.read_u16()
    stages = [(br.read_u16(), br.read_u64()) for _ in range(n)]
    return {"token": token, "stages": stages}


def _read_struct_088dd630(br: BitReader) -> dict:
    """FUN_088dd630 — BattlePass::PlayerData::ReadFromBitStream.
        u64 token
        u16 stage_count + count×{u16 + u16}
        u32 string_list_count + count×cstr59
        u32 timed_count + count×{u64 ts + u32 sub_count + sub_count×u16}
    """
    token = br.read_u64()
    n_stages = br.read_u16()
    stages = [(br.read_u16(), br.read_u16()) for _ in range(n_stages)]
    n_strings = br.read_u32()
    strings = [br.read_cstring(max_len=59) for _ in range(n_strings)]
    n_timed = br.read_u32()
    timed = []
    for _ in range(n_timed):
        ts = br.read_u64()
        n_inner = br.read_u32()
        inner = [br.read_u16() for _ in range(n_inner)]
        timed.append({"ts": ts, "items": inner})
    return {"token": token, "stages": stages, "strings": strings, "timed": timed}


# ── Outer body parser ────────────────────────────────────────────────────────

class AcLoadInitialPlayerDataBody:
    """Bit-stream parse of AC_LOAD_INITIAL_PLAYER_DATA's body.

    Public attributes (set only when successfully parsed):
        head_*       : 7 prefix scalars
        section_a    : list of records (sec A — count + count×StructA)
        section_b    : list of records (sec B)
        section_c    : list of records (sec C)
        sec_c_x      : FUN_088fcea0 result attached to sec C
        sec_c_y      : FUN_088fe1c0 result attached to sec C
        sec_c_z      : FUN_088fe450 result attached to sec C
        bag_11       : property bag
        … more fields after bag_11 modelled incrementally.
        ok           : True if every modelled field decoded
        error        : exception text on the first failure
        bits_read    : how far the cursor advanced
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self.raw: bytes = _io.read_bytes_full()
        self.ok = True
        self.error: str | None = None
        self.bits_read = 0

        if not self.raw:
            return

        br = BitReader(self.raw)
        try:
            # ── head ──────────────────────────────────────────────
            self.head_field_0 = br.read_u64()
            self.head_field_1 = br.read_u32()
            self.head_flag_2  = br.read_bool()
            self.head_field_3 = br.read_u32()
            self.head_flag_4  = br.read_bool()
            self.head_field_5 = br.read_u64()
            self.head_text_6  = br.read_cstring(max_len=60)

            # ── section A ─────────────────────────────────────────
            n = br.read_u32()
            self.section_a_count = n
            self.section_a = [_read_struct_088fc1e0(br) for _ in range(n)]

            # ── section B ─────────────────────────────────────────
            n = br.read_u32()
            self.section_b_count = n
            self.section_b = [_read_struct_088fc1e0(br) for _ in range(n)]

            # ── section C ─────────────────────────────────────────
            n = br.read_u32()
            self.section_c_count = n
            self.section_c = [_read_struct_088fc1e0(br) for _ in range(n)]
            self.sec_c_x = _read_struct_088fcea0(br)
            self.sec_c_y = _read_struct_088fe1c0(br)
            self.sec_c_z = _read_struct_088fe450(br)

            # ── bag_10, bag_11, … (outer handler positions 10..28) ─
            self.bag_10 = _read_bag(br)
            self.bag_11 = _read_bag(br)
            self.field_12 = br.read_u32()
            self.flag_13  = br.read_bool()
            self.field_14 = br.read_u8()
            self.field_15 = br.read_u8()
            self.field_16 = br.read_i32()
            self.flag_17  = br.read_bool()
            self.bag_18   = _read_bag(br)
            self.bag_19   = _read_bag(br)
            self.field_20 = br.read_i32()
            self.field_21 = br.read_i32()
            self.flag_22  = br.read_bool()
            self.field_23 = br.read_i32()
            self.field_24 = br.read_u64()
            # Hidden sub-handlers in the outer code path between
            # field_24 and field_25 — not visible from outer-handler
            # CALL grep alone:
            #   FUN_082590e0 → bag        (player_aux bag)
            #   FUN_088d9700 → battle pass activation (u64 + u16 + …)
            #   FUN_088dd630 → battle pass player data
            self.aux_bag      = _read_struct_082590e0(br)
            self.battle_pass_activation = _read_struct_088d9700(br)
            self.battle_pass_player     = _read_struct_088dd630(br)
            self.field_25 = br.read_i32()
            self.flag_26  = br.read_bool()
            self.bag_27   = _read_bag(br)
            self.field_28 = br.read_u8()
        except EOFError:
            # The handler tolerates short bodies via its lastReadOK
            # flag — every reader returns 0 instead of throwing. We
            # mirror that: stop cleanly, leave the rest unset.
            self.ok = False
        except Exception as e:
            self.ok = False
            self.error = f"{type(e).__name__}: {e}"
        self.bits_read = br.pos

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if not self.raw:
            return "AcLoadInitialPlayerDataBody(empty body)"

        parts = [f"{len(self.raw)}B"]
        if self.error:
            parts.append(f"err={self.error}")
        if not self.ok and not self.error:
            parts.append("truncated")

        # Head — print every parsed scalar.
        for name in ("head_field_0", "head_field_1", "head_flag_2",
                     "head_field_3", "head_flag_4", "head_field_5",
                     "head_text_6"):
            if name in self.__dict__:
                parts.append(f"{name[5:]}={getattr(self, name)!r}")

        # Sections — print sizes only, not the records (huge dumps otherwise).
        for sec in ("a", "b", "c"):
            cnt = getattr(self, f"section_{sec}_count", None)
            if cnt is not None:
                parts.append(f"sec_{sec}={cnt}")
        if hasattr(self, "sec_c_x"): parts.append(f"sec_c_x={len(self.sec_c_x)}")
        if hasattr(self, "sec_c_y"): parts.append(
            f"sec_c_y[{len(self.sec_c_y['pairs'])} pairs, {self.sec_c_y['name']!r}]")
        if hasattr(self, "sec_c_z"): parts.append(f"sec_c_z={len(self.sec_c_z)}")

        # Tail — bag sizes + scalars.
        for name in ("bag_10", "bag_11"):
            if name in self.__dict__:
                v = getattr(self, name)
                parts.append(f"{name}=bag({len(v)})")
        for name in ("field_12", "flag_13", "field_14", "field_15",
                     "field_16", "flag_17"):
            if name in self.__dict__:
                parts.append(f"{name}={getattr(self, name)!r}")
        for name in ("bag_18", "bag_19"):
            if name in self.__dict__:
                parts.append(f"{name}=bag({len(getattr(self, name))})")
        for name in ("field_20", "field_21", "flag_22", "field_23",
                     "field_24", "field_25", "flag_26"):
            if name in self.__dict__:
                parts.append(f"{name}={getattr(self, name)!r}")
        if "bag_27" in self.__dict__:
            parts.append(f"bag_27=bag({len(self.bag_27)})")
        if "field_28" in self.__dict__:
            parts.append(f"field_28={self.field_28!r}")

        return "AcLoadInitialPlayerDataBody(" + " ".join(parts) + ")"
