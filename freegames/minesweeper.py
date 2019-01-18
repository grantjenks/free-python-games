"""Minesweeper

Exercises

1. Increase the size of the grid.
2. ???

"""

from freegames import floor, square
from random import randrange, seed
from turtle import *

seed(0)
bombs = {}
counts = {}
display = {}


def initialize():
    "Initialize `bombs` and `counts` grids."
    for x in range(-250, 250, 50):
        for y in range(-250, 250, 50):
            bombs[x, y] = False
            counts[x, y] = -1
            display[x, y] = False

    for _ in range(8):
        x = randrange(-200, 200, 50)
        y = randrange(-200, 200, 50)
        bombs[x, y] = True

    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            total = 0
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    total += bombs[x + i, y + j]
            counts[x, y] = total


def stamp(x, y, text):
    square(x, y, 50, 'white')
    color('black')
    write(text, font=('Arial', 50, 'normal'))


def draw():
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            stamp(x, y, '?')


def end():
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            if bombs[x, y]:
                stamp(x, y, 'X')


def tap(x, y):
    x = floor(x, 50)
    y = floor(y, 50)

    if bombs[x, y]:
        end()
        return

    pairs = [(x, y)]

    while pairs:
        x, y = pairs.pop()
        stamp(x, y, counts[x, y])
        display[x, y] = True

        if counts[x, y] != 0:
            break

        for i in (-50, 0, 50):
            for j in (-50, 0, 50):
                if i == j == 0:
                    continue
                pair = x + i, y + j
                if display[pair]:
                    continue
                if counts[pair] == 0:
                    pairs.append(pair)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
initialize()
draw()
onscreenclick(tap)
done()
