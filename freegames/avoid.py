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
bombs1 = []
bombs2 = []
bombs3 = []
bombs4 = []
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
        dot(10, 'black')
    else:
        dot(10, 'red')
    for bomb1, bomb2, bomb3, bomb4 in zip(bombs1, bombs2, bombs3, bombs4):
        goto(bomb1.x, bomb1.y)
        dot(20, 'blue')
        goto(bomb2.x, bomb2.y)
        dot(20, 'blue')
        goto(bomb3.x, bomb3.y)
        dot(20, 'blue')
        goto(bomb4.x, bomb4.y)
        dot(20, 'blue')
    present = time.time()
    print('\rtime : %.3f' %float(present-start), end='sec')
    update()

def move():
    """Update object positions."""
    person.move(aim)

    for bomb1, bomb2, bomb3, bomb4 in zip(bombs1, bombs2, bombs3, bombs4):
        bomb1.y -= 7
        bomb2.y += 7
        bomb3.x -= 7
        bomb4.x += 7

    if randrange(5) == 0:
        x = randrange(-199, 199)
        y = randrange(-199, 199)
        bomb1 = vector(x, 199)
        bomb2 = vector(x, -199)
        bomb3 = vector(199, y)
        bomb4 = vector(-199, y)
        bombs1.append(bomb1)
        bombs2.append(bomb2)
        bombs3.append(bomb3)
        bombs4.append(bomb4)

    while len(bombs1) > 0 and not inside(bombs1[0]):
        bombs1.pop(0)
    while len(bombs2) > 0 and not inside(bombs2[0]):
        bombs2.pop(0)
    while len(bombs3) > 0 and not inside(bombs3[0]):
        bombs3.pop(0)
    while len(bombs4) > 0 and not inside(bombs4[0]):
        bombs4.pop(0)

    if not inside(person):
        draw(False)
        return

    for bomb1, bomb2, bomb3, bomb4 in zip(bombs1, bombs2, bombs3, bombs4):
        if abs(bomb1 - person) < 15 or abs(bomb2 - person) < 15 or abs(bomb3 - person) < 15 or abs(bomb4 - person) < 15 :
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
