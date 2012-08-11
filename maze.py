"""
Maze game.

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
1. Change where the end is placed.
2. Change where the player starts.
3. Display only the player's immediate surroundings (no history).
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
