"""Illusion, just create a small illusion.

Exercises :

1. Change the number of line.
2. Change the size of the line or the square
"""

from turtle import *

from freegames import line, square

square_size = 25


def draw_one_line_square(start_x, start_y):
    for i in range(0, 10):
        place_x = start_x + (i * square_size * 2)
        square(place_x, start_y, square_size, 'black')


def draw_all_lines():
    base_x = -200
    base_y = 150
    for i in range(0, 11):
        line(
            base_x,
            base_y - i * square_size,
            base_x + 16 * square_size,
            base_y - i * square_size,
        )


def draw_all_square():
    draw_one_line_square(-200, 150)
    draw_one_line_square(-190, 125)
    draw_one_line_square(-180, 100)
    draw_one_line_square(-190, 75)
    draw_one_line_square(-200, 50)
    draw_one_line_square(-190, 25)
    draw_one_line_square(-180, 0)
    draw_one_line_square(-190, -25)
    draw_one_line_square(-200, -50)
    draw_one_line_square(-190, -75)
    draw_one_line_square(-180, -100)


setup(420, 400, 30, 0)
hideturtle()
tracer(False)
listen()
draw_all_lines()
draw_all_square()
done()
