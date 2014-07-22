"""
Tiles, a game of re-arranging an image.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1. Track a score by the number of tile moves.
2. Permit diagonal squares as adjacent.
3. Respond to arrow keys instead of mouse clicks.
"""

import sys, pygame
import random
from pygame.locals import *

pygame.init()

# Initialize variables.

tile_size = 160
size = width, height = 480, 480
font = pygame.font.Font(None, 14)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
image = pygame.image.load('car.jpg')
#TODO: Track 'score' by number of tile moves.

# These are the valid adjacent squares.

above, below = (0, -tile_size), (0, tile_size)
left, right = (-tile_size, 0), (tile_size, 0)
#TODO: Permit diagonal squares as adjacent.

# Create tiles.

tiles = []
for x_pos in range(width / tile_size):
    for y_pos in range(height / tile_size):
        area = pygame.Rect(x_pos * tile_size, y_pos * tile_size,
                           tile_size, tile_size)
        tile = pygame.Surface((tile_size, tile_size))
        tile.blit(image, (0, 0), area)
        tiles.append([area, tile])

# Replace last tile with black square.

tiles[-1][1] = pygame.Surface((tile_size, tile_size))
black_tile = tiles[-1]

# Mix up tile locations.

for rpt in range(1000):
    # Swap black tile with random adjacent tile.
    areas = map(black_tile[0].move, (above, below, left, right))
    adjacent_tiles = [tile for tile in tiles if tile[0] in areas]
    tile = random.choice(adjacent_tiles)
    tile[0], black_tile[0] = black_tile[0], tile[0]

while True:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT):
            # TODO: Respond to arrow keys.
            pass
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))
    elif event.type == MOUSEBUTTONDOWN:
        # Swap a clicked tile if it is adjacent.

        place = ((event.pos[0] / tile_size) * tile_size,
                 (event.pos[1] / tile_size) * tile_size)

        tile = [tile for tile in tiles if tile[0].topleft == place][0]

        diff = (tile[0][0] - black_tile[0][0],
                tile[0][1] - black_tile[0][1])

        if diff in (above, below, left, right):
            black_tile[0], tile[0] = tile[0], black_tile[0]

    for tile in tiles:
        screen.blit(tile[1], tile[0])

    pygame.display.flip()
