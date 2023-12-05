from Trabalho_jogo.tabuleiro import Tabuleiro
from Trabalho_jogo.jogador import Jogador
from Trabalho_jogo.juiz import Juiz


class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador1 = None
        self.jogador2 = None
        self.juiz = Juiz(self)
