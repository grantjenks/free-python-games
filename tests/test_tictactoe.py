import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_tictactoe():
    random.seed(0)
    mockturtle.events[:] = [
        ('click', 100, 100),
        ('click', 100, 0),
    ]
    runpy.run_module('freegames.tictactoe')
