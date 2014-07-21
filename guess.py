"""
Guess a number within a range game.

Copyright (c) 2014 Grant Jenks
http://www.grantjenks.com/

Exercises
1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print out the number of required guesses for the right answer.
"""

import random

start = 0
end = 100
value = random.randint(start, end)

print "I'm thinking of a number between", start, 'and', end

guess = None

while guess != value:

    try:
        guess = int(raw_input('Guess the number: '))
    except Exception:
        print 'Whoops! Be sure the number contains only digits.'
        continue

    if guess < value:

        print 'Higher.'

    elif guess > value:

        print 'Lower.'

print 'Congratulations! You guessed the right answer:', value
