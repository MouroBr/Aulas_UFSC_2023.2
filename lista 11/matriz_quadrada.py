from random import randint


def matriz_quadrada(linha, coluna):
    matriz = []
    lin = 0
    while lin < linha:
        linha_nova = []
        col = 0
        while col < coluna:
            linha_nova.append(randint(-9, 9))
            col += 1
        lin += 1
        matriz.append(linha_nova)
    return matriz


resultado = matriz_quadrada(4, 5)
print(resultado)
