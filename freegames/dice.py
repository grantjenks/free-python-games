from turtle import *
import random
from freegames import *
import time

def dice(sides):
    options = []
    a=0
    for i in range (0,sides):
        a+=1
        options.append(a)
    random.shuffle(options)
    return options

def run():
    sides = int(input("Please enter number of sides:"))
    setup(420, 420, 370, 0)
    bgcolor('light blue')
    hideturtle()
    tracer(False)
    options = dice(sides)
    roll(options)
    done()

def roll(options):
    for i in range(0 , 20):
        penup()
        goto(0, 0)
        pendown()
        square(-50, -10, 100, 'white')
        penup()
        goto(0, 0)
        pendown()
        color("black")
        write(random.choice(options), align='center',font=("Arial", 50, "normal"))
        time.sleep(0.3)

def main():
    run()

main()