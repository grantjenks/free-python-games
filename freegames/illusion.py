"""Illusion, just create a small illusion.


Exercises :

1. Change the number of line.
2. Change the size of the line or the square
"""

from turtle import *
from random import randint

from freegames import line, square

square_size = 25

def drawOneLineSquare(start_x, start_y):
    for i in range(0, 10):
        place_x = start_x + (i * square_size *2)
        square(place_x, start_y, square_size, "black")

def drawAllLines():
    base_x = -200
    base_y = 150
    for i in range(0,11):
        line(base_x, base_y - i * square_size, base_x + 16 * square_size, base_y - i * square_size)

def drawAllSquare():
    drawOneLineSquare(-200, 150)
    drawOneLineSquare(-190, 125)
    drawOneLineSquare(-180, 100)
    drawOneLineSquare(-190, 75)
    drawOneLineSquare(-200, 50)
    drawOneLineSquare(-190, 25)
    drawOneLineSquare(-180, 0)
    drawOneLineSquare(-190, -25)
    drawOneLineSquare(-200, -50)
    drawOneLineSquare(-190, -75)
    drawOneLineSquare(-180, -100)

setup(420, 400, 30, 0)
hideturtle()
tracer(False)
listen()
drawAllLines()
drawAllSquare()
done()