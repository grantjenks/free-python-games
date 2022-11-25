"""TurtleRace, classic race game.

Exercises

1. Change the speed of obstacle.
2. Change the generation frequency of obstacle.
3. Change the color of obstacle.
3. Upgrade 3-line race to 5-line race.
"""

from freegames import line
from freegames import vector
from turtle import *
from random import choice, random

turtle = vector(-5, -160)
obstacle_speed = -2
ob_timer = 0
obstacle = []


def raceline():
    """Draw two race lines."""
    line(-20, 200, -20, -200)
    line(10, 200, 10, -200)


def move(change):
    """Move player position by change."""
    if -30 <= turtle.x + change <= 20:
        turtle.move(vector(change, 0))


def draw():
    """Draw game, move obstacles and player."""
    clear()

    raceline()

    if ob_timer > 40 and random() > 0.8:
        obstacle.append(vector(-25 * choice([-1, 0, 1]) - 5, 200))
        ob_timer = 0
    else:
        ob_timer += 1

    for i in range(len(obstacle)):
        up()
        goto(obstacle[i].x, obstacle[i].y)
        dot(10, 'red')

    for i in range(len(obstacle)):
        obstacle[i].move(vector(0, obstacle_speed))

    x = turtle.x
    y = turtle.y

    up()
    goto(x, y)
    dot(10)

    for i in range(len(obstacle)):
        if obstacle[i].__eq__(vector(x, y)):
            done()

    ontimer(draw, 5)


setup(width=100, height=400)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(25), 'd')
onkey(lambda: move(-25), 'a')
draw()

done()
