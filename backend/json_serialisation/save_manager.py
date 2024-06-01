import json
import os

from backend.json_serialisation.fabrics import *
from backend.character_sheets.sheets import *
from backend.character_sheets.equipment import *


class SaveManager:
    _DEFAULT_CARDS_LOCALISATION = os.path.normpath("saves/cards")
    _DEFAULT_CREATURES_LOCALISATION = os.path.normpath("saves/creatures")
    _DEFAULT_ITEMS_LOCALISATION = os.path.normpath("saves/items")

    @staticmethod
    def saveCharacterCard(characterCard: Card, localisation: str = _DEFAULT_CARDS_LOCALISATION, saveName: str = "default"):
        localisation = os.path.normpath(localisation)

        if not os.path.exists(localisation):
            os.makedirs(localisation)

        path = os.path.join(localisation, saveName.replace(" ", "_") + ".json")
        path = os.path.normpath(path)

        with open(path, 'w') as file:
            json.dump(characterCard.__dict__(), file, indent=4)

    @staticmethod
    def loadCharacterCard(localisation: str) -> Card | None:
        localisation = os.path.normpath(localisation)
        try:
            with open(localisation, 'r') as file:
                return CardFabric.createCard(json.load(file))
        except FileNotFoundError:
            return None

    @staticmethod
    def saveCreature(creature: Creature, localisation: str = _DEFAULT_CREATURES_LOCALISATION, saveName: str = "default") -> None:
        localisation = os.path.normpath(localisation)

        if not os.path.exists(localisation):
            os.makedirs(localisation)

        path = os.path.join(localisation, saveName + ".json")
        path = os.path.normpath(path)

        with open(path, 'w') as file:
            json.dump(creature.__dict__(), file, indent=4)

    @staticmethod
    def loadCreature(localisation: str) -> Creature | None:
        localisation = os.path.normpath(localisation)
        try:
            with open(localisation, 'r') as file:
                return CreaturesFabric.createCreature(json.load(file))
        except FileNotFoundError:
            return None

    @staticmethod
    def saveItemList(lst: list, localisation: str = _DEFAULT_ITEMS_LOCALISATION) -> None:
        localisation = os.path.normpath(localisation)

        if not os.path.exists(localisation):
            os.makedirs(localisation)

        path = os.path.join(localisation, "items.json")
        path = os.path.normpath(path)

        with open(path, 'w') as file:
            preparedToSave = [item.__dict__() for item in lst]
            json.dump(preparedToSave, file, indent=4)

    @staticmethod
    def loadItemList(localisation: str) -> list:
        localisation = os.path.normpath(localisation)
        try:
            with open(localisation, 'r') as file:
                lst = json.load(file)
                return [ItemsFabric.create(item) for item in lst]
        except FileNotFoundError:
            return None
