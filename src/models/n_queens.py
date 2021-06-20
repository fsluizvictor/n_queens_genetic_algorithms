from abc import ABC
from random import shuffle
from typing import List, Optional

from src.interfaces.individual import Individual


class NQueens(Individual):
    _amount_queens: int
    _genes: List[int]

    def __init__(self, amount_queens: Optional[int] = 8):
        # inicializar o tamanho do vetor de genes e seus valores de forma aleatória
        # os valores aleatórios devem obedecer a ideia da permutação
        self._amount_queens = amount_queens
        self._genes = [i for i in range(self._amount_queens)]
        shuffle(self._genes)

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


