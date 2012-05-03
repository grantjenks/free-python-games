"""
Pacman.

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

"""
Needs
- 4 ghosts
- end game scenario:
  * everything eaten
  * eaten by ghost
"""

import sys
import math
import pygame
import random
from pygame.locals import *
from itertools import count

pygame.init()

board_width, board_height = 17, 19
font = pygame.font.Font(None, 24)
pacman = pygame.image.load('pacman.jpg')
ghost = pygame.image.load('ghost.jpg')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((340, 400))

score = 0
direction = new_dir = 0
board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0,
         0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0,
         0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0,
         0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0,
         0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0,
         0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0,
         0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0,
         0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0,
         0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0,
         0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0,
         0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0,
         0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0,
         0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0,
         0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0,
         0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0,
         0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0,
         0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pac_pos_lft = 160
pac_pos_top = 260
ghosts = [[20, 20, 0],
          [300, 20, 2],
          [20, 340, 0],
          [300, 340, 2]]

def update_position(new_dir, lft, top):
    new_lft = lft
    new_top = top

    if new_dir == 0:
        new_lft += 4
    elif new_dir == 1:
        new_top -= 4
    elif new_dir == 2:
        new_lft -= 4
    elif new_dir == 3:
        new_top += 4

    return new_lft, new_top

def calculate_idx(lft, top):
    return (top / 20) * board_width + (lft / 20)

def valid_position(lft, top):
    prev_idx = calculate_idx(lft, top)
    next_idx = calculate_idx(lft + 19, top + 19)
    on_track = lft % 20 == 0 or top % 20 == 0
    return board[prev_idx] != 0 and board[next_idx] != 0 and on_track

def update_ghost(val):
    cur_dir = new_dir = val[2]
    if val[0] % 20 == 0 and val[1] % 20 == 0:
        new_dir = (cur_dir + random.choice((1, 3))) % 4
    new_lft, new_top = update_position(new_dir, val[0], val[1])
    if valid_position(new_lft, new_top):
        val[0] = new_lft
        val[1] = new_top
        val[2] = new_dir
    else:
        new_lft, new_top = update_position(cur_dir, val[0], val[1])
        if valid_position(new_lft, new_top):
            val[0] = new_lft
            val[1] = new_top

for counter in count():

    event = pygame.event.poll()

    # Response to key presses.

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_UP:
            new_dir = 1
        elif event.key == K_RIGHT:
            new_dir = 0
        elif event.key == K_DOWN:
            new_dir = 3
        elif event.key == K_LEFT:
            new_dir = 2
        elif event.key == K_r:
            pass
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    # Update pacman position.

    new_lft, new_top = update_position(new_dir, pac_pos_lft, pac_pos_top)

    if valid_position(new_lft, new_top):
        pac_pos_lft = new_lft
        pac_pos_top = new_top
        direction = new_dir
    else:
        new_lft, new_top = update_position(direction, pac_pos_lft, pac_pos_top)

        if valid_position(new_lft, new_top):
            pac_pos_lft = new_lft
            pac_pos_top = new_top

    new_dir = direction

    # Update ghosts position.

    for val in ghosts:
        update_ghost(val)

    # Update board.

    idx = calculate_idx(pac_pos_lft, pac_pos_top)
    if board[idx] == 2:
        score += 1
        board[idx] = 1

    # Draw the board.

    for idx, val in enumerate(board):
        left = (idx % board_width) * 20
        top = (idx / board_width) * 20
        if val == 0:
            color = (0, 0, 128)
            pygame.draw.rect(screen, color, (left, top, 20, 20))
        else:
            color = (0, 0, 0)
            pygame.draw.rect(screen, color, (left, top, 20, 20))
            if val == 2:
                color = (255, 255, 255)
                pygame.draw.circle(screen, color, (left + 10, top + 10), 2)

    # Draw pacman.

    pacman_dir = pygame.transform.rotate(pacman, 90 * direction)
    screen.blit(pacman_dir, (pac_pos_lft, pac_pos_top))

    # Draw ghosts.

    for val in ghosts:
        screen.blit(ghost, (val[0], val[1]))

    # Draw score.

    pygame.draw.rect(screen, (0, 0, 0), (0, 380, 100, 20))
    msg = 'Score: ' + str(score)
    text = font.render(msg , True, (255, 255, 255))
    screen.blit(text, (5, 382))

    # TODO Check end game condition.

    # Display next frame.

    pygame.display.flip()
    clock.tick(12)
