import pandas as pd
import sqlite3

# Criando a conexão com o banco de dados e criando o cursor
conn = sqlite3.connect('bancodedados/database.db')
con = conn.cursor()


# Criando a tabela do Homem-de-Armas no banco de dados
def create_table_HdA():
    # Transformando as informações de um csv em DataFrame
    df_HdA = pd.read_csv('arquivos/hda_progressao.csv')
    # Criando a tabela no banco de dados
    conn.execute('CREATE TABLE IF NOT EXISTS Homem_de_Armas ( \
                        Nível text, XP text, DV integer, BA_1 integer, \
                        BA_2 integer, JP integer)')
    # Adicionando os dados do DataFrame na tabela
    df_HdA.to_sql(name='Homem_de_Armas', con=conn,
                  if_exists='append', index=False)


# Criando a tabela do Ladrão no banco de dados
def create_table_Ladrao():
    # Transformando as informações de um csv em DataFrame
    df_Ladrao = pd.read_csv('arquivos/ladrao_progressao.csv')
    # Criando a tabela no banco de dados
    conn.execute('CREATE TABLE IF NOT EXISTS Ladrao ( \
                        Nível text, XP text, DV integer, \
                        BA integer, JP integer)')
    # Adicionando os dados do DataFrame na tabela
    df_Ladrao.to_sql(name='Ladrao', con=conn,
                     if_exists='append', index=False)


create_table_HdA()
create_table_Ladrao()

# back = pd.read_sql('select * from Homem_de_Armas', conn)
# print(back)
conn.commit()

conn.close()
