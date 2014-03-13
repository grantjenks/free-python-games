"""
Bagels.

Copied from: http://inventwithpython.com/chapter11.html
"""

import random

def getSecretNum(numDigits):
    # Returns a string that is numDigits long, made up of unique random digits.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Returns a string with the pico, fermi, bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)

def isOnlyDigits(num):
    # Returns True if num is a string made up only of digits. Otherwise returns False.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print 'Do you want to play again? (yes or no)'
    return raw_input().lower().startswith('y')

NUMDIGITS = 3
MAXGUESS = 10

print 'I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS)
print 'Here are some clues:'
print 'When I say:    That means:'
print '  Pico         One digit is correct but in the wrong position.'
print '  Fermi        One digit is correct and in the right position.'
print '  Bagels       No digit is correct.'

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print 'I have thought up a number. You have %s guesses to get it.' % (MAXGUESS)

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print 'Guess #%s: ' % (numGuesses)
            guess = raw_input()

        clue = getClues(guess, secretNum)
        print clue
        numGuesses += 1

        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print 'You ran out of guesses. The answer was %s.' % (secretNum)

    if not playAgain():
        break
