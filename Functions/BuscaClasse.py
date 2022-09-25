from Characters.HomemDeArmas import HomemDeArmas
from Characters.Clerigo import Clerigo
from Characters.Mago import Mago
from Characters.Ladrao import Ladrao


# A função cria_personagem é responsável por criar o personagem
# baseando-se da classe de personagem feita por parte do usuário
# ela recebe o valor da escolha do usuário, e instancia a class
# respectiva
def buscaClasse(classe_escolhida, nome, nivel):
    if classe_escolhida == 0:
        novo_personagem = Clerigo(nome, nivel)
    elif classe_escolhida == 1:
        novo_personagem = HomemDeArmas(nome, nivel)
    elif classe_escolhida == 2:
        novo_personagem = Mago(nome, nivel)
    else:
        novo_personagem = Ladrao(nome, nivel)
    return novo_personagem
