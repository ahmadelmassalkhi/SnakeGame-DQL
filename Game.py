from abc import abstractmethod
import pygame
from Entities.Map import Map
from Entities.Snake import Snake
from Entities.Apple import Apple
from Enums.Direction import Direction

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self, width, height, fps=10, nbOfApples=1):
        # game settings
        self.fps = fps
        self.width, self.height = width, height
        self.clock = pygame.time.Clock()
        self.running = True

        # game entities
        self.apples = {}
        self.nbOfApples = nbOfApples
        self.reset()

    def spawn_apples(self):
        """
            Respawns apples on the map.
            Returns True if at least one apple was spawned.
            Else False
        """
        # respawn apples
        self.apples = {} # reset
        for i in range(self.nbOfApples):
            # create apple
            apple = Apple(map=self.map)
            if not apple.relocate():
                if i==0: return False
                break
            # store apple
            self.apples[apple.get_pos()] = apple
        return True
    
    def reset(self):
        self.score = 0
        self.map = Map(self.width, self.height)
        self.snake = Snake(map=self.map)
        self.spawn_apples()

    def draw(self):
        self.map.draw()
        self.snake.draw()
        for apple in self.apples.values(): apple.draw()
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


