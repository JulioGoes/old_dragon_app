from SuperClass.Classe import Classe


class ClasseMagica(Classe):

    def __init__(self, nome, nivel, PROGRESSAO, MAGIAS, classe) -> None:
        super().__init__(nome, nivel, PROGRESSAO, classe)
        self.magias = MAGIAS

        # Espaços de Magias
        self._circulo1Total = self.magias[nivel - 1][0]
        self._circulo2Total = self.magias[nivel - 1][1]
        self._circulo3Total = self.magias[nivel - 1][2]

        self._circulo1Atual = self.magias[nivel - 1][0]
        self._circulo2Atual = self.magias[nivel - 1][1]
        self._circulo3Atual = self.magias[nivel - 1][2]

    def mostraEspacosDeMagia(self):
        print('***Espaços de Magia***')
        print(f'1º Círculo: {self._circulo1Atual}/{self._circulo1Total}')
        print(f'2º Círculo: {self._circulo2Atual}/{self._circulo2Total}')
        print(f'3º Círculo: {self._circulo3Atual}/{self._circulo3Total}')
