import sqlite3
from criaHdA import criaHdA
# import random as rd
import os

conn = sqlite3.connect('bancodedados/database.db')
cur = conn.cursor()
tabela_HdA = []
tabela_Ladrao = []
for row in cur.execute('SELECT * FROM Homem_de_Armas'):
    tabela_HdA.append(row)

for row in cur.execute('SELECT * FROM Ladrao'):
    tabela_Ladrao.append(row)

conn.close()

os.system('clear')

nome = input('Qual o nome do seu personagem? ')
nivel = int(input('Qual o nível do seu personagem? '))
print('***')
personagem = criaHdA(nome, nivel, tabela_HdA)
personagem.status()
