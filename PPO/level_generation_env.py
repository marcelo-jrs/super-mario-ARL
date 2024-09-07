import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random

class LevelGenerationEnv(gym.Env):
    def __init__(self, width=20, height=16, max_ground_height=3):
        super(LevelGenerationEnv, self).__init__()
        self.width = width
        self.height = height
        self.max_ground_height = max_ground_height

        # Define action and observation space
        self.action_space = spaces.Discrete(5)  # Four actions (tile types: '-', 'X', '?', 'E', 'S')
        self.observation_space = spaces.Box(low=0, high=3, shape=(self.width,), dtype=np.int32)

        self.reset()

    def reset(self, seed=None, options=None):
        # Start with an empty level
        self.level = [['-' for _ in range(self.width)] for _ in range(self.height)]
        self.current_position = 0  # Track the position in the level
        self.observation = np.zeros(self.width, dtype=np.int32)  # Keep track of placed tiles as integers
        return self.observation, {}

    def step(self, action):
        tile_types = ['-', 'X', '?', 'E', 'S']  # Empty, ground, question block, enemy, solid (breakable)
        tile = tile_types[action]
        
        x = self.current_position
        
        # For ground tiles ('X'), randomly choose a height between 1 and max_ground_height
        if tile == 'X':
            y = random.randint(self.height - self.max_ground_height, self.height - 1)
        else:
            y = self.height - 2 if tile in ['?', 'E'] else self.height - 1
            
        self.level[y][x] = tile
        self.observation[self.current_position] = action  # Store the tile as an integer in the observation

        self.current_position += 1
        done = self.current_position >= self.width

        # Simple reward for valid placement
        reward = 1 if (tile == 'X' and y >= self.height - self.max_ground_height) or (tile in ['?', 'E'] and y < self.height - 1) else -1
        
        return self.observation, reward, done, False, {}

    def render(self):
        for row in self.level:
            print(''.join(row))
        print("\n")
