"""
Hangman.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1. Change the look of the hangman.
2. Reduce the number of allowed guesses.
3. Penalize the player for repeated guesses.
4. Display an error message if punctuation is used.
"""

import os
import sys

def draw_man(guess_count):
    if guess_count == 0:
        print ''
        print ''
        print ''
        print ''
        print ''
        print ''
        print ''
        print ''
    elif guess_count == 1:
        print ''
        print ''
        print ''
        print ''
        print ''
        print ''
        print ''
        print '-----'
    elif guess_count == 2:
        print ''
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '-----'
    elif guess_count == 3:
        print '  ______'
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '-----'
    elif guess_count == 4:
        print '  ______'
        print '  |    |'
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '-----'
    elif guess_count == 5:
        print '  ______'
        print '  |    |'
        print '  |    O'
        print '  |'
        print '  |'
        print '  |'
        print '  |'
        print '-----'
    elif guess_count == 6:
        print '  ______'
        print '  |    |'
        print '  |    O'
        print '  |    |'
        print '  |    |'
        print '  |'
        print '  |'
        print '-----'
    elif guess_count == 7:
        print '  ______'
        print '  |    |'
        print '  |    O'
        print '  |   /|'
        print '  |    |'
        print '  |'
        print '  |'
        print '-----'
    elif guess_count == 8:
        print '  ______'
        print '  |    |'
        print '  |    O'
        print '  |   /|\\'
        print '  |    |'
        print '  |'
        print '  |'
        print '-----'
    elif guess_count == 9:
        print '  ______'
        print '  |    |'
        print '  |    O'
        print '  |   /|\\'
        print '  |    |'
        print '  |   /'
        print '  |'
        print '-----'
    elif guess_count == 10:
        print '  ______'
        print '  |    |'
        print '  |    O'
        print '  |   /|\\'
        print '  |    |'
        print '  |   / \\'
        print '  |'
        print '-----'

print 'Enter a word or phrase to guess:'
answer = sys.stdin.readline()[:-1]
answer = list(answer)

os.system('cls' if os.name=='nt' else 'clear')

wrong_guesses = 0
guess = [' ' if char == ' ' else '_' for char in answer]
guessed_letters = []

draw_man(wrong_guesses)
print ''.join(guess)

while True:

    guessed_letters.sort()
    print 'Guessed letters:', ' '.join(guessed_letters)
    print 'Guess a letter:'
    letter = sys.stdin.readline()[:-1]

    os.system('cls' if os.name=='nt' else 'clear')

    if len(letter) != 1:

        print 'Please enter a single letter.'

    elif letter in guessed_letters:

        print 'You already guessed that letter, try again.'

    elif letter in answer:

        print 'Good guess!'
        for index in range(len(answer)):
            if answer[index] == letter:
                guess[index] = letter
        guessed_letters.append(letter)

    else:

        print 'WRONG guess.'
        wrong_guesses += 1
        guessed_letters.append(letter)

    draw_man(wrong_guesses)
    print ''.join(guess)

    if wrong_guesses == 10:

        print 'Your DEAD!'
        break

    if '_' not in guess:

        print 'Success! You LIVE!'
        break
