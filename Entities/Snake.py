import pygame
from .Map import Map
import random
from Enums.Direction import Direction
from Enums.Tile import Tile

class Snake:

    def __init__(self, map:Map):
        self.map = map
        self.body = [(map.width//2, map.height//2)]
        self.direction = random.choice(list(Direction)).value

    def move(self, direction:tuple[int, int] = None):
        if direction:
            self.direction = direction
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        tail = self.body.pop()

        # Update map grid
        self.map.grid[new_head] = Tile.SNAKE_HEAD.value # new head
        self.map.grid[head] = Tile.SNAKE_BODY.value # is now a body segment
        self.map.grid[tail] = Tile.EMPTY.value # is now empty

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        head = self.body[0]
        return (
            head[0] < 0 or head[1] < 0 or
            head[0] >= self.map.width or head[1] >= self.map.height or
            head in self.body[1:]
        )

    def draw(self):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * self.map.TILE_SIZE, segment[1] * self.map.TILE_SIZE, self.map.TILE_SIZE, self.map.TILE_SIZE)
            pygame.draw.rect(self.map.screen, (0, 255, 0), rect)
