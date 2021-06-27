import operator
import sys
import random
from typing import List, Optional

from src.models.n_queens import NQueens
from src.services.n_queens_service import NQueensService
from src.view.view_data import ViewData


class GeneticAlgorithmService(object):

    def __init__(self, service: NQueensService, view: ViewData):
        self.service = service
        self.view = view

    def execute(self, amount_steps: Optional[int] = 10000, amount_individuals: Optional[int] = 20):

        initial_population = list()
        for i in range(amount_individuals):
            initial_population.append(NQueens())

        for s in range(amount_steps):

            sons_population = self._generate_sons(initial_population)
            mutants_population = self._generate_mutants(initial_population)

            all_population = list()

            for i in range(amount_individuals):
                all_population.append(initial_population[i])
                all_population.append(sons_population[i])
                all_population.append(mutants_population[i])

            recalculing_all_population = self._recalculing_rate(all_population)

            self._show_worse_individual(s, recalculing_all_population)

            individuals_selected = self.selection(recalculing_all_population, 16, 4)

            self._show_better_individual(s, individuals_selected)

    def selection(self, individual_population: List[NQueens], amount_individual: int, amount_elitism: int) -> List[
        NQueens]:

        individuals_elite = self._elitism(individual_population, amount_elitism)

        for i in range(len(individuals_elite)):
            individual_population.remove(individuals_elite[i])

        individuals_roulette = self._addited_roulette(individual_population, amount_individual)

        individuals_selected = list()

        for i in range(len(individuals_elite)):
            individuals_selected.append(individuals_elite[i])

        for i in range(len(individuals_roulette)):
            individuals_selected.append(individuals_roulette[i])

        return individuals_selected

    def _generate_sons(self, individual_population: List[NQueens]) -> List[NQueens]:
        sons = list()
        for i in range(0, len(individual_population) - 2, 2):
            for j in range(1, len(individual_population) - 1, 2):
                list_sons = self.service.recombine(individual_population[i], individual_population[j])
                sons.append(list_sons[0])
                sons.append(list_sons[1])

        return sons

    def _generate_mutants(self, individual_population: List[NQueens]) -> List[NQueens]:
        mutants = list()
        for i in range(len(individual_population)):
            mutant = self.service.mutate(individual_population[i])
            mutants.append(mutant)

        return mutants

    def _elitism(self, individuals_population: List[NQueens], amount_elitism: int) -> List[NQueens]:
        four_individuals = list()
        individuals_population.sort(key=operator.attrgetter('rate'))
        for i in range(amount_elitism):
            four_individuals.append(individuals_population[i])

        return four_individuals

    def _addited_roulette(self, individuals_population: List[NQueens], amount_individual: int) -> List[NQueens]:
        for i in range(len(individuals_population)):
            new_rate = 1 / individuals_population[i].rate
            individuals_population[i].rate = new_rate

        individuals_drawn = list()

        for i in range(amount_individual):
            sum_rate = 0.0
            for s in range(len(individuals_population)):
                sum_rate += individuals_population[s].rate
            random_rate = random.uniform(0.0, sum_rate)
            aux_sum_rate = 0.0

            for j in range(len(individuals_population)):
                aux_sum_rate += individuals_population[j].rate
                if aux_sum_rate >= random_rate:
                    individual = individuals_population[j]
                    individuals_drawn.append(individual)
                    individuals_population.remove(individual)
                    break

        return individuals_drawn

    def _recalculing_rate(self, individuals_population: List[NQueens]):
        for i in range(len(individuals_population)):
            new_rate = self.service.show_and_update_rate(individuals_population[i])
            individuals_population[i].rate = new_rate
            individuals_population[i].old_rate = new_rate

        return individuals_population



    def _show_better_individual(self, generation: int, individual_population: List[NQueens]):
        better_individual = NQueens()
        better_individual.rate = sys.maxsize
        for i in range(len(individual_population)):
            if individual_population[i].old_rate < better_individual.rate:
                better_individual = individual_population[i]

        self.view.show_better_individual(generation, better_individual)

    def _show_worse_individual(self, generation: int, individual_population: List[NQueens]):
        worse_individual = NQueens()
        worse_individual.rate = sys.maxsize * (-1)

        for i in range(len(individual_population)):
            if individual_population[i].old_rate > worse_individual.rate:
                worse_individual = individual_population[i]

        self.view.show_worse_individual(generation, worse_individual)
