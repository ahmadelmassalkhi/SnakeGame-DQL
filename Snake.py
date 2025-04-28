import pygame
from Map import Map
import random

class Snake:
    DIRECTIONS = {
            'UP': (0, -1),
            'DOWN': (0, 1),
            'LEFT': (-1, 0),
            'RIGHT': (1, 0)
        }

    def __init__(self, map:Map):
        self.map = map
        self.body = [(map.width//2, map.height//2)]
        self.direction = random.choice(list(Snake.DIRECTIONS.values()))  # Start moving in a random direction
        self.vision_grid = [[0 for _ in range(self.map.width)] for _ in range(self.map.height)]

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
