"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *
from freegames import vector

bird = vector(0, 0)
balls = []

def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

def draw():
    "Update objects and draw screen."
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)
        
    alive = inside(bird)

    for ball in balls:
        dodge = abs(ball - bird) > 15
        alive = alive and dodge

    if len(balls) > 30:
        balls.pop(0)

    clear()

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    update()

    if alive:
        ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
draw()
done()
