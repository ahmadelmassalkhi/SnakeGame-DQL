import pygame
from .Map import Map
import random
from Enums.Direction import Direction
from Enums.Tile import Tile

class Snake:

    def __init__(self, map:Map):
        self.map = map
        self.body = [(map.width//2, map.height//2)]
        self.direction = random.choice(list(Direction))
        self.map.grid[self.body[0][1]][self.body[0][0]] = Tile.SNAKE_HEAD.value

    def move(self, direction:Direction = None):
        # Change direction if a new one is provided
        if direction and direction != Direction.opposite(self.direction):
            self.direction = direction

        # Move one square in the current direction
        head = self.body[0]
        new_head = (head[0] + self.direction.value[0], head[1] + self.direction.value[1])
        self.body.insert(0, new_head)
        tail = self.body.pop()

        # Check if the move was valid
        if self.check_collision():
            return False

        # Update map grid
        self.map.grid[new_head[1]][new_head[0]] = Tile.SNAKE_HEAD.value # new head
        self.map.grid[head[1]][head[0]] = Tile.SNAKE_BODY.value # is now a body segment
        self.map.grid[tail[1]][tail[0]] = Tile.EMPTY.value # is now empty
        return True
    
    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        head = self.body[0]
        return (
            head[0] < 0 or head[1] < 0 or
            head[0] >= self.map.width or head[1] >= self.map.height or
            head in self.body[1:]
        )
    
    def get_head_pos(self):
        """ returns tuple of (x,y) coordinates of the snake's head """
        return self.body[0]

    def draw(self):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * self.map.TILE_SIZE, segment[1] * self.map.TILE_SIZE, self.map.TILE_SIZE, self.map.TILE_SIZE)
            pygame.draw.rect(self.map.screen, (0, 255, 0), rect)
