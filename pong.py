"""
Pong - Classic game of pong.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1.
"""

import sys, pygame, random
from pygame.locals import *

pygame.init()

lhs, rhs = x, y = 0, 1
width, height, fps = 320, 320, 20

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

white, black = (255, 255, 255), (0, 0, 0)

def draw():
    pygame.draw.rect(screen, black, (0, 0, width, height))
    pygame.draw.circle(screen, white, map(int, ball), 2)
    pygame.draw.rect(screen, white, paddle[lhs])
    pygame.draw.rect(screen, white, paddle[rhs])

def update():
    global dead

    ball[x] += motion[x]
    ball[y] += motion[y]

    if ball[x] <= 0 or ball[x] >= width:
        dead = True
        return

    if ball[y] <= 0 or ball[y] >= height:
        motion[y] *= -1
        motion[y] += random.random() - 0.5

    ball_rect = Rect(ball[x] - 2, ball[y] - 2, 4, 4)
    paddles = map(Rect, paddle)

    if (ball_rect.colliderect(paddles[lhs])
        or ball_rect.colliderect(paddles[rhs])):
        motion[x] *= -1
        motion[x] += random.random() - 0.5

def reset():
    global ball, motion, paddle, dead
    dead = False
    ball = [width / 2, height / 2]
    motion = [random.choice([-7, -6, -5, -4, 4, 5, 6, 7]) / 2.0,
              random.choice([-7, -6, -5, -4, 4, 5, 6, 7]) / 2.0]
    paddle = [[5, height / 2 - 20, 5, 40],
              [width - 10, height / 2 - 20, 5, 40]]

reset()

while True:
    clock.tick(fps)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_r:
            reset()
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))
        elif event.key == K_UP:
            paddle[rhs][y] -= 20
        elif event.key == K_DOWN:
            paddle[rhs][y] += 20
        elif event.key == K_e:
            paddle[lhs][y] -= 20
        elif event.key == K_d:
            paddle[lhs][y] += 20

    if not dead:
        update()
    draw()

    pygame.display.flip()
