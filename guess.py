"""
Guess a number within a range game.

Written by Grant Jenks
http://www.grantjenks.com/

DISCLAIMER
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE
LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY
SERVICING, REPAIR OR CORRECTION.

Copyright
This work is licensed under the
Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-nd/3.0/
or send a letter to Creative Commons, 171 Second Street, Suite 300,
San Francisco, California, 94105, USA

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
