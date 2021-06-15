import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_paint():
    random.seed(0)
    mockturtle.events[:] = [
        ('key K',),
        ('key l',),
        ('click', 0, 0),
        ('click', 10, 10),
        ('key W',),
        ('key s',),
        ('click', 20, 20),
        ('click', 30, 30),
        ('key G',),
        ('key c',),
        ('click', 30, 30),
        ('click', 40, 40),
        ('key B',),
        ('key r',),
        ('click', 30, 30),
        ('click', 40, 40),
        ('key R',),
        ('key t',),
        ('click', 30, 30),
        ('click', 40, 40),
    ]
    runpy.run_module('freegames.paint')
