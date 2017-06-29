import random
import runpy
import turtle
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_bounce():
    random.seed(0)
    mockturtle.events[:] = [('timer',)] * 600
    runpy.run_module('freegames.bounce')
