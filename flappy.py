"""
Flappy - yet another Flappy Bird ripoff.

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
1.
"""

import sys, pygame, random
from pygame.locals import *

pygame.init()

width, height, fps = 320, 320, 20

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

white, black = (255, 255, 255), (0, 0, 0)

def draw():
    pygame.draw.rect(screen, white, (0, 0, width, height))

def reset():
    pass

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

    draw()

    pygame.display.flip()
