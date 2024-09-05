import random

# Define tile types
TILE_TYPES = ['-', 'X', '?', 'E', 'S']  # Empty, ground, question block, enemy

def generate_random_level_segment(width=20, height=16):
    level = [['-' for _ in range(width)] for _ in range(height)]

    # Place ground on the bottom row
    for x in range(width):
        level[height - 1][x] = 'X'
        level[height][x] = 'X'
        level[height + 1][x] = 'X'  # Ground tiles at the bottom

    # Randomly place obstacles and enemies above ground
    for x in range(width):
        if random.random() < 0.4:  # 20% chance to place a block above ground
            level[height - 2][x] = random.choice(['?', 'E', 'X'])  # Question block or enemy
    
    lvl_file = open(r"C:\Users\labinfo\Desktop\super-mario-ARL\levels/teste.txt", "w")
    for row in level:
        lvl_file.write(f"{''.join(row)} \n")

    return level

# Display the generated level segment
def display_level_segment(level):
    for row in level:
        print(''.join(row))


# Example usage
level_segment = generate_random_level_segment()
display_level_segment(level_segment)
