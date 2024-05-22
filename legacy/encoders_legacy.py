# import json
#
# from backend.characterCard.cards import Creature, CharacterDescription, Character, Card
# from backend.characterCard.characteristics import MainStats, SecondaryStats, AttributesType
# from backend.characterCard.equipment import WeaponTrait, ArmorType, HitLocalisation, Item, Armor, Weapon, Equipment
# from backend.characterCard.races import Races, MonsterCategory
# from backend.characterCard.skillsAndTalents import AdvancedSkills, BasicSkills
# from backend.characterCard.statistics import TestModificator, Statistics, Development
#
#
# class StatisticsEncoder(json.JSONEncoder):
#     def default(self, o:Statistics):
#         return o.__dict__
#
# class DevelopmentEncoder(json.JSONEncoder):
#     def default(self, o:Development):
#         return o.__dict__
#
# class ItemEncoder(json.JSONEncoder):
#     def default(self, o:Item):
#         return o.__dict__
# class ArmorEncoder(json.JSONEncoder):
#     def default(self, o:Armor):
#         return o.__dict__
# class WeaponEncoder(json.JSONEncoder):
#     def default(self, o:Weapon):
#         return o.__dict__
# class EquipmentEncoder(json.JSONEncoder):
#     def default(self, o:Equipment):
#         return o.__dict__
# class CreatureEncoder(json.JSONEncoder):
#     def default(self, o:Creature):
#         return o.__dict__
# class CharacterDescriptionEncoder(json.JSONEncoder):
#     def default(self, o:CharacterDescription):
#         return o.__dict__
# class CharacterEncoder(json.JSONEncoder):
#     def default(self, o:Character):
#         return o.__dict__
# class CardEncoder(json.JSONEncoder):
#     def default(self, o:Card):
#         return  o.__dict__
# class AttributesEncoder(json.JSONEncoder):
#     def default(self, o:AttributesType):
#         return o.__dict__