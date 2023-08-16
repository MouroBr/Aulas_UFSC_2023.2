km_percorridos = int(input('Digite a quantidade de quilometros percorridos: '))
dias_alugados = int(input('Digite a quantidade de dias alugados: '))

total_valor_dias = dias_alugados * 60
valor_total_km = km_percorridos * 0.15

total_pagar = total_valor_dias + valor_total_km

print('Valor total do aluguel do veiculo: R${}'.format(total_pagar))


