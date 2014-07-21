"""
Memory, a game of remembering number pairs.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises:
1. Change the image.
2. Change the background color to white and the foreground color to black.
3. Increase the number of tiles to an 8x8 grid.
"""

import sys, pygame, random, time
from pygame.locals import *

pygame.init()

# Initialize variables.

tile_size = 120
size = width, height = 480, 480
font = pygame.font.Font(None, 14)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
image = pygame.image.load('car.jpg')
font = pygame.font.Font(None, 60)
black, white = (0, 0, 0), (255, 255, 255)

# Create tiles.

tiles = []
for y_pos in range(0, height, tile_size):
    for x_pos in range(0, width, tile_size):
        area = pygame.Rect(x_pos, y_pos, tile_size, tile_size)
        tile = pygame.Surface((tile_size, tile_size))
        tile.blit(image, (0, 0), area)
        tiles.append((area, tile))

def draw_game():
    """Draw the game state."""

    # Clear the screen with a black background.

    pygame.draw.rect(screen, black, (0, 0, width, height))

    # Draw lines to create grid for tiles.

    for pos in range(1, width / tile_size):
        offset = pos * tile_size
        pygame.draw.line(screen, white, (offset, 0), (offset, height))

    for pos in range(1, height / tile_size):
        offset = pos * tile_size
        pygame.draw.line(screen, white, (0, offset), (width, offset))

    # Draw tiles correctly guessed.

    for pos, tile in enumerate(tiles):
        if guesses[pos]:
            screen.blit(tile[1], tile[0])

    def draw_number(value):
        """Draw the number at a particular tile."""
        surface = font.render(str(values[value]), True, white)
        screen.blit(surface, tiles[value][0].move(45, 45))

    if select is not None: draw_number(select)
    if match is not None: draw_number(match)

    pygame.display.flip()

def restart():
    """Reset the game with random values."""
    global values, guesses, select, match, pause
    select, match, pause = None, None, 0
    count = len(tiles)
    assert count % 2 == 0
    values = list(range(count / 2)) * 2
    random.shuffle(values)
    guesses = [False] * count
    draw_game()

restart()

while True:
    clock.tick(12)

    event = pygame.event.wait()
    pos = None

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_r:
            restart()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))
    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
        pos = event.pos

    if pause > 0:
        if pos is None:
            if pause == 1:
                select, match, pause = None, None, 0
                draw_game()
            else:
                pause -= 1
                continue
        else:
            select, match, pause = None, None, 0
            draw_game()

    if pos is None: continue

    xxx = pos[0] / tile_size
    yyy = pos[1] / tile_size
    index = yyy * (width / tile_size) + xxx

    if guesses[index]:
        continue
    else:
        if select is None:
            select = index
        else:
            if select == index:
                continue
            else:
                if values[select] == values[index]:
                    guesses[select] = True
                    guesses[index] = True
                    select = None
                else:
                    pause = 12 * 3
                    match = index

    draw_game()
