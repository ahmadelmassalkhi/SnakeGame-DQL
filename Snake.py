import pygame
from Map import Map
from Apple import Apple


class Snake:
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # up, right, down, left

    def __init__(self, map:Map):
        self.map = map
        self.body = [(map.width//2, map.height//2)]
        self.direction = Snake.directions[1]  # Start moving to the right

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

    def update_vision(self, apple: Apple):
        """
        Update the vision grid with the current state of the map.
        0 = empty, 1 = snake body, 2 = snake head, 3 = apple.
        """
        # Init/Reset the grid
        self.vision_grid = [[0 for _ in range(self.map.width)] for _ in range(self.map.height)]

        # Mark the snake's body
        for segment in self.body[1:]:
            self.vision_grid[segment[1]][segment[0]] = 1  # Body

        # Mark the snake's head
        head = self.body[0]
        self.vision_grid[head[1]][head[0]] = 2

        # Mark the apple
        apple_pos = apple.position
        self.vision_grid[apple_pos[1]][apple_pos[0]] = 3
        
        print(self.vision_grid)