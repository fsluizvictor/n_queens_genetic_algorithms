import random
from typing import Optional, List

from src.models.n_queens import NQueens


class NQueensService:

    def __init__(self, amount_queens: Optional[int] = 8):
        self._amount_queens = amount_queens

    def recombine(self, first_individual: NQueens, second_individual: NQueens) -> List[NQueens]:

        first_son = self._without_repetition(first_individual.genes, second_individual.genes)
        second_son = self._without_repetition(second_individual.genes, first_individual.genes)
        return [NQueens(8, first_son), NQueens(8, second_son)]

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

    def to_rate(self, individual: NQueens) -> float:
        collisions = 0.0
        genes = individual.genes
        for i in range(len(genes)):
            for j in range(i + 1, len(genes)):
                if genes[i] == genes[j] or i - genes[i] == j - genes[j] or i + genes[i] == j + genes[j]:
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
        return self.to_rate(individual)
