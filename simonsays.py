"""
Simon Says

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
