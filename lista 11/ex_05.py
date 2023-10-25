from ex_02 import matriz_0


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


def imprime_matriz(nova_matriz):
    linha = 0
    matriz_utilizada = nova_matriz
    while linha < len(nova_matriz):
        coluna = 0
        while coluna < len(nova_matriz):
            print(matriz_utilizada[linha][coluna], end='')
            coluna += 1
        linha += 1





 def main():
     matriz_0(6, 6, 9)