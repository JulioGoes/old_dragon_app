import sqlite3


# A função a seguir coleta
def cria_lista_classe(classe):

    conn = sqlite3.connect('bancodedados/bancodedados.db')
    con = conn.cursor()

    lista = []
    if classe == 'mago' or classe == 'clerigo':
        for row in con.execute('SELECT * FROM ' + classe + ' INNER \
                                JOIN ' + classe + '_magia ON ' +
                               classe + '.nivel = \
                                ' + classe + '_magia.nivel'):
            lista.append(row)
    else:
        for row in con.execute('SELECT * FROM ' + classe + ''):
            lista.append(row)
    return lista
