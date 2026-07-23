from enum import Enum


class GameState(Enum):

    WAIT_FOR_NEW_LEVEL = 1

    POSITION_CART = 2

    AIMING = 3

    THROWING = 4

    CATCHING = 5

    GAME_OVER = 6

    PAUSED = 7