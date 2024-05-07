class Observer:
    def update(self, subject):
        pass

class RollObserver(Observer):
    def __init__(self):
        self.lastRoll = []

    def update(self, subject):
        self.lastRoll = subject