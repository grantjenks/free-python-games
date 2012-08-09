"""
Maze game.

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

tiles, block = 24, 20
size = width, height = (tiles * block), (tiles * block + 10)

dirs = up, right, down, left = (-tiles, 1, tiles, -1)
view = (up, right, down, left, up - 1, up + 1, down - 1, down + 1)

hall, wall, boundary, extra = 0, 1, 2, 3

red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
white, grey, black = (255, 255, 255), (100, 100, 100), (0, 0, 0)

font = pygame.font.Font(None, 14)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

def make_maze():
    global maze, player, end, moves

    # Create the initial, empty maze.

    maze = [boundary] * tiles
    maze += ([boundary] + [wall] * (tiles - 2) + [boundary]) * (tiles - 2)
    maze += [boundary] * tiles

    # Make the maze. This is a randomized version of Prim's algorithm
    # to build a minimum spanning tree.

    player = tiles + 1
    maze[player] = 0
    frontier = [tiles + 2, 2 * tiles + 1]
    while len(frontier) > 0:
        pos = random.randrange(len(frontier))
        frontier[pos], frontier[-1] = frontier[-1], frontier[pos]
        spot = frontier.pop()

        if maze[spot] != wall: continue

        if map(lambda diff: maze[spot + diff], dirs).count(0) != 1:
            continue

        maze[spot] = hall

        frontier.extend(map(lambda diff: spot + diff, dirs))

    # End goal should be farthest reachable hall.

    frontier = [player]
    while True:
        next = []
        for front in frontier:
            maze[front] = extra
            next.extend(filter(lambda pos: maze[pos] == hall,
                               map(lambda diff: front + diff, dirs)))
        if next:
            frontier = next
        else:
            last = random.choice(frontier)
            break

    for pos, val in enumerate(maze):
        if val == extra: maze[pos] = hall

    moves = 0
    end = last

def draw_tile(func, color, pos):
    left = (pos % tiles) * block
    top = (pos / tiles) * block
    func(screen, color, (left, top, block, block))

def draw_maze():
    for pos, val in enumerate(maze):
        color = white if val == hall else black
        draw_tile(pygame.draw.rect, color, pos)

def draw_view():
    for diff in view:
        pos = player + diff
        color = white if maze[pos] == hall else black
        draw_tile(pygame.draw.rect, color, pos)

    draw_tile(pygame.draw.rect, white, player)
    draw_tile(pygame.draw.rect, green, end)
    draw_tile(pygame.draw.ellipse, blue, player)

    pygame.draw.rect(screen, (0, 0, 0), (0, width, width, 10))
    surface = font.render(str(moves), True, (255, 255, 255))
    screen.blit(surface, (5, tiles * block))

    pygame.display.flip()

def restart():
    make_maze()
    pygame.draw.rect(screen, grey, (0, 0, width, height))
    draw_view()

restart()

while True:
    clock.tick(12)

    event = pygame.event.poll()
    move_dir = None

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_UP:
            move_dir = up
        elif event.key == K_RIGHT:
            move_dir = right
        elif event.key == K_DOWN:
            move_dir = down
        elif event.key == K_LEFT:
            move_dir = left
        elif event.key == K_r:
            restart()
        elif event.key == K_s:
            draw_maze()
            draw_view()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if player == end: continue

    if move_dir is not None:
        if maze[player + move_dir] == hall:
            player += move_dir
            moves += 1
        draw_view()

    pygame.display.flip()
