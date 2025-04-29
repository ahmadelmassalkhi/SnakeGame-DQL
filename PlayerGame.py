from typing import override
from Game import Game
import pygame
from Enums.Direction import Direction

class PlayerGame(Game):
    def __init__(self, width, height, fps=10):
        super().__init__(width, height, fps)

    @override
    def generate_action(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.snake.direction != Direction.DOWN.value:
            return Direction.UP
        if keys[pygame.K_DOWN] and self.snake.direction != Direction.UP.value:
            return Direction.DOWN
        if keys[pygame.K_LEFT] and self.snake.direction != Direction.RIGHT.value:
            return Direction.LEFT
        if keys[pygame.K_RIGHT] and self.snake.direction != Direction.LEFT.value:
            return Direction.RIGHT
        return None

    @override
    def step(self, direction:Direction = None):
        ''' CHECK COLLISION '''
        if not self.snake.move(direction):
            self.reset()

        ''' EAT APPLE '''
        if self.snake.get_head_pos() == self.apple.get_pos():
            self.score += 1
            self.snake.grow()
            self.apple.relocate()



# Run the game
if __name__ == "__main__":
    game = PlayerGame(20, 20) # Dynamic map size
    game.run()