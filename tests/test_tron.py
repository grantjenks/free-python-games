import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_tron_1():
    random.seed(0)
    mockturtle.events[:] = (
        [('key a',), ('key a',)]
        + [('timer', True)] * 600
    )
    runpy.run_module('freegames.tron')

def test_tron_2():
    random.seed(0)
    mockturtle.events[:] = (
        [('key j',), ('key j',)]
        + [('timer', True)] * 600
    )
    runpy.run_module('freegames.tron')
