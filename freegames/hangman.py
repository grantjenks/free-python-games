

import numpy as np
import random
import turtle
import enchant
import time

turtle.hideturtle()
turtle.penup()
words = []
#file that contains list of hangman words
file = open("Hangman_wordbank.txt", "r")
content = file.read()
words = content.split(",")

Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#gets position of character in word, return list of indexes
def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos

#select a random word, and print the correct amount of underscores, return the word
def Initialize(vsComp, word):
    if vsComp == False:
        word = words[random.randint(0,len(words))]
        word = word[1:len(word)]
        for i in range(len(word)):
            turtle.write("_ ",font=("Verdana",15, "normal"), move = True)
        return word
    else:
        for i in range(len(word)):
            turtle.write("_ ",font=("Verdana",15, "normal"), move = True)
        return word

def drawbodyPart(attempts):
    #head
    if attempts == 6:
        turtle.goto(50,350)
        turtle.pendown()
        turtle.circle(25)
    #body
    elif attempts == 5: 
        turtle.goto(50,350)
        turtle.pendown()
        turtle.goto(50,250)
    #left arm
    elif attempts == 4: 
        turtle.goto(50,350)
        turtle.pendown()
        turtle.goto(20,300)
    #right arm
    elif attempts == 3: 
        turtle.goto(50,350)
        turtle.pendown()
        turtle.goto(80,300)
    #left leg
    elif attempts == 2: 
        turtle.goto(50,250)
        turtle.pendown()
        turtle.goto(30,150)
    #right leg
    elif attempts == 1: 
        turtle.goto(50,250)
        turtle.pendown()
        turtle.goto(80,150)
    turtle.penup()


#guess characters to get the full word
def Play():
    turtle.goto(-300,300)
    word = Initialize(False, "")
    attempts = 6 #5 guess attempts then game over
    correct = len(word)
    #list of all guesses
    guesses = []
    pos = []
    counter = 0
    turtle.goto(-300,250)
    correctnum = 0
    #game ends when attemps = 0 or you guessed the word, correct = 0
    while attempts > 0 and correct > 0:
        counter+=1
        guess = turtle.textinput("Guess", "Enter your character guess!")
        turtle.goto(300, 400-(50*counter))
        turtle.write('{}{}'.format(guess, " ") ,font=("Verdana",15, "normal"), move = True)
        turtle.goto(-300,250-(50*correctnum))
        #guessed a correct letter
        if guess in word:
            correctnum = correctnum + 1
            turtle.penup()
            if guess not in guesses:
                 correct -= len(charposition(word, guess))
            guesses.append(guess)

            #get indexes of characters to print letters 
            for j in range(len(guesses)):
                pos += charposition(word, guesses[j])

            for i in range(len(word)):
                if i in pos:
                    turtle.write('{}{}'.format(word[i], " ") ,font=("Verdana",15, "normal"), move = True)
                    # print(word[i],end='')
                else:
                    turtle.write(" _ ",font=("Verdana",15, "normal"), move = True)
                    #print("_ ",end='')
        #guessed wrong, draw a body part
        else :
            guesses.append(guess)
            drawbodyPart(attempts)
            attempts-=1
        turtle.penup()
        turtle.goto(-300,300-(50*(counter+1)))

    #you win! or lose...
    while True:       
        if correct == 0:
            turtle.goto(-25,25)
            turtle.write("You Win!",font=("Verdana",15, "normal"), move = True )
        elif attempts == 0 :
            drawbodyPart(1)
            turtle.goto(-25,25)
            turtle.write("You Lose!",font=("Verdana",15, "normal"), move = True )

def PlayComputer(word):
    turtle.goto(-300,300)
    Initialize(True, word)
    attempts = 6
    correct = len(word)
    guesses = []
    pos = []
    counter = 0
    correctnum = 0
    turtle.goto(-300,250)
    while attempts > 0 and correct > 0:
        time.sleep(1)
        counter+=1
        guess = Letters[random.randint(0,len(Letters))-1]
        turtle.goto(400, 400-(50*counter))
        turtle.write('{}{}'.format(guess, " ") ,font=("Verdana",15, "normal"), move = True)
        turtle.goto(-300,250-(50*correctnum))
        #guessed a correct letter
        if guess in word:
            correctnum = correctnum + 1
            turtle.penup()
            if guess not in guesses:
                 correct -= len(charposition(word, guess))
            guesses.append(guess)

            #get indexes of characters to print letters 
            for j in range(len(guesses)):
                pos += charposition(word, guesses[j])

            for i in range(len(word)):
                if i in pos:
                    turtle.write('{}{}'.format(word[i], " ") ,font=("Verdana",15, "normal"), move = True)
                    # print(word[i],end='')
                else:
                    turtle.write(" _ ",font=("Verdana",15, "normal"), move = True)
                    #print("_ ",end='')
  
        else :
            guesses.append(guess)
            drawbodyPart(attempts)
            attempts-=1
        turtle.penup()
        turtle.goto(-300,300-(50*(counter+1)))

    while True:       
        if correct == 0:
            turtle.goto(-25,25)
            turtle.write("You Lose, Computer Wins!",font=("Verdana",15, "normal"), move = True )
        elif attempts == 0 :
            drawbodyPart(1)
            turtle.goto(-25,25)
            turtle.write("You Outsmarted the Computer!",font=("Verdana",15, "normal"), move = True )


selection = int(turtle.textinput("Game selection", "press 0 to play hangman vs computer generated words!, press 1 to specify a word for the computer!"))

if selection == 0:
    Play()
elif selection == 1:
    #validate word from us dictionary
    d = enchant.Dict("en_US")
    word = turtle.textinput("Word selection", "Type a word for the Computer to guess!")
    while d.check(word) == False:
        word = turtle.textinput("Word selection", "Not a word, Try again!")
    PlayComputer(word)

