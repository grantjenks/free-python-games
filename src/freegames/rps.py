"""Rock, Paper, Scissors

The game is played in a series as follows:

1. Player chooses "r" for rock, "p" for paper, or "s" for scissors.
2. The computer will also choose rock, paper, or scissors.
3. The result will either be a win, loss, or tie:
   a. Rock crushes scissors.
   b. Scissors cuts paper.
   c. Paper covers rock.

First to score 5 points wins the series!
"""
# Exercises:
#
# 1. Create a strategy to rotate through 'r', 'p', and 's' in a cycle.
# 2. Create a strategy to do the same as the last computer choice.
# 3. Create a new strategy of your own.

import random

beats = {'r': 's', 'p': 'r', 's': 'p'}
loses = {value: key for key, value in beats.items()}
state = {'player': 0, 'computer': 0, 'ties': 0}
guesses = []
default = random.choice('rps')


def always_same():
    return default


def random_strategy():
    return random.choice('rps')


def beat_last():
    if not guesses:
        return default
    last, _ = guesses[-1]
    return loses[last]


strategies = [always_same, random_strategy, beat_last]
strategy = random.choice(strategies)


def get_option():
    while True:
        choice = input('Enter "r" for rock, "p" for paper, "s" for scissors: ')
        if choice not in beats:
            print('Invalid choice.')
            continue
        return choice


print(__doc__)

while True:
    player = get_option()
    computer = strategy()
    guess = (player, computer)
    guesses.append(guess)

    print('Player chooses:', player)
    print('Computer chooses:', computer)

    if player == computer:
        state['ties'] += 1
        print('Tie!')
    elif beats[player] == computer:
        state['player'] += 1
        print('Player wins!')
    else:
        state['computer'] += 1
        print('Computer wins!')

    print()
    print('Player points:', state['player'])
    print('Computer points:', state['computer'])
    print()

    if state['player'] == 5:
        print('PLAYER WINS!')
        break

    if state['computer'] == 5:
        print('COMPUTER WINS!')
        break

print('Computer strategy:', strategy.__name__)
