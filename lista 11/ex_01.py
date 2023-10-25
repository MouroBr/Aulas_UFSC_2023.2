def matriz_0(linha, coluna):
    matriz = []
    lin = 0
    while lin < linha:
        linha_nova = []
        col = 0
        while col < coluna:
            linha_nova.append(0)
            col += 1
        lin += 1
        matriz.append(linha_nova)
    return matriz


resultado = matriz_0(3, 3)
print(resultado)
