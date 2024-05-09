from enum import Enum
from characteristics import MainStats

class Skills(Enum):
    pass

class AdvancedSkills(Skills):
    ACADEMIC_KNOWLEDGE = "as.1.0", #Need to Add Specialization
    ANIMAL_TRAINING = "as.2",
    BLATHER = "as.3",
    CHANNELING = "as.4",
    CHARM_ANIMAL = "as.5",
    COMMON_KNOWLEDGE = "as.6.0", #Need to Add Specialization
    DODGE_BLOW = "as.7",
    FOLLOW_TRAIL = "as.8",
    HEAL = "as.9",
    HYPNOTISM = "as.10",
    LIP_READING = "as.11",
    MAGICAL_SENSE = "as.12",
    NAVIGATION = "as.13",
    PERFORMER = "as.14.0",  #Need to Add Specialization
    PICK_LOCK = "as.15",
    PREPARE_POISON = "as.16",
    READ_AND_WRITE = "as.17",
    SAIL = "as.18",
    SECRET_LANGUAGE  = "as.19.0", #Need to Add Specialization
    SECRET_SIGNS = "as.20.0", #Need to Add Specialization
    SET_TRAP = "as.21",
    SHADOWING = "as.22",
    SLEIGHT_OF_HAND = "as.23",
    SPEAK_LANGUAGE = "as.24.0",  #Need to Add Specialization
    TORTURE = "as.25",
    TRADE = "as.26.0",  #Need to Add Specialization
    VENTRILOQUISM = "as.27"
class BasicSkills(Skills):
    ANIMAL_CARE = "bs.1",
    CHARM = "bs.2",
    COMMAND = "bs.3",
    CONCEALMENT = "bs.4"
    CONSUME_ALCOHOL = "bs.5"
    DISGUISE = "bs.6"
    DRIVE = "bs.7"
    EVALUATE = "bs.8"
    GAMBLE = "bs.9"
    GOSSIP = "bs.10"
    HAGGLE = "bs.11"
    INTIMIDATE = "bs.12"
    OUTDOOR_SURVIVAL = "bs.13"
    PERCEPTION = "bs.14"
    RIDE = "bs.15"
    ROW = "bs.16"
    SCALE_SHEER_SURFACE = "bs.17"
    SEARCH = "bs.18"
    SILENT_MOVE = "bs.19"
    SWIM = "bs.20"


class Talents(Enum):
    ACURATE_HEARING = "t.1",
    AETHYRIC_ATTUNEMENT = "t.2",
    ALLEY_CAT = "t.3",
    AMBIDEXTROUS = "t.4",
    ARCANE_LORE = "t.5",
    ARMOURED_CASTING = "t.6",
    ARTISTIC = "t.7",
    CONTORTIONIST = "t.8",
    COOLHEADED = "t.9",
    DARK_LORE = "t.10",
    DARK_MAGIC = "t.11",
    DEALMAKER = "t.12",
    DISARM = "t.13",
    DIVINE_LORE = "t.14",
    DWARFCRAFT = "t.15",
    ETIQUETTE = "t.16",
    EXCELLENT_VISION = "t.17",
    FAST_HANDS = "t.18",
    FEARLESS = "t.19",
    FLEE = "t.20",
    FLEET_FOOTED = "t.21",
    FLIER = "t.22",
    FRENZY = "t.23",
    FRIGHTENING = "t.24",
    GRUDGE_BORN_FURY = "t.25",
    HARDY = "t.26",
    HEDGE_MAGIC = "t.27",
    HOVERER = "t.28",
    KEEN_SENSES = "t.29",
    LESSER_MAGIC = "t.30",
    LIGHTNING_PARRY = "t.31",
    LIGHTNING_REFLEXES = "t.32",
    LINGUISTICS = "t.33",
    LUCK = "t.34",
    MARKSMAN = "t.35",
    MASTER_GUNNER = "t.36",
    MASTER_ORATOR = "t.37",
    MEDITATION = "t.38",
    MENACING = "t.39",
    MIGHTY_MISSILE = "t.40",
    MIGHTY_SHOT = "t.41",
    MIMIC = "t.42",
    NATURAL_WEAPONS = "t.43",
    NIGHT_VISION = "t.44",
    ORIENTATION = "t.45",
    PETTY_MAGIC = "t.46",
    PUBLIC_SPEAKING = "t.47",
    QUICK_DRAW = "t.48",
    RAPID_RELOAD = "t.49",
    RESISTANCE_TO_CHAOS = "t.50",
    RESISTANCE_TO_DISEASE = "t.51",
    RESISTANCE_TO_MAGIC = "t.52",
    RESISTANCE_TO_POISON = "t.53",
    ROVER = "t.54",
    SAVVY = "t.55",
    SCHEMER = "t.56",
    SEASONED_TRAVELLER = "t.57",
    SHARPSHOOTER = "t.58",
    SIXTH_SENSE = "t.59",
    SPECIALIST_WEAPON = "t.60",
    GROUP = "t.61.0", #Need to Add Specialization
    STOUT_HEARTED = "t.62",
    STREET_FIGHTING = "t.63",
    STREERWISE = "t.64",
    STRIKE_MIGHTY_BLOW = "t.65",
    STRIKE_TO_INJURE = "t.66",
    STRIKE_TO_STUN = "t.67",
    STRONG_MINDED = "t.68",
    STURDY = "t.69",
    SUAVE = "t.70",
    SURE_SHOT = "t.71",
    SURGERY = "t.72",
    SUPER_NUMERATE = "t.73",
    SWASHBUCKLER = "t.74",
    TERRIFYING = "t.75",
    TRAPFINDER = "t.76",
    TRICK_RIDING = "t.77",
    TUNNEL_RAT = "t.78",
    UNDEAD = "t.79",
    UNSETTLING = "t.80",
    VERY_RESILIENT = "t.81",
    VERY_STRONG = "t.82",
    WARRIOR_BORN = "t.83",
    WRESTLING = "t.84"


skilsDependency = {
    BasicSkills.ANIMAL_CARE : MainStats.INTELLIGENCE,
    BasicSkills.CHARM : MainStats.FELLOWSHIP,
    BasicSkills.COMMAND : MainStats.FELLOWSHIP,
    BasicSkills.CONCEALMENT : MainStats.AGILITY,
    BasicSkills.CONSUME_ALCOHOL : MainStats.TOUGHNESS,
    BasicSkills.DISGUISE : MainStats.FELLOWSHIP,
    BasicSkills.DRIVE : MainStats.STRENGTH,
    BasicSkills.EVALUATE : MainStats.INTELLIGENCE,
    BasicSkills.GAMBLE : MainStats.INTELLIGENCE,
    BasicSkills.GOSSIP : MainStats.FELLOWSHIP,
    BasicSkills.HAGGLE : MainStats.FELLOWSHIP,
    BasicSkills.INTIMIDATE : MainStats.STRENGTH,
    BasicSkills.OUTDOOR_SURVIVAL : MainStats.INTELLIGENCE,
    BasicSkills.PERCEPTION : MainStats.INTELLIGENCE,
    BasicSkills.RIDE : MainStats.AGILITY,
    BasicSkills.ROW : MainStats.STRENGTH,
    BasicSkills.SCALE_SHEER_SURFACE : MainStats.STRENGTH,
    BasicSkills.SEARCH : MainStats.INTELLIGENCE,
    BasicSkills.SILENT_MOVE : MainStats.AGILITY,
    BasicSkills.SWIM : MainStats.STRENGTH,
    AdvancedSkills.ACADEMIC_KNOWLEDGE : MainStats.INTELLIGENCE,  # Need to Add Specialization
    AdvancedSkills.ANIMAL_TRAINING : MainStats.FELLOWSHIP,
    AdvancedSkills.BLATHER : MainStats.FELLOWSHIP,
    AdvancedSkills.CHANNELING : MainStats.WILL_POWER,
    AdvancedSkills.CHARM_ANIMAL : MainStats.AGILITY,
    AdvancedSkills.COMMON_KNOWLEDGE : MainStats.INTELLIGENCE,
    AdvancedSkills.DODGE_BLOW : MainStats.AGILITY,
    AdvancedSkills.FOLLOW_TRAIL : MainStats.INTELLIGENCE,
    AdvancedSkills.HEAL : MainStats.INTELLIGENCE,
    AdvancedSkills.HYPNOTISM : MainStats.WILL_POWER,
    AdvancedSkills.LIP_READING : MainStats.INTELLIGENCE,
    AdvancedSkills.MAGICAL_SENSE : MainStats.WILL_POWER,
    AdvancedSkills.NAVIGATION : MainStats.INTELLIGENCE,
    AdvancedSkills.PERFORMER : MainStats.FELLOWSHIP,
    AdvancedSkills.PICK_LOCK : MainStats.AGILITY,
    AdvancedSkills.PREPARE_POISON : MainStats.INTELLIGENCE,
    AdvancedSkills.READ_AND_WRITE : MainStats.INTELLIGENCE,
    AdvancedSkills.SAIL : MainStats.AGILITY,
    AdvancedSkills.SECRET_LANGUAGE : MainStats.INTELLIGENCE,  # Need to Add Specialization
    AdvancedSkills.SECRET_SIGNS : MainStats.INTELLIGENCE,  # Need to Add Specialization
    AdvancedSkills.SET_TRAP : MainStats.AGILITY,
    AdvancedSkills.SHADOWING : MainStats.AGILITY,
    AdvancedSkills.SLEIGHT_OF_HAND : MainStats.AGILITY,
    AdvancedSkills.SPEAK_LANGUAGE : MainStats.INTELLIGENCE,  # Need to Add Specialization
    AdvancedSkills.TORTURE : MainStats.FELLOWSHIP,
    AdvancedSkills.TRADE : MainStats.FELLOWSHIP,  # Need to Add Specialization
    AdvancedSkills.VENTRILOQUISM : MainStats.FELLOWSHIP
}