from random import random, randrange

from backend.paterns.observer.observer import Observable


class RollGod(Observable): #Przetestować czy to cos działa XDD


    # _instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls, *args, **kwargs)
    #     return cls._instance

 #   def __init__(self):
    _observers = []
    @classmethod
    def rollD4(cls,d:int = 1, dsc:str = "" )-> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 4)+1)

        cls.notify((result,dsc))
        return result

    @classmethod
    def rollD6(cls,d: int = 1,dsc:str = "") -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 6) + 1)
        cls.notify((result,dsc))
        return result

    @classmethod
    def rollD8(cls,d: int = 1,dsc:str = "") -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 8) + 1)
        cls.notify((result,dsc))
        return result

    @classmethod
    def rollD10(cls,d: int = 1,dsc:str = "") -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 10) + 1)
        cls.notify((result,dsc))
        return result
    @classmethod
    def rollD12(cls,d: int = 1,dsc:str = "") -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 12) + 1)
        cls.notify((result,dsc))
        return result

    @classmethod
    def rollD20(cls,d: int = 1,dsc:str = "") -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 20) + 1)
        cls.notify((result,dsc))
        return result

    @classmethod
    def rollD100(cls,d: int = 1,dsc:str = "") -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 100) + 1)
        print(cls._observers)
        cls.notify((result,dsc))
        return result

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

