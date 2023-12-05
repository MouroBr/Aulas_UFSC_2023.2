def maiores_diagonais_acima_principal(matriz):
    tamanho = len(matriz)
    i = 0

    # Verifica se a matriz é quadrada usando um while
    while i < tamanho:
        if len(matriz[i]) != tamanho:
            return []  # Retorna uma lista vazia se a matriz não for quadrada
        i += 1

    maiores_elementos = []

    i = 0
    while i < tamanho - 1:
        j = 0
        diagonal_acima_principal = []

        # Constrói a diagonal acima da principal sem usar for
        while j < tamanho - i - 1:
            diagonal_acima_principal.append(matriz[j][i + j + 1])
            j += 1

        # Encontra o maior elemento manualmente
        maior_elemento = diagonal_acima_principal[0]
        j = 1
        while j < len(diagonal_acima_principal):
            if diagonal_acima_principal[j] > maior_elemento:
                maior_elemento = diagonal_acima_principal[j]
            j += 1

        maiores_elementos.append(maior_elemento)
        i += 1

    return maiores_elementos

# Exemplo de uso:
matriz_exemplo = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

resultado = maiores_diagonais_acima_principal(matriz_exemplo)
print(resultado)
