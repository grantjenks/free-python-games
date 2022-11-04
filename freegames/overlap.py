"""Overlap, classic arcade game.

Exercises

1. Change the shape.
2. Change the color.
3. Change the speed of rectangle.
4. Change the a diminishing amount.
5. Change the the direction of the path(ex.horizontal orientation).
6. Change thr speed of frame.
"""

from turtle import *
from freegames import vector

rectangle = vector(0, 0)
move = vector(0, 5)
top = {0: vector(0, 0)}
top_size = {0: 300, 1: 200}


def rectangle_top(x, y, size):
    """Draw empty rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    down()
    for count in range(2):
        forward(size)
        left(90)
        forward(size)
        left(90)


def rectangle_move(x, y, size):
    """Draw filled rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    begin_fill()
    for count in range(2):
        forward(size)
        left(90)
        forward(size)
        left(90)
    end_fill()
    update()


def score(x, y, text):
    """Display `text` at coordinates `x` and `y`."""
    goto(x, y)
    color('black')
    write(text, font=('Arial', 10, 'normal'))


def draw():
    """Draw rectangles of top and a moving rectangle."""
    clear()

    score(-200, -200, 'Score : ' + str(len(top) - 1))

    size = top_size[len(top_size) - 1]

    for i in range(0, len(top)):
        size_i = top_size[i]
        rectangle_top(top[i].x - size_i / 2, top[i].y - size_i / 2, size_i)

    rectangle.move(move)
    x = rectangle.x
    y = rectangle.y

    rectangle_move(x - (size / 2), y - (size / 2), size)

    if y + move.y - size * 0.5 <= -210 or y + move.y + size * 0.5 >= 210:
        move.y = -move.y

    ontimer(draw, 5)


def tap(x, y):
    """Respond to screen click at a moving rectangle."""
    top[len(top)] = vector(rectangle.x, rectangle.y)
    top_size[len(top)] = top_size[len(top) - 1] - 20
    if top[len(top) - 1].x - top_size[len(top) - 1] / 2 < top[len(top) - 2].x - top_size[len(top) - 2] / 2 or \
        top[len(top) - 1].y - top_size[len(top) - 1] / 2 < top[len(top) - 2].y - top_size[len(top) - 2] / 2 or \
            top[len(top) - 1].x + top_size[len(top) - 1] / 2 > top[len(top) - 2].x + top_size[len(top) - 2] / 2 or \
        top[len(top) - 1].y + top_size[len(top) - 1] / 2 > top[len(top) - 2].y + top_size[len(top) - 2] / 2:
        move.y = 0
        del top[len(top) - 1]
        del top_size[len(top_size) - 1]


setup(width=420, height=420)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()

done()
