from SuperClass.Classe import Classe
from Global.CLASSES_VARIAVEIS_GLOBAIS import LADRAO_PROGRESSAO, LADRAO_TALENTOS


class Ladrao(Classe):

    def __init__(self, nome, nivel) -> None:
        # Status Gerais
        self.classe = 'Ladrão'
        super().__init__(nome, nivel, LADRAO_PROGRESSAO, self.classe)

        # Talentos de Ladrão
        self.ladraoTalentos = LADRAO_TALENTOS
        self.arrombar = self.ladraoTalentos[nivel - 1][1]
        self.armadilhas = self.ladraoTalentos[nivel - 1][2]
        self.escalar = self.ladraoTalentos[nivel - 1][3]
        self.furtividade = self.ladraoTalentos[nivel - 1][4]
        self.punga = self.ladraoTalentos[nivel - 1][5]
        self.percepcao = self.ladraoTalentos[nivel - 1][6]
        self.ataqueFurtivo = self.ladraoTalentos[nivel - 1][7]

    def mostraTalentos(self):
        print('***Talentos de Ladrão***')
        print(f'Arrombar: {self.arrombar} | Armadilhas: {self.armadilhas}')
        print(f'Escalar: {self.escalar}% | Furtividade: {self.furtividade}%')
        print(f'Punga: {self.punga}% | Percepção: {self.percepcao} no 1d6')
        print(f'Ataque Furtivo: x{self.ataqueFurtivo}')
