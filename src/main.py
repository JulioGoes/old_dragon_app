from cria_classe import criaClerigo, criaHdA, criaMago, criaLadrao
from cria_bancodedados import cria_lista_classe

classes = ['clerigo', 'hda', 'mago', 'ladrao']

print('Seja bem-vindo a criação de fichas do Old Dragon RPG')
nome = input('Informe o nome do personagem: ')
nivel = int(input('Digite o nível do personagem: '))
print('Qual classe deseja jogar?')
classe_escolhida = int(input('Clerigo (0) | Homem-de-Armas (1)' +
                             '| Mago (2) | Ladrão (3) '))

lista_de_classe = cria_lista_classe(classes[classe_escolhida])


def cria_personagem(classe_escolhida, nome, nivel, lista_de_classe):
    if classe_escolhida == 0:
        novo_personagem = criaClerigo(nome, nivel, lista_de_classe)
    elif classe_escolhida == 1:
        novo_personagem = criaHdA(nome, nivel, lista_de_classe)
    elif classe_escolhida == 2:
        novo_personagem = criaMago(nome, nivel, lista_de_classe)
    elif classe_escolhida == 3:
        novo_personagem = criaLadrao(nome, nivel, lista_de_classe)
    return novo_personagem


novo_personagem = cria_personagem(classe_escolhida, nome,
                                  nivel, lista_de_classe)
novo_personagem.status()
