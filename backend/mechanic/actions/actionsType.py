from enum import Enum



class ActionTypes(Enum):
    pass

class BasicActions(ActionTypes):
    MOVE = "ba.1",
    USE_ITEM = "ba.2",
    AIMING = "ba.3",
    SIMPLE_ATACK = "ba.4",
    FEINT = "ba.5",
    PUSH = "ba.6",
    PARRY = "ba.7",
    WAKE_UP = "ba.8",



class DoubleActions(ActionTypes):
    MULTIPLE_ATACK = "da.1",
    RETREAT = "da.2",
    RUN = "da.3",
    CAREFULL_ATACK = "da.4",
    DEFENSE_STAND = "da.5",
    JUMP = "da.6",


class SpeciallActions(ActionTypes):
    USE_TALENT = "sa.1"
    THROW_SPEEL = "sa.2"
    RELOAD = "sa.3"