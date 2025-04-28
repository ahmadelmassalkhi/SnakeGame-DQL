import pygame
from .Map import Map
import random
from Enums.Direction import Direction

class Snake:

    def __init__(self, map:Map):
        self.map = map
        self.body = [(map.width//2, map.height//2)]
        self.direction = random.choice(list(Direction)).value

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

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
