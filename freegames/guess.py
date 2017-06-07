"""Guess a number within a range.

Exercises

1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.

"""

import random

start = 0
end = 100
value = random.randint(start, end)

print("I'm thinking of a number between", start, 'and', end)

guess = None

while guess != value:

    try:
        guess = int(input('Guess the number: '))
    except:
        print('Whoops! Be sure the number contains only digits.')
        continue

    if guess < value:
        print('Higher.')
    elif guess > value:
        print('Lower.')

print('Congratulations! You guessed the right answer:', value)
