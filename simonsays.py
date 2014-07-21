"""
Simon Says

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1. Add more rectangles.
"""

import sys, pygame, random
from pygame.locals import *
from pygame import Rect

pygame.init()

screen = pygame.display.set_mode((480, 480))
font = pygame.font.Font(None, 16)
clock = pygame.time.Clock()

black, white = (0, 0, 0), (255, 255, 255)
rects = ((Rect(  5,   5, 230, 230), (200, 200,   0), (255, 255,   0)),
         (Rect(245,   5, 230, 230), (200,   0,   0), (255,   0,   0)),
         (Rect(  5, 245, 230, 230), (  0, 200,   0), (  0, 255,   0)),
         (Rect(245, 245, 230, 230), (  0,   0, 200), (  0,   0, 255)))

def reset():
    global guess, pattern
    guess, pattern = [], [random.randrange(len(rects))]
    draw_pattern()

def draw_pattern():
    for value in pattern:
        rect = rects[value]

        clock.tick(12)
        draw_screen()
        pygame.display.flip()

        clock.tick(12)
        draw_screen()
        pygame.draw.rect(screen, rect[2], rect[0])
        pygame.display.flip()

def draw_screen():
    pygame.draw.rect(screen, black, (0, 0, 480, 480))
    for rect in rects:
        pygame.draw.rect(screen, rect[1], rect[0])

def draw_message(message):
    surface = font.render(message, True, black)
    screen.blit(surface, (10, 10))

reset()

while True:
    clock.tick(12)
    event = pygame.event.poll()

    draw_screen()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_r:
            reset()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))
    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
        for index, rect in enumerate(rects):
            if rect[0].collidepoint(event.pos):
                pygame.draw.rect(screen, rect[2], rect[0])
                guess.append(index)

    draw_message('Pattern length: ' + str(len(pattern)))

    if len(guess) > 0:
        if all(lhs == rhs for lhs, rhs in zip(pattern, guess)):
            if len(pattern) == len(guess):
                pygame.display.flip()
                pattern.append(random.randrange(len(rects)))
                guess = []
                draw_pattern()
        else:
            pygame.draw.rect(screen, white, (0, 0, 480, 480))
            draw_message('Max pattern length: ' + str(len(pattern) - 1))
            pygame.display.flip()
    else:
        pygame.display.flip()
