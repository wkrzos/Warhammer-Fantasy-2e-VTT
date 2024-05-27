class CreaturesModel:
    def __init__(self):
        self.creatures = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def get_creatures(self):
        return self.creatures
