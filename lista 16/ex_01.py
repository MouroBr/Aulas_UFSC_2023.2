class Pessoa:
    def __init__(self, nome, endereco, telefone, email):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email


class Estudante(Pessoa):
    def __init__(self, nome, endereco, telefone, email, graduacao):
        super().__init__(nome, endereco, telefone, email)
        self.__graduacao = graduacao


class Funcionario(Pessoa):
    def __init__(self, nome, endereco, telefone, email, numero_sala, salario, data_admicao):
        super().__init__(nome, endereco, telefone, email)
        self.__numero_sala = numero_sala
        self.__salario = salario
        self.__data_admicao = data_admicao


class Data:

    def _init_(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano







