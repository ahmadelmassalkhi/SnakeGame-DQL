import pygame
from Enums.Tile import Tile

class Map:
    def __init__(self, width, height, TILE_SIZE=20):
        self.TILE_SIZE = TILE_SIZE
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width * TILE_SIZE, self.height * TILE_SIZE))
        pygame.display.set_caption("Snake Game")
        self.grid = [[Tile.EMPTY.value for _ in range(self.width)] for _ in range(self.height)]

    def print_grid(self):
        for row in self.grid:
            print(row)
        print()
        print()

    def draw(self, color=(0, 0, 0)):
        self.screen.fill(color)
        for x in range(0, self.width * self.TILE_SIZE, self.TILE_SIZE):
            for y in range(0, self.height * self.TILE_SIZE, self.TILE_SIZE):
                rect = pygame.Rect(x, y, self.TILE_SIZE, self.TILE_SIZE)
                pygame.draw.rect(self.screen, (40, 40, 40), rect, 1)
