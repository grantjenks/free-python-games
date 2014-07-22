"""
Sonar.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1. Increase the number of targets to 10.
2. How would you create a computer player?
3. How would moving targets change things?
"""

import sys, pygame, random
from pygame.locals import *

pygame.init()

width = 800
screen = pygame.display.set_mode((width, width))
font = pygame.font.Font(None, 18)
clock = pygame.time.Clock()

red, blue = (255, 0, 0), (0, 0, 255)
black, white = (0, 0, 0), (255, 255, 255)

def distance(buoy, target):
    return ((target[0] - buoy[0]) ** 2 + (target[1] - buoy[1]) ** 2) ** 0.5

def reset():
    global clicks, targets
    clicks = []
    targets = [(random.randrange(width), random.randrange(width))
               for value in range(5)]

def draw_board():
    pygame.draw.rect(screen, black, (0, 0, width, width))

    for click in clicks:
        pygame.draw.rect(screen, white, (click[0], click[1], 2, 2))

    for click in clicks:
        radius = int(min(distance(click, target) for target in targets))
        pygame.draw.circle(screen, blue, click, radius, 1)

    found = 0

    for target in targets:
        total = sum(1 for click in clicks
                    if min((distance(click, target), target)
                           for target in targets)[1] == target)

        if total >= 3:
            found += 1
            pygame.draw.circle(screen, red, target, 4)

    message = str(len(targets) - found) + ' targets remaining and '
    message += str(len(clicks)) + ' buoys placed.'

    surface = font.render(message, True, white)
    screen.blit(surface, (0, 0))

reset()

while True:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_r:
            reset()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))
    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
        clicks.append((event.pos[0], event.pos[1]))

    draw_board()
    pygame.display.flip()
