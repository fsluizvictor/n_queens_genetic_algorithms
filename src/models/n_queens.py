from abc import ABC
from typing import List, Optional

from src.interfaces.individual import Individual


class NQueens(Individual):
    _amount_queens: int
    _genes: List[int]

    def __init__(self, amount_queens: Optional[int] = 8):
        # inicializar o tamanho do vetor de genes e seus valores de forma aleatória
        # os valores aleatórios devem obedecer a ideia da permutação
        self._amount_queens = amount_queens
        self._genes = None

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

    def recombine(self, individual: ABC) -> List[ABC]:
        # recombinar os individuos self e p2 gerando 2 filhos utilizando a ideia de permutação
        pass

    def mutate(self) -> ABC:
        # gerar um novo individuo mutante com os genes do individuo self mutados e uma taxa de mutação de 10% à 5%
        pass

    def to_rate(self) -> float:
        # realizar a contagem de colisões que ocorrem entre as rainhas.
        pass
