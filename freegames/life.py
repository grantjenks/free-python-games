"""Life simulation game.

Conway's game of life is a classic cellular automation created in 1970 by John
Conway. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Exercises

1. Track the development and movement of randomly created cells.
2. Make the grid bigger.
3. Generate some of the example patterns found here:
    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns
4. Step uses two nested loops back to back. Can you find a way to do the work
    in one pass?
"""

from turtle import *
from random import choice
from freegames import square

# Setup grid.
grid = []
box_size = 10


def randomize_grid(x, y):
    """Returns a grid of X by Y random values"""

    # Add two extra rows and columns to create a border around the actual grid.
    # to ease to process of checking the actual values during each step.
    for i in range(x+2):
        grid.append([])
        for j in range(y+2):
            if 0 < i < x+1:
                if 0 < j < y+1:
                    grid[i].append(choice([0, 1]))
                else:
                    grid[i].append(0)
            else:
                grid[i].append(0)


def step(x, y):
    """Update the grid for one step in the simulation."""

    # Build a fresh grid to fill with updated values.
    fresh_grid = []

    for i in range(x+2):
        fresh_grid.append([])
        for j in range(y+2):
            fresh_grid[i].append(0)

            # Compute 8-neighbor sum. Skip the edges of the grid confining the
            # simulation to a fixed space.
            if i == 0 or i == x+1 or j == 0 or j == y+1:
                total = 0
            else:
                total = grid[i][(j-1)] + grid[i][(j+1)] \
                      + grid[(i-1)][j] + grid[(i+1)][j] \
                      + grid[(i-1)][(j-1)] + grid[(i-1)][(j+1)] \
                      + grid[(i+1)][(j-1)] + grid[(i+1)][(j+1)]

            # Apply Conway's rules.
            if grid[i][j] == 1:
                if 1 < total < 4:
                    fresh_grid[i][j] = 1
            else:
                if total == 3:
                    fresh_grid[i][j] = 1

    # Copy the new grid over the old copy.
    grid[:] = fresh_grid[:]


def redraw_grid():
    draw_grid(20, 20)


def draw_grid(x, y):
    """Update the simulation display and trigger next pass"""
    step(x, y)
    for i in range(x+2):
        for j in range(y+2):
            if grid[i][j] == 1:
                square(i * box_size, j * box_size, box_size, 'green')
            else:
                square(i * box_size, j * box_size, box_size, 'black')

    ontimer(redraw_grid, 500)


setup(600, 600, 0, 0)
hideturtle()
tracer(False)
randomize_grid(20, 20)
redraw_grid()
done()
