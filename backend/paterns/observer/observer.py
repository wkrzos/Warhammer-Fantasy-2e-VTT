from backend.characterCard.equipment import HitLocalisation

class Observer:
    def reactForNotify(self, subject):
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
    def notify(signal):
        for observer in Observable._observers:
            observer.reactForNotify(signal)


class RollObserver(Observer):
    def __init__(self):
        self.lastRoll = []

    def reactForNotify(self, subject):
        self.lastRoll = subject

class  FightObserver(Observer):
    def __init__(self):
        self.lastHitLocalisation = None
        self.lastDmgDealed = None

    def reactForNotify(self, subject):
        if isinstance(subject, HitLocalisation):
            self.lastHitLocalisation = subject
        elif isinstance(subject,int):
            self.lastDmgDealed = subject