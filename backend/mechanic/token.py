from backend.characterCard.cards import Creature

class Token:
    def __init__(self, creature: Creature = Creature(), position: (int, int) = (0, 0)):
        self.position = position
        self.creature = creature

    def set_position(self, x, y):
        self.position = (x, y)

    def get_position(self):
        return self.position

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)
