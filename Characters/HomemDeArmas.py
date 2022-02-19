from Global.CLASSES_VARIAVEIS_GLOBAIS import HDA_PROGRESSAO
from SuperClass.Classe import Classe


class HomemDeArmas(Classe):

    def __init__(self, nome, nivel) -> None:
        # Status Gerais
        self.classe = 'Homem-de-Armas'
        super().__init__(nome, nivel, HDA_PROGRESSAO, self.classe)
