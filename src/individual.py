from abc import ABC, abstractmethod
from typing import List


class Individual(ABC):
    _rate: float
    _rated: bool

    @abstractmethod
    def recombine(self, individual: ABC) -> List[ABC]:
        pass

    @abstractmethod
    def mutate(self) -> ABC:
        pass

    @abstractmethod
    def to_rate(self) -> float:
        pass

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate: float):
        self._rate = rate

    @property
    def reated(self):
        return self._rated

    @reated.setter
    def reated(self, rated: bool):
        self._rated = rated

    def find_rate(self):
        if not self.rate:
            self.rate = self.to_rate()

        return self.rate
