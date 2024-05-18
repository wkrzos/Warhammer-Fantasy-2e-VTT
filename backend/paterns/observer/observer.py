from backend.characterCard.equipment import HitLocalisation

class Observer:
    def update(self, subject):
        pass

class Observable:

    _observers = []
    @classmethod
    def attach(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def detach(cls,observer):
        try:
            cls._observers.remove(observer)
        except ValueError:
            pass

    @classmethod
    def notify(cls,rolls):
        for observer in cls._observers:
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