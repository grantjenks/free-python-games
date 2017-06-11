"""Simon Says

Exercises

1. Speed up tile flash rate.
2. Add more tiles.

"""

from random import choice
from time import sleep
from turtle import *
from freegames import floor, vector

pattern = []
guesses = []
tiles = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
}

def square(x, y, name):
    "Draw square at (x, y) with color name."
    up()
    goto(x, y)
    down()
    color(name)
    begin_fill()
    for count in range(4):
        forward(200)
        left(90)
    end_fill()
    update()

def grid():
    "Draw grid of tiles."
    square(0, 0, 'dark red')
    square(0, -200, 'dark blue')
    square(-200, 0, 'dark green')
    square(-200, -200, 'khaki')

def flash(tile):
    "Flash tile in grid."
    glow, dark = tiles[tile]
    square(tile.x, tile.y, glow)
    sleep(0.5)
    square(tile.x, tile.y, dark)
    sleep(0.5)

def grow():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()

def tap(x, y):
    "Respond to screen tap."
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        exit()

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

    onscreenclick(tap)

def start(x, y):
    "Start game."
    grow()
    onscreenclick(tap)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()
