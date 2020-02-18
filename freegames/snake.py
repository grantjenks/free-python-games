"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
import time

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def printTitle():
    penup()
    goto(120,50)
    pendown()
    color('red')
    style = ('courier', 35, 'italic')
    write('YOU HAVE LOST', font=style, align='right')
    hideturtle()
    
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def lost():
    '''New'''
    printTitle()
    print('YOU HAVE LOST')
    time.sleep(3) 
    bye()
    SystemExit()                   

def wall(head,x,y):
    if x == (-200):
        head.x = 190
        head.y = y
        head = (head.x, head.y)
        return(head)
    if y == (-200):
        head.x = x
        head.y = 190
        head = (head.x, head.y)
        return(head)
    if x == (190):
        head.x = -200
        head.y = y
        head = (head.x, head.y)
        return(head)
    if y == (190):
        head.x = x
        head.y = -200
        head = (head.x, head.y)
        return(head)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    game = 1

    if head in snake:
        game = 0
        for body in snake:
            square(body.x, body.y, 9, 'red')
        '''return(head)'''

    if game == 0:
        lost()
        return (head)
    

    if not inside(head):
        wallx = head.x
        wally = head.y
        wall(head, wallx, wally)
        
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'yellow')
    update()
    ontimer(move, 90 )

setup(420, 420, 370, 0)
bgcolor('black')
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
