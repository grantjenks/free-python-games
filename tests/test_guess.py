import random
import runpy
import unittest.mock as mock


def test_guess():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = [20, 70, 50]
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.guess')
