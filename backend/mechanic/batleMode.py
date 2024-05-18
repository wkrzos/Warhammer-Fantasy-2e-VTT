

class FightManager:
    def __init__(self,involvedCreatures:list = []):
        self.involvedCreatures = involvedCreatures
        self.tourCounter = 0
        self._currentIndex = 0
        self.currentCreature = None


    def start(self):
        self.tourCounter = 1
        self.involvedCreatures.sort(key=lambda x: x.initiative)
        self.currentCreature = self.involvedCreatures[self._currentIndex]
        self.currentCreature.attributes.restartAttributes()

    def nextCreature(self):
        self._currentIndex = self._currentIndex + 1
        if self._currentIndex >= len(self.involvedCreatures):
            self._currentIndex = 0
            self.tourCounter += 1

        self.currentCreature = self.involvedCreatures[self._currentIndex]
        self.currentCreature.attributes.restartAttributes()

