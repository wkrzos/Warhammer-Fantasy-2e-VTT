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

    @staticmethod
    def rollD4(d:int = 1)-> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 4)+1)

        RollGod.notify(result)
        return result

    @staticmethod
    def rollD6(d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 6) + 1)
        RollGod.notify(result)
        return result

    @staticmethod
    def rollD8(d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 8) + 1)
        RollGod.notify(result)
        return result

    @staticmethod
    def rollD10(d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 10) + 1)
        RollGod.notify(result)
        return result
    @staticmethod
    def rollD12(d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 12) + 1)
        RollGod.notify(result)
        return result

    @staticmethod
    def rollD20(d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 20) + 1)
        RollGod.notify(result)
        return result

    @staticmethod
    def rollD100(d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 100) + 1)
        RollGod.notify(result)
        return result


