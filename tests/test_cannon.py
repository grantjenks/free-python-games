import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_cannon():
    random.seed(0)
    mockturtle.events[:] = (
        [('timer',)] * 300 + [('click', 0, 0)] + [('timer', True)] * 3000
    )
    runpy.run_module('freegames.cannon')
