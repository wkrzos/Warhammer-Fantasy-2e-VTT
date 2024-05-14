import json

from backend.characterCard.characteristics import MainStats, SecondaryStats, AttributesType
from backend.characterCard.equipment import WeaponTrait, ArmorType, HitLocalisation, Item, Armor, Weapon
from backend.characterCard.races import Races, MonsterCategory
from backend.characterCard.skillsAndTalents import AdvancedSkills, BasicSkills
from backend.characterCard.statistics import TestModificator, Statistics, Development


class EnumDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def decode(self, s, _w = ...):
        obj = super().decode(s)
        index = obj.split(".")
        match index[0]:
            case "tm":
                return TestModificator(index)
            case "as":
                return AdvancedSkills(index)
            case "bs":
                return BasicSkills(index)
            case "r":
                return Races(index)
            case "mc":
                return MonsterCategory(index)
            case "wtr":
                return WeaponTrait(index)
            case "atp":
                return ArmorType(index)
            case "hl":
                return HitLocalisation(index)
            case "ms":
                return MainStats(index)
            case "ss":
                return SecondaryStats(index)
            case "at":
                return AttributesType(index)


class EnumSetDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def decode(self, s, _w = ...):
        obj = super().decode(s)
        enumDecoder = EnumDecoder()
        result = set()
        for element in obj:
            result.add(enumDecoder.decode(element))
        return result

class StatisticsDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def decode(self, s, _w = ...):
        dic = super().decode(s)
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

class DevelopmentDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def decode(self, s, _w = ...):
        dic= super().decode(s)
        enumDecoder = EnumDecoder()
        result = Development()
        result.exp = dic["exp"]
        updates = {}
        for key in dic["updates"]:
            updates[enumDecoder.decode(key)] = dic["updates"][key]
        result.updates = updates
        return result


class ItemDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def decode(self, s, _w = ...):
        dic = super().decode(s)
        return Item(
            name= dic["name"],
            price= dic["price"],
            description= dic["description"],
            weight= dic["weight"],
        )

class ArmorDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def decode(self, s, _w = ...):
        dic = super().decode(s)
        enumDecoder = EnumDecoder()
        enumSetDecoder = EnumSetDecoder()
        result = Armor(
            name=dic["name"],
            price=dic["price"],
            description=dic["description"],
            weight=dic["weight"],
            armorPoints= dic["armorPoints"],
            protectedLocalisations= enumSetDecoder.decode(dic["protectedLocalisations"]),
            armorType= enumDecoder.decode(dic["type"])
        )

class WeaponDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def decode(self, s, _w = ...):
        dic = super().decode(s)
        enumDecoder = EnumDecoder()
        enumSetDecoder = EnumSetDecoder()

        return Weapon(
            name=dic["name"],
            price=dic["price"],
            description=dic["description"],
            weight=dic["weight"],
            traits= enumSetDecoder.decode(dic["traits"]),
            type= enumDecoder.decode(dic["type"]),
            range= dic["range"],
            dmgModifier= dic["dmgModifier"],
            strengthModificator= dic["strengthModificator"]
        )


class EquipmentDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def decode(self, s, _w = ...):
        dic = super().decode(s)
