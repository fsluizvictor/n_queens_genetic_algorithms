from typing import Optional, List

from src.dao.n_queens_dao import NQueensDao
from src.interfaces.individual import Individual
from src.models.n_queens import NQueens


class NQueensController(Individual):
    _amount_queens: int
    _dao: NQueensDao

    def __init__(self, amount_queens: Optional[int] = 8):
        self._amount_queens = amount_queens
        self._dao = NQueensDao(amount_queens)

    # recombinar os individuos self e p2 gerando 2 filhos utilizando a ideia de permutação
    def recombine(self, first_individual: NQueens, second_individual: NQueens) -> List[NQueens]:
        first_son = self._dao.create()
        second_son = self._dao.create()

        first_son.genes(None)
        second_son.genes(None)

        chunk_first = first_individual.genes[0:len(first_individual.genes) / 2]
        chunk_second = second_individual.genes[len(first_individual.genes) / 2:len(first_individual.genes)]
        assistent_array = chunk_first
        assistent_array.append(chunk_second)

        first_son.genes(assistent_array)

        chunk_first = first_individual.genes[len(first_individual.genes) / 2:len(first_individual.genes)]
        chunk_second = second_individual.genes[0:len(first_individual.genes) / 2]
        assistent_array = chunk_first
        assistent_array.append(chunk_second)

        second_son.genes(assistent_array)

        return [first_son, second_son]

    def mutate(self, individual: NQueens) -> NQueens:
        # gerar um novo individuo mutante com os genes do individuo self mutados e uma taxa de mutação de 10% à 5%
        pass

    def to_rate(self, individual: NQueens) -> float:
        # realizar a contagem de colisões que ocorrem entre as rainhas.
        pass
