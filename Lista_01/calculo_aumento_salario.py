salario_atual = int(input('Digite o valor atual do sálario: '))
percentual_aumento = float(input('Digite o percentual de aumento: '))

novo_salario = (salario_atual * (percentual_aumento/100)) + salario_atual

print("O salário com aumento de {}% é de R${:.2f}.".format(percentual_aumento, novo_salario))
