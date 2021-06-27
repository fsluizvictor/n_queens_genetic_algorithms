from typing import List

from src.models.n_queens import NQueens


class ViewData:
    def __init__(self):
        pass

    def show_better_individual(self, step_generation: int, individual: NQueens):
        print('==============================================')
        print('===============BETTER INDIVIDUAL===============')
        print('GENERATION : ', step_generation)
        print('Collisions : {:.2f}'.format(individual.old_rate))
        print('Collisions : {:.2f}'.format(individual.rate))
        print('Genes : ')
        print(individual.genes)
        print('==============================================')

    def show_worse_individual(self, step_generation: int, individual: NQueens):
        print('==============================================')
        print('===============WORSE INDIVIDUAL================')
        print('GENERATION : ', step_generation)
        print('Collisions : {:.2f}'.format(individual.old_rate))
        print('Collisions : {:.2f}'.format(individual.rate))
        print('Genes : ')
        print(individual.genes)
        print('==============================================')
