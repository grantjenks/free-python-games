"""
Connect Four.

Written by Grant Jenks
http://www.grantjenks.com/

Copyright (c) 2012 Grant Jenks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

Exercises
1. Change the colors.
2. Draw squares instead of circles for open spaces.
3. Add logic to detect a full board.
4. Add logic to detect a winner.
"""

import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 560, 480
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

# Notice that these colors do not precisely match their names.

white, black = (245, 245, 220), (0, 0, 128)
blue, red, yellow = (65, 105, 225), (255, 99, 71), (255, 215, 0)

def draw_game():
    """Draw the connect four board."""

    pygame.draw.rect(screen, blue, (0, 0, 560, 480))

    # Draw the circles representing open and played spaces.

    for row, line in enumerate(board):
        for col, val in enumerate(line):
            rect = (col * 80 + 5, row * 80 + 5, 70, 70)
            pygame.draw.ellipse(screen, val, rect)

    # Draw vertical lines denoting column choices.

    for val in range(6):
        offset = 80 + 80 * val
        pygame.draw.line(screen, black, (offset, 0), (offset, 480), 3)

    pygame.display.flip()

def restart():
    global board, turn
    board = [[white] * 7, [white] * 7, [white] * 7,
             [white] * 7, [white] * 7, [white] * 7]
    turn = red
    draw_game()

restart()

while True:
    clock.tick(12)

    event = pygame.event.poll()
    col = None

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_r:
            restart()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))
    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
        col = event.pos[0] / 80

    if col is None: continue

    # Search for an open row in this column.

    for val in reversed(range(6)):
        if board[val][col] == white: break
    else:
        continue

    board[val][col] = turn
    draw_game()

    turn = yellow if turn == red else red
