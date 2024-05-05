from random import random, randrange


class RollGod: #Przetestować czy to cos działa XDD

    _observers = []
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

 #   def __init__(self):

    @staticmethod
    def rollD4(self,d:int = 1)-> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 4)+1)

        self.notify(result)
        return result

    @staticmethod
    def rollD6(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 6) + 1)
        self.notify(result)
        return result

    @staticmethod
    def rollD8(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 8) + 1)
        self.notify(result)
        return result

    @staticmethod
    def rollD12(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 12) + 1)
        self.notify(result)
        return result

    @staticmethod
    def rollD20(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 20) + 1)
        self.notify(result)
        return result

    @staticmethod
    def rollD100(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 100) + 1)
        self.notify(result)
        return result

    @staticmethod
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    @staticmethod
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    @staticmethod
    def notify(self, rolls):
        for observer in self._observers:
            observer.update(rolls)

