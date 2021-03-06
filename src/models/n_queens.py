from random import shuffle
from typing import List, Optional


class NQueens(object):

    def __init__(self, amount_queens: Optional[int] = 8, genes: Optional[List[int]] = None, rate: Optional[float] = 0):

        self._amount_queens = amount_queens
        if genes:
            self._genes = genes
        else:
            self._genes = [i for i in range(self._amount_queens)]
        shuffle(self._genes)
        self._rate = rate
        self._old_rate = rate

    @property
    def amount_queens(self):
        return self._amount_queens

    @amount_queens.setter
    def amount_queens(self, amount_queens: int):
        self._amount_queens = amount_queens

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, genes: List[int]):
        self._genes = genes

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate: int):
        self._rate = rate

    @property
    def old_rate(self):
        return self._old_rate

    @old_rate.setter
    def old_rate(self, old_rate: float):
        self._old_rate = old_rate
