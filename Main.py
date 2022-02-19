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
novo_personagem.mostraStatus()
novo_personagem.mostraEspacosDeMagia()
