import json
import os

from backend.mechanics.actions.actions_type import BasicActions, DoubleActions


class ActionsTextAggregator:

    basicActionsText = {action : "" for action in BasicActions}
    doubleActionsText = {action : "" for action in DoubleActions}

    @classmethod
    def serialize_basic_actions(cls):

        return {action.value : cls.basicActionsText[action] for action in cls.basicActionsText.keys()}
    @classmethod
    def serialize_double_actions(cls):
        return {action.value : cls.doubleActionsText[action] for action in cls.doubleActionsText.keys()}

    @classmethod
    def load_basic_actions(cls, language: str):
        path = os.path.join(os.path.dirname(__file__), "language", language, "basicActionsText.json")
        try:
            with open(path, "r") as f:
                jsonData = json.load(f)
                for key in cls.basicActionsText.keys():
                    if key.value in jsonData.keys():
                        cls.basicActionsText[key] = jsonData[key.value]
        except FileNotFoundError:
            pass

    @classmethod
    def load_double_actions(cls, language: str):
        path = os.path.join(os.path.dirname(__file__), "language", language, "doubleActionsText.json")
        try:
            with open(path, "r") as f:
                jsonData = json.load(f)
                for key in cls.doubleActionsText.keys():
                    if key.value in jsonData.keys():
                        cls.doubleActionsText[key] = jsonData[key.value]
        except FileNotFoundError:
            pass
if __name__ == '__main__':
    print(ActionsTextAggregator.serialize_basic_actions())
    with open("language/pl/basicActionsText.json", "w") as f:
        json.dump(ActionsTextAggregator.serialize_basic_actions(), f, indent=4)
    with open("language/pl/doubleActionsText.json", "w") as f:
        json.dump(ActionsTextAggregator.serialize_double_actions(), f, indent=4)