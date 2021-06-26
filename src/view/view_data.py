from typing import List

from src.models.n_queens import NQueens


class ViewData:
    def __init__(self):
        pass

    def show_list(self, list_genes: List[int]):
        print("Genes : ")
        print(list_genes)

    def show_better_individual(self, step_generation: int, individual: NQueens):
        print("==============================================")
        print("GENERATION : %s", step_generation)
        print("Collisions : %s", individual.rate)
        print("Genes : ")
        print(individual.genes)
        print("==============================================")
