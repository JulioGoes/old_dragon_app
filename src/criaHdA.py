import random as rd


class criaHdA:

    def __init__(self, nome, lvl):
        self.name = nome
        self.classe = 'Homem-de-Armas'
        self.lvl = lvl
        self.pontos_de_vida = 10
        self.acerto = 1

    def status(self):
        print('*******************************')
        print('{} é um {} de lvl {}'.format(self.name, self.classe, self.lvl))
        print('Sua arma é um Machado')
        print('*******************************')

    def ataque(self, ba):
        print('*******************************')
        print('Machado de Batalha | 1d10 | +4 BA')
        acerto = rd.randrange(1, 21) + ba
        print('Você rolou um {} no dado!'.format(acerto))
        print('*******************************')
        return acerto
