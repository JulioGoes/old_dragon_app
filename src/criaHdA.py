# import random as rd


class criaHdA:

    def __init__(self, nome, lvl, tabela_HdA):
        self.name = nome
        self.classe = 'Homem-de-Armas'
        self.lvl = tabela_HdA[lvl - 1][0]
        self.xp = tabela_HdA[lvl - 1][1]
        self.dv = tabela_HdA[lvl - 1][2]
        self.ba = tabela_HdA[lvl - 1][3]
        self.ba_2 = tabela_HdA[lvl - 1][4]
        self.jp = tabela_HdA[lvl - 1][5]

    def status(self, lvl):
        print('Seu nível é {}'.format(lvl))
