from enum import Enum

class WeaponTrait(Enum):
    HEAVY = "wtr.1",
    DEVASTATING = "wtr.2",
    EXPERIMENTAL = "wtr.3",
    SHRAPNEL = "wtr.4",
    DEAFENING = "wtr.5",
    PARRYING = "wtr.6",
    SLOW = "wtr.7",
    PRECISE = "wtr.8",
    PIERCING = "wtr.9",
    SPECIAL = "wtr.10",
    FAST = "wtr.11",
    IMMOBILIZING = "wtr.12",
    BALANCED = "wtr.13",
    UNRELIABLE = "wtr.14",

class WeaponType(Enum):
    ORDINARY = "wtp.1",
    TWO_HANDED = "wtp.2",
    CAVALRY = "wtp.3",
    FLAIL = "wtp.4",
    PARRYING = "wtp.5",
    FENCING = "wtp.6",
    IMMOBILIZING = "wtp.7",
    LONG_BOW = "wtp.8",
    FIREARM = "wtp.9",
    CROSSBOW = "wtp.10",
    MECHANICAL = "wtp.11",
    THROWN = "wtp.12",
    SLINGSHOT = "wtp.13"


class ArmorType(Enum):
    LIGHT = "atp.1",
    MEDIUM = "atp.2",
    HEAVY = "atp.3"

class HitLocalisation(Enum):
    HEAD = "hl.1"
    ARMS = "hl.2"
    BODY = "hl.3"
    LEGS = "hl.4"
    ALL = "hl.5"


class Item:
    def __init__(self, name:str = "", price:int = 0, description:str= "", weight:int = 0):
        self.name = name
        self.price = price
        self.description = description
        self.weight = weight

    @property
    def priceInSilver(self):
        return self.price / 20
    @property
    def priceInGold(self):
        return self.priceInSilver/12
    def __dict__(self):
        return {
            'class' : 'item',
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'weight': self.weight
        }

class Weapon(Item):
    def __init__(self,name:str = "", price:int = 0, description:str = "", weight:int = 0, traits:set = set(), type:WeaponType = WeaponType.ORDINARY, range:int = 1, dmgModifier:int = -3, strengthModificator = True ):
        super().__init__(name,price,description,weight)
        self.traits = traits
        self.type = type
        self.range = range
        self.dmgModificator = dmgModifier
        self.strengthModificator = strengthModificator

    def __dict__(self):
        return {
            'class' : "weapon",
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'weight': self.weight,
            'traits': list(self.traits),
            'type': self.type,
            'range': self.range,
            'dmgModificator': self.dmgModificator,
            'strengthModificator': self.strengthModificator
        }
    @property
    def isRange(self):
        return self.range > 1

class Armor(Item):

    def __init__(self,name,price, description:str = "", weight:int = 0,protectedLocalisations:set = set, armorPoints:int = 0,  armorType:ArmorType = ArmorType.LIGHT ):
        super().__init__(name,price,description,weight)
        self.protectedLocalisations = protectedLocalisations
        self.armorPoints = armorPoints
        self.armorType = armorType

    def __dict__(self):
        return {
            'class' : "armor",
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'weight': self.weight,
            'protectedLocalisations': list(self.protectedLocalisations),
            'armorPoints': self.armorPoints,
            'armorType': self.armorType

        }


class Equipment:

    def __init__(self, items:list = [], equiptArmors:list= [], weapon: Weapon = Weapon()):
        self.items = items
        self.equiptArmors = equiptArmors
        self.weapon = weapon

    def equipWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def equipArmor(self, armor: Armor):

        if HitLocalisation.ALL in armor.protectedLocalisations:
            self.armors = [armor]
        else:
            for localisation in armor.protectedLocalisations:
                self.armors = filter(lambda x: localisation not in x.protectedLocalisations, self.armors)
        self.armors.append(armor)

    def addItem(self, item: Item):
        self.items.append(item)

    def __dict__(self):
        serializedItems = []
        for item in self.items:
            serializedItems.append(item.__dict__())
        serializedArmors = []
        for armor in self.equiptArmors:
            serializedArmors.append(armor.__dict__())
        return {
            'items': serializedItems,
            'equipArmors': serializedArmors,
            'weapon' : self.weapon.__dict__()
        }