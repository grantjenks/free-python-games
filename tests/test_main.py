import io
import os
import random
import runpy
import unittest.mock as mock


def test_main_list():
    random.seed(0)

    with mock.patch('sys.argv', ['__main__.py', 'list']):
        runpy.run_module('freegames.__main__')

def test_main_copy():
    random.seed(0)
    mock_open = mock.Mock()
    mock_open.side_effect = [io.StringIO(), io.StringIO()]

    with mock.patch('sys.argv', ['__main__.py', 'copy', 'guess']):
        with mock.patch('builtins.open', mock_open):
            runpy.run_module('freegames.__main__')

def test_main_copy_error():
    cwd = os.getcwd()
    path = os.path.join(cwd, 'guess.py')

    with open(path, 'w'):
        pass

    try:
        with mock.patch('sys.argv', ['__main__.py', 'copy', 'guess']):
            runpy.run_module('freegames.__main__')
    finally:
        os.remove('guess.py')

def test_main_show():
    random.seed(0)

    with mock.patch('sys.argv', ['__main__.py', 'show', 'guess']):
        runpy.run_module('freegames.__main__')
