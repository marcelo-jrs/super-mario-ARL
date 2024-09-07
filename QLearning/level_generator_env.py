# level_generation_env.py
import random

class LevelGenerationEnv:
    def __init__(self, width=20, height=16, max_ground_height=3):
        self.width = width
        self.height = height
        self.max_ground_height = max_ground_height
        self.reset()

    def reset(self):
        # Start with an empty level
        self.level = [['-' for _ in range(self.width)] for _ in range(self.height)]
        self.current_position = 0  # Track the position in the level
        return self.level

    def step(self, action):
        # Action corresponds to the type of tile to place at the current position
        tile_types = ['-', 'X', '?', 'E', 'S']  # Empty, ground, question block, enemy, solid (breakable)
        tile = tile_types[action]
        
        # Determine where to place the tile
        x = self.current_position
        
        # For ground tiles ('X'), randomly choose a height between 1 and max_ground_height
        if tile == 'X':
            y = random.randint(self.height - self.max_ground_height, self.height - 1)
        else:
            y = self.height - 2 if tile in ['?', 'E'] else self.height - 1
        
        # Place the tile in the level grid
        self.level[y][x] = tile
        
        # Move to the next position
        self.current_position += 1

        # Check if level is complete
        done = self.current_position >= self.width
        
        # Basic reward: encourage valid tile placement (ground at bottom, enemies above ground)
        reward = 1 if (tile == 'X' and y >= self.height - self.max_ground_height) or (tile in ['?', 'E'] and y < self.height - 1) else -1
        
        return self.level, reward, done, {}

    def render(self):
        for row in self.level:
            print(''.join(row))
