from typing import override
from Game import Game
import pygame
from Enums.Direction import Direction

class PlayerGame(Game):
    def __init__(self, width, height, fps=10, nbOfApples=10):
        super().__init__(width, height, fps, nbOfApples)

    @override
    def generate_action(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: return Direction.UP
        if keys[pygame.K_DOWN]: return Direction.DOWN
        if keys[pygame.K_LEFT]: return Direction.LEFT
        if keys[pygame.K_RIGHT]: return Direction.RIGHT
        return None

    @override
    def step(self, direction:Direction = None):
        ''' CHECK COLLISION '''
        if not self.snake.move(direction):
            self.reset()

        ''' EAT APPLE '''
        if self.snake.get_head_pos() in self.apples:
            # increase score & snake size
            self.score += 1
            self.snake.grow()

            # remove apple
            del self.apples[self.snake.get_head_pos()]
            # re-fill if last apple eaten
            if len(self.apples) == 0 and not self.spawn_apples():
                print("YOU WIN! WHAT A LEGEND!")
                pygame.quit()
                exit()


# Run the game
if __name__ == "__main__":
    game = PlayerGame(20, 20) # Dynamic map size
    game.run()