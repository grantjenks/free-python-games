"""Guess a number within a range.

Exercises

1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.

"""

from random import randint

start = 1
end = 100
value = randint(start, end)

print("I'm thinking of a number between", start, "and", end)
guess=0
attempt=0
while guess != value:
    guess =int(input("Guess the number: "))
    attempt=attempt+1
    if guess < value:
        print("Higher.")
    elif guess > value:
        print("Lower.")

print("Congratulations! You guessed the right answer:", value,"attempts=",attempt)
