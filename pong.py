"""
Pong - Classic game of pong.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1. Change how the ball bounces.
"""

import sys, pygame, random
from pygame.locals import *

"""
Initalize game start state. Used to setup before the game begins.
Width and height define the size of the game window
Clock is used to restrict framerate to the value stored in fps
lhs and rhs define where the paddles of each player will be placed
Screen defines a window for the game to be played, calibrated to the width and height parameters
White and black define RGB triplets for their corresponding colour
"""
pygame.init()

lhs, rhs = x, y = 0, 1
width, height, fps = 320, 320, 20

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

white, black = (255, 255, 255), (0, 0, 0)

def draw():
    """Function to draw each item to the screen. Called each frame."""
    pygame.draw.rect(screen, black, (0, 0, width, height))  # Draws the entire screen to be black. This overwrites the previous locations of where the ball and paddles used to be.
    pygame.draw.circle(screen, white, map(int, ball), 2)  # Draws the ball at its current location.
    pygame.draw.rect(screen, white, paddle[lhs])  # Draws the left paddle at its current location
    pygame.draw.rect(screen, white, paddle[rhs])  # Draws the right paddle at its current location

def update():
    """Function to update the position of the ball each frame.
    If the ball hits the left or right screen boundaries we end the game.
    If the ball hits the top or bottom the vertical motion is inverted and changed to a random value.
    If the ball hits a paddle the horizontal movement is inverted and changed to a random value.
    """
    global dead

    ball[x] += motion[x]
    ball[y] += motion[y]

    if ball[x] <= 0 or ball[x] >= width:  # If the ball gets past either paddle, hitting the edge of the screen
        dead = True
        return

    if ball[y] <= 0 or ball[y] >= height:  # If the ball hits the ceiling or floor
        motion[y] *= -1
        motion[y] += random.random() - 0.5  # Increment the vertical velocity by -0.5 to 0.5 

    ball_rect = Rect(ball[x] - 2, ball[y] - 2, 4, 4)  # Creates a rect around the ball
    paddles = map(Rect, paddle)  # Creates a rect around each paddle, used for collision detection with ball_rect

    if (ball_rect.colliderect(paddles[lhs])
        or ball_rect.colliderect(paddles[rhs])):  # If the ball hits either paddle
        motion[x] *= -1
        motion[x] += random.random() - 0.5  # Increment the horizontal velocity by -0.5 to 0.5 

def reset():
    """Resets the system to the initial state.
    Dead is set to False to signify the system being active
    The ball and paddle define the initial locations for their respective objects to be drawn
    Motion defines a random direction for the ball to move
    """
    global ball, motion, paddle, dead
    dead = False
    ball = [width / 2, height / 2]
    motion = [random.choice([-7, -6, -5, -4, 4, 5, 6, 7]) / 2.0,
              random.choice([-7, -6, -5, -4, 4, 5, 6, 7]) / 2.0]  # Sets x and y motion to be a random direction chosen from the values in the list
    paddle = [[5, height / 2 - 20, 5, 40],
              [width - 10, height / 2 - 20, 5, 40]]  # Sets the paddles to the middle of the screen on their proper side

reset()

while True:
    """Main loop that controls the system.
    Will always delay to run at most fps times per second.
    The system gets the most recent event from the event queue, often being user input.
    This event is then processed if it is either a quit command or button press. 
    Finally the update function is called.
    """
    clock.tick(fps)

    event = pygame.event.poll()

    # Handle the event if it is either a quit or button press
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:  # If the event type is a button press
        if event.key == K_r:  # If r key is pressed
            reset()
        elif event.key == K_q:  # If q key is pressed
            pygame.event.post(pygame.event.Event(QUIT))  # Add to event queue the quit event. This will be processed next frame
        elif event.key == K_UP:  # If up arrow key is pressed
            paddle[rhs][y] -= 20  # Move right paddle down 20 pixels
        elif event.key == K_DOWN:  # If up down key is pressed
            paddle[rhs][y] += 20  # Move right paddle up 20 pixels
        elif event.key == K_e:  # If e key is pressed
            paddle[lhs][y] -= 20  # Move left paddle down 20 pixels
        elif event.key == K_d:  # If d key is pressed
            paddle[lhs][y] += 20  # Move left paddle up 20 pixels

    if not dead:
        update()
    draw()

    pygame.display.flip()  # Update the screen, actually draws things previously specified to be displayed
