from pytest import raises

import freegames.utils as utils

def test_change_after_hash():
    v = utils.vector(0, 0)
    hash(v)
    with raises(ValueError):
        v.x = 1
    with raises(ValueError):
        v.y = 1
    with raises(ValueError):
        v += 1
    with raises(ValueError):
        v -= 1
    with raises(ValueError):
        v *= 2
    with raises(ValueError):
        v /= 2
    with raises(ValueError):
        v.rotate(90)

def test_not_implemented_paths():
    v = utils.vector(0, 0)
    assert not (v == 0)
    assert v != 0
