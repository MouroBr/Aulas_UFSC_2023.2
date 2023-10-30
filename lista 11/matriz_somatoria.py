from matriz_quadrada import matriz_quadrada


def matriz_somatoria(matriz):
    somatoria = 0
    linha = 0
    while linha < len(matriz):
        coluna = 0
        while coluna < len(matriz):
            somatoria = somatoria + (matriz[linha][coluna])
            coluna += 1
        linha += 1
    return somatoria


matriz = matriz_quadrada(4, 4)
resultado = matriz_somatoria(matriz)
print(resultado)
