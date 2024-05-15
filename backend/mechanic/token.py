from pygame import Vector2


class Token:
    def __init__(self):
        self.posistion = Vector2(0, 0)
        self.creature = None