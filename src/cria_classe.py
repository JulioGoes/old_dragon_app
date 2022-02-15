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
        self.c1 = progressao[nivel - 1][6]
        self.c2 = progressao[nivel - 1][7]
        self.c3 = progressao[nivel - 1][8]
        self.afm1 = progressao[nivel - 1][14]
        self.afm2 = progressao[nivel - 1][15]
        self.afm3 = progressao[nivel - 1][16]
        self.afm4 = progressao[nivel - 1][17]
        self.afm5 = progressao[nivel - 1][18]

    def status(self):
        super().status(self.hp, self.classe)
        print('\n****ESPAÇOS DE MAGIA****')
        print(f'1º: {self.c1} | 2º: {self.c2} | 3º: {self.c3}')
        print('\n**AFASTAR MORTOS-VIVOS**')
        print(f'1 DV: {self.afm1} | 2 DV: {self.afm2} | 3 DV: {self.afm3}')
        print(f'4 DV: {self.afm4} | 5 DV: {self.afm5}')


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
        self.c1 = progressao[nivel - 1][6]
        self.c2 = progressao[nivel - 1][7]
        self.c3 = progressao[nivel - 1][8]

    def status(self):
        super().status(self.hp, self.classe)
        print('\n****ESPAÇOS DE MAGIA****')
        print(f'1º: {self.c1} | 2º: {self.c2} | 3º: {self.c3}')


class criaLadrao(criaClasse):

    def __init__(self, nome, nivel, progressao):
        super().__init__(nome, nivel, progressao)
        self.classe = 'Ladrão'
        self.hp = 6 * self.dv
        self.arrombar = progressao[nivel - 1][6]
        self.armadilhas = progressao[nivel - 1][7]
        self.escalar = progressao[nivel - 1][8]
        self.furtividade = progressao[nivel - 1][9]
        self.punga = progressao[nivel - 1][10]
        self.percepcao = progressao[nivel - 1][11]
        self.ataque_furtivo = progressao[nivel - 1][12]
        print(progressao)

    def status(self):
        super().status(self.hp, self.classe)
        print('\n')
        print('**TALENTOS DE LADRÃO**')
        print(f'Arrombar: {self.arrombar} | Armadilhas: {self.armadilhas}')
        print(f'Escalar: {self.escalar}% | Furtividade: {self.furtividade}%')
        print(f'Punga: {self.punga}% | Percepção: {self.percepcao} no 1d6')
        print(f'Ataque Furtivo: {self.ataque_furtivo}X')
