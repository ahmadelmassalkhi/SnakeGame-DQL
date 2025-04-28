import pygame
import random
from .Map import Map


class Apple:
    def __init__(self, map:Map):
        self.map = map
        self.relocate()

    def relocate(self):
        self.position = (random.randint(0, self.map.width - 1), random.randint(0, self.map.height - 1))

    def draw(self):
        rect = pygame.Rect(self.position[0] * self.map.TILE_SIZE, self.position[1] * self.map.TILE_SIZE, self.map.TILE_SIZE, self.map.TILE_SIZE)
        pygame.draw.rect(self.map.screen, (255, 0, 0), rect)
