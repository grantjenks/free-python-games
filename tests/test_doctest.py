import doctest

import freegames.utils


def test_utils():
    failures, _ = doctest.testmod(freegames.utils)
    assert failures == 0
