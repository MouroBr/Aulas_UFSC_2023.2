def encontra_primo(numero):
    valor = 1
    contador = 0
    while valor <= numero:
        if (numero % valor) == 0:
            contador += 1
        valor += 1
    if contador == 2:
        return numero


resultado = encontra_primo(7)
print(resultado)
