from typing import List

from src.interfaces.individual import Individual


class GeneticAlgorithm:

    def execute(self, amount_steps: int, amount_individuals: int) -> Individual:
        # fazer um for para preencher uma lista popIni com o nInd(individuos)
        # para gerar os incdividuos iniciar utilizar o individuo factory passado por parametro
        pass

    def show_better_individual(self, generation: int, individual_population: List[Individual]):
        # imprimir o numero da geração, o melhor individuo e a avaliação deste melhor individuo
        # levar em consideração se o problema é de minimização ou maximização
        pass

    def selection(self, individual_population: List[Individual], amount_individual, amount_elitism: int) -> List[
        Individual]:
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

    def find_sons(self, individual_population: List[Individual]) -> List[Individual]:
        pass

    def find_mutantes(self, individual_population: List[Individual]) -> List[Individual]:
        pass
