"""Game to practice typing.

Exercises

1. Change the speed of letters.
2. Add uppercase letters.
3. Make the game faster as the score gets higher.
4. Make the letters more frequent as the score gets higher.
"""

from random import choice, randrange
from string import ascii_lowercase
from turtle import *

from freegames import vector

targets = []
letters = []
score = 0


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw():
    """Draw letters."""
    clear()

    for target, letter in zip(targets, letters):
        goto(target.x, target.y)
        write(letter, align='center', font=('Consolas', 20, 'normal'))

    update()


def move():
    """Move letters."""
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(ascii_lowercase)
        letters.append(letter)

    for target in targets:
        target.y -= 1

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 100)


def press(key):
    """Press key."""
    global score

    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    else:
        score -= 1

    print('Score:', score)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
for letter in ascii_lowercase:
    onkey(lambda letter=letter: press(letter), letter)
move()
done()
