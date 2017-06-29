import random
import runpy
import sys
import unittest.mock as mock

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_simonsays():
    random.seed(0)
    mockturtle.events[:] = (
        ('click', 0, 0),
        ('click', -100, -100),
        ('click', 100, 100),
    )

    try:
        with mock.patch('time.sleep', lambda delay: None):
            runpy.run_module('freegames.simonsays')
    except SystemExit:
        pass
