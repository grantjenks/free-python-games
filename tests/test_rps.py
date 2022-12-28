import random
import runpy
import unittest.mock as mock


def test_rps_same():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = list('xrpsrpsrpsrpsrpsrpsrpsrps')
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.rps')


def test_rps_beat_last():
    random.seed(1)
    mock_input = mock.Mock()
    mock_input.side_effect = list('sprsprsprsprsprsprsprspr')
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.rps')


def test_rps_random():
    random.seed(2)
    mock_input = mock.Mock()
    mock_input.side_effect = list('rpsrpsrpsrpsrpsrpsrpsrps')
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.rps')
