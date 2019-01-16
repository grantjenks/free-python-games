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

## Grant Jenks

# 1. Python trainer for Fortune 100 companies.
# 2. Married to Chemistry teacher, father of two.
# 3. 100s of hours of 4-12th grade instruction.
'''.splitlines(),
'''

## Setup

# 1. Install Python: https://www.python.org/
# 2. Run IDLE: $ python -m idlelib.idle
# 3. Use built-in Turtle module!
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
        'fd(100)', 1,
        'rt(90)', 1,
        'backward(-100)', 1,
        'left(-90)', 1,
        'forward(100)', 1,
        'right(90)', 1,
        'undo()', 1,
        'undo()', 1,
    ],
    [
        '',
        '## Loops',
        '',
        'reset()', 0.5,
        'for each in range(5):', 0.5,
        'bk(100)', 0.5,
        'lt(144)', 0.5,
        '', 3,
    ],
    [
        '',
        '## Functions and Shapes',
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
        'help(dot)', 1,
        'dot(100)', 1,
    ],
    [
        '',
        '## Colors'
        '',
        'reset()', 0.5,
        'from itertools import *', 0.5,
        "colors = cycle(['red', 'green', 'blue', 'purple'])", 0.5,
        'def present():', 0.5,
        'for i in range(4):', 0.5,
	'color(next(colors))', 0.5,
        'square()', 0.5,
        'left(90)', 0.5,
        '',
        'present()', 5,
    ],
    [
        '',
        '## Locations',
        '',
        'reset()', 0.5,
        'def line(a, b, x, y):', 0.5,
        'up()', 0.5,
        'goto(a, b)', 0.5,
        'down()', 0.5,
        'goto(x, y)', 0.5,
        '',
        "color('red')", 0.5,
        'width(20)', 0.5,
        'line(-100, -100, 0, 200)', 1,
        'line(0, 200, 100, -100)', 1,
        'line(100, -100, -100, -100)', 1,
    ],
    [
        '',
        '## Mouse Inputs',
        '',
        'width(10)', 0.5,
        "color('green')", 0.5,
        'def tap(x, y):', 0.5,
        'goto(x, y)', 0.5,
        'dot(20)', 0.5,
        '',
        'onscreenclick(tap)', 0.5,
    ],
    [
        '',
        '## Keyboard Events',
        '',
        'reset()', 0.5,
        'width(10)', 0.5,
        "onkey(lambda: fd(30), 'Up')", 0.5,
        "onkey(lambda: bk(30), 'Down')", 0.5,
        "onkey(lambda: lt(30), 'Left')", 0.5,
        "onkey(lambda: rt(30), 'Right')", 0.5,
        'listen()', 0.5,
    ],
    [
        '',
        '## Animation',
        '',
        'hideturtle()', 0.5,
        'tracer(False)', 0.5,
        'running = True', 0.5,
        'def draw():', 0.5,
        'clear()', 0.5,
        'present()', 0.5,
        'update()', 0.5,
        'left(1)', 0.5,
        'if running:', 0.5,
        'ontimer(draw, 100)',
        '',
        'reset()', 0.5,
        'draw()', 0.5,
    ],
'''

## Free Python Games

# 1. Search: Free Python Games
# 2. $ python -m pip install freegames
# 3. http://www.grantjenks.com/docs/freegames/
'''.splitlines(),
]


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
                    time.sleep(0.25)
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
        if value == 'q':
            exit()
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
