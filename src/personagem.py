from criaHdA import criaHdA
import os

nome = input('Digite o nome do seu personagem: ')
personagem = criaHdA(nome, '1')
# # print(personagem.classe)
# personagem.status()

# decisao = input('Você quer atacar? ')

# if decisao == 'sim':
#     acerto = personagem.ataque(personagem.acerto)
#     print(acerto)
#     input()
#     if (acerto > 15):
#         print('Você acertou!')
#     else:
#         print('Você errou!')

condicao = True

while condicao is True:
    print('Bem Vindo ao Jogo de RPG do Goes!')
    print('Nessa aventura, você será um Homem de Armas de nível 1!')
    entrada = int(input('Checar Status (1) | Atacar (2) | Sair (3): '))
    if entrada == 1:
        os.system('clear')
        personagem.status()
    elif entrada == 2:
        os.system('clear')
        personagem.ataque(personagem.acerto)
    else:
        print('Você encerrou o jogo!')
        condicao = False
