"""
Maze game.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1. Change where the end is placed.
2. Change where the player starts.
3. Display only the player's immediate surroundings (no history).
"""

import sys, pygame
import random
from pygame.locals import *

"""Initialize system.
tiles represents how many squares the maze is made up of, block is the size of each tile.
size is a tuple representing (width,height) of the board.
dirs is a tuple containing the difference in index each direction is from the current location
view defines the difference in index the 3x3 space the user can currently see
hall wall boundary extra define the different tiles that can be within the maze.
red, green, blue, white, grey and black define RGB triplets for their corresponding colours.
"""
pygame.init()

tiles, block = 24, 20
size = width, height = (tiles * block), (tiles * block + 10)

dirs = up, right, down, left = (-tiles, 1, tiles, -1)  # Left and right are +1 or -1 index within the maze array, up and down are -width or +width
view = (up, right, down, left, up - 1, up + 1, down - 1, down + 1)  # Tuple defines a 3x3 (center omitted) space representing the tiles the player can see

hall, wall, boundary, extra = 0, 1, 2, 3  # Defines the type each tile can be

red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
white, grey, black = (255, 255, 255), (100, 100, 100), (0, 0, 0)

font = pygame.font.Font(None, 14)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

def make_maze():
    """Function to define the game world.
    The blank maze is generated and populated, finally the goal is placed.
    """
    global maze, player, end, moves

    # Create the initial, empty maze.

    maze = [boundary] * tiles
    maze += ([boundary] + [wall] * (tiles - 2) + [boundary]) * (tiles - 2)
    maze += [boundary] * tiles

    # Make the maze. This is a randomized version of Prim's algorithm
    # to build a minimum spanning tree.

    player = tiles + 1  # Defines starting location
    maze[player] = 0  # Set starting location to be a walkable tile (hall)
    frontier = [tiles + 2, 2 * tiles + 1]
    while len(frontier) > 0:
        pos = random.randrange(len(frontier))
        frontier[pos], frontier[-1] = frontier[-1], frontier[pos]
        spot = frontier.pop()

        if maze[spot] != wall: continue

        if map(lambda diff: maze[spot + diff], dirs).count(0) != 1:  # If there is not 1 hall connected to the current square
            continue

        maze[spot] = hall

        frontier.extend(map(lambda diff: spot + diff, dirs))  # Adds all directions around current square to frontier array

    # End goal should be farthest reachable hall.

    frontier = [player]
    while True:
        next = []  # Defines spaces further away than the current location
        for front in frontier:
            maze[front] = extra
            next.extend(filter(lambda pos: maze[pos] == hall,
                               map(lambda diff: front + diff, dirs)))  # Adds areas around current location to next if they are halls
        if next:  # If next has any entries
            frontier = next
        else:  # If no spaces are further away
            last = random.choice(frontier)  # Choose any space that is equally far away to be the goal
            break

    # Set all tiles of type extra to halls
    for pos, val in enumerate(maze):
        if val == extra: maze[pos] = hall

    moves = 0
    end = last

def draw_tile(func, color, pos):
    """draw_tile is given a function to draw with as well as a colour.
    This function is called while looping over every tile within the maze to
    draw each tile as either black or white if it is a hall or wall/boundary.
    """
    left = (pos % tiles) * block
    top = (pos / tiles) * block
    func(screen, color, (left, top, block, block))

def draw_maze():
    """draw_maze iterates through the maze list and uses draw_tile to draw
    the maze to the screen defined earlier.
    """
    for pos, val in enumerate(maze):  # for every tile, tile type in maze
        color = white if val == hall else black  # Specify a colour for that space
        draw_tile(pygame.draw.rect, color, pos)  # Draw it

def draw_view():
    """draw_view draws what the player has seen in the past and can currently see.
    This overwrites the initial state where all tiles are grey every time the player moves.
    """
    for diff in view:  # For each tile in the defined 3x3 window the player can see
        pos = player + diff  # Defines position of square to be drawn
        color = white if maze[pos] == hall else black  # Chooses colour for current square
        draw_tile(pygame.draw.rect, color, pos)  # Draws the specified tile with the specified colour

    draw_tile(pygame.draw.rect, white, player)  # Draws the space the player is on white.
    draw_tile(pygame.draw.rect, green, end)  # Draws the goal green.
    draw_tile(pygame.draw.ellipse, blue, player)  # Draws the player over the square they are on as a blue elipse.

    pygame.draw.rect(screen, (0, 0, 0), (0, width, width, 10))  # Draws main screen
    surface = font.render(str(moves), True, (255, 255, 255))  # Counter keeping track of the users total moves. 
    screen.blit(surface, (5, tiles * block))  # Draws the total number of moves in the bottom left corner.

    pygame.display.flip()  # Function that updates the display

def restart():
    """Restarts the game by creating an entirely new maze and drawing it grey"""
    make_maze()
    pygame.draw.rect(screen, grey, (0, 0, width, height))
    draw_view()

restart()

while True:
    """Main loop of the system.
    Gathers an event, and processes it each iteration.
    Moves the player if the player has chosen to move.
    Updates the screen.
    """
    clock.tick(12)  # Every second 12 frames will happen

    event = pygame.event.poll()  # Gets an event from the event queue
    move_dir = None

    if event.type == pygame.QUIT:  # If the event is a quit event
        pygame.quit()  # Close the game
        sys.exit()
    elif event.type == KEYDOWN:  # If the event is a button press
        if event.key == K_UP:
            move_dir = up
        elif event.key == K_RIGHT:
            move_dir = right
        elif event.key == K_DOWN:
            move_dir = down
        elif event.key == K_LEFT:
            move_dir = left
        elif event.key == K_r:
            restart()
        elif event.key == K_s:
            draw_maze()
            draw_view()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))  # Add a quit event to the top of the queue

    if player == end: continue  # If the player has reached the end of the maze we do not want them to be able to move, end the loop iteration here

    if move_dir is not None:  # If the player has chosen to move
        if maze[player + move_dir] == hall:  # If the player is moving into an open space
            player += move_dir  # Move the player
            moves += 1
        draw_view()

    pygame.display.flip()
