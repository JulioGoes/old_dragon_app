from cria_classe import criaClasse, criaClerigo, criaHdA, criaLadrao, criaMago
# from consulta_bancodedados import cria_lista_classe


class CriaPersonagem(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.nome = nome
        self.hp = 1

    def status_atributos(self, atributos):
        self.str = atributos[0]
        self.dex = atributos[1]
        self.con = atributos[2]
        self.int = atributos[3]
        self.sab = atributos[4]
        self.cha = atributos[5]
        print('\n**ATRIBUTOS**')
        print(f'Força: {self.str} | Destreza: {self.dex}')
        print(f'Constituição: {self.con} | Inteligência {self.int}')
        print(f'Sabedoria: {self.sab} | Carisma: {self.cha}')


class CriaPersonagemClerigo(criaClerigo, CriaPersonagem):

    def __init__(self, nome, nivel, progressao, atributos):
        super().__init__(nome, nivel, progressao)
        self.hp = self.dv * 8
        self.classe = 'Clerigo'
        self.atributos = atributos

    def status_classe(self):
        super().status_classe(self.hp, self.classe)

    def status_atributos(self):
        super().status_atributos(self.atributos)


class CriaPersonagemHdA(criaHdA, CriaPersonagem):

    def __init__(self, nome, nivel, progressao, atributos):
        super().__init__(nome, nivel, progressao)
        self.hp = self.dv * 10
        self.classe = 'Homem-de-Armas'
        self.atributos = atributos

    def status_classe(self):
        super().status_classe(self.hp, self.classe)

    def status_atributos(self):
        super().status_atributos(self.atributos)


class CriaPersonagemLadrao(criaLadrao, CriaPersonagem):

    def __init__(self, nome, nivel, progressao, atributos):
        super().__init__(nome, nivel, progressao)
        self.hp = self.dv * 6
        self.classe = 'Ladrão'
        self.atributos = atributos

    def status_classe(self):
        super().status_classe(self.hp, self.classe)

    def status_atributos(self):
        super().status_atributos(self.atributos)


class CriaPersonagemMago(criaMago, CriaPersonagem):

    def __init__(self, nome, nivel, progressao, atributos):
        super().__init__(nome, nivel, progressao)
        self.hp = self.dv * 4
        self.classe = 'Mago'
        self.atributos = atributos

    def status_classe(self):
        super().status_classe(self.hp, self.classe)

    def status_atributos(self):
        super().status_atributos(self.atributos)
