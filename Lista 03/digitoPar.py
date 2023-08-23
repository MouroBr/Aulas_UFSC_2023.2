valor = int(input('Digite um valor no padrão 000: '))

segundo_digito = (valor // 10) % 10

if (segundo_digito % 2) == 0:
    print('Valor da casa decimal par')

else:
    print('Valor da casa decimal impar')
