import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_memory():
    random.seed(0)
    events = []

    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            events += [('timer',)] * 10
            events += [('click', x + 25, y + 25)]

    events += [('timer',)] * 10
    mockturtle.events[:] = events
    runpy.run_module('freegames.memory')
