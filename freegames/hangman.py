"""Hangman, a letter guessing game

Exercises
1. Change Hangman's picture (position, length, etc)
2. Make an additional dictionary, not fruits
3. Convert lowercase letters to uppercase letters
"""

from turtle import *
from random import choice
import functools

def screen_write(letter):
    """write text on the screen"""
    write(letter, move=True, font=("Courier", 14, "normal"))

def move_write(x, y, letter):
    """After move, write text on the screen"""
    goto(x, y)
    screen_write(letter)


def draw(x, y, angle, length, straight):
    """draw a hangman game"""
    goto(x, y)
    pendown()
    left(angle)
    if straight:
        forward(length)
    else:
        circle(length, None, 100)
    penup()

def draw_Hangman(step):
    if step == 1: 
        # draw head
        draw(-45, 160, 270, 15, False)
    elif step == 2:
        # draw torso
        draw(-45, 130, 90, 40, True)
    elif step == 3:
        # draw left arm
        draw(-45, 120, 235, 40, True)
    elif step == 4:
        # draw right arm
        draw(-45, 120, 250, 40, True)
    elif step == 5:
        # draw left leg
        draw(-45, 90, 205, 40, True)
    elif step == 6:
        # draw right leg
        draw(-45, 90, 60, 40, True)

def guess(letter):
    global correct
    global use
    global wrong
    global finish
    if not finish:
        if letter not in use:
            goto(-100,-35)
            for i in word:
                if i == letter:
                    screen_write(letter.lower() + " ")
                    correct += letter
                else:
                     screen_write("_ ") 
            use += letter 
            if letter not in word:
                wrong += 1
                draw_Hangman(wrong)
            move_write(-200, -100, "Guesses: ")
            for i in use:
                screen_write(i.lower() + " ")
        if wrong == 6:
            goto(-100,-35)
            for i in word:
                if i in correct:
                    screen_write("_ ")
                else:
                    screen_write(i.lower() + " ")
            move_write(-130, -60, "Sorry, you lose!")
            finish = True
        if len(correct) == len(word):
            move_write(-130, -60, "Congratulations, you win!")
            finish = True

hideturtle()
speed(0)

fruitword = ['apple', 'banana', 'blueberry', 'cherry', 'coconut', 'durian', 'grape', 'kiwi', 'lemon',
            'lime', 'mango', 'melon', 'orange', 'peach', 'pear', 'pineapple', 'strawberry','watermelon']

"""draw gallows"""
penup()
draw(50, 0, 90, 175, True)
draw(50, 175, 90, 95, True)
draw(-45, 175, 90, 15, True)

goto(-100,-35)
word = choice(fruitword)
correct = []
use = []
wrong = 0
finish = False
for i in word:
    screen_write("_ ")
for ascii in range(ord('a'), ord('z')+1):
    letter = chr(ascii)
    onkey(functools.partial(guess, letter), letter)    
listen()
done()