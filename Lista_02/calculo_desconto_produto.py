preco_inicial = float(input('Digite o preço do produto: R$ '))
percentual_desconto = float(input('Digite o percenualde desconto:  '))

valor_desconto = (preco_inicial * (percentual_desconto/100))
calcula_desconto = preco_inicial - percentual_desconto


print(f'O valor do desconto {valor_desconto} e o valor final R${calcula_desconto}')

