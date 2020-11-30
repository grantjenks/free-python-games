"""Sudoku, japanese number Puzzle

Exercises

...

"""

from turtle import *
from random import randrange
from freegames import square, vector, line



setup(1000, 1000, 370, 0)
title("sudoku")
hideturtle()
penup()
goto(-130, 300)
pendown()
write("SUDOKU", font = ("consolas", 50, "bold"))    # 문자 쓰기
#textinput()
hideturtle()
done()
