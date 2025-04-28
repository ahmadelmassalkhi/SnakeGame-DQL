from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @classmethod
    def from_index(cls, index:int):
        if index == 0:
            return cls.UP
        elif index == 1:
            return cls.DOWN
        elif index == 2:
            return cls.LEFT
        elif index == 3:
            return cls.RIGHT
        else:
            raise ValueError(f"Invalid index: {index}. Must be between 0 and 3.")