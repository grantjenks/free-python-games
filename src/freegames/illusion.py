"""Illusion

Exercises:

1. Change the size of the squares.
2. Change the number of rows and lines.
"""

from itertools import cycle
from turtle import *

from freegames import line, square

size = 25


def draw_row(x, y):
    for i in range(0, 10):
        offset = x + (i * size * 2)
        square(offset, y, size, 'black')


def draw_rows():
    offsets = [-200, -190, -180, -190]
    pairs = zip(cycle(offsets), range(150, -176, -25))
    for offset, y in pairs:
        draw_row(offset, y)


def draw_lines():
    x = -200
    y = 150
    for i in range(0, 14):
        line(x, y - i * size, x + 16 * size, y - i * size)


setup(420, 400, 30, 0)
hideturtle()
tracer(False)
listen()
draw_rows()
draw_lines()
done()
