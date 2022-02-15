import sqlite3


# A função a seguir coleta as informações respectiva de cada classe
# e retorna uma super lista com os valores
def cria_lista_classe(classe):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    con = conn.cursor()

    lista = []

    if classe == 'mago':
        for row in con.execute('SELECT * FROM ' + classe + ' INNER \
                                JOIN ' + classe + '_magia ON ' +
                               classe + '.nivel = \
                                ' + classe + '_magia.nivel'):
            lista.append(row)

    elif classe == 'clerigo':
        for row in con.execute('SELECT * FROM ' + classe + ' INNER \
            JOIN ' + classe + '_magia ON ' + classe + '.nivel = \
             ' + classe + '_magia.nivel INNER \
            JOIN ' + classe + '_afastar_mortos_vivos ON \
             ' + classe + '.nivel= ' + classe + '_afastar_mortos_vivos.nivel'):
            lista.append(row)

    elif classe == 'ladrao':
        for row in con.execute('SELECT * FROM ladrao INNER JOIN\
             ladrao_talentos ON ladrao.nivel = ladrao_talentos.nivel'):
            lista.append(row)

    else:
        for row in con.execute('SELECT * FROM ' + classe + ''):
            lista.append(row)
    return lista
