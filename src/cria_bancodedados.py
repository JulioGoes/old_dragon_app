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


def cria_tabela_magia(nome):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    df = pd.read_csv('arquivos/lv5_' + nome + '_espacos-de-magias.csv')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS ' + nome + ' (Nivel int, 1º int, 2º int, \
        3º int, 4º int, 5º int, 6º int, 7º int)'
    )
    df.to_sql(name=nome, con=conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


def cria_lista_classe(classe):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    con = conn.cursor()

    lista = []
    for row in con.execute('SELECT * FROM ' + classe + ' INNER \
                            JOIN magias_' + classe + ' ON ' +
                           classe + '.Nível = \
                            magias_' + classe + '.Nivel'):
        lista.append(row)
    return lista


classes = ['clerigo', 'hda', 'mago', 'ladrao']
classes_conjuradoras = ['clerigo', 'mago']

for classe_conjuradora in classes_conjuradoras:
    cria_tabela_classe(classe_conjuradora)

# for classe in classes:
#     cria_tabela_classe(classe)
