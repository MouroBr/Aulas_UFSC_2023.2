class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        self.criar_grid()

    def criar_grid(self):
        for i in range(1, 6):
            linha = []
            for j in range(1, 7):
                celula = []
                linha.append(celula)
            self.tabuleiro.append(linha)

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print(linha)


# tabuleiro = Tabuleiro()
# tabuleiro.mostrar_tabuleiro()
