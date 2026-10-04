import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_snake():
    messages = []

    def record(text, font=None, align=None):
        messages.append(text)

    mockturtle.write = record
    random.seed(0)
    mockturtle.events.clear()
    mockturtle.events += [
        ('timer',),
        ('key Left',),
        ('timer',),
        ('key Up',),
        ('timer',),
        ('key Right',),
        ('timer',),
        ('key Down',),
        ('timer',),
        ('key Left',),
        ('timer',),
        ('key Up',),
    ]
    mockturtle.events += [('timer', True)] * 300
    runpy.run_module('freegames.snake')
    assert 'Game Over' in messages
