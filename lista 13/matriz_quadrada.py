from random import randint


def matriz_quadrada(linha, coluna, limite=(randint(9))):
    matriz = []
    lin = 0
    while lin < linha:
        linha_nova = []
        col = 0
        while col < coluna:
            linha_nova.append(randint(limite))
            col += 1
        lin += 1
        matriz.append(linha_nova)
    return matriz
