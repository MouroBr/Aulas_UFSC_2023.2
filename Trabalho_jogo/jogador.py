class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo


class CPU(Jogador):
    def __init__(self, nome="CPU", simbolo="0"):
        super().__init__(nome, simbolo)


# jogador01 = Jogador("Bruno", "x")
# jogador02 = CPU()
