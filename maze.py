"""
Maze, a trek from corner to corner.

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
from itertools import Counter

pygame.init()

size = width, height = 720, 730
tiles = 72
dirs = (-1, 1, tiles, -tiles)
font = pygame.font.Font(None, 14)
up, right, down, left = (0, -10), (10, 0), (0, 10), (-10, 0)
foreground, background = (255, 255, 255), (0, 0, 0)

def make_maze():
    square = tiles * tiles
    maze = [0] * square
    def helper(pos):
        if pos == 0:
            maze[pos] = 1
            return True
        elif pos >= square:
            return False
        else:
            moves = list(dirs)
            random.shuffle(moves)
            for move in moves:
                new_pos = pos + move
                if helper(new_pos):
                    maze[new_pos] = 1
                    return True
            else:
                return False
                

        
    helper(tiles * tiles - 1)
    pos = last
    while pos != 0:
        maze[pos] = 1
        move = random.choice(dirs)
        if pos + move > last: continue
        pos += move
    def bfs(pos):
        
    path = [last]
    pos = last
    while pos != 0:
        

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

player = pygame.Rect(0, 0, 10, 10)
monster = pygame.Rect(710, 710, 10, 10)
maze = make_maze()
dead = False

for counter in count():
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
            player = pygame.Rect(0, 0, 10, 10)
            monster = pygame.Rect(710, 710, 10, 10)
            maze = make_maze()
            dead = False
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if dead:
        continue

    


    next = snake[-1].move(snake_dir)
    if next.left < 0: next.left = width - 10
    if next.left >= width: next.left = 0
    if next.top < 0: next.top = height - 10
    if next.top >= height: next.top = 0

    if next in snake:
        dead = True
        foreground, background = background, foreground
    else:
        snake.append(next)

        if food and next == food:
            food = None
            snake_len += 1
        else:
            snake.popleft()

    if food is None and counter % 50 == 0:
        food = pygame.Rect(randrange(48) * 10, randrange(48) * 10, 10, 10)

    screen.fill(background)
    for rect in snake:
        pygame.draw.rect(screen, foreground, rect)
    if food:
        pygame.draw.rect(screen, foreground, food)
    surface = font.render(str(snake_len), True, foreground)
    screen.blit(surface, (0, 0))

    pygame.display.flip()
    clock.tick(12)
