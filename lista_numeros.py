# dada a lista acima eu tenho que devolver uma nova lista com os modulos dos valores
# passo 1: percorre a lista e verificar se valor é <0
# caso valor negativo * (-1):
# cada valor apos ser verificado deve ser realocado em uma nova lista na mesma ordem
# retornar a tela a lista contendo os módulos

def modulo_lista(lista):
    modulos = []

    for numero in lista:

        if numero < 0:
            modulo = -numero
        else:
            modulo = numero
        modulos.append(modulo)

    return modulos


lista_original = [1, -2, 3, -4, 5]
resultados = modulo_lista(lista_original)
print(resultados)
