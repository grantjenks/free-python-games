"""Snake, classic arcade game.

Excercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def square(x, y, size, name):
    "Draw square at x, y with given size and color."
    up()
    goto(x, y)
    down()
    color(name)
    begin_fill()
    for i in range(4):
        forward(size - 1)
        left(90)
    end_fill()

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 10, 'red')
        update()
        return

    square(head.x, head.y, 10, 'black')
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        tail = snake.pop(0)
        square(tail.x, tail.y, 10, 'white')

    square(food.x, food.y, 10, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
