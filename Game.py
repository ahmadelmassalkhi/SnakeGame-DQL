import pygame
from Map import Map
from Snake import Snake
from Apple import Apple

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self, width, height, fps=10):
        # game settings
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True

        # game objects
        self.map = Map(width, height)
        self.snake = Snake(map=self.map)
        self.apple = Apple(map=self.map)


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
        if self.snake.body[0] == self.apple.position:
            self.snake.grow()
            self.apple.relocate()
        if self.snake.check_collision():
            self.running = False

    def draw(self):
        self.map.screen.fill((0, 0, 0))
        self.map.draw()
        self.snake.draw()
        self.apple.draw()
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