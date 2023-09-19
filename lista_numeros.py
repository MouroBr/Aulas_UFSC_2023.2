from questao01 import lista_aleatoria

numeros = lista_aleatoria(10)
cont = 0

while cont < 10:

    for numero in numeros:
        if numero < 0:
            numero = numero * (-1)
            lista = [numero]
