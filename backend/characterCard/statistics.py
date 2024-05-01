from enum import Enum

class Statistics:
    def __init__(self, ws, bs,s,t,ag,int,wp,fel,w,m,fp):
        self.weaponSkill = ws #Weapon Skill
        self.ballisticSkill = bs #Ballistic Skill
        self.strength = s #Strength
        self.toughness = t #Toughness
        self.agility = ag #Agility
        self.intelligence = int #Inteligence
        self.willPower = wp #Will Power
        self.fellowship = fel #Fellowship
        self.attacks = 1 #Attacks
        self.wounds = w #Wounds
        self.movement = m #Movement
        self.magic = 0 #Magic
        self.insanityPoints = 0 #Insanity Points
        self.fatePoint = fp #Fate Point

    # def __init__(self):
    #     self.weaponSkill = 0 #Weapon Skill
    #     self.ballisticSkill = 0 #Ballistic Skill
    #     self.strength = 0 #Strength
    #     self.toughness = 0 #Toughness
    #     self.agility = 0 #Agility
    #     self.intelligence = 0 #Inteligence
    #     self.willPower = 0 #Will Power
    #     self.fellowship = 0 #Fellowship
    #     self.attacks = 1 #Attacks
    #     self.wounds = 0 #Wounds
    #     self.movement = 0 #Movement
    #     self.magic = 0 #Magic
    #     self.insanityPoints = 0 #Insanity Points
    #     self.fatePoint = 0 #Fate Point

    @property
    def strengthBonus(self):
        return self.strength /10
    @property
    def  toughnessBonus(self):
        return self.toughness /10

class TestModificator(Enum):
    VERY_EASY = ("tm.1",30),
    EASY = ("tm.2", 20),
    SIMPLE = ("tm.3",10),
    COMMON = ("tm.4", 0),
    DEMANDING = ("tm.5", -10),
    HARD = ("tm.6", -20),
    VERY_HARD = ("tm.7", -30)
