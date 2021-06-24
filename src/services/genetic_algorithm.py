from typing import List

from src.interfaces.individual import Individual
from src.models.n_queens import NQueens
from src.services.n_queens_service import NQueensService


class GeneticAlgorithm:

    def __init__(self, service: NQueensService):
        self.service = service

    def execute(self, amount_steps: int, amount_individuals: int) -> List[NQueens]:
        # fazer um for para preencher uma lista popIni com o nInd(individuos)
        # para gerar os incdividuos iniciar utilizar o individuo factory passado por parametro
        initial_population = list()
        for i in range(amount_individuals):
            initial_population.append(NQueens())

        sons_population = self.generate_sons(initial_population)
        mutants_population = self.generate_mutants(initial_population)

        return list()

    def show_better_individual(self, generation: int, individual_population: List[Individual]):
        # imprimir o numero da geração, o melhor individuo e a avaliação deste melhor individuo
        # levar em consideração se o problema é de minimização ou maximização
        pass

    def selection(self, individual_population: List[Individual], amount_individual, amount_elitism: int) -> List[
        NQueens]:
        # ELITISMO
        # verificar se o problema é de minimização, caso seja é preciso ordenar o array do menor para maior avaliação
        # selecionar os "amount_elitism" individuos no inicio do array e coloca-los em uma nova população
        # ROLETA VICIADA
        # --> MAXIMIZAÇÃO
        # 1 - Obter a soma das avaliações de todos os individuos que irão  participar da roleta
        # 2 - gerar um numero aleatorio (r) q vai de 0 ao somatorio
        # 3- para selecionar um individuo da minha lista, vou percorrendo a lista somando (soma2) novamente a avaliação até obter um valor de soma maior que o valor aletório (soma2>r)
        # --> MINIMIZAÇÃO
        # 0 - inverter a avaliação de todos os individuos na forma (1/avaliação) e utilizar estes novos valores para os passos 1, 2 e 3.
        # 1 - Obter a soma das avaliações de todos os individuos que irão  participar da roleta
        # 2 - gerar um numero aleatorio (r) q vai de 0 ao somatorio
        # 3- para selecionar um individuo da minha lista, vou percorrendo a lista somando (soma2) novamente a avaliação até obter um valor de soma maior que o valor aletório (soma2>r)
        # 4 - retirar o individuo selecionado para a nova população e voltar para o passo 1
        # observação --> realizar os passos 1,2,3 e 4 n vezes até completar newPop.size() = amount_individual
        pass

    def generate_sons(self, individual_population: List[NQueens]) -> List[NQueens]:
        sons = list()
        for i in range(0, len(individual_population) - 2, 2):
            for j in range(1, len(individual_population) - 1, 2):
                list_sons = self.service.recombine(individual_population[i], individual_population[j])
                sons.append(list_sons[0])
                sons.append(list_sons[1])

        return sons

    def generate_mutants(self, individual_population: List[NQueens]) -> List[NQueens]:
        mutants = list()
        for i in range(len(individual_population)):
            mutant = self.service.mutate(individual_population[i])
            mutants.append(mutant)

        return mutants
