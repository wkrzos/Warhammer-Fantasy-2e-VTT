from backend.character_sheets.characteristics import AttributesType
from backend.mechanics import token


class FightManager:
    def __init__(self,involvedCreatures:list = []):
        self.involvedCreatures = involvedCreatures
        self.tourCounter = 0
        self._currentIndex = 0
        self.currentCreature:token = None


    def start(self):
        self.tourCounter = 1
        self.involvedCreatures.sort(key=lambda x: x.initiative)
        self.currentCreature = self.involvedCreatures[self._currentIndex]
        self.currentCreature.creature.attributes.restartAttributes()

    def nextCreature(self):

        self._currentIndex = self._currentIndex + 1
        while AttributesType.DEAD in  self.involvedCreatures[self._currentIndex].token.attributes:
            self.involvedCreatures.remove(self.involvedCreatures[self._currentIndex])
            if self._currentIndex >= len(self.involvedCreatures):
                self._currentIndex = 0
                self.tourCounter += 1
        if self._currentIndex >= len(self.involvedCreatures):
            self._currentIndex = 0
            self.tourCounter += 1

        self.currentCreature = self.involvedCreatures[self._currentIndex]
        self.currentCreature.creature.attributes.restartAttributes()
        if AttributesType.UNCONSCIOUS in self.currentCreature.creature.attributes:
            self.currentCreature.creature.attributes.actionsRemain = 0

