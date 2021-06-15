import random
import runpy
import sys
import unittest.mock as mock

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_minesweeper():
    random.seed(0)
    mockturtle.events[:] = (
        ('click', 175, -175),
        ('click', -75, -75),
        ('click', 125, 125),
    )

    try:
        with mock.patch('time.sleep', lambda delay: None):
            runpy.run_module('freegames.minesweeper')
    except SystemExit:
        pass
