"""Sudoku, japanese number Puzzle

Exercises

...

"""

from turtle import *
from random import randrange
from freegames import square, vector, line

# def sudoku_load 를 정의한다. -> 실행할 때마다 현재 sudoku 상태를 입력된 숫자를 base로 업데이트
                              #입력된 것이 1~9가 아닐경우 에러 메세지를 출력한다.
                              #입력된 것이 한줄 혹은 한 박스를 모두 채우면 색깔을 바꾼다?
                              #입력된 숫자는 업데이트 할 수 있어야 한다.
                              

# def sudoku_restart를 정의한다. -> 초기화 한다.

# def game_start를 정의한다. -> game start 버튼을 생성한다. 누르면 sudoku_load 한다. 

setup(1000, 1000, 370, 0)
title("sudoku")
hideturtle()
penup()
goto(-130, 300)
pendown()
write("SUDOKU", font = ("consolas", 50, "bold"))    # 문자 쓰기
hideturtle()
done()
