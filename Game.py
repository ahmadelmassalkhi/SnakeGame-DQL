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

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.snake.direction != Direction.DOWN.value:
            return Direction.UP.value
        if keys[pygame.K_DOWN] and self.snake.direction != Direction.UP.value:
            return Direction.DOWN.value
        if keys[pygame.K_LEFT] and self.snake.direction != Direction.RIGHT.value:
            return Direction.LEFT.value
        if keys[pygame.K_RIGHT] and self.snake.direction != Direction.LEFT.value:
            return Direction.RIGHT.value
        return None

    def step(self):
        self.snake.move(self.handle_input())
        
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

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.step() # update game state
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


# Run the game
if __name__ == "__main__":
    game = Game(20, 20) # Dynamic map size
    game.run()
