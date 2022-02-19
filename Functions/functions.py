from Clerigo import Clerigo


def escolheAtributos():
    atributos = ['Força', 'Destreza', 'Constituição',
                 'Inteligência', 'Sabedoria', 'Carisma']

    atributos_personagem = []

    for i in range(6):
        valor = int(input(f'Digite o valor de seu atributo {atributos[i]}: '))
        atributos_personagem.append(valor)

    return atributos_personagem


# A função cria_personagem é responsável por criar o personagem
# baseando-se da classe de personagem feita por parte do usuário
# ela recebe o valor da escolha do usuário, e instancia a class
# respectiva
def cria_personagem(classe_escolhida, nome, nivel):
    if classe_escolhida == 0:
        novo_personagem = Clerigo(nome, nivel)
    # elif classe_escolhida == 1:
    #     novo_personagem = CriaPersonagemHdA(nome, nivel,
    #                                         lista_de_classe, atributos)
    # elif classe_escolhida == 2:
    #     novo_personagem = CriaPersonagemMago(nome, nivel,
    #                                          lista_de_classe, atributos)
    # elif classe_escolhida == 3:
    #     novo_personagem = CriaPersonagemLadrao(nome, nivel,
    #                                            lista_de_classe, atributos)
    return novo_personagem
