from SuperClass.ClasseMagica import ClasseMagica
from Global.CLASSES_VARIAVEIS_GLOBAIS import MAGO_PROGRESSAO, MAGO_MAGIAS


class Mago(ClasseMagica):

    def __init__(self, nome, nivel) -> None:
        # Status Gerais
        self.classe = 'mago'
        super().__init__(nome, nivel, MAGO_PROGRESSAO,
                         MAGO_MAGIAS, self.classe)

    def mostraEspacosDeMagia(self):
        super().mostraEspacosDeMagia()
