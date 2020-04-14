#Common imports used on other projects here for now
from random import *
from turtle import *
from freegames import vector

def draw():
    #Placeholder for rendering
    return 0

def generateSudoku():
    #Make a board
    board=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
           ]
    #Now we need to randomize the numbers
    numbers=[1,2,3,4,5,6,7,8,9]

    #Now  we need to insert these back into the board and make sure they go in legal positions


    #Return the board
    return board
