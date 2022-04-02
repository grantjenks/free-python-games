"""Battleship, classic arcade game.

Exercises

"""

from ftplib import error_perm
from turtle import *
# from random import choice

from freegames import line, square

# sea_width = 6
# destroyer_length = 2
# cruiser_length = 3
# aircraft_carrier_length = 4

base_player_grid_x = -250
base_player_grid_y = 100
base_enemy_grid_x = 100
base_enemy_grid_y = 100
tiles_size = 25

# own_score = {'score': 0}
# enemy_score = {'score': 0}

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)

player_grid    =  [[0,0,0,0,0,0,0,0,0,0]]
player_grid.append([0,0,0,0,0,0,0,0,0,0])
player_grid.append([0,0,0,0,0,0,0,0,0,0])
player_grid.append([0,0,0,0,0,0,0,0,0,0])
player_grid.append([0,0,0,0,0,0,0,0,0,0])
player_grid.append([0,0,0,0,0,0,0,0,0,0])
player_grid.append([0,0,0,0,0,0,0,0,0,0])
player_grid.append([0,0,0,0,0,0,0,0,0,0])
player_grid.append([0,0,0,0,0,0,0,0,0,0])
player_grid.append([0,0,0,0,0,0,0,0,0,0])

enemy_grid    =  [[0,0,0,0,0,0,0,0,0,0]]
enemy_grid.append([0,0,0,0,0,0,0,0,0,0])
enemy_grid.append([0,0,2,2,0,0,0,0,0,0])  ## add the 22 ship for the test // uncomment only for testing
# enemy_grid.append([0,0,0,0,0,0,0,0,0,0])  ## Uncomment it to play // Comment for testing
enemy_grid.append([0,0,0,0,0,0,0,0,0,0])
enemy_grid.append([0,0,0,0,0,0,0,0,0,0])
enemy_grid.append([0,0,0,0,0,0,0,0,0,0])
enemy_grid.append([0,0,0,0,0,0,0,0,0,0])
enemy_grid.append([0,0,0,0,0,0,0,0,0,0])
enemy_grid.append([0,0,0,0,0,0,0,0,0,0])
enemy_grid.append([0,0,0,0,0,0,0,0,0,0])

def drawGrid(base_x, base_y, size):
    """Draw a grid with a base to start"""
    for i in range(0,11):
        line(base_x, base_y - i * size, base_x + 10 * size, base_y - i * size)
    for i in range(0,11):
        line(base_x + i * size, base_y, base_x + i * size, base_y - 10 * size)
    for i in range(0,10):
        path.penup()
        path.goto(base_x + i * size + 10, base_y + 10)
        path.write(chr(65+i))
    for i in range(1,11):
        path.penup()
        path.goto(base_x - 15 , base_y - i * size + 10)
        path.write(str(i))

def tap(x, y):
    """Respond to screen tap."""
    if insideGrid(x, y, base_player_grid_x, base_player_grid_y):  # Check if inside the player grid 
        updateGrid(x, y, True)
        drawSquareOnScreenGrid(base_player_grid_x, base_player_grid_y, player_grid)
    if insideGrid(x, y, base_enemy_grid_x, base_enemy_grid_y):  # Check if inside the player grid 
        updateGrid(x, y, False)
        drawSquareOnScreenGrid(base_enemy_grid_x, base_enemy_grid_y, enemy_grid)

def insideGrid(x, y, base_x, base_y):
    """Return True if the x,y is within the grid"""
    is_in_base_x = False
    is_in_base_y = False

    if (x >= base_x and x <= (base_x + (tiles_size * 10))):
        is_in_base_x = True
    
    if (y <= base_y and y >= (base_y - (tiles_size * 10))):
        is_in_base_y = True

    if (is_in_base_y and is_in_base_x):
        return True
    else :
        return False

def drawSquareOnScreenGrid(base_x, base_y, grid):
    for row in range (0,10):
        for column in range (0,10):
            place_x = (int)(base_x + (row * tiles_size)) + 0
            place_y = (int)(base_y - (column * tiles_size)) - 25
            if grid[column][row] == -1:
                square(place_x, place_y, tiles_size, "black")
            if grid[column][row] > 0 and grid[column][row] < 10 :
                square(place_x, place_y, tiles_size, "blue")
            if grid[column][row] == 10:
                square(place_x, place_y, tiles_size, "red")

def updateGrid(x, y, playerGrid):
    if playerGrid:
        column = (int)((y - base_player_grid_y) / tiles_size) * -1
        row = (int)((x - base_player_grid_x) / tiles_size)
        if (player_grid[column][row] > 0):
            player_grid[column][row] = 10
        if (player_grid[column][row] == 0):
            player_grid[column][row] = -1
    else:
        column = (int)((y - base_enemy_grid_y) / tiles_size) * -1
        row = (int)((x - base_enemy_grid_x) / tiles_size)
        if (enemy_grid[column][row] > 0):
            enemy_grid[column][row] = 10
        if (enemy_grid[column][row] == 0):
            enemy_grid[column][row] = -1 


setup(820, 400, 30, 0)
hideturtle()
tracer(False)
listen()
drawGrid(base_player_grid_x, base_player_grid_y, tiles_size)  # draw the player grid
drawGrid(base_enemy_grid_x, base_enemy_grid_y, tiles_size)    # draw the enemy grid
onscreenclick(tap)
done()