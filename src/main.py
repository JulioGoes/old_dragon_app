from cria_classe import criaClerigo, criaHdA, criaMago, criaLadrao
from cria_bancodedados import cria_lista_classe
import os

os.system('clear')
# Essa lista armazena os nomes das classes de Old Dragon
# Ela será usada como parâmetro em diversas funcionalidades do programa
classes = ['clerigo', 'hda', 'mago', 'ladrao']

# Imprime a mensagem inicial, onde recebe do usuário
# o nome, nível e classe do personagem com o qual ele pretenda jogar
print('Seja bem-vindo a criação de fichas do Old Dragon RPG')
nome = input('Informe o nome do personagem: ')
nivel = int(input('Digite o nível do personagem: '))
print('Qual classe deseja jogar?')
classe_escolhida = int(input('Clerigo (0) | Homem-de-Armas (1)' +
                             '| Mago (2) | Ladrão (3) '))

os.system('clear')

# Após feita a escolha do personagem, a função cria_lista_classe
# retorna toda a progressão do personagem do nível 1 ao nível 5
lista_de_classe = cria_lista_classe(classes[classe_escolhida])


# A função cria_personagem é responsável por criar o personagem
# baseando-se da classe de personagem feita por parte do usuário
# ela recebe o valor da escolha do usuário, e instancia a class
# respectiva
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


# É chamado a função cria_personagem, criando finalmente nosso
# personagem de RPG
novo_personagem = cria_personagem(classe_escolhida, nome,
                                  nivel, lista_de_classe)

# Convoca o método status(), que imprime na tela as informações
# da ficha do personagem
novo_personagem.status()
