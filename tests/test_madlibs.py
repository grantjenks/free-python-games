import random
import runpy
import unittest.mock as mock


def test_madlibs():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = ["quick", "brown","lazy","brown","dog","car","jumps"]
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.madlibs')