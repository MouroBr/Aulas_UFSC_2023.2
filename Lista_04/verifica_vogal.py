numero = int(input())

if numero == 2:
    print('É primo!')

elif (numero % 2) == 0 and (numero % 3) == 0:
    print('Não é primo!')

else:

    if numero % numero == 0 and numero % 1 == 0:
        print('É primo!')


