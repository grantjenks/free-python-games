import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_pong_1():
    random.seed(0)
    mockturtle.events.clear()
    mockturtle.events += [('timer',), ('key s',)] * 12
    mockturtle.events += [('timer',), ('key w',)] * 4
    mockturtle.events += [('timer', True)] * 600
    runpy.run_module('freegames.pong')


def test_pong_2():
    random.seed(1)
    mockturtle.events.clear()
    mockturtle.events += [('timer',), ('key k',)] * 18
    mockturtle.events += [('timer',), ('key i',)] * 6
    mockturtle.events += [('timer', True)] * 600
    runpy.run_module('freegames.pong')
