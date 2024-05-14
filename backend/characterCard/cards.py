import random

from backend.mechanic.rolingMachine import RollGod
from equipment import *
from characteristics import *
from races import *
from skillsAndTalents import *
from statistics import *

class Creature:
    def __init__(self, name:str, statistics:Statistics = Statistics()):
        self.name = name
        self.statistics = statistics
        self.skills = set()
        self.talents = set()
        self.development = Development()
        self.attributes = Attributes()
        self.currentHp = self.statistics.wounds

    def skillTest(self,skill:Skills, modificator:TestModificator = TestModificator.COMMON) -> (bool,int,int): #(Test sucsesfully, Value of roll, Number of succeses)

        if isinstance(skill,BasicSkills):
            if skill in self.skills:
               return self.statTest(skilsDependency(skill),modificator)
            else:
                stat = skilsDependency(skill)
                value = RollGod.rollD100(1)[0]
                match stat:
                    case MainStats.AGILITY:
                        return (value < self.summaryAgility/2 + modificator[1], value, (self.summaryAgility/2 - value)/10)
                    case MainStats.FELLOWSHIP:
                        return (value < self.summaryFellowship/2 + modificator[1], value,(self.summaryFellowship/2 - value)/10)
                    case MainStats.INTELLIGENCE:
                        return (value < self.summaryInteligence/2 + modificator[1], value,(self.summaryInteligence/2 - value)/10)
                    case MainStats.WILL_POWER:
                        return (value < self.summaryWillPower/2 + modificator[1], value,(self.summaryWillPower/2 - value)/10)
                    case MainStats.STRENGTH:
                        return (value < self.summaryStrength/2 + modificator[1], value,(self.summaryStrength/2 - value)/10)
                    case MainStats.TOUGHNESS:
                        return (value < self.summaryToughness/2 + modificator[1], value,(self.summaryAgility/2 - value)/10)
                    case MainStats.BALLISTIC_SKILL:
                        return (value < self.summaryBalisticSkill/2 + modificator[1], value,(self.summaryAgility/2 - value)/10)
                    case MainStats.WEAPON_SKILL:
                        return (value < self.summaryWeaponSkill/2 + modificator[1], value)
        elif isinstance(skill,AdvancedSkills):
            if skill in self.skills:
                return self.statTest(skilsDependency(skill),modificator)
            else:
                return False
    def statTest(self, stat:MainStats, modificator:TestModificator = TestModificator.COMMON) -> (bool,int,int):
        value = RollGod.rollD100(1)[0]
        match stat:
            case MainStats.AGILITY:
                return (value < self.summaryAgility + modificator[1], value, (self.summaryAgility - value) / 10)
            case MainStats.FELLOWSHIP:
                return (value < self.summaryFellowship + modificator[1], value,(self.summaryFellowship - value) / 10)
            case MainStats.INTELLIGENCE:
                return (value < self.summaryInteligence + modificator[1], value,(self.summaryInteligence - value) / 10)
            case MainStats.WILL_POWER:
                return (value < self.summaryWillPower + modificator[1], value,(self.summaryWillPower - value) / 10)
            case MainStats.STRENGTH:
                return (value < self.summaryStrength + modificator[1], value,(self.summaryStrength - value) / 10)
            case MainStats.TOUGHNESS:
                return (value < self.summaryToughness + modificator[1], value,(self.summaryToughness - value) / 10)
            case MainStats.BALLISTIC_SKILL:
                return (value < self.summaryBalisticSkill+ modificator[1], value,(self.summaryBalisticSkill - value) / 10)
            case MainStats.WEAPON_SKILL:
                return (value < self.summaryWeaponSkill + modificator[1], value,(self.summaryWeaponSkill - value) / 10)

    def __dict__(self):
        return {
            "name" : self.name,
            "statistics" : self.statistics.__dict__(),
            "skills" : list(self.skills),
            "talents" : list(self.talents),
            "development" : self.development.__dict__(),
            "attributes" : self.attributes.__dict__(),
            "currentHp" : self.currentHp

        }

    @property
    def summaryWeaponSkill(self):
        return  self.statistics.weaponSkill + self.development.getStatsBonus(MainStats.WEAPON_SKILL) +(5 if Talents.WARRIOR_BORN in self.talents else 0)

    @property
    def summaryBalisticSkill(self):
        return self.statistics.ballisticSkill + self.development.getStatsBonus(MainStats.BALLISTIC_SKILL) + (5 if Talents.MARKSMAN in self.talents else 0)

    @property
    def summaryStrength(self):
        return self.statistics.strength + self.development.getStatsBonus(MainStats.STRENGTH) + (5 if Talents.VERY_STRONG in self.talents else 0)

    @property
    def summaryToughness(self):
        return self.statistics.toughness + self.development.getStatsBonus(MainStats.TOUGHNESS) + (5 if Talents.VERY_RESILIENT in self.talents else 0)

    @property
    def summaryAgility(self):
        return self.statistics.agility + self.development.getStatsBonus(MainStats.AGILITY) + (5 if Talents.LIGHTNING_REFLEXES in self.talents else 0)

    @property
    def summaryInteligence(self):
        return self.statistics.intelligence + self.development.getStatsBonus(MainStats.INTELLIGENCE) + (5 if Talents.SAVVY in self.talents else 0)

    @property
    def summaryWillPower(self):
        return self.statistics.willPower + self.development.getStatsBonus(MainStats.WILL_POWER) + (5 if Talents.COOLHEADED in self.talents else 0)

    @property
    def summaryFellowship(self):
        return self.statistics.fellowship + self.development.getStatsBonus(MainStats.FELLOWSHIP) + (5 if Talents.SUAVE in self.talents else 0)

    @property
    def summaryHp(self):
        return self.statistics.wounds + self.development.getStatsBonus(SecondaryStats.WOUNDS)
    def summaryAttacks(self):
        return self.statistics.attacks + self.development.getStatsBonus(SecondaryStats.ATTACKS)
    @property
    def summaryMovement(self):
        return self.statistics.movement + self.development.getStatsBonus(SecondaryStats.MOVEMENT) + (
            5 if Talents.FLEET_FOOTED in self.talents else 0)
    @property
    def summaryMagic(self):
        return self.statistics.magic + self.development.getStatsBonus(SecondaryStats.MAGIC)

    @property
    def toughnessBonus(self):
        return self.statistics.toughnessBonus
    @property
    def strengthBonus(self):
        return self.statistics.strengthBonus

class Character(Creature):
    def __init__(self, name: str, statistics: Statistics = Statistics(), race: Races = Races.HUMAN):
        super().__init__(name, statistics)
        self.equipment = Equipment()
        self.race = race

    def __dict__(self):
        return {
            'name': self.name,
            'statistics': self.statistics.__dict__(),
            'skills': list(self.skills),
            'talents': list(self.talents),
            'development': self.development.__dict__(),
            'attributes': self.attributes.__dict__(),
            'currentHp': self.currentHp,
            'equipment': self.equipment.__dict__(),
            'race' : self.race
        }


class CharacterDescription:
    def __init__(self, colorOfEyes:str = "", colorOfHairs:str = "", weight:int = 0, height:int = 0, sex:str = "",age:int = 0):
        self.colorOfEyes =  colorOfEyes
        self.colorOfHairs = colorOfHairs
        self.weight = weight
        self.height = height
        self.sex = sex
        self.age = age

    def __dict__(self):
        return {
            'colorOfEyes' : self.colorOfEyes,
            'colorOfHairs' : self.colorOfHairs,
            'weight' : self.weight,
            'height' : self.height,
            'sex' : self.sex,
            'age' : self.age
        }


class Card:
    def __init__(self, playerName:str = "", playerCharacter:Character = Character(), characterPicture = "", characterDescription:CharacterDescription = CharacterDescription(),history:str =""):
        self.playerName = playerName
        self.playerCharacter =  playerCharacter
        self.characterPicture = characterPicture
        self.characterDescription = characterDescription
        self.history = history

    def __dict__(self):
        return {
            'playerName' : self.playerName,
            'playerCharacter' : self.playerCharacter.__dict__(),
            'characterPicture' : self.characterPicture,
            'characterDescription' : self.characterDescription.__dict__(),
            'history' : self.history

        }

