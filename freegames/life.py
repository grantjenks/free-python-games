"""Life simulation game.

Conway's game of life is a classic cellular automation created in 1970 by John
Conway. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Exercises

1. Track the development and movement of randomly created cells.
2. Make the grid bigger.
3. Generate some of the example patterns found here:
    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns

"""

import turtle
from random import choice
from freegames import square

# Setup grid.
x = 20
y = 20
grid = []
boxSize = 10
stepCount = 0

# On/Off values.
ON = 255
OFF = 0
vals = [ON, OFF]


def randomGrid(x, y):
    """Returns a grid of X by Y random values"""
    return [
        [choice(vals) for _ in range(x)]
        for _ in range(y)
    ]


def step():
    """Update the grid for one step in the simulation."""

    # Copy grid since we require 8 neighbors for calculation
    # and we go line by line (and memory is cheap).
    newGrid = grid.copy()

    print("Step")

    for i in range(x):
        for j in range(y):
            # Compute 8-neighbor sum using toroidal boundary conditions x and y
            # wrap around so that the simulation takes place on a toroidal
            # surface.
            total = int((grid[i][(j-1) % x] + grid[i][(j+1) % y]
                     + grid[(i-1) % x][j] + grid[(i+1) % x][j]
                     + grid[(i-1) % x][(j-1) % y] + grid[(i-1) % x][(j+1) % y]
                     + grid[(i+1) % x][(j-1) % y] + grid[(i+1) % x][(j+1) % y])
                     / 255)

            # Apply Conway's rules.
            if grid[i][j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i][j] = OFF
            else:
                if total == 3:
                    newGrid[i][j] = ON

    grid[:] = newGrid[:]


def draw():
    """Update the simulation display and trigger next pass"""
    step()
    print("draw")
    for i in range(x):
        for j in range(y):
            if grid[i][j] == ON:
                square(i * boxSize, j * boxSize, boxSize, 'black')
            else:
                square(i * boxSize, j * boxSize, boxSize, 'white')

    turtle.ontimer(draw, 20)


def load():
    # Generate random starting grid
    grid[:] = randomGrid(x, y)[:]


turtle.setup(x * boxSize, y * boxSize, 0, 0)
turtle.hideturtle()
turtle.tracer(False)
load()
draw()
turtle.done()
