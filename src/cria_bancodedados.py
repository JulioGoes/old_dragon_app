import sqlite3
import pandas as pd

conn = sqlite3.connect('bancodedados/bancodedados.db')
con = conn.cursor()


def cria_tabela_classe(nome):

    df = pd.read_csv('arquivos/lv5_' + nome + '_progressao.csv')
    conn.execute('CREATE TABLE IF NOT EXISTS ' + nome + ' \
                (Nível text, XP int, DV int, BA int, JP int)')
    df.to_sql(name=nome, con=conn, if_exists='append', index=False)


cria_tabela_classe('clerigo')
cria_tabela_classe('hda')
cria_tabela_classe('mago')
cria_tabela_classe('ladrao')
