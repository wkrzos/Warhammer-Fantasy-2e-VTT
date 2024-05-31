from backend.character_sheets.sheets import Creature, Character
from backend.character_sheets.equipment import Item, HitLocalisation
from backend.character_sheets.skills_and_talents import Skills, AdvancedSkills
from backend.character_sheets.statistics import TestModificator
from backend.mechanics.token import Token
from backend.character_sheets.characteristics import *
from backend.mechanics.rolling_machine import *
from localisation.descriptions import RollDescriptionAggregator, FightDescriptionsType
from localisation.itemsText import ItemsTextAggregator


class Action:
    pass

class SelfAction(Action):

    @staticmethod
    def parry(player:Token):
        player.creature.attributes.add(AttributesType.IS_PARING)

    @staticmethod
    def aiming(player:Token):
        player.creature.attributes.add(AttributesType.IS_AIMING)

    @staticmethod
    def wakeUp(player:Token):
        player.creature.attributes.remove(AttributesType.IS_LYING)

    @staticmethod
    def defenseStand(player:Token):
        player.creature.attributes.add(AttributesType.IS_IN_DEFENCE)

    @staticmethod
    def useTalent(player:Token):
        pass

class ActionOnAnother(Action):

    @staticmethod
    def simpleAtack(player:Token,other:Token, mod: TestModificator = TestModificator.COMMON):
        dmg = 0

        mod = DmgManager.calculateMod(player, mod)
        testResult, rollValue, _ = player.creature.statTest(MainStats.WEAPON_SKILL,mod)

        if testResult:
            if AttributesType.FURIOUS in other.creature.attributes:
                dmg = DmgManager.calculateDmg(player, other,rollValue)
            elif AdvancedSkills.DODGE_BLOW in other.creature.skills:
                if AttributesType.ALREADY_DODGED not in other.creature.attributes:
                    other.creature.attributes.append(AttributesType.ALREADY_DODGED)
                    if not PassiveAction.tryDoge(other):
                        dmg = DmgManager.calculateDmg(player, other,rollValue)
            elif AttributesType.IS_IN_DEFENCE in other.creature.attributes and not PassiveAction.tryParry(other):
                    dmg = DmgManager.calculateDmg(player, other,rollValue)
            elif AttributesType.IS_PARING in other.creature.attributes:
                other.creature.attributes.remove(AttributesType.IS_PARING)
                if not PassiveAction.tryParry(other):
                    dmg = DmgManager.calculateDmg(player, other,rollValue)
            else:
                dmg = DmgManager.calculateDmg(player, other,rollValue)
        other.creature.currentHp -= dmg

    @staticmethod
    def multipleAtack(player:Token,other:Token):
        for i in range(player.creature.statistics.attacks):
            ActionOnAnother.simpleAtack(player,other)
    @staticmethod
    def furiousAtack(player:Token,other:Token):
        player.creature.attributes.add(AttributesType.FURIOUS)
        ActionOnAnother.simpleAtack(player,other)
    @staticmethod
    def carefullAtack(player:Token,other:Token):
        ActionOnAnother.simpleAtack(player,other)
        player.creature.attributes.add(AttributesType.IS_PARING)
    @staticmethod
    def push(player: Token,other: Token):
        if player.creature.statTest(MainStats.STRENGTH)[2] > other.creature.statTest(MainStats.STRENGTH)[2]:
            other.move(other.position[0] - player.position[0],other.position[1] - player.position[1] )  #Check good operation
    @staticmethod
    def feint(player:Token,other:Token):
        pass


class SpecialAction(Action):
    @staticmethod
    def useItem(player: Creature, item: Item):
        pass

class PassiveAction(Action):
    @staticmethod
    def tryDoge(player:Token,mod: TestModificator = TestModificator.COMMON) -> bool:
        return player.creature.skillTest(AdvancedSkills.DODGE_BLOW,mod)[0]
    @staticmethod
    def tryParry(player:Token, mod: TestModificator = TestModificator.COMMON) -> bool:
        return player.creature.statTest(MainStats.WEAPON_SKILL, mod)[0]

class DmgManager(Observable):



    # _instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls, *args, **kwargs)
    #     return cls._instance

    @staticmethod
    def calculateHitLocalisation(roll:int) -> HitLocalisation:
        reversRoll = roll / 10 + roll % 10 * 10
        if reversRoll <= 15:
            DmgManager.notify(HitLocalisation.HEAD)
            return HitLocalisation.HEAD
        elif reversRoll <= 55:
            DmgManager.notify(HitLocalisation.ARMS)
            return HitLocalisation.ARMS
        elif reversRoll <= 80:
            DmgManager.notify(HitLocalisation.BODY)
            return HitLocalisation.BODY
        else:
            DmgManager.notify(HitLocalisation.LEGS)
            return HitLocalisation.LEGS


    @staticmethod
    def calculateDmgReduction(player: Token, location: HitLocalisation) -> int:
        reduction = player.creature.toughnessBonus
        if isinstance(player.creature, Character):
            for item in player.creature.equipment.armors:
                if location in item.protectedLocalisations:
                    reduction += item.armorPoints
        return reduction

    @staticmethod
    def calculateDmgBonus(player: Token) -> int:
        if isinstance(player.creature, Creature):
            return player.creature.strengthBonus
        elif isinstance(player.creature, Character):
            weapon = player.creature.equipment.weapon
            if weapon is not None:
                if weapon.strengthModificator:
                    return player.creature.strengthBonus + weapon.dmgModificator
                else:
                    return weapon.dmgModificator + player.creature.strengthBonus
            else:
                return player.creature.strengthBonus - 3
    @staticmethod
    def calculateDmg(player: Token, other: Token, rollValue:int) -> int:
        dmgBonus = DmgManager.calculateDmgBonus(player)
        hitLocalisation = DmgManager.calculateHitLocalisation(rollValue)
        dmgReduction = DmgManager.calculateDmgReduction(other, hitLocalisation)
        dmgRoll = RollGod.rollD10(dsc= RollDescriptionAggregator.fightDescriptions[FightDescriptionsType.DMG_ROLL] + " " + player.creature.name )[0]
        dmg = dmgBonus - dmgReduction  + dmgRoll
        msgLocalisation = player.creature.name + " " +  RollDescriptionAggregator.fightDescriptions[FightDescriptionsType.HIT_LOCALISATION] + " " + ItemsTextAggregator.hitLocalisationNames[hitLocalisation]
        msgDmgDealt = ""
        DmgManager.notify((dmg,hitLocalisation,player.creature.name))
        return dmg

    @staticmethod
    def calculateMod(player: Token, baseMod: TestModificator = TestModificator.COMMON) -> TestModificator:
        match baseMod:
            case TestModificator.VERY_EASY:
                return TestModificator.VERY_EASY
            case TestModificator.EASY:
                if AttributesType.IS_AIMING in player.creature.attributes or AttributesType.FURIOUS in player.creature.attributes:
                    return TestModificator.VERY_EASY
                else:
                    return TestModificator.EASY
            case TestModificator.SIMPLE:
                if AttributesType.FURIOUS in player.creature.attributes:
                    return TestModificator.VERY_EASY
                elif AttributesType.IS_AIMING in player.creature.attributes:
                    return TestModificator.EASY
                else:
                    return TestModificator.SIMPLE
            case TestModificator.COMMON:
                if AttributesType.FURIOUS in player.creature.attributes:
                    return TestModificator.EASY
                elif AttributesType.IS_AIMING in player.creature.attributes:
                    return TestModificator.SIMPLE
                else:
                    return TestModificator.COMMON
            case TestModificator.HARD:
                if AttributesType.FURIOUS in player.creature.attributes:
                    return TestModificator.SIMPLE
                elif AttributesType.IS_AIMING in player.creature.attributes:
                    return TestModificator.COMMON
                else:
                    return TestModificator.HARD
            case TestModificator.VERY_HARD:
                if AttributesType.FURIOUS in player.creature.attributes:
                    return TestModificator.COMMON
                elif AttributesType.IS_AIMING in player.creature.attributes:
                    return TestModificator.HARD
                else:
                    return TestModificator.VERY_HARD