import random

# tile types
TILE_TYPES = ['-', 'X', '?', 'E', 'S','-']

def generate_random_level_segment(width=20, height=16):
    level = [['-' for _ in range(width)] for _ in range(height)]

    for x in range(width):
        level[height - 1][x] = 'X'
        level[height - 2][x] = 'X'
        level[height - 3][x] = 'X'


    for x in range(width):
        for i in range(height):
            if random.random() < 0.1:
                level[i][x] = random.choice(['-', '?', 'E', 'S','-'])
    
    lvl_file = open("levels/level.txt", "w")
    for row in level:
        lvl_file.write(f"{''.join(row)} \n")

    return level

def display_level_segment(level):
    for row in level:
        print(''.join(row))


level_segment = generate_random_level_segment()
display_level_segment(level_segment)
