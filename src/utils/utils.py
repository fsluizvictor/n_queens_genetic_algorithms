#ALGORITHM - STEPS
# inicializar o tamanho do vetor de genes e seus valores de forma aleatória
# os valores aleatórios devem obedecer a ideia da permutação

# fazer um for para preencher uma lista popIni com o nInd(individuos)
# para gerar os incdividuos
# iniciar utilizar o individuo factory passado por parametro

# ELITISMO
# verificar se o problema é de minimização, caso seja é preciso ordenar o array do menor para maior avaliação
# selecionar os "amount_elitism" individuos no inicio do array e coloca-los em uma nova população
# ROLETA VICIADA
# --> MAXIMIZAÇÃO
# 1 - Obter a soma das avaliações de todos os individuos que irão  participar da roleta
# 2 - gerar um numero aleatorio (r) q vai de 0 ao somatorio
# 3 - para selecionar um individuo da minha lista, vou percorrendo a lista somando (soma2) novamente a avaliação até obter um valor de soma maior que o valor aletório (soma2>r)
# --> MINIMIZAÇÃO
# 0 - inverter a avaliação de todos os individuos na forma (1/avaliação) e utilizar estes novos valores para os passos 1, 2 e 3.
# 1 - Obter a soma das avaliações de todos os individuos que irão  participar da roleta
# 2 - gerar um numero aleatorio (r) q vai de 0 ao somatorio
# 3 - para selecionar um individuo da minha lista, vou percorrendo a lista somando (soma2) novamente a avaliação até obter um valor de soma maior que o valor aletório (soma2>r)
# 4 - retirar o individuo selecionado para a nova população e voltar para o passo 1
# observação --> realizar os passos 1,2,3 e 4 n vezes até completar newPop.size() = amount_individual

# imprimir o numero da geração, o melhor individuo e a avaliação deste melhor individuo
        # levar em consideração se o problema é de minimização ou maximização


# recombinar os individuos self e p2 gerando 2 filhos utilizando a ideia de permutação


# gerar um novo individuo mutante com os genes do individuo self mutados e uma taxa de mutação de 5% a 10%
    # --> se maior que noventa deve sofrer mutação


# realizar a contagem de colisões que ocorrem entre as rainhas.
