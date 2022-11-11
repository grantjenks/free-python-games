"""hangman, letter guessing game

Exercises
1. Change Hangman's picture (position, length, etc)
2. Make a additional dictionary, not a fruit
3. Convert lowercase letters to uppercase letters
4. Make it possible to enter not only the alphabet, but also the word to guess the answer
"""

from turtle import *
from random import choice

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
    if straight == True:
        forward(length)
    elif straight == False:
        circle(length, None, 100)
    penup()

def drawHangman(num):
    if num == 1: 
        """draw head"""
        draw(-45, 160, 270, 15, False)
    elif num == 2:
        """draw torso"""
        draw(-45, 130, 90, 40, True)
    elif num == 3:
        """draw left arm"""
        draw(-45, 120, 235, 40, True)
    elif num == 4:
        """draw right arm"""
        draw(-45, 120, 250, 40, True)
    elif num == 5:
        """draw left leg"""
        draw(-45, 90, 205, 40, True)
    elif num == 6:
        """draw right leg"""
        draw(-45, 90, 60, 40, True)

hideturtle()
speed(0)

fruitword = ['apple', 'avocado', 'banana', 'blueberry', 'cherry', 'citron',
        'coconut', 'durian', 'fig', 'grape', 'grapefruit', 'kiwi', 'lemon',
        'lime', 'mandarin', 'mango', 'melon', 'orange', 'papaya', 'peach',
        'pear', 'persimmon', 'pineapple', 'plum', 'raspberry', 'strawberry',
        'tomato', 'watermelon']

"""draw gallows"""
penup()
draw(50, 0, 90, 175, True)
draw(50, 175, 90, 95, True)
draw(-45, 175, 90, 15, True)

goto(-100,-35)
word = choice(fruitword)
for i in word:
    screen_write("_ ")
correct = []
use = []
wrong = 0
while wrong < 6:
    """Modify the code to solve Exercise 4"""
    letter = textinput("Hangman","Guess a letter:")
    while len(letter) != 1:
        letter = textinput("Hangman","Guess a letter:")
    goto(-100,-35)
    if letter not in use:
        for i in word:
            if i == letter:
                screen_write(letter.lower() + " ")
                correct += letter
            else:
                screen_write("_ ") 
        use += letter 
        if letter not in word:
            wrong += 1
            drawHangman(wrong)
        move_write(-200, -100, "You use alphbet: ")
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
    if len(correct) == len(word):
        move_write(-130, -60, "Congratulations, you win!")
        break
done()