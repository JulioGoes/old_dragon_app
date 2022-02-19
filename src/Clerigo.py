from CLASSES_VARIAVEIS_GLOBAIS import CLERIGO_AFASTAR, \
                                      CLERIGO_MAGIAS, \
                                      CLERIGO_PROGRESSAO
from Classe import Classe


class Clerigo(Classe):

    def __init__(self, nome, nivel) -> None:
        # Status Gerais
        self.classe = 'clerigo'
        super().__init__(nome, nivel, CLERIGO_PROGRESSAO, self.classe)

        # Espaços de Magias
        self.primeiroCirculoTotal = CLERIGO_MAGIAS[nivel - 1][0]
        self.segundoCirculoTotal = CLERIGO_MAGIAS[nivel - 1][1]
        self.terceiroCirculoTotal = CLERIGO_MAGIAS[nivel - 1][2]

        self.primeiroCirculoAtual = CLERIGO_MAGIAS[nivel - 1][0]
        self.segundoCirculoAtual = CLERIGO_MAGIAS[nivel - 1][1]
        self.terceiroCirculoAtual = CLERIGO_MAGIAS[nivel - 1][2]

        # Afastar Mortos-Vivos
        self.afastarDV1 = CLERIGO_AFASTAR[nivel - 1][1]
        self.afastarDV2 = CLERIGO_AFASTAR[nivel - 1][2]
        self.afastarDV3 = CLERIGO_AFASTAR[nivel - 1][3]
        self.afastarDV4 = CLERIGO_AFASTAR[nivel - 1][4]
        self.afastarDV5 = CLERIGO_AFASTAR[nivel - 1][5]

    def mostraAfastar(self):
        print('***AFASTAR MORTOS-VIVOS***')
        print(f'DV 1: {self.afastarDV1} | DV 2: {self.afastarDV2}')
        print(f'DV 3: {self.afastarDV3} | DV 4: {self.afastarDV4}')
        print(f'DV 5: {self.afastarDV5}')
