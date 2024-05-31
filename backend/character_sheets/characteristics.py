from enum import Enum

class Stats(Enum):
    pass

class MainStats(Stats):
    WEAPON_SKILL = "ms.1"
    BALLISTIC_SKILL = "ms.2"
    STRENGTH = "ms.3"
    TOUGHNESS = "ms.4"
    AGILITY = "ms.5"
    INTELLIGENCE = "ms.6"
    WILL_POWER = "ms.7"
    FELLOWSHIP = "ms.8"

class SecondaryStats(Stats):
    ATTACKS = "ss.1"
    WOUNDS = "ss.2"
    STRENGTH_BONUS = "ss.3"
    TOUGHNESS_BONUS = "ss.4"
    MOVEMENT = "ss.5"
    MAGIC = "ss.6"
    INSANITY_POINTS = "ss.7"
    FATE_POINTS = "ss.8"

class AttributesType(Enum):
    ACTIONS_REMAIN = "at.1"
    IS_AIMING = "at.2"
    IS_PARING = "at.3"
    IS_IN_DEFENCE = "at.4"
    ALREADY_DODGED = "at.5"
    IS_LYING = "at.6"
    FURIOUS = "at.7"
    UNCONSCIOUS = "at.8"
    DEAD = "at.9"

class Attributes:
    def __init__(self, actionsRemain:int = 2, attributesActive:set = set()):
        self.actionsRemain = actionsRemain
        self.attributesActive = attributesActive

    def __contains__(self, attributes: AttributesType):
        return attributes in self.attributesActive

    def add(self, attributes: AttributesType) -> None:
        self.attributesActive.add(attributes)

    def remove(self, attributes: AttributesType) -> None:
        if attributes in self.attributesActive:
            self.attributesActive.remove(attributes)
    def restartAttributes(self) -> None:
        if AttributesType.DEAD not in self.attributesActive or AttributesType.UNCONSCIOUS not in self.attributesActive:
            self.actionsRemain = 2
            if AttributesType.IS_LYING in self.attributesActive:
                self.attributesActive.clear()
                self.attributesActive.add(AttributesType.IS_LYING)
            else:
                self.attributesActive.clear()


    def __dict__(self):
        return {
            "actionsRemain": self.actionsRemain,
            "attributesActive": list(self.attributesActive)
        }
