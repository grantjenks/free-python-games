import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_maze():
    random.seed(0)
    mockturtle.events[:] = [
        ('click', -200, 0),
        ('click', -190, 10),
        ('click', -170, 30),
    ]
    runpy.run_module('freegames.maze')
