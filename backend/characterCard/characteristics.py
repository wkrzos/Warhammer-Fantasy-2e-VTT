from enum import Enum

class Stats(Enum):
    pass

class MainStats(Stats):
    WEAPON_SKILL = "ms.1",
    BALISSTIC_SKILL = "ms.2",
    STRENGTH = "ms.3",
    TOUGHNESS = "ms.4",
    AGILITY = "ms.5",
    INTELIGENCE = "ms.6",
    WILL_POWER = "ms.7",
    FELLOWSHIP = "ms.8"
class SecondaryStats(Stats):
    ATTACKS = "ss.1"
    WOUNDS = "ss.2"
    STRENGTH_BONNUS = "ss.3"
    TOUGHNESS_BONUS = "ss.4"
    MOVEMENT = "ss.5"
    MAGIC = "ss.6"
    INSANITY_POINTS = "ss.7"
    FATE_POINTS = "ss.8"

