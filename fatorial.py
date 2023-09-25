def fatorial(numero):
    fator = 1
    n = 1
    if numero == 0 or numero == 1:
        print("1")
    else:
        while n <= numero:
            fator = fator * n
            n += 1
    return fator


resultado = fatorial(5)
print(resultado)