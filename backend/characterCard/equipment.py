from enum import Enum


class Item:
    def __init__(self, name:str, price:int, descriptionId:str, weight:int):
        self.name = name
        self.price = price
        self.descriptionId = descriptionId
        self.weight = weight

    @property
    def priceInSilver(self):
        return self.price / 20
    @property
    def priceInGold(self):
        return self.priceInSilver/12

class Weapon(Item):
    def __init__(self,name,price):
        super().__init__(name,price)
        self.traits = []
        self.type = WeaponType.ORDINARY
        self.range = 1
        self.dmgModificator = 0
        self.strengthModificator = True

    @property
    def isRange(self):
        return self.range > 1

class Armor(Item):

    def __init__(self,name,price):
        super().__init__(name,price)
        self.protectedLocalisations = set()
        self.armorPoints = 0
        self.armorType = ArmorType.LIGHT
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
    HEAD = "pl.1"
    ARMS = "pl.2"
    BODY = "pl.3"
    LEGS = "pl.4"
    ALL = "pl.5"


class Equipment:

    def __init__(self):
        self.items = []
        self.equiptArmors = []
        self.weapon = None

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

