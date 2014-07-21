"""
Flappy - yet another Flappy Bird ripoff.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

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
