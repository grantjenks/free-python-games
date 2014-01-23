"""
Tron, the video game.

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
1. Make the tron players faster/slower.
2. Allow a tron player to run into itself.
3. Allow the tron players to go around the edge of the screen.
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

    curr_x = curr % tiles
    curr_y = curr / tiles

    if player['direction'] == left:
        curr_x -= 1
    elif player['direction'] == right:
        curr_x += 1
    elif player['direction'] == up:
        curr_y -= 1
    elif player['direction'] == down:
        curr_y += 1

    curr_x %= tiles
    curr_y %= tiles

    next = curr_x + tiles * curr_y

    if board[next] != black:
        player['dead'] = True
    else:
        board[next] = player['color']

    player['position'] = next

def draw_rect(player):
    left, top = player['position'] % tiles, player['position'] / tiles
    return (left * width, top * width, width, width)

while True:
    clock.tick(36)
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
