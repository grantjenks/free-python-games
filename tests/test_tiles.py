import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_tiles():
    random.seed(0)
    mockturtle.events[:] = (
        ('click', x + 50, y + 50)
        for x in range(-200, 200, 100)
        for y in range(-200, 200, 100)
    )
    runpy.run_module('freegames.tiles')
