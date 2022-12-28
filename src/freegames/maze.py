"""Maze, move from one side to another.

Excercises

1. Keep score by counting taps.
2. Make the maze harder.
3. Generate the same maze twice.
"""

from random import random
from turtle import *

from freegames import line


def draw():
    """Draw maze."""
    color('black')
    width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    update()


def tap(x, y):
    """Draw line and dot for screen tap."""
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()

    width(2)
    color('red')
    goto(x, y)
    dot(4)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
