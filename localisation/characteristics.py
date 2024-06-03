import json
import os

from backend.character_sheets.characteristics import MainStats, SecondaryStats, AttributesType
from backend.character_sheets.races import Races
from backend.character_sheets.skills_and_talents import BasicSkills, AdvancedSkills, Talents


class CharacterTextAggregator:

    racesNames = {
        Races.HUMAN : "",
        Races.ELF : "",
        Races.DWARF : "",
        Races.HALFLING : ""
    }


    statsNames = {
        MainStats.WEAPON_SKILL : "",
        MainStats.BALLISTIC_SKILL : "",
        MainStats.STRENGTH : "",
        MainStats.TOUGHNESS : "",
        MainStats.AGILITY : "",
        MainStats.INTELLIGENCE : "",
        MainStats.WILL_POWER : "",
        MainStats.FELLOWSHIP : "",
        SecondaryStats.ATTACKS : "",
        SecondaryStats.WOUNDS : "",
        SecondaryStats.STRENGTH_BONUS : "",
        SecondaryStats.TOUGHNESS_BONUS : "",
        SecondaryStats.MOVEMENT :"",
        SecondaryStats.MAGIC : "",
        SecondaryStats.INSANITY_POINTS : "",
        SecondaryStats.FATE_POINTS : ""

    }

    attributesNames = {
        AttributesType.ACTIONS_REMAIN : "",
        AttributesType.IS_AIMING : "",
        AttributesType.IS_PARING : "",
        AttributesType.IS_IN_DEFENCE : "",
        AttributesType.ALREADY_DODGED : "",
        AttributesType.IS_LYING : "",
        AttributesType.FURIOUS : "",
        AttributesType.UNCONSCIOUS : "",
        AttributesType.DEAD : ""
    }

    skillsNames = {
        BasicSkills.ANIMAL_CARE: "",
        BasicSkills.CHARM: "",
        BasicSkills.COMMAND: "",
        BasicSkills.CONCEALMENT: "",
        BasicSkills.CONSUME_ALCOHOL: "",
        BasicSkills.DISGUISE: "",
        BasicSkills.DRIVE: "",
        BasicSkills.EVALUATE: "",
        BasicSkills.GAMBLE: "",
        BasicSkills.GOSSIP: "",
        BasicSkills.HAGGLE: "",
        BasicSkills.INTIMIDATE: "",
        BasicSkills.OUTDOOR_SURVIVAL: "",
        BasicSkills.PERCEPTION: "",
        BasicSkills.RIDE: "",
        BasicSkills.ROW: "",
        BasicSkills.SCALE_SHEER_SURFACE: "",
        BasicSkills.SEARCH: "",
        BasicSkills.SILENT_MOVE: "",
        BasicSkills.SWIM: "",
        AdvancedSkills.ACADEMIC_KNOWLEDGE: "",  # Need to Add Specialization
        AdvancedSkills.ANIMAL_TRAINING: "",
        AdvancedSkills.BLATHER: "",
        AdvancedSkills.CHANNELING: "",
        AdvancedSkills.CHARM_ANIMAL: "",
        AdvancedSkills.COMMON_KNOWLEDGE: "",
        AdvancedSkills.DODGE_BLOW: "",
        AdvancedSkills.FOLLOW_TRAIL: "",
        AdvancedSkills.HEAL: "",
        AdvancedSkills.HYPNOTISM: "",
        AdvancedSkills.LIP_READING: "",
        AdvancedSkills.MAGICAL_SENSE: "",
        AdvancedSkills.NAVIGATION: "",
        AdvancedSkills.PERFORMER: "",
        AdvancedSkills.PICK_LOCK: "",
        AdvancedSkills.PREPARE_POISON: "",
        AdvancedSkills.READ_AND_WRITE: "",
        AdvancedSkills.SAIL: "",
        AdvancedSkills.SECRET_LANGUAGE: "",  # Need to Add Specialization
        AdvancedSkills.SECRET_SIGNS: "",  # Need to Add Specialization
        AdvancedSkills.SET_TRAP: "",
        AdvancedSkills.SHADOWING: "",
        AdvancedSkills.SLEIGHT_OF_HAND: "",
        AdvancedSkills.SPEAK_LANGUAGE: "",  # Need to Add Specialization
        AdvancedSkills.TORTURE: "",
        AdvancedSkills.TRADE: "",  # Need to Add Specialization
        AdvancedSkills.VENTRILOQUISM: ""
    }


    talentsName = {talent: "" for talent in Talents}

    @classmethod
    def serialize_races_names(cls):
        return {race.value: cls.racesNames[race] for race in Races}
    @classmethod
    def serialize_stats_names(cls):
        return {stat.value: cls.statsNames[stat] for stat in cls.statsNames.keys()}

    @classmethod
    def serialize_attributes_names(cls):
        return  {attribute.value : cls.attributesNames[attribute] for attribute in AttributesType}

    @classmethod
    def serialize_skills_names(cls):
        return {skill.value: cls.skillsNames[skill] for skill in cls.skillsNames.keys()}

    @classmethod
    def serialize_talents_name(cls):
        return {talent.value: cls.talentsName[talent] for talent in cls.talentsName.keys()}

    @classmethod
    def load_races_names(cls,language:str):
        path = os.path.join(os.path.dirname(__file__), "language", language, "racesNames.json")
        try:
            with open(path, "r",encoding='utf-8') as f:
                jsonData = json.load(f)
                for key in cls.racesNames.keys():
                    if key.value in jsonData.keys():
                        cls.racesNames[key] = jsonData[key.value]
        except FileNotFoundError:
            pass

    @classmethod
    def load_stats_names(cls, language: str):
        path = os.path.join(os.path.dirname(__file__), "language", language, "statsNames.json")
        try:
            with open(path, "r",encoding='utf-8') as f:
                jsonData = json.load(f)
                for key in cls.statsNames.keys():
                    if key.value in jsonData.keys():
                        cls.statsNames[key] = jsonData[key.value]
        except FileNotFoundError:
            pass

    @classmethod
    def load_attributes_names(cls, language: str):
        path = os.path.join(os.path.dirname(__file__), "language", language, "statsNames.json")

        try:
            with open(path, "r",encoding='utf-8') as f:
                jsonData = json.load(f)
                for key in cls.attributesNames.keys():
                    if key.value in jsonData.keys():
                        cls.attributesNames[key] = jsonData[key.value]
        except FileNotFoundError:
            pass

    @classmethod
    def load_skills_names(cls, language: str):
        path = os.path.join(os.path.dirname(__file__), "language", language, "statsNames.json")

        try:
            with open(path, "r",encoding='utf-8') as f:
                jsonData = json.load(f)
                for key in cls.skillsNames.keys():
                    if key.value in jsonData.keys():
                        cls.skillsNames[key] = jsonData[key.value]
        except FileNotFoundError:
            pass

    @classmethod
    def load_talents_names(cls, language: str):
        path = os.path.join(os.path.dirname(__file__), "language", language, "talentsNames.json")

        try:
            with open(path, "r",encoding='utf-8') as f:
                jsonData = json.load(f)
                for key in cls.talentsName.keys():
                    if key.value in jsonData.keys():
                        cls.talentsName[key] = jsonData[key.value]
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    with open("language/pl/statsNames.json", "w") as f:
        json.dump(CharacterTextAggregator.serialize_stats_names(), f, indent=4)