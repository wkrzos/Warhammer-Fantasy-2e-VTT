from enum import Enum

from backend.character_sheets.sheets import Creature, Character, CharacterDescription, Card
from backend.character_sheets.equipment import Item, Armor, Weapon, WeaponType, Equipment
from backend.character_sheets.statistics import TestModificator
from backend.character_sheets.characteristics import MainStats, SecondaryStats, AttributesType, Attributes
from backend.character_sheets.equipment import WeaponTrait, ArmorType, HitLocalisation, Item, Armor, Weapon
from backend.character_sheets.races import Races, MonsterCategory
from backend.character_sheets.skills_and_talents import AdvancedSkills, BasicSkills
from backend.character_sheets.statistics import TestModificator, Statistics, Development

class ItemsFabric:



    @staticmethod
    def create(dic : dict):
        try:
            match dic["class"]:
                case "item":
                    return ItemsFabric._createItem(dic)
                case "armor":
                    return ItemsFabric._createArmor(dic)
                case "weapon":
                    return ItemsFabric._createWeapon(dic)
        except KeyError as e:
            return Item()
    @staticmethod
    def _createItem(dic : dict) -> Item:
        try:
            return Item(
                name= dic["name"],
                price= dic["price"],
                description= dic["description"],
                weight= dic["weight"],
            )
        except KeyError as e:
            return Item()
    @staticmethod
    def _createArmor(dic : dict) -> Armor:
        try:
            return Armor(
                name=dic["name"],
                price=dic["price"],
                description=dic["description"],
                weight=dic["weight"],
                armorPoints=dic["armorPoints"],
                protectedLocalisations=EnumFabric.createEnumSet(dic["protectedLocalisations"]),
                armorType = EnumFabric.createEnum(dic["armorType"])
            )
        except KeyError as e:
            return Armor()
    @staticmethod
    def _createWeapon(dic : dict) ->Weapon:
        return Weapon(
            name=dic["name"],
            price=dic["price"],
            description=dic["description"],
            weight=dic["weight"],
            traits=EnumFabric.createEnumSet(dic["traits"]),
            type= EnumFabric.createEnum(dic["type"]),
            range=dic["range"],
            dmgModifier=dic["dmgModifier"],
            strengthModificator=dic["strengthModificator"]
        )

class EnumFabric:

    @staticmethod
    def createEnum(s:str):
        index = s.split(".")
        match index[0]:
            case "tm":
                return TestModificator(s)
            case "as":
                return AdvancedSkills(s)
            case "bs":
                return BasicSkills(s)
            case "r":
                return Races(s)
            case "mc":
                return MonsterCategory(s)
            case "wtp":
                return WeaponType(s)
            case "wtr":
                return WeaponTrait(s)
            case "atp":
                return ArmorType(s)
            case "hl":
                return HitLocalisation(s)
            case "ms":
                return MainStats(s)
            case "ss":
                return SecondaryStats(s)
            case "at":
                return AttributesType(s)
    @staticmethod
    def createEnumSet(lst:list) -> set:
        result = set()
        for element in lst:
            result.add(EnumFabric.createEnum(element))
        return result

class CreaturesFabric:


    @staticmethod
    def createCharacter(dic:dict)->Character:
        try:
            return Character(
                name=dic["name"],
                statistics=CreaturesFabric._createStatistics(dic["statistics"]),
                skills=EnumFabric.createEnumSet(dic["skills"]),
                talents=EnumFabric.createEnumSet(dic["talents"]),
                development=CreaturesFabric._createDevelopmnets(dic["development"]),
                attributes=CreaturesFabric._createAtributes(dic["attributes"]),
                currentHp=dic["currentHp"],
                race=EnumFabric.createEnum(dic["race"]),
                equipment=CreaturesFabric._createEquipment(dic["equipment"])
            )
        except KeyError as e:
            return Character()
    @staticmethod
    def createCreature(dic:dict)-> Creature:
        try:
            return Creature(
                name=dic["name"],
                statistics=CreaturesFabric._createStatistics(dic["statistics"]),
                skills=EnumFabric.createEnumSet(dic["skills"]),
                talents=EnumFabric.createEnumSet(dic["talents"]),
                development=CreaturesFabric._createDevelopmnets(dic["development"]),
                attributes=CreaturesFabric._createAtributes(dic["attributes"]),
                currentHp=dic["currentHp"]
            )
        except KeyError as e:
            return Creature()

    @staticmethod
    def _createEquipment(dic:dict) ->Equipment:
        try:
            items = []
            armors = []
            for item in dic["items"]:
                items.append(ItemsFabric.create(item))
            for armor in dic["equiptArmors"]:
                armors.append(ItemsFabric.create(armor))
            return Equipment(
                items=items,
                equiptArmors=armors,
                weapon=ItemsFabric.create(dic["weapon"])
            )
        except KeyError:
            return Equipment()
    @staticmethod
    def _createStatistics(dic:dict)->Statistics:
        try:
            return Statistics(
                ws=dic["weaponSkill"],
                bs=dic["ballisticSkill"],
                s=dic["strength"],
                t=dic["toughness"],
                ag=dic["agility"],
                int=dic["intelligence"],
                wp=dic["willPower"],
                fel=dic["fellowship"],
                attacks=dic["attacks"],
                w=dic["wounds"],
                m=dic["movement"],
                magic=dic["magic"],
                ip=dic["insanityPoints"],
                fp=dic["fatePoints"]

            )
        except KeyError:
            return Statistics()
    @staticmethod
    def _createDevelopmnets(dic:dict) -> Development:

        result = Development()
        try:
            result.exp = dic["exp"]
            updates = {}
            for key in dic["updates"].keys():
                updates[EnumFabric.createEnum(key)] = dic["updates"][key]
            result.updates = updates
        except KeyError:
            pass
        return result
    @staticmethod
    def _createAtributes(dic:dict) -> Attributes:
        try:
            return Attributes(
                actionsRemain= dic["actionsRemain"],
                attributesActive= EnumFabric.createEnumSet(dic["attributesActive"])
            )
        except KeyError:
            return Attributes()

class CardFabric:

    @staticmethod
    def createCard(dic:dict)->Card:
        try:
            result = Card(
                playerName=dic["playerName"],
                playerCharacter=CreaturesFabric.createCharacter(dic['playerCharacter']),
                characterPicture= dic['characterPicture'],
                history=dic['history']
            )
        except KeyError:
            result = Card()
        return result
    @staticmethod
    def _createDescription(dic:dict)->CharacterDescription:
        try:
            return CharacterDescription(
                colorOfEyes=dic['colorOfEyes'],
                colorOfHairs=dic['colorOfHairs'],
                weight=dic['weight'],
                height=dic['height'],
                sex=dic['sex'],
                age=dic['age'],
                starSign=dic['starSign'],
                birthplace=dic['birthplace'],
                distenguishingMarks=dic['distenguishingMarks'],
                previousProfession=dic['previousProfession'],
                currentProfession=dic['currentProfession']
            )
        except KeyError as e:
            return CharacterDescription()