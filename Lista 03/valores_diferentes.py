valor_01 = int(input('Digite o primeiro valor: '))
valor_02 = int(input('Digite o segundo valor: '))
valor_03 = int(input('Digite o terceiro valor: '))

verificador = False

if valor_01 != valor_02 and valor_01 != valor_03 and valor_02 != valor_03:
    verificador = True

print(verificador)
