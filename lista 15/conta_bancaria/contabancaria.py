class ContaBancaria:

    def __init__(self, numero_conta, cliente, senha):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.senha = senha
        self.saldo = 0

    def verifica_saldo(self):
        if self.saldo < 0:
            print(self.mostrar_saldo_negativo())
        else:
            return f"R${self.saldo}"

    def sacar(self, valor_saque):
        if valor_saque <= 0:
            return False
        if valor_saque > self.saldo:
            return False
        else:
            self.saldo -= valor_saque
            return True

    def depositar(self, valor_deposito):
        if valor_deposito < 0:
            return False
        else:
            self.saldo += valor_deposito

    def trocar_senha(self, nova_senha):
        self.senha = nova_senha
        return "Senha alterada com sucesso."

    def mostrar_saldo_negativo(self):
        if self.saldo < 0:
            return f"Saldo negativo R${self.saldo}"
