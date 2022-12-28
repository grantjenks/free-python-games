import io
import os
import random
import unittest.mock as mock

from freegames import __main__


def test_main_list():
    random.seed(0)

    with mock.patch('sys.argv', ['__main__.py', 'list']):
        __main__.main()


def test_main_copy():
    random.seed(0)
    mock_open = mock.Mock()
    mock_open.side_effect = [io.StringIO(), io.StringIO()]

    with mock.patch('sys.argv', ['__main__.py', 'copy', 'guess']):
        with mock.patch('builtins.open', mock_open):
            __main__.main()


def test_main_copy_error():
    cwd = os.getcwd()
    path = os.path.join(cwd, 'guess.py')

    with open(path, 'w'):
        pass

    try:
        with mock.patch('sys.argv', ['__main__.py', 'copy', 'guess']):
            __main__.main()
    finally:
        os.remove('guess.py')


def test_main_show():
    random.seed(0)

    with mock.patch('sys.argv', ['__main__.py', 'show', 'guess']):
        __main__.main()


def test_main_play():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = [20, 70, 50]
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        with mock.patch('sys.argv', ['__main__.py', 'play', 'guess']):
            __main__.main()
