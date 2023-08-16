cigarros_dias = int(input('Quantos cigarros você fuma por dia em média: '))
anos_fumo = int(input('Fumante a quantos anos: '))

total_cigarros = (cigarros_dias * 365 * anos_fumo)

minutos_perdidos = total_cigarros * 10

dias_perdidos = minutos_perdidos / (24 * 60)

print('Total de tempo fumado {}dias.'.format(dias_perdidos))
