import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_typing():
    random.seed(0)
    mockturtle.events.clear()
    mockturtle.events += [('timer',)] * 100
    mockturtle.events += [('key i',)]
    mockturtle.events += [('timer',)] * 100
    mockturtle.events += [('key k',)]
    mockturtle.events += [('timer', True)] * 1000
    runpy.run_module('freegames.typing')
