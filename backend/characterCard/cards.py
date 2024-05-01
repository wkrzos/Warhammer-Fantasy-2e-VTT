import random

from characteristics import *
from races import *
from skillsAndTalents import *
from statistics import *

class Creature:
    def __init__(self, name:str, statistics:Statistics):
        self.name = name
        self.statistics = statistics
        self.skills = []
        self.talents = []

    def skillTest(self,skill:Skills, modificator:TestModificator = TestModificator.COMMON) -> (bool,int):



        if isinstance(skill,BasicSkills):
            if skill in self.skills:
               return self.statTest(skilsDependency(skill),modificator)
            else:
                stat = skilsDependency(skill)
                value = random.randrange(0, 100)
                match stat:
                    case MainStats.AGILITY:
                        return (value < self.statistics.agility / 2 + modificator[1], value)
                    case MainStats.FELLOWSHIP:
                        return (value < self.statistics.fellowship / 2+ modificator[1], value)
                    case MainStats.INTELIGENCE:
                        return (value < self.statistics.intelligence / 2+ modificator[1], value)
                    case MainStats.WILL_POWER:
                        return (value < self.statistics.willPower / 2 + modificator[1], value)
                    case MainStats.STRENGTH:
                        return (value < self.statistics.strength / 2 + modificator[1], value)
                    case MainStats.TOUGHNESS:
                        return (value < self.statistics.toughness / 2+ modificator[1], value)
                    case MainStats.BALISSTIC_SKILL:
                        return (value < self.statistics.ballisticSkill / 2 + modificator[1], value)
                    case MainStats.WEAPON_SKILL:
                        return (value < self.statistics.weaponSkill / 2 + modificator[1], value)
        elif isinstance(skill,AdvancedSkills):
            if skill in self.skills:
                return self.statTest(skilsDependency(skill),modificator)
            else:
                return False
    def statTest(self, stat:MainStats, modificator:TestModificator = TestModificator.COMMON) -> (bool,int):
        value = random.randrange(0, 100)
        match stat:
            case MainStats.AGILITY:
                return (value < self.statistics.agility + modificator[1], value)
            case MainStats.FELLOWSHIP:
                return (value < self.statistics.fellowship + modificator[1], value)
            case MainStats.INTELIGENCE:
                return (value < self.statistics.intelligence + modificator[1], value)
            case MainStats.WILL_POWER:
                return (value < self.statistics.willPower + modificator[1], value)
            case MainStats.STRENGTH:
                return (value < self.statistics.strength + modificator[1], value)
            case MainStats.TOUGHNESS:
                return (value < self.statistics.toughness + modificator[1], value)
            case MainStats.BALISSTIC_SKILL:
                return (value < self.statistics.ballisticSkill + modificator[1], value)
            case MainStats.WEAPON_SKILL:
                return (value < self.statistics.weaponSkill + modificator[1], value)