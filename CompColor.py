from operator import add
from functools import partial
from abc import ABC, abstractmethod


class ComputerColor(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, *args):
        self.rgb = tuple(map(self._normalize, args))

    def _normalize(self, level: int) -> int:
        return max(min(level, 255), 0)

    def __repr__(self):
        return f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Color(*map(add, self.rgb, other.rgb))
        else:
            raise TypeError('wrong class addition')

    def __hash__(self):
        return hash(self.rgb)

    def _contrast(self, c, value):
        cl = (-256) * (1 - c)
        f = (259 * (cl + 259)) / (255 * (259 - cl))
        l = f * (value - 128) + 128
        return int(l)

    def __mul__(self, other):
        if isinstance(other, float):
            contrast = partial(self._contrast, other)
            return Color(*map(contrast, self.rgb))

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == '__main__':
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)

    color_list = [orange1, red, green, orange2]
    print(set(color_list))
    print(red * 0.5)
    print(0.5 * red)

