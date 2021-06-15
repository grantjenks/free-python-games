"""Tiles, number swapping game.

Exercises

1. Track a score by the number of tile moves.
2. Permit diagonal squares as neighbors.
3. Respond to arrow keys instead of mouse clicks.
4. Make the grid bigger.

"""

from random import *
from turtle import *

from freegames import floor, vector

tiles = {}
neighbors = [
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]


def load():
    "Load tiles and scramble."
    count = 1

    for y in range(-200, 200, 100):
        for x in range(-200, 200, 100):
            mark = vector(x, y)
            tiles[mark] = count
            count += 1

    tiles[mark] = None

    for count in range(1000):
        neighbor = choice(neighbors)
        spot = mark + neighbor

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot


def square(mark, number):
    "Draw white square with black outline and number."
    up()
    goto(mark.x, mark.y)
    down()

    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(99)
        left(90)
    end_fill()

    if number is None:
        return
    elif number < 10:
        forward(20)

    write(number, font=('Arial', 60, 'normal'))


def tap(x, y):
    "Swap tile and empty square."
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)

    for neighbor in neighbors:
        spot = mark + neighbor

        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)


def draw():
    "Draw all tiles."
    for mark in tiles:
        square(mark, tiles[mark])
    update()


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
load()
draw()
onscreenclick(tap)
done()
