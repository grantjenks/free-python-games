"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower.
2. Stop a tron player from running into itself.
3. Allow the tron player to go around the edge of the screen.
4. How would you create a computer player?

"""

from turtle import *
from freegames import square, vector

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    "Return True if head inside screen."
    return -300 < head.x < 300 and -300 < head.y < 300

def draw():
    "Advance players and draw game."
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body:
        print('Player blue wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player red wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)

setup(620, 620, 570, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(0), 'Right')
onkey(lambda: p1aim.rotate(180), 'Left')
onkey(lambda: p1aim.rotate(90), 'Up')
onkey(lambda: p1aim.rotate(270), 'Down')

onkey(lambda: p2aim.rotate(90), 'w')
onkey(lambda: p2aim.rotate(270), 's')
onkey(lambda: p2aim.rotate(180), 'a')
onkey(lambda: p2aim.rotate(0), 'd')
draw()
done()
