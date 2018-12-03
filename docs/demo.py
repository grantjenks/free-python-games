import docutils.frontend
import docutils.parsers.rst
import docutils.utils
import pyautogui
import pynput.keyboard as kb
import queue
import subprocess as sp
import threading
import time


slide = 0
slides = [
'''
# Give the Gift of Python
'''.splitlines(),
'''

## Who am I?

# 1. Professional Python trainer for Fotune 100 companies.
# 2. Married to High School Chemistry teacher, father of two.
# 3. Hundreds of hours of 4th-12th grade instruction.


'''.splitlines(),
'''

## Setup

# 1. Install Python:  https://www.python.org/
# 2. Run IDLE:        $ python -m idlelib.idle
# 3. Use Turtle:      https://docs.python.org/library/turtle.html
'''.splitlines(),
    [
        '',
        '## Open the Turtle Window',
        '',
        'from turtle import *', 0.5,
        'reset()', 0.5,
    ],
    [
        '',
        '## Basic Commands',
        '',
        'forward(100)', 1,
        'right(90)', 1,
        'forward(100)', 1,
        'right(90)', 1,
        'forward(100)', 1,
        'right(90)', 1,
        'forward(100)', 1,
        'right(90)', 1,
    ],
    [
        '',
        '## Loops',
        '',
        'reset()', 0.5,
        'for each in range(4):', 0.5,
        'forward(100)', 0.5,
        'right(90)', 0.5,
        '', 3,
    ],
    [
        '',
        '### Star Loop',
        '',
        'reset()', 0.5,
        'for each in range(5):', 0.5,
        'forward(100)', 0.5,
        'right(144)', 0.5,
        '', 3,
    ],
    [
        '',
        '## Shapes',
        '',
        'reset()', 0.5,
        'begin_fill()', 0.5,
        'for each in range(4):', 0.5,
        'forward(100)', 0.5,
        'right(90)', 0.5,
        '', 3,
        'end_fill()', 0.5,
    ],
    [
        '',
        '## Functions',
        '',
        'def square():', 0.5,
        'begin_fill()', 0.5,
        'for each in range(4):', 0.5,
        'forward(100)', 0.5,
        'right(90)', 0.5,
        -1,
        'end_fill()', 0.5,
        '',
        'reset()', 0.5,
        'square()', 3,
    ],
    [
        '',
        '## Dots',
        '',
        'reset()', 0.5,
        'dot(10)', 1,
    ],
    [
        '',
        '## Colors',
        '',
        'reset()', 0.5,
        "color('orange')", 0.5,
        'square()', 3,
    ],
    [
        '',
        '### Color Spiral'
        '',
        'from itertools import *', 0.5,
        'reset()', 0.5,
        "bgcolor('black')", 0.5,
        "colors = 'red', 'orange', 'yellow', 'green', 'blue', 'purple'", 0.5,
        'rainbow = cycle(colors)', 0.5,
        'width(4)', 0.5,
        'for length in range(2, 120, 2):', 0.5,
	'color(next(rainbow))', 0.5,
	'forward(length)', 0.5,
	'left(59)', 0.5,
        '', 5,
    ],
    [
        '',
        '## Locations',
        '',
        'reset()', 0.5,
        'up()', 0.5,
        'goto(100, 100)', 0.5,
        'down()', 0.5,
        'dot(40)', 0.5,
        'up()', 0.5,
        'goto(-100, -100)', 0.5,
        'down()', 0.5,
        'dot(40)', 0.5,
    ],
    [
        '',
        '## Open the Turtle Window',
        '',
        'from turtle import *', 0.5,
        'reset()', 1,
    ],
    [
        ''
        '## Inputs',
        '',
        # TODO -- paint.py -- mouse
        # TODO -- keys -- move dot
    ],
    # animation
    # ant.py -- random walk
    # vector
    # bounce.py -- vector
    # maze.py -- animation with inputs
    # tictactoe.py
    # tips, activities, notes

]
slide = -2 + len(slides)


def worker():
    global slide
    while True:
        key = inputs.get()
        if key == kb.Key.esc:
            print('Typing slide', slide)
            parts = slides[slide]
            for part in parts:
                if part == '':
                    pyautogui.press('enter')
                elif part == -1:
                    pyautogui.press('backspace')
                elif isinstance(part, str):
                    pyautogui.typewrite(part, interval=0.1)
                    pyautogui.press('enter')
                else:
                    time.sleep(part)
            slide += 1


def ticker():
    def on_press(key):
        inputs.put(key)

    with kb.Listener(on_press=on_press) as listener:
        listener.join()


def commander():
    global slide
    while True:
        value = input()
        try:
            slide = int(value)
        except ValueError:
            pass


def main():
    global inputs
    idle = sp.Popen(['python', '-m', 'idlelib.idle'])
    inputs = queue.Queue()
    work = threading.Thread(target=worker)
    work.start()
    tick = threading.Thread(target=ticker)
    tick.start()
    cmdr = threading.Thread(target=commander)
    cmdr.start()
    cmdr.join()
    tick.join()
    work.join()
    idle.wait()


if __name__ == '__main__':
    main()
