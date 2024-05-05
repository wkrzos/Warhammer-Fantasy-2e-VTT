from backend.characterCard.cards import Creature
from backend.characterCard.equipment import Item


class Action:
    pass


class SelfAction(Action):

    def useItem(self,player:Creature,item:Item):
        pass
    def parry(self,player:Creature):
        pass
    def aiming(self,player:Creature):
        pass
    def wakeUp(self,player:Creature):
        pass
    def defenseStand(self,player:Creature):
        pass
    def useTalent(self,player:Creature):
        pass

class ActionOnAnother(Action):

    @staticmethod
    def simpleAtack(self,player:Creature,other:Creature):
        pass
    @staticmethod
    def multipleAtack(self,player:Creature,other:Creature):
        pass
    @staticmethod
    def atackAtack(self,player:Creature,other:Creature):
        pass
    @staticmethod
    def carefullAtack(self,player:Creature,other:Creature):
        pass
    @staticmethod
    def push(self,player:Creature,other:Creature):
        pass
    @staticmethod
    def feint(self,player:Creature,other:Creature):
        pass


class MoveAction(Action):
    pass


