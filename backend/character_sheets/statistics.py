from enum import Enum

from backend.character_sheets.characteristics import *


class Statistics:
    def __init__(self, ws=0, bs=0,s=0,t=0,ag=0,int=0,wp=0,fel=0,attacks=1,w=0,m=0,magic=0,ip=0,fp=0):
        self.weaponSkill = ws #Weapon Skill
        self.ballisticSkill = bs #Ballistic Skill
        self.strength = s #Strength
        self.toughness = t #Toughness
        self.agility = ag #Agility
        self.intelligence = int #Inteligence
        self.willPower = wp #Will Power
        self.fellowship = fel #Fellowship
        self.attacks = attacks #Attacks
        self.wounds = w #Wounds
        self.movement = m #Movement
        self.magic = magic #Magic
        self.insanityPoints = ip #Insanity Points
        self.fatePoint = fp #Fate Point

    @property
    def strengthBonus(self):
        return self.strength // 10
    @property
    def  toughnessBonus(self):
        return self.toughness //10
    @property
    def burden(self):
        return self.strength * 10
    @property
    def walk(self):
        return self.movement * 2
    @property
    def chargeRange(self):
        return self.movement * 3
    @property
    def runRange(self):
        return self.movement * 4
    def __dict__(self):
        return {
            "weaponSkill" : self.weaponSkill,
            "ballisticSkill" : self.ballisticSkill,
            "strength" : self.strength,
            "toughness" : self.toughness,
            "agility" : self.agility,
            "intelligence" : self.intelligence,
            "willPower" : self.willPower,
            "fellowship" : self.fellowship,
            "attacks" : self.attacks,
            "wounds" : self.wounds,
            "movement" : self.movement,
            "magic" : self.magic,
            "insanityPoints" : self.insanityPoints,
            "fatePoints" : self.fatePoint
        }
class TestModificator(Enum):
    VERY_EASY = ("tm.1",30)
    EASY = ("tm.2", 20)
    SIMPLE = ("tm.3",10)
    COMMON = ("tm.4", 0)
    DEMANDING = ("tm.5", -10)
    HARD = ("tm.6", -20)
    VERY_HARD = ("tm.7", -30)

class Development:

    def __init__(self):
        self.exp = 0
        self.updates = {
        MainStats.WEAPON_SKILL : 0,
        MainStats.BALLISTIC_SKILL : 0,
        MainStats.STRENGTH : 0,
        MainStats.TOUGHNESS : 0,
        MainStats.AGILITY : 0,
        MainStats.INTELLIGENCE : 0,
        MainStats.WILL_POWER : 0,
        MainStats.FELLOWSHIP : 0,
        SecondaryStats.ATTACKS : 0,
        SecondaryStats.WOUNDS : 0,
        SecondaryStats.MAGIC : 0,
        SecondaryStats.MOVEMENT : 0

        }

    def levelUp(self, stat:Stats) -> None:
        if self.exp >= 100:
            self.exp -= 100
            self.updates[stat] += 1


    def getStatsBonus(self, stat:Stats) -> int:
        if isinstance(stat,MainStats):
            return self.updates[stat] * 5
        else:
            return self.updates[stat]

    def __dict__(self):
        return {
            "exp" : self.exp,
            "updates" : {
                MainStats.WEAPON_SKILL.value : 0,
                MainStats.BALLISTIC_SKILL.value : 0,
                MainStats.STRENGTH.value : 0,
                MainStats.TOUGHNESS.value : 0,
                MainStats.AGILITY.value : 0,
                MainStats.INTELLIGENCE.value : 0,
                MainStats.WILL_POWER.value : 0,
                MainStats.FELLOWSHIP.value : 0,
                SecondaryStats.ATTACKS.value : 0,
                SecondaryStats.WOUNDS.value : 0,
                SecondaryStats.MAGIC.value : 0,
                SecondaryStats.MOVEMENT.value : 0

            }
        }