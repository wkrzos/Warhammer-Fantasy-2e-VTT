import random

from backend.mechanics.rolling_machine import RollGod
from backend.character_sheets.equipment import *
from backend.character_sheets.characteristics import *
from backend.character_sheets.races import *
from backend.character_sheets.skills_and_talents import *
from backend.character_sheets.statistics import *
from localisation.descriptions import RollDescriptionAggregator, FightDescriptionsType


class Creature:
    def __init__(self, name:str = "", statistics:Statistics = Statistics(), skills:set = set(), talents:set = set(), development:Development = Development(), attributes: Attributes = Attributes(), currentHp:int = None):
        self.name = name
        self.statistics = statistics
        self.skills = skills
        self.talents = talents
        self.development = development
        self.attributes = attributes
        self.currentHp = self.statistics.wounds if currentHp is None else currentHp

    def skillTest(self,skill:Skills, modificator:TestModificator = TestModificator.COMMON) -> (bool,int,int): #(Test sucsesfully, Value of roll, Number of succeses)

        if isinstance(skill,BasicSkills):
            modValue = modificator.value[1]
            if skill in self.skills:
               return self.statTest(skilsDependency[skill],modificator)
            else:
                stat = skilsDependency(skill)
                value = RollGod.rollD100(dsc=RollDescriptionAggregator.testDescriptions[skilsDependency[skill]] + " " + self.name)[0]
                match stat:
                    case MainStats.AGILITY:
                        return (value < self.summaryAgility/2 + modValue, value, (self.summaryAgility/2 - value)/10)
                    case MainStats.FELLOWSHIP:
                        return (value < self.summaryFellowship/2 + modValue, value,(self.summaryFellowship/2 - value)/10)
                    case MainStats.INTELLIGENCE:
                        return (value < self.summaryInteligence/2 + modValue, value,(self.summaryInteligence/2 - value)/10)
                    case MainStats.WILL_POWER:
                        return (value < self.summaryWillPower/2 + modValue, value,(self.summaryWillPower/2 - value)/10)
                    case MainStats.STRENGTH:
                        return (value < self.summaryStrength/2 + modValue, value,(self.summaryStrength/2 - value)/10)
                    case MainStats.TOUGHNESS:
                        return (value < self.summaryToughness/2 + modValue, value,(self.summaryAgility/2 - value)/10)
                    case MainStats.BALLISTIC_SKILL:
                        return (value < self.summaryBalisticSkill/2 + modValue, value,(self.summaryAgility/2 - value)/10)
                    case MainStats.WEAPON_SKILL:
                        return (value < self.summaryWeaponSkill/2 + modValue, value)
        elif isinstance(skill,AdvancedSkills):
            if skill in self.skills:
                return self.statTest(skilsDependency(skill),modificator)
            else:
                return False
    def statTest(self, stat:MainStats, modificator:TestModificator = TestModificator.COMMON) -> (bool,int,int):
        value = RollGod.rollD100(dsc=RollDescriptionAggregator.testDescriptions[stat] + " " + self.name)[0]
        modValue = modificator.value[1]
        match stat:
            case MainStats.AGILITY:
                return (value < self.summaryAgility + modValue, value, (self.summaryAgility - value) / 10)
            case MainStats.FELLOWSHIP:
                return (value < self.summaryFellowship + modValue, value,(self.summaryFellowship - value) / 10)
            case MainStats.INTELLIGENCE:
                return (value < self.summaryInteligence + modValue, value,(self.summaryInteligence - value) / 10)
            case MainStats.WILL_POWER:
                return (value < self.summaryWillPower + modValue, value,(self.summaryWillPower - value) / 10)
            case MainStats.STRENGTH:
                return (value < self.summaryStrength + modValue, value,(self.summaryStrength - value) / 10)
            case MainStats.TOUGHNESS:
                return (value < self.summaryToughness + modValue, value,(self.summaryToughness - value) / 10)
            case MainStats.BALLISTIC_SKILL:
                return (value < self.summaryBalisticSkill+ modValue, value,(self.summaryBalisticSkill - value) / 10)
            case MainStats.WEAPON_SKILL:
                return (value < self.summaryWeaponSkill + modValue, value,(self.summaryWeaponSkill - value) / 10)

    def __dict__(self):
        skills = []
        talents = []
        for skill in self.skills:
            skills.append(skill.value)
        for talent in self.talents:
            talents.append(talent.value)
        return {
            "class" : "creature",
            "name" : self.name,
            "statistics" : self.statistics.__dict__(),
            "skills" : skills,
            "talents" : talents,
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
    @property
    def initiative(self):
        return self.summaryAgility + RollGod.rollD10(dsc= RollDescriptionAggregator.fightDescriptions[FightDescriptionsType.INITIATIVE_ROLL] + " " + self.name)[0]

    @property
    def walk(self):
        return self.statistics.walk

    @property
    def chargeRange(self):
        return self.statistics.chargeRange

    @property
    def runRange(self):
        return self.statistics.runRange

    @property
    def maxHP(self):
        return self.statistics.wounds
class Character(Creature):
    def __init__(self, name:str="", statistics:Statistics = Statistics(), skills:set = set(), talents:set = set(), development:Development = Development(), attributes: Attributes = Attributes(), currentHp:int = None, race: Races = Races.HUMAN, equipment: Equipment = Equipment()):
        super().__init__(name, statistics,skills,talents,development,attributes,currentHp)
        self.equipment = equipment
        self.race = race

    def __dict__(self):
        skills = []
        talents = []
        for skill in self.skills:
            skills.append(skill.value)
        for talent in self.talents:
            talents.append(talent.value)
        return {
            'class' : "character",
            'name': self.name,
            'statistics': self.statistics.__dict__(),
            'skills': skills,
            'talents': talents,
            'development': self.development.__dict__(),
            'attributes': self.attributes.__dict__(),
            'currentHp': self.currentHp,
            'equipment': self.equipment.__dict__(),
            'race' : self.race.value
        }


class CharacterDescription:
    def __init__(self, colorOfEyes:str = "", colorOfHairs:str = "", weight:int = 0, height:int = 0, sex:str = "",age:int = 0, starSign:str = "", birthplace:str = "", distenguishingMarks:str = "", previousProfession: str = "", currentProfession:str = ""):
        self.colorOfEyes =  colorOfEyes
        self.colorOfHairs = colorOfHairs
        self.weight = weight
        self.height = height
        self.sex = sex
        self.age = age
        self.starSign = starSign
        self.birthplace = birthplace
        self.distenguishingMarks = distenguishingMarks
        self.previousProfession = previousProfession
        self.currentProfession = currentProfession


    def __dict__(self):
        return {
            'colorOfEyes' : self.colorOfEyes,
            'colorOfHairs' : self.colorOfHairs,
            'weight' : self.weight,
            'height' : self.height,
            'sex' : self.sex,
            'age' : self.age,
            'starSign' : self.starSign,
            'birthplace' : self.birthplace,
            'distenguishingMarks' : self.distenguishingMarks,
            'previousProfession' : self.previousProfession,
            'currentProfession' : self.currentProfession

        }


class Card:
    def __init__(self, playerName:str = "", playerCharacter:Character = Character(), characterPicture = "", characterDescription:CharacterDescription = CharacterDescription(),history:str =""):
        self.playerName = playerName
        self.playerCharacter = playerCharacter
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

