"""
Guess a number within a range game.

Written by Grant Jenks
http://www.grantjenks.com/

Copyright (c) 2012 Grant Jenks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

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
