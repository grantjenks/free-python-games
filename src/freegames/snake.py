"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How do you make the snake change color?
3. How do you make the snake respond to the mouse?
4. How would you improve the snake's intelligence?

"""

from random import randrange
from turtle import (
    Screen,
    Turtle,
    addshape,
    clear,
    hideturtle,
    listen,
    ontimer,
    onkey,
    setup,
    tracer,
    update,
    done,
)
from freegames import square, vector

# --- Constants & Game State ---
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# NEW: State to manage game flow ('start', 'playing', 'over')
state = {'current': 'start'}
# NEW: Writer turtle for displaying messages
writer = Turtle(visible=False)

# --- Game Functions ---

def change(x, y):
    """Change snake direction."""
    if state['current'] != 'playing':
        return
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 <= head.x <= 190 and -200 <= head.y <= 190

def display_message(message):
    """Display a message in the center of the screen."""
    writer.clear()
    writer.penup()
    writer.goto(0, 0)
    writer.color('white')
    writer.write(message, align="center", font=("Arial", 16, "normal"))

def reset_game():
    """Reset all game variables to their initial state."""
    global food, snake, aim
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    state['current'] = 'start'

def start_game():
    """Start the game loop."""
    if state['current'] == 'start':
        state['current'] = 'playing'
        writer.clear()
        move()

def restart_game():
    """Clear the screen and restart the game."""
    if state['current'] == 'over':
        reset_game()
        clear()  # Turtle's clear screen function
        setup_game()  # Re-initialize the game setup
        display_message("Press SPACE to start")

def move():
    """Move snake one segment."""
    # NEW: Only move if in 'playing' state
    if state['current'] != 'playing':
        return

    head = snake[-1].copy()
    head.move(aim)

    # NEW: Check for game over
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        state['current'] = 'over'
        display_message("Game Over! Press 'R' to Restart")
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

    # NEW: Continue game loop only if 'playing'
    if state['current'] == 'playing':
        ontimer(move, 100)

def setup_game():
    """Set up the game window, controls, and initial state."""
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    # NEW: Bind Start and Restart keys
    onkey(start_game, 'space')
    onkey(restart_game, 'r')

# --- Main Game Execution ---
setup_game()
display_message("Press SPACE to start")
done()
