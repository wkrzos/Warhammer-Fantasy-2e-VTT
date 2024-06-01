from backend.json_serialisation.save_manager import SaveManager

class CharactersModel:
    def __init__(self):
        self.characters = self.load_characters()

    def load_characters(self):
        return SaveManager.loadAllCharacterCards()

    def add_character(self, character):
        self.characters.append(character)

    def get_characters(self):
        return self.characters

    def get_character_by_name(self, name):
        for creature in self.characters:
            if creature.playerName == name:
                return creature
        return None
