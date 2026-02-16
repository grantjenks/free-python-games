"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
5. How can you change the design of the start menu?
6. How would you change the button required to start the game?
"""

from random import randrange
from turtle import *
from freegames import square, vector
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
game_started = False 
"""Variable to determine game state, needed to prevent infinite loop"""

def start_game():
    """Clear the screen and start the game loop."""
    global game_started
    if game_started:
        return 
    game_started = True
    clear() 
    move()  

def draw_start_screen():
    """Draws the initial menu text."""
    clear()
    up()
    goto(0, 50)
    color('black')
    write("SNAKE", align="center", font=("Courier", 30, "bold"))
    
    goto(0, -50)
    write("Press SPACE to Start", align="center", font=("Courier", 16, "normal"))
    update()

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


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
"""Sets up start menu"""
onkey(start_game, 'space')
draw_start_screen()
done()
