num = int((input()))
a, b = 0, 1


while a < num :
    print(a, end=',')
    a, b = b , a+b
print(a)

'''
def modulo_lista(lista):
    # Inicializa uma lista vazia para armazenar os módulos
    modulos = []

    # Percorre a lista original
    for numero in lista:
        # Verifica se o número é negativo
        if numero < 0:
            modulo = -numero  # Se for negativo, torna-o positivo
        else:
            modulo = numero   # Se for positivo ou zero, mantém o mesmo valor
        modulos.append(modulo)

    # Retorna a lista de módulos
    return modulos

# Exemplo de uso da função
lista_original = [1, -2, 3, -4, 5]
resultados = modulo_lista(lista_original)
print(resultados)  # Isso imprimirá [1, 2, 3, 4, 5]




'''