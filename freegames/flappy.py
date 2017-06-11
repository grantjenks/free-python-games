"""Flappy Bird Clone

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
    up = vector(0, 40)
    bird.move(up)

def inside(point):
    return -200 < point.x < 200 and -200 < point.y < 200

def draw():
    alive = True

    bird.y -= 5

    for ball in balls:
        ball.x -= 2

    if randrange(20) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)
        
    alive &= inside(bird)

    for ball in balls:
        alive &= abs(ball - bird) > 15

    balls[:] = [ball for ball in balls if inside(ball)]

    clear()
    goto(bird.x, bird.y)
    dot(10, 'green')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()

    if alive:
        ontimer(draw, 50)

def start(x, y):
    draw()
    onscreenclick(tap)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(start)
done()
