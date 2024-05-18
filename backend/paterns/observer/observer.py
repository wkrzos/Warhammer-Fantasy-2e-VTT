from backend.characterCard.equipment import HitLocalisation

class Observer:
    def update(self, subject):
        pass

class Observable:

    _observers = []
    @staticmethod
    def attach(observer):
        if observer not in Observable._observers:
            Observable._observers.append(observer)

    @staticmethod
    def detach(observer):
        try:
            Observable._observers.remove(observer)
        except ValueError:
            pass

    @staticmethod
    def notify(rolls):
        for observer in Observable._observers:
            observer.update(rolls)


class RollObserver(Observer):
    def __init__(self):
        self.lastRoll = []
        self.description = ""

    def update(self, subject):
        self.lastRoll = subject[0]
        self.description = subject[1]

class  FightObserver(Observer):
    def __init__(self):
        self.lastHitLocalisation = None
        self.lastDmgDealed = None

    def update(self, subject):
        if isinstance(subject, HitLocalisation):
            self.lastHitLocalisation = subject
        elif isinstance(subject,int):
            self.lastDmgDealed = subject