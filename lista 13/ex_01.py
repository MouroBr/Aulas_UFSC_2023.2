from matriz_quadrada import matriz_quadrada


def media_diagonal(matriz):
    linha = 0
    while linha < len(matriz):
        coluna = 0
        while coluna < len(matriz):
            valor = (matriz[linha][coluna])
