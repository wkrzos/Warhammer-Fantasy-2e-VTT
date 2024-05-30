import json

from backend.character_sheets.equipment import WeaponType, WeaponTrait, ArmorType, HitLocalisation


class ItemsTextAggregator:


    weaponTypesNames = {weaponType: "" for weaponType in WeaponType}

    weaponTraitsNames = {weaponTrait: "" for weaponTrait in WeaponTrait}

    armorTypesNames = {armorType: "" for armorType in ArmorType}

    hitLocalisationNames = {hitLocalisation: "" for hitLocalisation in HitLocalisation}

    @classmethod
    def serialize_weapon_types_names(cls):
        return {weaponType.value : cls.weaponTypesNames[weaponType] for weaponType in WeaponType}

    @classmethod
    def serialize_weapon_trait_names(cls):
        return {weaponTrait.value: cls.weaponTraitsNames[weaponTrait] for weaponTrait in WeaponTrait}

    @classmethod
    def serialize_armor_types_names(cls):
        return {armorType.value: cls.armorTypesNames[armorType] for armorType in ArmorType}

    @classmethod
    def serialize_hit_localisation_names(cls):
        return {hitLocalisation.value: cls.hitLocalisationNames[hitLocalisation] for hitLocalisation in HitLocalisation}

    @classmethod
    def load_weapon_types_names(cls,path:str):
        try:
            with open(path, "r") as f:
                jsonData = json.load(f)
                for key in cls.weaponTypesNames.keys():
                    if key.value in jsonData.keys():
                        cls.weaponTypesNames[key] = jsonData[key.value]
        except FileNotFoundError:
            pass
    @classmethod
    def load_weapon_trait_names(cls,path:str):
        try:
            with open(path, "r") as f:
                jsonData = json.load(f)
                for key in cls.weaponTraitsNames.keys():
                    if key.value in jsonData.keys():
                        cls.weaponTraitsNames[key] = jsonData[key.value]
        except FileNotFoundError:
            pass
    @classmethod
    def load_armor_types_names(cls,path:str):
        try:
            with open(path, "r") as f:
                jsonData = json.load(f)
                for key in cls.armorTypesNames.keys():
                    if key.value in jsonData.keys():
                        cls.armorTypesNames[key] = jsonData[key.value]
        except FileNotFoundError:
            pass
    @classmethod
    def load_hit_localisation_names(cls,path:str):
        try:
            with open(path, "r") as f:
                jsonData = json.load(f)
                for key in cls.hitLocalisationNames.keys():
                    if key.value in jsonData.keys():
                        cls.hitLocalisationNames[key] = jsonData[key.value]
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    with open("language/pl/hitLocalisationNames.json", "w") as f:
        json.dump(ItemsTextAggregator.serialize_hit_localisation_names(), f, indent=4)
