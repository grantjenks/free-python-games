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
move = vector(0, 3)
overlap = {0: vector(0, 0)}
defualt_size = 270
goal_size = 0


def empty_rectangle(x, y, size):
    """Draw empty rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    down()
    draw_rectangle(size)


def filled_ractangle(x, y, size):
    """Draw filled rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    begin_fill()
    draw_rectangle(size)
    end_fill()


def draw_rectangle(size):
    """Draw rectangle line with given size."""
    for count in range(2):
        forward(size)
        left(90)
        forward(size)
        left(90)


def stamp(x, y, text, _color='black', font_size=10):
    """Display `text` at coordinates `x` and `y`."""
    goto(x, y)
    color(_color)
    write(text, font=('Arial', font_size, 'normal'))


def i_size(step):
    """Return the rectangle size of the step"""
    return defualt_size - (step) * 30


def end():
    """End the game by stopping moving rectangle"""
    move.y = 0
    del overlap[len(overlap) - 1]


def draw():
    """Draw rectangle frames and a moving rectangle."""
    clear()

    if i_size(len(overlap)) == goal_size:
        stamp(-200, 100, 'Win!', _color='red', font_size=30)
        done()

    stamp(-200, -200, 'Score : ' + str(len(overlap) - 1))

    size = i_size(len(overlap))

    for i in range(0, len(overlap)):
        size_i = i_size(i)
        empty_rectangle(overlap[i].x - size_i / 2, overlap[i].y - size_i / 2, size_i)

    rectangle.move(move)
    x = rectangle.x
    y = rectangle.y

    filled_ractangle(x - (size / 2), y - (size / 2), size)

    if y + move.y - size * 0.5 <= -210 or y + move.y + size * 0.5 >= 210:
        move.y = -move.y

    ontimer(draw, 5)


def tap(x, y):
    """Respond to screen click at a moving rectangle."""
    overlap[len(overlap)] = vector(rectangle.x, rectangle.y)

    curr_size = i_size(len(overlap) - 1)
    prev_size = i_size(len(overlap) - 2)

    curr_square = overlap[len(overlap) - 1]
    prev_square = overlap[len(overlap) - 2]

    if curr_square.x - curr_size / 2 < prev_square.x - prev_size / 2:
        end()
        done()
    elif curr_square.y - curr_size / 2 < prev_square.y - prev_size / 2:
        end()
        done()
    elif curr_square.x + curr_size / 2 > prev_square.x + prev_size / 2:
        end()
        done()
    elif curr_square.y + curr_size / 2 > prev_square.y + prev_size / 2:
        end()
        done()
    elif i_size(len(overlap)) == goal_size:
        move.y = 0


setup(width=420, height=420)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
