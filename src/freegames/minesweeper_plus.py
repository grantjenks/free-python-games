"""Minesweeper

Exercises

1. What does the `seed(0)` function call do?
2. Change the number of bombs on the grid.
3. Change the size of the grid.
"""

from random import randrange, seed
from turtle import *

from freegames import floor, square

seed(0)
bombs = {}
shown = {}
counts = {}

# 参数设置
grid_size = 10  # Grid Size
num_bombs = 20  # No. Mines
cell_size = 50  # Cell Size
colors = { # Color Setup
    0: 'white',
    1: 'blue',
    2: 'green',
    3: 'red',
    4: 'purple',
    5: 'maroon',
    6: 'turquoise',
    7: 'black',
    8: 'gray'
}

def initialize():
    """Initialize `bombs`, `counts`, and `shown` grids."""
    for x in range(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size):
        for y in range(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size):
            bombs[x, y] = False
            shown[x, y] = False
            counts[x, y] = -1

    for _ in range(num_bombs):
        while True:
            x = randrange(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size)
            y = randrange(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size)
            if not bombs[x, y]:
                bombs[x, y] = True
                break

    for x in range(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size):
        for y in range(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size):
            total = 0
            for i in (-cell_size, 0, cell_size):
                for j in (-cell_size, 0, cell_size):
                    if i == 0 and j == 0:
                        continue
                    total += bombs.get((x + i, y + j), 0)
            counts[x, y] = total


def stamp(x, y, text, display_color=False):
    """Display `text` at coordinates `x` and `y`."""
    square(x, y, cell_size, 'white')
    if not display_color:
        color('black')
    else:
        color(colors[counts[x, y]])
    write(text, font=('Arial', cell_size // 2, 'normal'))


def draw():
    """Draw the initial board grid."""
    for x in range(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size):
        for y in range(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size):
            stamp(x, y, '?')
            # 绘制网格线
            for i in range(x, x + cell_size + 1):
                goto(i, y)
                goto(i, y + cell_size)
            for j in range(y, y + cell_size + 1):
                goto(x, j)
                goto(x + cell_size, j)


def end():
    """Draw the bombs as X's on the grid."""
    for x in range(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size):
        for y in range(-grid_size // 2 * cell_size, grid_size // 2 * cell_size, cell_size):
            if bombs[x, y]:
                stamp(x, y, 'X')


def tap(x, y):
    """Respond to screen click at `x` and `y` coordinates."""
    x = floor(x, cell_size)
    y = floor(y, cell_size)

    if bombs[x, y]:
        end()
        return

    pairs = [(x, y)]

    while pairs:
        x, y = pairs.pop()
        if counts[x, y] == 0:
            color(colors[counts[x, y]])
            square(x, y, cell_size, colors[counts[x, y]])
        else:
            stamp(x, y, counts[x, y], display_color=True)
        shown[x, y] = True

        if counts[x, y] == 0:
            for i in (-cell_size, 0, cell_size):
                for j in (-cell_size, 0, cell_size):
                    pair = x + i, y + j
                    if not shown.get(pair, False):
                        pairs.append(pair)


setup(cell_size * grid_size + 100, cell_size * grid_size + 100, 370, 0)
hideturtle()
tracer(False)
initialize()
draw()
onscreenclick(tap)
done()