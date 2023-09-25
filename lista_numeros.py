from typing import List


# dada a lista acima eu tenho que devolver uma nova lista com os modulos dos valores
# passo 1: percorre a lista e verificar se valor é <0
# caso valor negativo * (-1):
# cada valor apos ser verificado deve ser realocado em uma nova lista na mesma ordem
# retornar a tela a lista contendo os módulos


def lista_modulos(lista):
    indice = 0
    modulos = []
    while indice < len(lista):
        if lista[indice] >= 0:
            modulos.append(lista_inicial[indice])

        else:
            valor_negativo = lista[indice]
            modulos.append(valor_negativo * -1)
        indice += 1
    return modulos


lista_inicial = [8, -8, 45]
resultado = lista_modulos(lista_inicial)
print(resultado)
