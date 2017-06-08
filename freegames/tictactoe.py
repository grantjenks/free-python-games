"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?

"""

from turtle import *

turns = {'X': 'O', 'O': 'X'}
state = {'player': 'X'}

def line(a, b, x, y):
    "Draw line from (a, b) to (x, y)."
    up()
    goto(a, b)
    down()
    goto(x, y)

def grid():
    "Draw tic-tac-toe grid."
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)
    update()

def tap(x, y):
    "Draw X or O in tapped square."
    x = ((x + 200) // 133) * 133 - 200
    y = ((y + 200) // 133) * 133 - 200

    player = state['player']

    if player == 'X':
        line(x, y, x + 133, y + 133)
        line(x, y + 133, x + 133, y)
    elif player == 'O':
        up()
        goto(x + 67, y + 5)
        down()
        circle(62)

    update()
    state['player'] = turns[player]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
listen()
onscreenclick(tap)
done()
