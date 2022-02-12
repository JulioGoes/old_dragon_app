import sqlite3
import pandas as pd


def cria_tabela_classe(nome):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    df = pd.read_csv('arquivos/lv5_' + nome + '_progressao.csv')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS ' + nome + ' (Nível text, XP int, \
        DV int, BA int, JP int)'
    )
    df.to_sql(name=nome, con=conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


def cria_lista_classe(classe):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    con = conn.cursor()

    lista = []
    for row in con.execute('SELECT * FROM ' + classe + ' '):
        lista.append(row)
    return lista


classes = ['clerigo', 'hda', 'mago', 'ladrao']

for classe in classes:
    cria_tabela_classe(classe)
