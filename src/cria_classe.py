# A classe 'criaClasse' é responsável por setar todos os atributos
# e metódos que estão presentes em todas as outras classes
class criaClasse:

    # O método construtor define o Lvl, XP, Dado de Vida, Base de Acerto
    # e Jogada de Proteção
    def __init__(self, nome, nivel, progressao):
        self.nome = nome
        self.lvl = progressao[nivel - 1][0]
        self.xp = progressao[nivel - 1][1]
        self.dv = progressao[nivel - 1][2]
        self.ba = progressao[nivel - 1][3]
        self.jp = progressao[nivel - 1][4]

    # O método status imprime na tela as informações do personagem
    def status(self, hp, classe):
        print('Nome: {} | Nível: {}'.format(self.nome.title(), self.lvl))
        print(f'PVs: {hp}/{hp} | Classe: {classe}')
        print('XP: {} | DV: {} | BA: {} | JP: {}'.format(self.xp, self.dv,
                                                         self.ba, self.jp))


# As classes a seguir são filhas de 'criaClasse, elas definem alguns
# atributos e métodos especificos de cada classe de personagem
# exemplo: valor do Dado de Vida, imprimir na tela qual a classe do personagem

class criaClerigo(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Clerigo'
        self.hp = 8 * self.dv

    def status(self):
        super().status(self.hp, self.classe)


class criaHdA(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Homem-de-Armas'
        self.hp = 10 * self.dv

    def status(self):
        super().status(self.hp, self.classe)


class criaMago(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Mago'
        self.hp = 4 * self.dv

    def status(self):
        super().status(self.hp, self.classe)


class criaLadrao(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Ladrão'
        self.hp = 6 * self.dv

    def status(self):
        super().status(self.hp, self.classe)
