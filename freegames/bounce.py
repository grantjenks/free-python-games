"""Bounce, a simple animation demo.

Exercises

1. Make the ball speed up and down.
2. Change how the ball bounces when it hits a wall.
3. Make the ball leave a trail.
4. Change the ball color based on position.

"""

from random import *
from turtle import *
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())

def draw():
    "Move ball and draw game."
    ball.move(aim)

    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x

    if y < -200 or y > 200:
        aim.y = -aim.y

    clear()
    goto(x, y)
    # color(abs(ball.x), abs(ball.y), 200)
    dot(10)

    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
# colormode(255)
draw()
done()
