"""Bagels: a number game.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Based on the Bagels game from:
http://inventwithpython.com/chapter11.html

Exercises:
1. Can you guess the number?
2. How much harder is 6 digits? Do you need more guesses?
3. What's the maximum number of digits we could support?

"""

from random import sample, shuffle

digits = 3
guesses = 10

print 'I am thinking of a {}-digit number. Try to guess what it is.'.format(digits)
print 'Here are some clues:'
print 'When I say:    That means:'
print '  Pico         One digit is correct but in the wrong position.'
print '  Fermi        One digit is correct and in the right position.'
print '  Bagels       No digit is correct.'
print 'There are no repeated digits in the number.'

while True:
    # Create a random number.

    letters = sample('0123456789', digits)

    if letters[0] == '0':
        letters = letters[::-1]

    number = ''.join(letters)

    print 'I have thought up a number. You have {} guesses to get it.'.format(guesses)

    counter = 1

    while True:
        prompt = 'Guess #{}: '.format(counter)
        guess = raw_input(prompt)

        if len(guess) != digits:
            print 'Wrong number of digits. Try again!'
            continue

        if not all(letter in '0123456789' for letter in guess):
            print 'That is not a number. Try again!'
            continue

        # Create the clues.

        clues = []

        for pos in range(len(guess)):

            if guess[pos] == number[pos]:
                clues.append('Fermi')
            elif guess[pos] in number:
                clues.append('Pico')

        shuffle(clues)

        if len(clues) == 0:
            print 'Bagels'
        else:
            print ' '.join(clues)

        counter += 1

        if guess == number:
            print 'You got it!'
            break

        if counter > guesses:
            print 'You ran out of guesses. The answer was {}.'.format(number)
            break

    print 'Do you want to play again? (yes or no)'
    answer = raw_input()
    if not answer.lower().startswith('y'):
        break
