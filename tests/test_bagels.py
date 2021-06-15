import random
import runpy
import unittest.mock as mock


def test_bagels_pass():
    random.seed(2)
    mock_input = mock.Mock()
    mock_input.side_effect = ['123', '1234', '456', '789', '810']
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.bagels')


def test_bagels_fail():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = ['123'] * 11
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.bagels')
