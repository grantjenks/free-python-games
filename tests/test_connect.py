import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_connect():
    random.seed(0)
    mockturtle.events[:] = [
        ('click', 25, 0),
        ('click', 75, 0),
    ]
    runpy.run_module('freegames.connect')
