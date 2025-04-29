import pygame
import random
from Entities.Map import Map
from Enums.Tile import Tile

class Apple:
    def __init__(self, map:Map):
        self.map = map
        self.relocate()

    def relocate(self):
        '''
            Relocates the apple to a random empty tile on the map.
        '''
        # Ensure the apple does not spawn on the snake
        empty_tiles = [tile for tile in self.map.grid if self.map.grid[tile] == Tile.EMPTY.value]
        if not empty_tiles:
            return False  # No empty tiles available
        
        # Randomly select an empty tile
        self.position = random.choice(empty_tiles) 
        # Mark the tile as occupied by an apple
        self.map.grid[self.position] = Tile.APPLE.value

        # Found and Occupied an empty tile
        return True
    
    def get_pos(self):
        """ returns tuple (x,y) coordinates of the apple """
        return self.position

    def draw(self):
        rect = pygame.Rect(self.position[0] * self.map.TILE_SIZE, self.position[1] * self.map.TILE_SIZE, self.map.TILE_SIZE, self.map.TILE_SIZE)
        pygame.draw.rect(self.map.screen, (255, 0, 0), rect)
