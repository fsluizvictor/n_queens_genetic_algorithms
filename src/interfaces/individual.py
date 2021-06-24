from abc import ABC, abstractmethod
from typing import List


class Individual(ABC):

    def __init__(self):
        self.rate = None
        self.rated = None
        self.is_minimize = True

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
        if not self._rated:
            self._rated = True
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
