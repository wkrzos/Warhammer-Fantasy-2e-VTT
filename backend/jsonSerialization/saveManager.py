import json
import os

from backend.jsonSerialization.fabrics import *
from backend.characterCard.cards import *
from backend.characterCard.equipment import *



class SaveManager:
    _DEFAULT_CARDS_LOCALISATION = r"../../saves/cards"
    _DEFAULT_CREATURES_LOCALISATION = r"../../saves/creatures"
    _DEFAULT_ITEMS_LOCALISATION = r"../../saves/items"
    @staticmethod
    def saveCharacterCard(characterCard :Card, localisation:str=_DEFAULT_CARDS_LOCALISATION, saveName:str = "default"):
        if not os.path.exists(localisation):
            os.makedirs(localisation)
        path = os.path.join(localisation,saveName+".json" )
        with open(path, 'w') as file:
            json.dump(characterCard.__dict__(), file)
            file.close()

    @staticmethod
    def loadCharacterCard(localisation:str)->Card:
        try:
            with open(localisation, 'r') as file:
                return  CardFabric.createCard(json.load(file))
        except FileNotFoundError:
            return None

    @staticmethod
    def saveCreature(creature :Creature, localisation:str=_DEFAULT_CREATURES_LOCALISATION, saveName:str = "default") -> None:
        if not os.path.exists(localisation):
            os.makedirs(localisation)
        path = os.path.join(localisation,saveName+".json" )
        with open(path, 'w') as file:
            json.dump(creature.__dict__(), file)
            file.close()

    @staticmethod
    def loadCreature(localisation) -> Creature:
        try:
            with open(localisation, 'r') as file:
                return CreaturesFabric.createCreature(json.load(file))
        except FileNotFoundError:
            return None

    @staticmethod
    def saveItemList(lst:list, localisation:str= _DEFAULT_ITEMS_LOCALISATION) -> None:
        if not os.path.exists(localisation):
            os.makedirs(localisation)
        path = os.path.join(localisation, "items.json")
        with open(path, 'w') as file:
            preparedToSave = []
            for item in lst:
                preparedToSave.append(item.__dict__())
            json.dump(preparedToSave, file)
            file.close()

    @staticmethod
    def loadItemList(localisation) -> list:
        try:
            with open(localisation, 'r') as file:
                lst = json.load(file)
                result = []
                for item in lst:
                    result.append(ItemsFabric.create(item))

                return result
        except FileNotFoundError:
            return None
