'''
Recebe uma lista com números,
encontra o maior número dessa lista
e retorna uma nova lista com todos os números da lista original
divididos pelo maior número.
(utilize a função max do Python):
'''


def dividindo_lista(lista):
    divisor = max(lista)
    divididos = []

    for valor in lista:
        resultado = valor / divisor
        divididos.append(resultado)

    return divididos


lista_original = [10, 10, 10, 10, 10]

print(dividindo_lista(lista_original))
