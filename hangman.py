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
    """This is called after each guess by the player.
    It represents the amount of guesses the player has left in the spirit of hangman.
    """
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

"""Get the word the user is trying to guess as input from user"""
print 'Enter a word or phrase to guess:'
answer = sys.stdin.readline()[:-1]
answer = list(answer)

os.system('cls' if os.name=='nt' else 'clear')  # Clear the command window the game is running in

"""Initalize starting variables
Wrong guesses is a counter used to end the game at 10
guess displays the number of letter in the answer for visualization purposes
guessed_letters keeps track of which letters the user has guessed
"""
wrong_guesses = 0
guess = [' ' if char == ' ' else '_' for char in answer]
guessed_letters = []

draw_man(wrong_guesses)
print ''.join(guess)  # Print the contents of the guess array, omitting all formatting

while True:
    """Main loop of the program.
    Displays to the user the letters they have guessed and requests a new guess.
    Once input is given the screen is cleared and the input is checked to be consistent with expected values.
    The user is either asked to input a different value or the game is updated based on whether their guess is correct or incorrect
    """
    guessed_letters.sort()
    print 'Guessed letters:', ' '.join(guessed_letters)  # Display the letters the user has guessed, sorted alphabetically
    print 'Guess a letter:'
    letter = sys.stdin.readline()[:-1]  # Ask the user for a new guess

    os.system('cls' if os.name=='nt' else 'clear')  # Clear the screen

    if len(letter) != 1:  # If more or less than 1 character was entered

        print 'Please enter a single letter.'

    elif letter in guessed_letters:  # If the letter was already guessed

        print 'You already guessed that letter, try again.'

    elif letter in answer:  # If the letter is correct

        print 'Good guess!'
        for index in range(len(answer)):  # Loop through all the letters in the answer
            if answer[index] == letter:  # If the guess matches the letter at the current index
                guess[index] = letter  # Update the guess list to include the correct letter
        guessed_letters.append(letter)  # Add the guessed letter to the guessed_letters list

    else:  # If the letter is incorrect

        print 'WRONG guess.'
        wrong_guesses += 1
        guessed_letters.append(letter)

    draw_man(wrong_guesses)  # Draw the man on screen again based on the new amount of wrong guesses
    print ''.join(guess)  # Display the word as the user has guessed it

    if wrong_guesses == 10:  # End the game if the player has 10 incorrect guesses

        print "You're DEAD!"
        break

    if '_' not in guess:  # If the guess array is populated with only letters, the user has completely guessed the answer

        print 'Success! You LIVE!'
        break
