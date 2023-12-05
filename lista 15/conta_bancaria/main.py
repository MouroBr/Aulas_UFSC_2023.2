from contabancaria import ContaBancaria

contas = []


def mostrar_menu():
    print("1 : Criar Conta")
    print("2 : Sacar")
    print("3 : Depositar ")
    print("4 : Trocar Senha")
    print("5 : Verificar Saldo")
    print("6 : Sair")

    while True:
        mostrar_menu()
        escolha = input("O que deseja fazer: ")
        numero_conta = 0000
        if escolha == "1":
            cliente = input('Digite o nome do Titular da conta: ')
            senha = int(input('Digite uma senha com 6 digitos: '))
            numero_conta += 1
            contas.append(ContaBancaria(numero_conta, cliente, senha))

        elif escolha == "2":
            saque = float(input('Digite o valor do saque: R$'))
            ContaBancaria.sacar(saque)

        elif escolha == "3":
            deposito = float(input('Digite o valor do deposito: R$'))
            ContaBancaria.depositar(deposito)

        elif escolha == "4":
            nova_senha = input("Digite a nova senha: ")
            ContaBancaria.trocar_senha(nova_senha)

        elif escolha == "5":
            ContaBancaria.verifica_saldo()

        else;

