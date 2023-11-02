from matriz_quadrada import matriz_quadrada


def mostra_matriz(matriz):
    matriz_funcional = matriz
    linha = 0
    while linha < len(matriz_funcional):
        coluna = 0
        while coluna < len(matriz_funcional):
            print(matriz_funcional[linha][coluna], end=' ')
            coluna += 1
        print()
        linha += 1


matriz = matriz_quadrada(3, 3)
print(mostra_matriz(matriz))
