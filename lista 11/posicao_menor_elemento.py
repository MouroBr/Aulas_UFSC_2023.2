from matriz_quadrada import matriz_quadrada


def posicao_menor_elemento(matriz):
    menor_elemento = 0
    posicao = []
    linha = 0
    while linha < len(matriz):
        coluna = 0
        while coluna < len(matriz):
            elemento = matriz[linha][coluna]
            if elemento < menor_elemento:
                menor_elemento = elemento
                posicao = [linha, coluna]
            coluna += 1
        linha += 1
    return [menor_elemento, posicao]


matriz = matriz_quadrada(6, 6)
resultado = posicao_menor_elemento(matriz)
print(resultado)
