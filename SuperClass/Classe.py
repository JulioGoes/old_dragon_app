class Classe:

    def __init__(self, nome, nivel, PROGRESSAO, classe) -> None:
        self.classe = classe
        # Status Gerais
        self.progressao = PROGRESSAO
        self.nome = nome.title()
        self.nivel = nivel
        self.dadoDeVida = self.progressao[nivel - 1][2]
        self.baseDeAtaque = self.progressao[nivel - 1][3]
        self.jogadaDeProtecao = self.progressao[nivel - 1][4]

        # Status de Atributos
        self.forca = 1
        self.destreza = 1
        self.constituicao = 1
        self.inteligencia = 1
        self.sabedoria = 1
        self.carisma = 1

        # Status Especificos
        self.atualXP = self.progressao[nivel - 1][1]
        if self.nivel < 5:
            self.proxNivelXP = self.progressao[nivel][1]
        else:
            self.proxNivelXP = 'Max'

    def ganhaXP(self, valor):
        if (self.atualXP == self.proxNivelXP and self.proxNivelXP != 0):
            self.atualizaStatus()
        self.atualXP = self.atualXP + valor

    def atualizaStatus(self):
        self.nivel += 1
        self.proxNivelXP = self.progressao[self.nivel][1]
        self.dadoDeVida = self.progressao[self.nivel - 1][2]
        self.baseDeAtaque = self.progressao[self.nivel - 1][3]
        self.jogadaDeProtecao = self.progressao[self.nivel - 1][4]

    def mostraStatus(self):
        print(f'Nome: {self.nome} | Nível: {self.nivel}')
        print(f'PVs: ?? | Classe: {self.classe}')
        print(f'XP: {self.atualXP}/{self.proxNivelXP} | DV: {self.dadoDeVida}')
        print(f'BA: {self.baseDeAtaque} | JP: {self.jogadaDeProtecao}')
        print(f"\nForça:        {self.forca}",
              f"\nDestreza:     {self.destreza}",
              f"\nConstituição: {self.constituicao}",
              f"\nInteligência: {self.inteligencia}",
              f"\nSabedoria:    {self.sabedoria}",
              f"\nCarisma:      {self.carisma}")

    def defineAtributo(self, atributos):
        self.forca = atributos[0]
        self.destreza = atributos[1]
        self.constituicao = atributos[2]
        self.inteligencia = atributos[3]
        self.sabedoria = atributos[4]
        self.carisma = atributos[5]
