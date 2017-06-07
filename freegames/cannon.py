"""Cannon - hitting a target with a cannon.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
0. Explore the effect of drag.
1. Make the target smaller.
2. Make the ball larger.
3. Move the target off the ground.

"""

import sys, pygame
from pygame.locals import *
from random import randrange
from itertools import count

pygame.init()

font = pygame.font.Font(None, 14)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((480, 480))

# Define colors.

white, black, purple = (255, 255, 255), (0, 0, 0), (200, 0, 200)

def reset():
    """Reset game settings."""
    global score, target
    score, target = 0, randrange(200, 450)

def redraw():
    """Redraw screen and settings."""
    global ball, xspeed, yspeed
    ball, xspeed, yspeed = None, 3.0, -6.0

    screen.fill(black)
    pygame.draw.line(screen, white, (0, 475), (480, 475), 11)
    pygame.draw.rect(screen, white, (20, 460, 10, 10))
    pygame.draw.line(screen, white, (25, 465), (35, 455), 3)
    pygame.draw.rect(screen, purple, (target, 450, 20, 20))

# Initialize start of game play.

drag = False
reset()
redraw()

for counter in count():
    if counter % 5 == 0:
        clock.tick(24)

    event = pygame.event.poll()

    # Handle pygame events.

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:

        # Handle user input.

        if event.key == K_SPACE:
            ball = (30.0, 460.0, xspeed, yspeed)
        elif event.key == K_UP:
            yspeed -= 0.1
        elif event.key == K_DOWN:
            yspeed += 0.1
        elif event.key == K_RIGHT:
            xspeed += 0.1
        elif event.key == K_LEFT:
            xspeed -= 0.1
        elif event.key == K_d:
            drag = (not drag)
        elif event.key == K_r:
            redraw();
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if ball is not None:

        # Update the ball's position.

        east, south, right, down = ball

        if drag:
            # Calculate the effect of air resistance (sort of).

            velocity = (right ** 2 + down ** 2) ** 0.5
            dragf = 0.005 * velocity ** 2
            down += (-down / velocity) * dragf
            right -= (right / velocity) * dragf

        # Update the velocity down due to gravity.

        down += 0.1   # gravity

        # Calculate the new position of the ball.

        east += right # xf = v * t + xi
        south += down # south_final = down_pixels/frame * 1_frame + south_initial

        ball = (east, south, right, down)

        # Draw the ball.

        ballrect = pygame.Rect(ball[0], ball[1], 3, 3)
        pygame.draw.rect(screen, white, ballrect)

        # Detect ball out of screen boundary.

        if not (0 < south < 480 and 0 < east < 480):
            ball = None

        # Detect ball hitting target.

        targetrect = pygame.Rect(target, 450, 20, 20)

        if targetrect.colliderect(ballrect):
            score += 1
            target = randrange(200, 450)
            redraw()

    # Draw text to the screen.

    pygame.draw.rect(screen, black, (0, 0, 120, 30))
    scoredisplay = font.render('score: ' + str(score), True, white)
    xdisplay = font.render('xspeed: ' + str(xspeed), True, white)
    ydisplay = font.render('yspeed: ' + str(-yspeed), True, white)
    screen.blit(scoredisplay, (0, 0))
    screen.blit(xdisplay, (0, 10))
    screen.blit(ydisplay, (0, 20))

    pygame.display.flip()
