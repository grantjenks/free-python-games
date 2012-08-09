"""
Connect Four.

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

    for val in reversed(range(6)):
        if board[val][col] == white: break
    else:
        continue

    board[val][col] = turn
    draw_game()

    turn = yellow if turn == red else red
