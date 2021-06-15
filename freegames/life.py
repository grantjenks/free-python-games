"""Game of Life simulation.

Conway's game of life is a classic cellular automation created in 1970 by John
Conway. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Exercises

1. Can you identify any Still Lifes, Oscillators, or Spaceships?
2. How can you make the simulation faster? Or bigger?
3. How would you modify the initial state?
4. Try changing the rules of life :)

"""

from random import choice
from turtle import *

from freegames import square

cells = {}


def initialize():
    "Randomly initialize the cells."
    for x in range(-200, 200, 10):
        for y in range(-200, 200, 10):
            cells[x, y] = False

    for x in range(-50, 50, 10):
        for y in range(-50, 50, 10):
            cells[x, y] = choice([True, False])


def step():
    "Compute one step in the Game of Life."
    neighbors = {}

    for x in range(-190, 190, 10):
        for y in range(-190, 190, 10):
            count = -cells[x, y]
            for h in [-10, 0, 10]:
                for v in [-10, 0, 10]:
                    count += cells[x + h, y + v]
            neighbors[x, y] = count

    for cell, count in neighbors.items():
        if cells[cell]:
            if count < 2 or count > 3:
                cells[cell] = False
        elif count == 3:
            cells[cell] = True


def draw():
    "Draw all the squares."
    step()
    clear()
    for (x, y), alive in cells.items():
        color = 'green' if alive else 'black'
        square(x, y, 10, color)
    update()
    ontimer(draw, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
initialize()
draw()
done()
