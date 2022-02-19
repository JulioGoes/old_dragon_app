from functions import cria_personagem
import os

os.system('clear')
# Essa tupla armazena os nomes das classes de Old Dragon
# Ela será usada como parâmetro em diversas funcionalidades do programa
classes = ('clerigo', 'hda', 'mago', 'ladrao')

# Imprime a mensagem inicial, onde recebe do usuário
# o nome, nível e classe do personagem com o qual ele pretenda jogar
print('Seja bem-vindo a criação de fichas do Old Dragon RPG')
nome = input('Informe o nome do personagem: ')
nivel = int(input('Digite o nível do personagem: '))
print('Qual classe deseja jogar?')
classe_escolhida = int(input('Clerigo (0) | Homem-de-Armas (1)' +
                             '| Mago (2) | Ladrão (3) '))

os.system('clear')

# atributos = escolheAtributos()
os.system('clear')


# É chamado a função cria_personagem, criando finalmente nosso
# personagem de RPG
novo_personagem = cria_personagem(classe_escolhida, nome, nivel)
# Convoca o método status(), que imprime na tela as informações
# da ficha do personagem
novo_personagem.mostraStatus()
print('')
novo_personagem.mostraAfastar()
