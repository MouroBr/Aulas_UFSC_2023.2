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
                linha_nova.append(matriz_ìnicial[linha][coluna] * 10)
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
        print()

 def main():
    matriz_inicial = matriz_0(6, 6, 9)
    nova_matriz = matriz_diagonal_0(matriz_inicial)
    imprime_matriz(nova_matriz)


if __name__ == "__main__":
    main()