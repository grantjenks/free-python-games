import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_ant():
    random.seed(0)
    mockturtle.events[:] = [('timer',)] * 600
    runpy.run_module('freegames.ant')
