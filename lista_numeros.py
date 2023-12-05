from typing import List

# dada a lista acima eu tenho que devolver uma nova lista com os modulos dos valores
# passo 1: percorre a lista e verificar se valor é <0
# caso valor negativo * (-1):
# cada valor apos ser verificado deve ser realocado em uma nova lista na mesma ordem
# retornar a tela a lista contendo os módulos

lista_inicial = [8, -8, 45]
indice = 0
lista_modulos = []
while indice < len(lista_inicial):
    if lista_inicial[indice] >= 0:
        lista_modulos.append(lista_inicial[indice])

    else:
        valor_negativo = lista_inicial[indice]
         lista_modulos.append(valor_negativo * -1)
