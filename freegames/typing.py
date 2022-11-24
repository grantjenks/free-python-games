""" Typing, typing game to remove the same letters.

Exercises

1. Change the speed of letters.
2. Change letters to simple words.
3. Add bonus words.

"""
from random import *
from turtle import *
from freegames import vector

targets = []
letters = []
score = 0

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Draw letters."""
    clear()
    count = 0
    for target in targets:
        goto(target.x, target.y)
        write(letters[count], align='center', font=('Consolas', 20, 'normal'))
        count += 1
    update()

def move():
    """Move letters."""
    if randrange(10) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        while True:
            letter = chr(ord('a') + randrange(26))
            if letter not in letters:
                letters.append(letter)
                break
    for target in targets:
        target.y -= 5
    draw()
    for target in targets:
        if not inside(target):
            return
    ontimer(move, 50)

def press(c):
    """Press key."""
    global score
    if c in letters:
        score += 1
        k = letters.index(c)
        targets.pop(k)
        letters.pop(k)
        print('\rscore:', score, end = '\t')
    else:
        score -= 1
        print('\rscore:', score, end='\t')

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
onkey(lambda: press('a'), 'a')
onkey(lambda: press('b'), 'b')
onkey(lambda: press('c'), 'c')
onkey(lambda: press('d'), 'd')
onkey(lambda: press('e'), 'e')
onkey(lambda: press('f'), 'f')
onkey(lambda: press('g'), 'g')
onkey(lambda: press('h'), 'h')
onkey(lambda: press('i'), 'i')
onkey(lambda: press('j'), 'j')
onkey(lambda: press('k'), 'k')
onkey(lambda: press('l'), 'l')
onkey(lambda: press('m'), 'm')
onkey(lambda: press('n'), 'n')
onkey(lambda: press('o'), 'o')
onkey(lambda: press('p'), 'p')
onkey(lambda: press('q'), 'q')
onkey(lambda: press('r'), 'r')
onkey(lambda: press('s'), 's')
onkey(lambda: press('t'), 't')
onkey(lambda: press('u'), 'u')
onkey(lambda: press('v'), 'v')
onkey(lambda: press('w'), 'w')
onkey(lambda: press('x'), 'x')
onkey(lambda: press('y'), 'y')
onkey(lambda: press('z'), 'z')
move()
done()