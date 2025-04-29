from abc import abstractmethod
import pygame
from Entities.Map import Map
from Entities.Snake import Snake
from Entities.Apple import Apple
from Enums.Direction import Direction

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self, width, height, fps=10):
        # game settings
        self.fps = fps
        self.width, self.height = width, height
        self.clock = pygame.time.Clock()
        self.running = True
        self.reset()

    def reset(self):
        self.score = 0
        self.map = Map(self.width, self.height)
        self.snake = Snake(map=self.map)
        self.apple = Apple(map=self.map)
        self.apple.relocate()

    def draw(self):
        self.map.draw()
        self.snake.draw()
        self.apple.draw()
        pygame.display.flip()

    @abstractmethod
    def generate_action(self):
        pass

    @abstractmethod
    def step(self, direction:Direction = None):
        pass

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.step(self.generate_action()) # update game state
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


