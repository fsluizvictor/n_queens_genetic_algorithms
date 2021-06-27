import random
from typing import Optional, List

from src.dao.n_queens_dao import NQueensDao
from src.models.n_queens import NQueens


class NQueensService:

    def __init__(self, amount_queens: Optional[int] = 8):
        self._amount_queens = amount_queens
        self._dao = NQueensDao(amount_queens)

    # [i for i in range(self._amount_queens)]
    # recombinar os individuos self e p2 gerando 2 filhos utilizando a ideia de permutação
    def recombine(self, first_individual: NQueens, second_individual: NQueens) -> List[NQueens]:

        first_son = self._without_repetition(first_individual.genes, second_individual.genes)
        second_son = self._without_repetition(second_individual.genes, first_individual.genes)
        return [NQueens(8, first_son), NQueens(8, second_son)]

    # gerar um novo individuo mutante com os genes do individuo self mutados e uma taxa de mutação de 5% a 10%
    # --> se maior que noventa deve sofrer mutação
    def mutate(self, individual: NQueens) -> NQueens:

        mutate_genes = [i for i in range(len(individual.genes))]
        for i in range(len(individual.genes)):
            mutation_rate = random.randint(1, 100)
            if mutation_rate > 90:
                mutant_index = random.randint(i, len(individual.genes) - 1)
                gene = individual.genes[i]
                mutant = individual.genes[mutant_index]
                mutate_genes.remove(mutant)
                mutate_genes.insert(i, mutant)
                mutate_genes.remove(gene)
                mutate_genes.insert(mutant_index, gene)
            else:
                mutate_genes.remove(individual.genes[i])
                mutate_genes.insert(i, individual.genes[i])
        return NQueens(8, mutate_genes)

    # realizar a contagem de colisões que ocorrem entre as rainhas.
    def to_rate(self, individual: NQueens) -> float:
        collisions = 0.0
        genes = individual.genes
        for i in genes:
            for j in genes:
                if genes[i] == genes[j] or genes[i] == genes[j] + (j - i) or genes[i] == genes[j] - (j - i):
                    collisions += 1

        return float(collisions)

    def _without_repetition(self, first_genes: List[int], second_genes: List[int]) -> List[int]:
        assistent_array = [i for i in range(self._amount_queens)]

        first_chunk = first_genes[0:int(len(first_genes) / 2)]
        second_chunk = second_genes[int(len(second_genes) / 2):len(second_genes)]
        new_genes = first_chunk

        for i in range(len(second_chunk)):
            if not second_chunk[i] in new_genes:
                new_genes.append(second_chunk[i])

        for i in range(len(assistent_array)):
            if not assistent_array[i] in new_genes:
                new_genes.append(assistent_array[i])

        return new_genes

    def show_and_update_rate(self, individual: NQueens) -> float:
        if not individual.is_rated:
            individual.is_rated = True
            return self.to_rate(individual)
