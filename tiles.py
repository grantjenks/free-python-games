"""
Tiles, a game of re-arranging an image.

Written by Grant Jenks
http://www.grantjenks.com/

DISCLAIMER
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE
LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY
SERVICING, REPAIR OR CORRECTION.

Copyright
This work is licensed under the
Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-nd/3.0/
or send a letter to Creative Commons, 171 Second Street, Suite 300,
San Francisco, California, 94105, USA
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
image = pygame.image.load(sys.argv[1])
#TODO: Track 'score' by number of tile moves.

# These are the valid adjacent squares.

above, below = (0, -tile_size), (0, tile_size)
left, right = (-tile_size, 0), (tile_size, 0)
#TODO: Permit diagonal squares as adjacent.

# Create tiles.

tiles = []
for x_pos in range(width / tile_size):
    for y_pos in range(height / tile_size):
        area = (x_pos * tile_size, y_pos * tile_size,
                tile_size, tile_size)
        tile = pygame.Surface((tile_size, tile_size))
        tile.blit(image, (0, 0), area)
        tiles.append([(area[0], area[1]), tile])

# Replace last tile with black square.

tiles[-1][1] = pygame.Surface((tile_size, tile_size))
black_tile = tiles[-1]

# Mix up tile locations.

for rpt in range(9):
    tile_one = random.choice(tiles)
    tile_two = random.choice(tiles)
    tile_one[0], tile_two[0] = tile_two[0], tile_one[0]

while True:

    event = pygame.event.poll()

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

        tile = filter(lambda tile: tile[0] == place, tiles)[0]

        diff = (tile[0][0] - black_tile[0][0],
                tile[0][1] - black_tile[0][1])

        if diff in (above, below, left, right):
            black_tile[0], tile[0] = tile[0], black_tile[0]

    for tile in tiles:
        screen.blit(tile[1], tile[0])

    pygame.display.flip()
    clock.tick(20)
