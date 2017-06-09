import collections
import math


class vector(collections.Sequence):
    """Two-dimensional vector.

    Vectors can be modified in place.

    """
    __slots__ = ('_x', '_y', '_hash')

    def __init__(self, x, y):
        """Initialize vector with coordinates: x, y.

        >>> v = vector(1, 2)
        >>> v.x
        1
        >>> v.y
        2

        """
        self._hash = None
        self._x = x
        self._y = y

    @property
    def x(self):
        """X-axis component of vector.

        >>> v = vector(1, 2)
        >>> v.x
        1
        >>> v.x = 3
        >>> v.x
        3

        """
        return self._x

    @x.setter
    def x(self, value):
        if self._hash is not None:
            raise ValueError('cannot set x after hashing')
        self._x = value

    @property
    def y(self):
        """Y-axis component of vector.

        >>> v = vector(1, 2)
        >>> v.y
        2
        >>> v.y = 5
        >>> v.y
        5

        """
        return self._y

    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError('cannot set y after hashing')
        self._y = value

    def __hash__(self):
        """v.__hash__() -> hash(v)

        >>> v = vector(1, 2)
        >>> h = hash(v)
        >>> v.x = 2
        Traceback (most recent call last):
            ...
        ValueError: cannot set x after hashing

        """
        if self._hash is None:
            pair = (self._x, self._y)
            self._hash = hash(pair)
        return self._hash

    def __len__(self):
        """v.__len__() -> len(v)

        >>> v = vector(1, 2)
        >>> len(v)
        2

        """
        return 2

    def __getitem__(self, index):
        """v.__getitem__(v, i) -> v[i]

        >>> v = vector(3, 4)
        >>> v[0]
        3
        >>> v[1]
        4
        >>> v[2]
        Traceback (most recent call last):
            ...
        IndexError

        """
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        else:
            raise IndexError

    def copy(self):
        """Return copy of vector.

        >>> v = vector(1, 2)
        >>> w = v.copy()
        >>> v is w
        False

        """
        type_self = type(self)
        return type_self(self._x, self._y)

    @staticmethod
    def _isclose(a, b):
        return abs(a - b) <= max(1e-05 * max(abs(a), abs(b)), 1e-08)

    def __eq__(self, other):
        """v.__eq__(w) -> v == w

        >>> v = vector(1, 2)
        >>> w = vector(1, 2)
        >>> v == w
        True

        """
        if isinstance(other, vector):
            x_isclose = self._isclose(self._x, other._x)
            return x_isclose and self._isclose(self._y, other._y)
        return NotImplemented

    def __ne__(self, other):
        """v.__ne__(w) -> v != w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v != w
        True

        """
        if isinstance(other, vector):
            x_isclose = self._isclose(self._x, other._x)
            return not x_isclose or not self._isclose(self._y, other._y)
        return NotImplemented

    def move(self, other):
        """Move vector by other (in-place).

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v.move(w)
        >>> v
        vector(4, 6)
        >>> v.move(3)
        >>> v
        vector(7, 9)

        """
        self.__iadd__(other)

    def __iadd__(self, other):
        """v.__iadd__(w) -> v += w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v += w
        >>> v
        vector(4, 6)
        >>> v += 1
        >>> v
        vector(5, 7)

        """
        if isinstance(other, vector):
            self._x += other._x
            self._y += other._y
        else:
            self._x += other
            self._y += other
        return self

    def __add__(self, other):
        """v.__add__(w) -> v + w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v + w
        vector(4, 6)
        >>> v + 1
        vector(2, 3)
        >>> 2.0 + v
        vector(3.0, 4.0)

        """
        copy = self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def __isub__(self, other):
        """v.__isub__(w) -> v -= w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v -= w
        >>> v
        vector(-2, -2)
        >>> v -= 1
        >>> v
        vector(-3, -3)

        """
        if isinstance(other, vector):
            self._x -= other._x
            self._y -= other._y
        else:
            self._x -= other
            self._y -= other
        return self

    def __sub__(self, other):
        """v.__sub__(w) -> v - w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v - w
        vector(-2, -2)
        >>> v - 1
        vector(0, 1)

        """
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self, other):
        """v.__imul__(w) -> v *= w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v *= w
        >>> v
        vector(3, 8)
        >>> v *= 2
        >>> v
        vector(6, 16)

        """
        if isinstance(other, vector):
            self._x *= other._x
            self._y *= other._y
        else:
            self._x *= other
            self._y *= other
        return self

    def __mul__(self, other):
        """v.__mul__(w) -> v * w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v * w
        vector(3, 8)
        >>> v * 2
        vector(2, 4)
        >>> 3.0 * v
        vector(3.0, 6.0)

        """
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def __itruediv__(self, other):
        """v.__itruediv__(w) -> v /= w

        >>> v = vector(2, 4)
        >>> w = vector(4, 8)
        >>> v /= w
        >>> v
        vector(0.5, 0.5)
        >>> v /= 2
        >>> v
        vector(0.25, 0.25)

        """
        if isinstance(other, vector):
            self._x /= other._x
            self._y /= other._y
        else:
            self._x /= other
            self._y /= other
        return self

    def __truediv__(self, other):
        """v.__truediv__(w) -> v / w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> w / v
        vector(3.0, 2.0)
        >>> v / 2
        vector(0.5, 1.0)

        """
        copy = self.copy()
        return copy.__itruediv__(other)

    def __neg__(self):
        """v.__neg__() -> -v

        >>> v = vector(1, 2)
        >>> -v
        vector(-1, -2)

        """
        copy = self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy

    def __abs__(self):
        """v.__abs__() -> abs(v)

        >>> v = vector(3, 4)
        >>> abs(v)
        5.0

        """
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def rotate(self, angle):
        """Rotate vector counter-clockwise by angle (in-place).

        >>> v = vector(1, 2)
        >>> v.rotate(90)
        >>> v == vector(-2, 1)
        True

        """
        radians = angle * math.pi / 180.0
        cosine = math.cos(radians)
        sine = math.sin(radians)
        x = self._x
        y = self._y
        self._x = x * cosine - y * sine
        self._y = y * cosine + x * sine

    def __repr__(self):
        """v.__repr__() -> repr(v)

        >>> v = vector(1, 2)
        >>> repr(v)
        'vector(1, 2)'

        """
        type_self = type(self)
        name = type_self.__name__
        return '{}({!r}, {!r})'.format(name, self._x, self._y)
