from Functions.BuscaClasse import buscaClasse
import os

os.system('clear')

classe = ('classe', 'hda', 'mago', 'ladrao')
print('Seja bem-vindo a criação de fichas do Old Dragon RPG')
nome = input('Informe o nome do personagem: ')
nivel = int(input('Digite o nível do personagem: '))
print('Qual classe deseja jogar?')
classe_escolhida = int(input('Clerigo (0) | Homem-de-Armas (1)' +
                             '| Mago (2) | Ladrão (3) '))

os.system('clear')

novo_personagem = buscaClasse(classe_escolhida, nome, nivel)
os.system('clear')


def escolheAtributos():
    atributos = ['Força', 'Destreza', 'Constituição',
                 'Inteligência', 'Sabedoria', 'Carisma']

    atributos_personagem = []

    for i in range(6):
        valor = int(input(f'Digite o valor de seu atributo {atributos[i]}: '))
        atributos_personagem.append(valor)

    return atributos_personagem


novo_personagem.defineAtributo(escolheAtributos())
os.system('clear')


novo_personagem.mostraStatus()
