import random
import runpy
import unittest.mock as mock


def test_crypto_encrypt():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = ['encrypt', 'Python since 1991', '10']
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.crypto')

def test_crypto_encrypt_bad_key():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = ['encrypt', 'Python since 1991', 'abc']
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.crypto')

def test_crypto_bad_command():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = ['bad command']
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.crypto')

def test_crypto_decrypt():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = ['decrypt', 'Zidryx csxmo 1991', '10']
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.crypto')

def test_crypto_decode():
    random.seed(0)
    mock_input = mock.Mock()
    mock_input.side_effect = ['decode', 'Zidryx csxmo 1991']
    mocks = {'print': lambda *args: None, 'input': mock_input}

    with mock.patch.multiple('builtins', **mocks):
        runpy.run_module('freegames.crypto')
