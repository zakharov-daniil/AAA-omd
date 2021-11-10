import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):
    @abstractmethod
    def inc_exp(self, value: int):
        """увеличиваем опыт"""
        pass

    @property
    @abstractmethod
    def exp(self):
        """вернуть опыт"""
        pass

    @exp.setter
    @abstractmethod
    def exp(self, value: int):
        """установить опыт"""
        pass


class Pokemon(AnimeMon):
    def __init__(self, name: str, poketype: str, exp: int = 0):
        self.name = name
        self.poketype = poketype
        self._exp = exp

    def inc_exp(self, value: int):
        self._exp += value

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value


class Digimon(AnimeMon):
    def __init__(self, name: str, exp: int = 0):
        self.name = name
        self._exp = exp

    def inc_exp(self, value: int):
        self._exp += value * 8

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value


def train(mon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - mon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            mon.inc_exp(step_size)


if __name__ == '__main__':
    p1 = Pokemon(name='Bulbasaur', poketype='fire')
    print(p1.name, p1.poketype, p1.exp)
    train(p1)
    print(p1.exp)

    agumon = Digimon(name='Agumon')
    print(agumon.name)
    train(agumon)
    print(agumon.exp)
