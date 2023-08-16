catOp = int(input('Digite o valor do cateto oposto: '))
catAd = int(input('Digite o valor do cateto adjacente: '))

hip = ((catOp ** 2) + (catAd ** 2)) ** 0.5

print(f'Hipotenusa = {hip}')
