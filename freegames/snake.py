"Classic arcade game Snake."

from turtle import *
from random import randrange

xdir = [10, 0, -10, 0]  # right, up, left, down
ydir = [0, 10, 0, -10]
state = {'food': [0, 0], 'snake': [[10, 0], [20, 0]], 'direction': 0}

def square(x, y, size, name):
    "Draw square at x, y with given size and color."
    tracer(False)
    up()
    goto(x, y)
    color(name)
    down()
    begin_fill()

    for i in range(4):
        forward(size - 1)
        left(90)

    end_fill()
    tracer(True)

def tap(x, y):
    "Change snake direction."
    if x > y and x > -y:
        state['direction'] = 0  # right
    elif x < y and -x < y:
        state['direction'] = 1  # up
    elif -x > y and -x > -y:
        state['direction'] = 2  # left
    elif -x < -y and x < -y:
        state['direction'] = 3  # down

def move():
    "Move snake forward one segment."
    snake = state['snake']
    last = snake[-1]
    direction = state['direction']
    xnew = last[0] + xdir[direction]
    ynew = last[1] + ydir[direction]
    head = [xnew, ynew]

    if head in snake:
        square(xnew, ynew, 10, 'red')
        return

    if not (-200 <= xnew < 200 and -200 <= ynew < 200):
        square(xnew, ynew, 10, 'red')
        return

    square(xnew, ynew, 10, 'white')
    snake.append(head)
    food = state['food']

    if head == food:
        print('Snake:', len(snake))
        food[0] = randrange(-15, 15) * 10
        food[1] = randrange(-15, 15) * 10
    else:
        tail = snake.pop(0)
        square(tail[0], tail[1], 10, 'black')

    square(food[0], food[1], 10, 'green')
    ontimer(move, 100)

reset()
hideturtle()
listen()
onscreenclick(tap)
square(-200, -200, 400, 'black')
move()
done()
