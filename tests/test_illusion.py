import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_illusion():
    random.seed(0)
    mockturtle.events.clear()
    mockturtle.events += [('timer', True)] * 10
    runpy.run_module('freegames.illusion')
