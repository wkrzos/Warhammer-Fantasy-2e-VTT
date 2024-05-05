from enum import Enum

class Races(Enum):
    HUMAN = "r.1",
    ELF = "r.2",
    DWARF = "r.3",
    HALFLING = "r.4"

class MonsterCategory(Enum):
    UNDEAD = "mc.1"
    GREENSKIN = "mc.2"
    HUMAN = "mc3"
    BEAST = "mc4"
    ETHERNAL = "mc5"