class Classe:

    def __init__(self, nome, nivel, PROGRESSAO, classe) -> None:
        self.classe = classe
        # Status Gerais
        self.progressao = PROGRESSAO
        self.nome = nome.title()
        self.nivel = nivel
        self.totalXP = PROGRESSAO[nivel - 1][1]
        self.dadoDeVida = PROGRESSAO[nivel - 1][2]
        self.baseDeAtaque = PROGRESSAO[nivel - 1][3]
        self.jogadaDeProtecao = PROGRESSAO[nivel - 1][4]

        # Status Especificos
        self.atualXP = self.totalXP
        self.proximoNivelXP = self.totalXP - self.atualXP

    def ganhaXP(self, valor):
        if (self.atualXP == self.totalXP and self.totalXP != 0):
            self.atualizaStatus()
        self.atualXP = self.atualXP + valor
        self.proximoNivelXP = self.totalXP - self.atualXP

    def atualizaStatus(self):
        self.nivel += 1
        self.totalXP = self.progressao[self.nivel][1]
        self.dadoDeVida = self.progressao[self.nivel - 1][2]
        self.baseDeAtaque = self.progressao[self.nivel - 1][3]
        self.jogadaDeProtecao = self.progressao[self.nivel - 1][4]

    def mostraStatus(self):
        print(f'Nome: {self.nome} | Nível: {self.nivel}')
        print(f'PVs: ?? | Classe: {self.classe}')
        print(f'XP: {self.atualXP}/{self.totalXP} | DV: {self.dadoDeVida}')
        print(f'BA: {self.baseDeAtaque} | JP: {self.jogadaDeProtecao}')
