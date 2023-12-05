class Juiz:
    def __init__(self, jogo):
        self.jogo = jogo

    def verificar_vitoria(self, jogador):
        return (
            self.verificar_horizontal(jogador) or
            self.verificar_vertical(jogador) or
            self.verificar_diagonal_principal(jogador) or
            self.verificar_diagonal_secundaria(jogador)
        )

    def verificar_horizontal(self, jogador):
        for linha in self.jogo.tabuleiro.tabuleiro:
            for i in range(len(linha) - 3):
                if all(jogador.simbolo == simbolo for simbolo in linha[i:i + 4]):
                    return True
        return False

    def verificar_vertical(self, jogador,):
        for coluna in range(self.jogo.tabuleiro.colunas):
            for i in range(self.jogo.tabuleiro.linhas - 3):
                if all(self.jogo.tabuleiro.tabuleiro[i + j][coluna] == jogador.simbolo for j in range(4)):
                    return True
            return  False

    def verificar_diagonal_principal(self, jogador):
        for i in range(self.jogo.tabuleiro.linhas - 3):
            for j in range(self.jogo.tabuleiro.colunas - 3):
                if all(self.jogo.tabuleiro.tabuleiro[i + k][j + k] == jogador.simbolo for k in range(4)):
                    return True
            return False

    def verificar_diagonal_secundaria(self, jogador):
        for i in range(self.jogo.tabuleiro.linhas - 3):
            for j in range(3, self.jogo.tabuleiro.colunas):
                if all(self.jogo.tabuleiro.tabuleiro[i + k][j + k] == jogador.simbolo for k in range(4)):
                    return True
            return False
