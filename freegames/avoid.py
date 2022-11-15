from random import *
from turtle import *
import time
from freegames import vector

person = vector(0, 0)
balls = []
aim = vector(0, 0)
start = time.time()

def change(x, y):
    """Change snake direction."""
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

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'blue')
    present = time.time()
    print('\rtime : %.3f' %float(present-start), end='sec')
    update()

def move():
    """Update object positions."""
    person.move(aim)

    for ball in balls:
        ball.y -= 7

    if randrange(5) == 0:
        x = randrange(-199, 199)
        ball = vector(x, 199)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(person):
        draw(False)
        return

    for ball in balls:
        if abs(ball - person) < 15:
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
