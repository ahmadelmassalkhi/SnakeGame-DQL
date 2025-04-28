from enum import IntEnum

class Tile(IntEnum):
    EMPTY = 0
    SNAKE_BODY = 1
    SNAKE_HEAD = 2
    APPLE = 3