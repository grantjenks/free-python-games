"""
Tron, the video game.

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

black, red, blue, white = (0, 0, 0), (255, 0, 0), (0, 0, 255), (255, 255, 255)
tiles, width = 120, 4
up, right, down, left = -tiles, 1, tiles, -1

clock = pygame.time.Clock()
screen = pygame.display.set_mode((tiles * width, tiles * width))

def restart():
    global board, player1, player2
    board = [black] * (tiles * tiles)
    player1 = dict(direction=left,
                   position=(tiles * 3 / 4) + (tiles * tiles / 2),
                   dead=False,
                   color=red)
    player2 = dict(direction=right,
                   position=(tiles / 4) + (tiles * tiles / 2),
                   dead=False,
                   color=blue)
    screen.fill(black)
    pygame.display.flip()

restart()

def move(player):
    curr = player['position']
    next = curr + player['direction']
    if next < 0 or next >= (tiles ** 2):
        player['dead'] = True
    elif abs((next % tiles) - (curr % tiles)) > 1:
        player['dead'] = True
    elif board[next] != black:
        player['dead'] = True
    else:
        board[next] = player['color']
    player['position'] = next

def draw_rect(player):
    left, top = player['position'] % tiles, player['position'] / tiles
    return (left * width, top * width, width, width)

while True:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_UP and player1['direction'] != down:
            player1['direction'] = up
        elif event.key == K_RIGHT and player1['direction'] != left:
            player1['direction'] = right
        elif event.key == K_DOWN and player1['direction'] != up:
            player1['direction'] = down
        elif event.key == K_LEFT and player1['direction'] != right:
            player1['direction'] = left
        elif event.key == K_w and player2['direction'] != down:
            player2['direction'] = up
        elif event.key == K_d and player2['direction'] != left:
            player2['direction'] = right
        elif event.key == K_s and player2['direction'] != up:
            player2['direction'] = down
        elif event.key == K_a and player2['direction'] != right:
            player2['direction'] = left
        elif event.key == K_r:
            restart()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if player1['dead'] or player2['dead']:
        continue

    move(player1)
    move(player2)

    rect1 = draw_rect(player1)
    rect2 = draw_rect(player2)

    pygame.draw.rect(screen, player1['color'], rect1)
    pygame.draw.rect(screen, player2['color'], rect2)

    pygame.display.update((rect1, rect2))
    clock.tick(36)
