def fatorial(numero):
    fator = 1
    n = 1
    if numero == 0 or numero == 1:
        return 1
    else:
        while n <= numero:
            fator = fator * n
            n += 1
        return fator


def serie_infinita(num):
    cont = 0
    valor = 0
    while cont < num:
        parcial = 1 / fatorial(cont)
        valor = parcial + valor
        cont += 1

    return valor


resultado = serie_infinita(20)
print(resultado)
