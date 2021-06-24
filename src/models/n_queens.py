from abc import ABC
from random import shuffle
from typing import List, Optional

from src.interfaces.individual import Individual


class NQueens(object):

    def __init__(self, amount_queens: Optional[int] = 8, genes: Optional[List[int]] = None, rate: Optional[int] = 0):
        # inicializar o tamanho do vetor de genes e seus valores de forma aleatória
        # os valores aleatórios devem obedecer a ideia da permutação
        self._amount_queens = amount_queens
        if genes:
            self._genes = genes
        else:
            self._genes = [i for i in range(self._amount_queens)]
        shuffle(self._genes)
        self.rate = rate
        self.rated = False

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
        return self.rate

    @rate.setter
    def rate(self, rate: int):
        self.rate = rate

    @property
    def rated(self):
        return self.rated

    @rated.setter
    def rated(self, rated: bool):
        self.rated = rated
