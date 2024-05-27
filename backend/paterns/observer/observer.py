from backend.character_sheets.equipment import HitLocalisation

class Observer:
    def reactForNotify(self, subject):
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
    def notify(cls, signal):
        for observer in cls._observers:
            observer.reactForNotify(signal)



class RollObserver(Observer):
    def __init__(self):
        self.lastRoll = []
        self.description = ""


    def reactForNotify(self, subject):
        self.lastRoll = subject[0]
        self.description = subject[1]


class  FightObserver(Observer):
    def __init__(self):
        self.lastHitLocalisation = None
        self.lastDmgDealed = None

    def reactForNotify(self, subject):
        if isinstance(subject, HitLocalisation):
            self.lastHitLocalisation = subject
        elif isinstance(subject,int):
            self.lastDmgDealed = subject