from enum import Enum


class ResponseType(Enum):
    ROLL_DICE = 1
    LIST_DICE = 2

    ONE_PARAMETERS = 11
    TWO_PARAMETERS = 12
    N_PARAMETERS = 13
    