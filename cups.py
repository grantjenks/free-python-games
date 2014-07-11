"""
Cups - a game of tracking a cup.

Written by Grant Jenks
http://www.grantjenks.com/

Copyright (c) 2014 Grant Jenks

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
1. Increase the number of cups.
2. Increase the frame rate.
3. Increase the cup rotation speed.
4. Increase the number of swaps.
5. Change the circles to squares.
6. How could you allow multiple pairs of cups to rotate at the same time?
"""

import sys, pygame, random
from pygame.locals import *
from math import pi, sin, cos

pygame.init()

cup_count, cup_width, margin, fps = 3, 80, 20, 20
block = cup_width + margin
width = block * cup_count

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, width))

white, blue, red = (255, 255, 255), (0, 0, 255), (255, 0, 0)

def draw_cup(index, color=blue, size=2):
    xpos = int(index * block + block / 2)
    ypos = int(width / 2)
    pygame.draw.circle(screen, color, (xpos, ypos), cup_width / size)

def draw_cups():
    pygame.draw.rect(screen, white, (0, 0, width, width))
    for index in range(cup_count):
        draw_cup(index)

def animate_start():
    for repeat in range(fps):
        draw_cups()
        for idx, val in enumerate(cups):
            if val == cup:
                draw_cup(idx, red, 4)
        yield

def animate_swap(left, right):
    if left > right:
        left, right = right, left

    direction = random.choice([1, -1])
    radius = (right - left) * (block / 2)
    center = (left + right) / 2.0 * block + (block / 2)

    for angle in range(0, 180, 10):
        angle *= direction
        pygame.draw.rect(screen, white, (0, 0, width, width))
        for index in range(cup_count):
            if index == left or index == right:
                offset = 0 if index == right else 180
                radians = (angle + offset) * pi / 180
                xpos = int(center + radius * cos(radians))
                ypos = int(width / 2 - radius * sin(radians))
                pygame.draw.circle(screen, blue, (xpos, ypos), cup_width / 2)
            else:
                draw_cup(index)
        yield

    cups[left], cups[right] = cups[right], cups[left]

def reset():
    global cups, cup, animation, swaps
    cups = list(range(cup_count))
    cup = random.randrange(cup_count)
    animation = animate_start()
    swaps = random.randrange(10, 20)

reset()

while True:
    clock.tick(fps)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_r:
            reset()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if animation is None:
        if swaps > 0:
            start = random.randrange(cup_count - 1)
            other = random.randrange(1, cup_count - start)
            animation = animate_swap(start, start + other)
        elif swaps > -(fps * 5):
            draw_cups()
        else:
            animation = animate_start()
        swaps -= 1
    else:
        try:
            animation.next()
        except:
            animation = None

    pygame.display.flip()
