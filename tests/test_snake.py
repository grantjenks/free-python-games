import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_snake():
    random.seed(0)
    mockturtle.events.clear()
    mockturtle.state.clear()
    mockturtle.events += [
        ('click', 0, 0),
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


def test_snake_waits_for_start_click():
    mockturtle.state.clear()
    mockturtle.events[:] = [('timer', True)]
    runpy.run_module('freegames.snake')
    assert 'timer' not in mockturtle.state

    mockturtle.state.clear()
    mockturtle.events[:] = [
        ('click', 0, 0),
        ('timer', True),
    ]
    runpy.run_module('freegames.snake')
    assert 'timer' in mockturtle.state
