from backend.json_serialisation.save_manager import SaveManager

class CreaturesModel:
    def __init__(self):
        self.creatures = self.load_creatures()

    def load_creatures(self):
        return SaveManager.loadAllCharacterCards()

    def add_creature(self, creature):
        self.creatures.append(creature)

    def get_creatures(self):
        return self.creatures

    def get_creature_by_name(self, name):
        for creature in self.creatures:
            if creature.playerName == name:
                return creature
        return None
