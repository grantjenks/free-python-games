import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_flappy_outside():
    random.seed(0)
    mockturtle.events[:] = [('timer', True)] * 300
    runpy.run_module('freegames.flappy')


def test_flappy_collision():
    random.seed(0)
    mockturtle.events[:] = ([('timer', True)] * 6 + [('click', 0, 0)]) * 100
    runpy.run_module('freegames.flappy')
