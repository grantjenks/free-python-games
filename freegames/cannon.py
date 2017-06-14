"""Cannon, hitting targets with a cannon.

Exercises

1.

"""

from random import randrange
from turtle import *
from freegames import vector

cannon = vector(100, 100)
balls = []
speeds = []
targets = []

def tap(x, y):
    ball = vector(-200, -200)
    balls.append(ball)
    speed = (vector(x, y) + 200) / 50
    speeds.append(speed)

def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    clear()

    if randrange(10) == 0:
        y = randrange(-200, 200)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1
        goto(target.x, target.y)
        dot(20, 'blue')

    for index in range(len(balls)):
        ball = balls[index]
        speed = speeds[index]
        speed.y -= 0.02
        ball += speed
        goto(ball.x, ball.y)
        dot(2, 'red')

    hits = targets.copy()
    targets.clear()

    for target in hits:
        if all(abs(target - ball) > 12 for ball in balls):
            targets.append(target)

    duds = balls.copy()
    balls.clear()

    for ball in duds:
        if inside(ball):
            balls.append(ball)  # Ooops, must update speed!

    update()
    ontimer(draw, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
draw()
done()
