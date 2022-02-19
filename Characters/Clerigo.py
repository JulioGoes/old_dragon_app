from SuperClass.ClasseMagica import ClasseMagica
from Global.CLASSES_VARIAVEIS_GLOBAIS import CLERIGO_AFASTAR, \
                                      CLERIGO_MAGIAS, \
                                      CLERIGO_PROGRESSAO


class Clerigo(ClasseMagica):

    def __init__(self, nome, nivel) -> None:
        # Status Gerais
        self.classe = 'clerigo'
        super().__init__(nome, nivel, CLERIGO_PROGRESSAO,
                         CLERIGO_MAGIAS, self.classe)

        # Afastar Mortos-Vivos
        self.clerigoAfastar = CLERIGO_AFASTAR
        self._afastarDV1 = self.clerigoAfastar[nivel - 1][1]
        self._afastarDV2 = self.clerigoAfastar[nivel - 1][2]
        self._afastarDV3 = self.clerigoAfastar[nivel - 1][3]
        self._afastarDV4 = self.clerigoAfastar[nivel - 1][4]
        self._afastarDV5 = self.clerigoAfastar[nivel - 1][5]

    def mostraAfastar(self):
        print('***AFASTAR MORTOS-VIVOS***')
        print(f'DV 1: {self._afastarDV1} | DV 2: {self._afastarDV2}')
        print(f'DV 3: {self._afastarDV3} | DV 4: {self._afastarDV4}')
        print(f'DV 5: {self._afastarDV5}')

    def mostraEspacosDeMagia(self):
        super().mostraEspacosDeMagia()
