from random import randrange
from bisect import bisect
from secrets import randbelow

class Percent:
    __slots__ = ("_objects","_cumulative",)
    def __init__(self, objects, chances):
        if len(objects) != len(chances):
            raise ValueError(
                "objects and chances "
                "must have the same length"
            )
        if not objects:
            raise ValueError(
                "objects cannot be empty"
            )
        if not all(isinstance(x, int) for x in chances) or any(x < 0 for x in chances):
            raise TypeError(
                "all values in chances must be int or values in chances cannot be negative"
            )
        if sum(chances) != 100:
            raise ValueError(
                "sum of chances must be 100"
            )

        self._objects = tuple(objects)
        cumulative = []
        total = 0
        for chance in chances:
            total += chance
            cumulative.append(total)
        self._cumulative = tuple(cumulative)
    def get(self):
        number = randrange(100)
        index = bisect(self._cumulative, number)
        return self._objects[index]

class SecurePercent:
    __slots__ = ("_objects","_cumulative",)
    def __init__(self, objects, chances):
        if len(objects) != len(chances):
            raise ValueError(
                "objects and chances "
                "must have the same length"
            )
        if not objects:
            raise ValueError(
                "objects cannot be empty"
            )
        if not all(isinstance(x, int) for x in chances) or any(x < 0 for x in chances):
            raise TypeError(
                "all values in chances must be int or values in chances cannot be negative"
            )
        if sum(chances) != 100:
            raise ValueError(
                "sum of chances must be 100"
            )

        self._objects = tuple(objects)
        cumulative = []
        total = 0
        for chance in chances:
            total += chance
            cumulative.append(total)
        self._cumulative = tuple(cumulative)
    def get(self):
        number = randbelow(100)
        index = bisect(self._cumulative, number)
        return self._objects[index]