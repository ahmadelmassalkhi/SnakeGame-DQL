import time
import pygame
import numpy as np
import gymnasium as gym
from gymnasium import spaces
from Game import Game
from Enums.Direction import Direction


from enum import Enum
class Rewards(Enum):
    DEATH = -20.0              # harsher penalty for dying
    EAT_APPLE = 5.0            # increased reward for eating an apple
    GAME_WIN = 100.0           # higher reward for winning the game
    MOVE_TOWARD_APPLE = 0.1    # stronger guidance towards apples
    STEP_PENALTY = -0.005      # reduced penalty for taking steps



class SnakeEnv(gym.Env, Game):
    def __init__(self, width=20, height=20, fps=10, nbOfApples=30, render_mode=None):
        gym.Env.__init__(self)
        Game.__init__(self, width=width, height=height, fps=fps, nbOfApples=nbOfApples)
        self.action_space = spaces.Discrete(4) # up left down right, do nothing
        self.observation_space = spaces.Box(low=0, high=3, shape=(self.height, self.width), dtype=np.uint8)
        self.render_mode = render_mode


    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        Game.reset(self)
        return self._get_obs(), {}
    

    def step(self, action: int):
        if self.render_mode == "human":
            self.render()
            time.sleep(1/self.fps)
            
        """ INVALID MOVE: COLLISION """
        old_distance = self._get_distance_to_closest_apple()
        if not self.snake.move(Direction.from_index(action)):
            print("DEATH BY COLLISION")
            return self._get_obs(), Rewards.DEATH.value, True, False, {}
        new_distance = self._get_distance_to_closest_apple()

        # distance-based rewarding
        done, reward = False, 0
        if new_distance < old_distance:
            reward += Rewards.MOVE_TOWARD_APPLE.value # closer to apple(s)
        else:
            reward -= Rewards.MOVE_TOWARD_APPLE.value # farther to apple(s)

        """ APPLE COLLISION """
        if self.snake.get_head_pos() in self.apples:
            self.score += 1
            self.snake.grow()

            # remove apple
            del self.apples[self.snake.get_head_pos()]
            # re-fill if last apple eaten
            if len(self.apples) == 0 and not self.spawn_apples():
                # no more space => player wins
                done, reward = True, Rewards.GAME_WIN.value
                print("SNAKE WINS")
            else:
                # apple eaten
                reward += Rewards.EAT_APPLE.value
        else:
            # moved into empty tile
            reward -= Rewards.STEP_PENALTY.value # discourage doing nothing

        return self._get_obs(), reward, done, False, {}

    #################################################################

    def _get_obs(self):
        return np.array(self.map.grid, dtype=np.uint8)

    def _get_distance_to_closest_apple(self):
        head_x, head_y = self.snake.get_head_pos()
        min_dist = float('inf')
        for (apple_x, apple_y) in self.apples:
            dist = abs(head_x - apple_x) + abs(head_y - apple_y)  # Manhattan distance
            if dist < min_dist:
                min_dist = dist
        return min_dist

    #################################################################

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if self.render_mode == "human":
            self.draw()

    def close(self):
        pygame.quit()