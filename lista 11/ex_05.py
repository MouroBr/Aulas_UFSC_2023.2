import ex_02


def matriz_diagonal_0(matriz_ìnicial):
    linha = 0
    nova_matriz = []
    while linha < len(matriz_ìnicial):
        linha_nova = []
        coluna = 0
        while coluna < len(matriz_ìnicial):
            if coluna == linha:
                linha_nova.append(0)
                coluna += 1
            else:
                linha.append(matriz_ìnicial[linha][coluna] * 10)
        linha += 1
        nova_matriz.append(linha_nova)
    return nova_matriz


def imprime_matriz(matriz):

