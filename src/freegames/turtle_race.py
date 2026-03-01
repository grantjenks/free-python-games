from turtle import *
from random import randint

def set_race():
    """Start from top left"""
    setup(420, 420, 370, 0)
    speed(0)
    penup()
    goto(-140, 140)

    """Draw finish line"""
    for step in range(15):
        write(step, align="center")
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

    """Set the colors of the players"""
    colors = ["green", "red", "blue", "orange"]
    all_turtles = []

    """Assign the colors"""
    for i in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-160, 100 - (i * 30))
        all_turtles.append(new_turtle)

    """Race players one by one"""
    for t in all_turtles:
        t.forward(randint(1, 5))

set_race()
done()