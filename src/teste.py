import sqlite3
from criaHdA import criaHdA
import random as rd

conn = sqlite3.connect('bancodedados/database.db')
cur = conn.cursor()
tabela_HdA = []
tabela_Ladrao = []
for row in cur.execute('SELECT * FROM Homem_de_Armas'):
    tabela_HdA.append(row)

for row in cur.execute('SELECT * FROM Ladrao'):
    tabela_Ladrao.append(row)
# print(tabela_HdA)
# print('***********')
# print(tabela_Ladrao)
conn.close()

nome = input('Qual o nome do seu personagem? ')
nivel = int(input('Qual o nível do seu personagem? '))
print('***')
personagem = criaHdA(nome, nivel, tabela_HdA)
personagem.status(personagem.lvl)
dado = rd.randrange(1, 21)
ataque = personagem.ba + dado
print('Seu BA é +{}'.format(personagem.ba))
print('Você rolou um {} no dado!'.format(ataque))
