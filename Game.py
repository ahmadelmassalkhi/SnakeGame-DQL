import pygame
from Map import Map
from Snake import Snake
from Apple import Apple

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self, width, height, fps=5):
        # game settings
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True
        self.width, self.height = width, height

        # game objects
        self.map = Map(width, height)
        self.snake = Snake(map=self.map)
        self.apple = Apple(map=self.map)
        self.reset()

    def reset(self):
        self.score = 0
        self.map = Map(self.width, self.height)
        self.snake = Snake(map=self.map)
        self.apple = Apple(map=self.map)
        self.apple.relocate()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.snake.direction != (0, 1):
            self.snake.direction = (0, -1)
        elif keys[pygame.K_DOWN] and self.snake.direction != (0, -1):
            self.snake.direction = (0, 1)
        elif keys[pygame.K_LEFT] and self.snake.direction != (1, 0):
            self.snake.direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and self.snake.direction != (-1, 0):
            self.snake.direction = (1, 0)

    def update(self):
        self.snake.move()
        ''' CHECK COLLISION '''
        if self.snake.check_collision():
            self.reset()

        ''' EAT APPLE '''
        # this logic must be AFTER the collision check
        # or else, eating first apple results in self-collision (head in body) 
        if self.snake.body[0] == self.apple.position:
            self.score += 1
            self.snake.grow()
            self.apple.relocate()

    def draw(self):
        self.map.draw()
        self.snake.draw()
        self.apple.draw()
        self.snake.update_vision(self.apple)
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


# Run the game
if __name__ == "__main__":
    game = Game(20, 20) # Dynamic map size
    game.run()
