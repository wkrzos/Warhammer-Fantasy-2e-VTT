from random import random, randrange


class RollGod:



    def rollD4(self,d:int = 1)-> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 4)+1)
        return result

    def rollD6(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 6) + 1)
        return result

    def rollD8(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 8) + 1)
        return result

    def rollD12(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 12) + 1)
        return result

    def rollD20(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 20) + 1)
        return result

    def rollD100(self, d: int = 1) -> list[int]:
        result = []
        for i in range(d):
            result.append(randrange(0, 100) + 1)
        return result
