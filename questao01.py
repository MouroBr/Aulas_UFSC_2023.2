from random import randint


def lista_aleatoria(num):
    numeros = []
    cont = 0
    while cont < num:
        numeros.append(randint(-100, num * 2))
        cont = cont + 1
    return numeros


lista = lista_aleatoria(10)

print(lista)
