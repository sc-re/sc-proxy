"""Bit-stream parser for ac_quests server-to-client response.

Handler 0x0822d960 reads, in order:

  u4 a, u4 b, u4 c
  u1 d, u1 e, u1 f, u1 g                  (four flag bits)

  u1 num_dailies
  num_dailies × { u4 daily_id, u1 daily_state_bit }

  u1 num_quests
  num_quests × {
    u2  quest_id
    u1  status
    u4  progress
    u1  has_field4   if 1: u8 field4
    u1  has_field5   if 1: u8 field5
  }

  u1 num_quest_descs
  num_quest_descs × { u2 desc_a, u1 desc_b }

  u2 num_quest_ids_a, num_quest_ids_a × u2  (e.g. accepted-quest IDs)
  u4 misc
  u2 num_quest_ids_b, num_quest_ids_b × u2

  (u8 idx, i4 value)*   terminated by idx=0xff
                        — sparse 0x200-entry table at game-state offset 0xb4860

The 4 flag bits drive UI but aren't grouped under a single semantic; we
keep them as bool d..g for now. The terminator-stream at the end stores
quest counter/progress entries indexed by a small u8.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Optional

from notification import BitReader


@dataclass
class DailyQuest:
    daily_id: int
    state: int


@dataclass
class Quest:
    quest_id: int
    status: int
    progress: int
    field4: Optional[int]
    field5: Optional[int]


@dataclass
class QuestDesc:
    a: int
    b: int


class AcQuestsBody:
    def __init__(self, _io, _parent=None, _root=None):
        self._raw: bytes = _io.read_bytes_full()
        self.error: Optional[str] = None
        self.a: int = 0
        self.b: int = 0
        self.c: int = 0
        self.flags = (False, False, False, False)
        self.dailies: List[DailyQuest] = []
        self.quests: List[Quest] = []
        self.descs: List[QuestDesc] = []
        self.quest_ids_a: List[int] = []
        self.misc: int = 0
        self.quest_ids_b: List[int] = []
        self.counters: Dict[int, int] = {}
        self.bits_consumed: int = 0
        try:
            br = BitReader(self._raw)
            self.a = br.read_u32()
            self.b = br.read_u32()
            self.c = br.read_u32()
            d = br.read_bool(); e = br.read_bool()
            f = br.read_bool(); g = br.read_bool()
            self.flags = (d, e, f, g)
            for _ in range(br.read_u8()):
                self.dailies.append(DailyQuest(br.read_u32(), int(br.read_bool())))
            for _ in range(br.read_u8()):
                qid = br.read_u16()
                status = br.read_u8()
                progress = br.read_u32()
                f4 = br.read_u64() if br.read_bool() else None
                f5 = br.read_u64() if br.read_bool() else None
                self.quests.append(Quest(qid, status, progress, f4, f5))
            for _ in range(br.read_u8()):
                self.descs.append(QuestDesc(br.read_u16(), br.read_u8()))
            n = br.read_u16()
            self.quest_ids_a = [br.read_u16() for _ in range(n)]
            self.misc = br.read_u32()
            n = br.read_u16()
            self.quest_ids_b = [br.read_u16() for _ in range(n)]
            # terminator-driven counter table
            while br.remaining() >= 8:
                idx = br.read_u8()
                if idx == 0xff:
                    break
                value = br.read_i32()
                self.counters[idx] = value
            self.bits_consumed = br.pos
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"

    def _fetch_instances(self):
        pass

    def __repr__(self) -> str:
        if self.error:
            return f"AcQuestsBody(<error: {self.error}>)"
        slack = len(self._raw) * 8 - self.bits_consumed
        return (f"AcQuestsBody({len(self._raw)}B, a={self.a}, b={self.b}, "
                f"c={self.c}, flags={self.flags}, dailies={len(self.dailies)}, "
                f"quests={len(self.quests)}, descs={len(self.descs)}, "
                f"ids_a={len(self.quest_ids_a)}, misc={self.misc}, "
                f"ids_b={len(self.quest_ids_b)}, counters={len(self.counters)}, "
                f"slack={slack}b)")
