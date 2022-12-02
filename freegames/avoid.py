"""Avoid, classic arcade game.

Exercises

1. Check the time you've lived.
2. Vary the person's speed & bomb's speed.
3. Vary the size of the bombs.
4. Vary the person's color & bomb's color.
"""
from random import *
from turtle import *
import time
from freegames import vector

person = vector(0, 0)
bombs = []
speeds = []
aim = vector(0, 0)
start = time.time()

def change(x, y):
    """Change person direction."""
    aim.x = x
    aim.y = y

def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    """Draw screen objects."""
    clear()
    goto(person.x, person.y)
    if alive:
        dot(10, 'blue')
    else:
        dot(10, 'red')
    for bomb in bombs:
        goto(bomb.x, bomb.y)
        dot(20, 'black')

    present = time.time()
    print('\rtime : %.3f' %float(present-start), end='sec')
    update()

def move():
    """Update object positions."""
    person.move(aim)

    for bomb, speed in zip(bombs, speeds):
        bomb.move(speed)

    if randrange(10) == 0:
        x = randrange(-199, 199)
        y = randrange(-199, 199)
        dir = randrange(4)
        s = randrange(3, 11)
        if dir == 0:
            bomb = vector(x, 199)
            speed = vector(0, -s)
        elif dir == 1:
            bomb = vector(x, -199)
            speed = vector(0, s)
        elif dir == 2:
            bomb = vector(199, y)
            speed = vector(-s, 0)
        else:
            bomb = vector(-199, y)
            speed = vector(s, 0)
        bombs.append(bomb)
        speeds.append(speed)

    while len(bombs) > 0 and not inside(bombs[0]):
        bombs.pop(0)
        speeds.pop(0)

    if not inside(person):
        draw(False)
        return

    for bomb in bombs:
        if abs(bomb - person) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
move()
done()