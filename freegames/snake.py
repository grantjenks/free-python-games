"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

1. Como você deixa a cobra mais rápida ou mais lenta? FEITO
2. Como você pode fazer a cobra contornar as bordas? 
3. Como você moveria a comida?
4. Mude a cobra para responder às teclas de seta FEITO
"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0) #posição inicial da comida
snake = [vector(10, 0)]#posição inicial da cobra
aim = vector(0,-10) # velocidade/direção da cobra

def change(x, y):
    "Change snake direction."#"Mudar a direção da cobra."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."#"Retorne True se a cabeça estiver dentro dos limites."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment." #Mova a cobra um segmento para frente
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake: # caso a cobra encoste nas bordas
        square(head.x, head.y, 9, 'red')# desenha um dradrado vermelho
        update()
        return

    snake.append(head) #adiciona um quadrado na direção aim no vetor snake

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10 #novo X da comida no intervalo determinado
        food.y = randrange(-15, 15) * 10 #novo Y da comida no intervalo determinado
    else:
        snake.pop(0) # remove o quadrado da posição anterior do vetor snake

    clear()
    #tamanho do corpo da cobra em relação ao vetor snake
    for body in snake:
        square(body.x, body.y, 9, 'black')
    #tamanho da comida
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
move()
done()