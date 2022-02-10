class criaClasse:

    def __init__(self, nome, nivel, progressao):
        self.nome = nome
        self.lvl = progressao[nivel - 1][0]
        self.xp = progressao[nivel - 1][1]
        self.dv = progressao[nivel - 1][2]
        self.ba = progressao[nivel - 1][3]
        self.jp = progressao[nivel - 1][4]

    def status(self):
        print('Nome: {} | Nível: {}'.format(self.nome.title(), self.lvl))
        print('XP: {} | DV: {} | BA: {} | JP: {}'.format(self.xp, self.dv,
                                                         self.ba, self.jp))


class criaClerigo(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Clerigo'
        self.hp = 8 * self.dv

    def status(self):
        print('Sua classe é', self.classe)
        print(f'Você tem {self.hp} PVs')
        return super().status()


class criaHdA(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Homem-de-Armas'
        self.hp = 10 * self.dv

    def status(self):
        print('Sua classe é', self.classe)
        print(f'Você tem {self.hp} PVs')
        return super().status()


class criaMago(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Mago'
        self.hp = 4 * self.dv

    def status(self):
        print('Sua classe é', self.classe)
        print(f'Você tem {self.hp} PVs')
        return super().status()


class criaLadrao(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Ladrão'
        self.hp = 6 * self.dv

    def status(self):
        print('Sua classe é', self.classe)
        print(f'Você tem {self.hp} PVs')
        return super().status()
