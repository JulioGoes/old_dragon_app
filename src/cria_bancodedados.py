import sqlite3
import pandas as pd


# A função a seguir faz uma conexão com o banco de dados e
# em seguida, transforma um arquivo csv em um dataframe, após isso
# cria uma tabela genérica para a classe que foi usada como parâmetro
# passando também os dados do datafram para dentro da tabela
def cria_tabela_classe(nome):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    df = pd.read_csv('arquivos/lv5_' + nome + '_progressao.csv')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS ' + nome + ' (nivel int, XP int,\
         dado_de_vida int, base_de_ataque int, jogada_de_protecao int)'
    )
    df.to_sql(name=nome, con=conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


# Em um processo semelhante com a função anterior, a função a seguir
# faz uma conexão com o banco de dados, lê um arquivo csv e o transforma
# em datafram. Após isso, cria uma tabela para os espaços de magia das
# classes conjuradoras, e insere o dataframe nessa tabela.
def cria_tabela_magia(nome):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    df = pd.read_csv('arquivos/lv5_' + nome + '_espacos-de-magia.csv')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS ' + nome + '_magia (nivel int, primeiro_circulo int,\
         segundo_circulo int, terceiro_circulo int, quarto_circulo int,\
         quinto_circulo int, sexto_circulo int, setimo_circulo int)'
    )
    df.to_sql(name=nome + "_magia", con=conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


def cria_tabela_talentos_de_ladrao(nome):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    df = pd.read_csv('arquivos/lv5_' + nome + '_talentos-de-ladrao.csv')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS ' + nome + '_talentos (nivel int, arrombar text,\
         armadilhas text, escalar int, furtividade int,\
         punga int, percepcao text, ataque_furtivo int)'
    )
    df.to_sql(name=nome + "_talentos", con=conn,
              if_exists='replace', index=False)

    conn.commit()
    conn.close()


def cria_tabela_afastar_mortos_vivos(nome):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    df = pd.read_csv('arquivos/lv5_' + nome + '_afastar-mortos-vivos.csv')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS ' + nome + '_afastar_mortos_vivos (\
            nivel int,\
            dado_de_vida1 text,\
            dado_de_vida2 text,\
            dado_de_vida3 text,\
            dado_de_vida4 text,\
            dado_de_vida5 text,\
            dado_de_vida6 text,\
            dado_de_vida7 text,\
            dado_de_vida8 text,\
            dado_de_vida9 text,\
            dado_de_vida10 text,\
            dado_de_vida11 text,\
            dado_de_vida12 text,\
            dado_de_vida13 text,\
            dado_de_vida14 text,\
            dado_de_vida15 text,\
            dado_de_vida16 text,\
            dado_de_vida17 text,\
            dado_de_vida18 text\
        )'
    )
    df.to_sql(name=nome + "_afastar_mortos_vivos",
              con=conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


classes = ['clerigo', 'hda', 'ladrao', 'mago']
classes_conjuradoras = ['clerigo', 'mago']

for classe_conjuradora in classes_conjuradoras:
    cria_tabela_magia(classe_conjuradora)

for classe in classes:
    cria_tabela_classe(classe)

cria_tabela_afastar_mortos_vivos('clerigo')
cria_tabela_talentos_de_ladrao('ladrao')
