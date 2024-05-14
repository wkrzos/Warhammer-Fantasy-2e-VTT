# import json
#
# from backend.characterCard.characteristics import MainStats, SecondaryStats, AttributesType
# from backend.characterCard.equipment import WeaponTrait, ArmorType, HitLocalisation, Item, Armor, Weapon
# from backend.characterCard.races import Races, MonsterCategory
# from backend.characterCard.skillsAndTalents import AdvancedSkills, BasicSkills
# from backend.characterCard.statistics import TestModificator, Statistics, Development
# from backend.jsonSerialization.fabrics import *
#
#
#
# class StatisticsDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     def decode(self, s, _w = ...):
#         dic = super().decode(s)
#         return Statistics(
#             ws=dic["weaponSkill"],
#             bs=dic["ballisticSkill"],
#             s=dic["strength"],
#             t=dic["toughness"],
#             ag=dic["agility"],
#             int=dic["intelligence"],
#             wp=dic["willPower"],
#             fel=dic["fellowship"],
#             attacks=dic["attacks"],
#             w=dic["wounds"],
#             m=dic["movement"],
#             magic=dic["magic"],
#             ip=dic["insanityPoints"],
#             fp=dic["fatePoints"]
#
#         )
#
# class DevelopmentDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     def decode(self, s, _w = ...):
#         dic= super().decode(s)
#         enumDecoder = EnumDecoder()
#         result = Development()
#         result.exp = dic["exp"]
#         updates = {}
#         for key in dic["updates"]:
#             updates[enumDecoder.decode(key)] = dic["updates"][key]
#         result.updates = updates
#         return result
#
#
# class ItemDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     def decode(self, s, _w = ...):
#         dic = super().decode(s)
#
#
# class ArmorDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     def decode(self, s, _w = ...):
#         dic = super().decode(s)
#         enumDecoder = EnumDecoder()
#         enumSetDecoder = EnumSetDecoder()
#
# class ArmorListDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def decode(self, s, _w = ...):
#         lst = super().decode(s)
#         result = []
#         armorDecoder = ArmorDecoder()
#         for armor in lst:
#             result.append(armorDecoder.decode(armor))
#
# class WeaponDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     def decode(self, s, _w = ...):
#         dic = super().decode(s)
#         enumDecoder = EnumDecoder()
#         enumSetDecoder = EnumSetDecoder()
#
#
#
#
# class EquipmentDecoder(json.JSONDecoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     def decode(self, s, _w = ...):
#         dic = super().decode(s)
#
#
