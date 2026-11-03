"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
started = False


def change(x, y):
    """Change snake direction."""
    if not started:
        return

    aim.x = x
    aim.y = y


def start_game(x, y):
    """Start the game when the start button is clicked."""
    global started

    if started or not (-80 <= x <= 80 and -25 <= y <= 25):
        return

    started = True
    onscreenclick(None)
    clear()
    move()


def draw_start_button():
    """Draw the start button."""
    up()
    goto(-80, -25)
    color('black', 'light gray')
    down()
    begin_fill()
    for _ in range(2):
        forward(160)
        left(90)
        forward(50)
        left(90)
    end_fill()
    up()
    goto(0, -18)
    color('black')
    write('Start Game', align='center', font=('Arial', 16, 'bold'))


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
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
draw_start_button()
onscreenclick(start_game)
done()
