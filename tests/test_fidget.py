import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_fidget():
    random.seed(0)
    mockturtle.events.clear()
    mockturtle.events += [('timer',), ('key space',)] * 30
    mockturtle.events += [('timer',)] * 600
    runpy.run_module('freegames.fidget')
