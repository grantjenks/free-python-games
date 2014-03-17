"""
Paint, for drawing shapes.

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
1. Add a color.
2. Complete draw_circle.
3. Complete draw_rectangle.
4. Complete draw_triangle.
5. Add width parameter.
"""

import sys, pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()

black, white = (0, 0, 0), (255, 255, 255)
red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)

def draw_line(color, start, end):
    pygame.draw.line(screen, color, start, end)

def draw_square(color, start, end):
    width = end[0] - start[0]
    pygame.draw.rect(screen, color, (start[0], start[1], width, width))

def draw_circle(color, start, end):
    # TODO
    pass

def draw_rectangle(color, start, end):
    # TODO
    pass

def draw_triangle(color, start, end):
    # TODO
    pass

shapes = [[draw_square, white, (0, 0), (480, 480)]]
shape, color, start = draw_line, black, None

def draw_shapes():
    for shape in shapes:
        func, color, start, end = shape
        func(color, start, end)

while True:
    clock.tick(12)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_r:
            color = red
        elif event.key == K_g:
            color = green
        elif event.key == K_u:
            color = blue
        elif event.key == K_b:
            color = black
        elif event.key == K_w:
            color = white
        elif event.key == K_l:
            shape = draw_line
        elif event.key == K_s:
            shape = draw_square
        elif event.key == K_c:
            shape = draw_circle
        elif event.key == K_e:
            shape = draw_rectangle
        elif event.key == K_t:
            shape = draw_triangle
        elif event.key == K_a:
            shapes = [[draw_square, white, (0, 0), (480, 480)]]
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))
    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
        start = pygame.mouse.get_pos()
        shapes.append([shape, color, start, start])
    elif event.type == MOUSEBUTTONUP and event.button == 1:
        start = None

    if start is not None:
        shapes[-1][-1] = pygame.mouse.get_pos()
        
    draw_shapes()
    pygame.display.flip()
