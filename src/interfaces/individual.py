from abc import ABC, abstractmethod
from typing import List


class Individual(ABC):
    _rate: float
    _rated: bool
    _is_minimize: bool

    def __init__(self):
        pass

    @abstractmethod
    def recombine(self, individual: ABC) -> List[ABC]:
        pass

    @abstractmethod
    def mutate(self) -> ABC:
        pass

    @abstractmethod
    def to_rate(self) -> int:
        pass

    @property
    def rate(self):
        if not self.rated:
            self.rated(True)
            self.rate(self.to_rate())

        return self.rate

    @rate.setter
    def rate(self, rate: float):
        self._rate = rate

    @property
    def reated(self):
        return self._rated

    @reated.setter
    def reated(self, rated: bool):
        self._rated = rated

    @property
    def is_minimize(self):
        return self._is_minimize

    @is_minimize.setter
    def is_minimize(self, is_minimize: bool):
        self._is_minimize = is_minimize
