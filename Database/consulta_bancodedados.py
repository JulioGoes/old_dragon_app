import sqlite3


def buscaClerigo():
    connection = sqlite3.connect('Database/bancodedados.db')
    cursor = connection.cursor()

    clerigo, clerigo_afastar, clerigo_magias = [], [], []
    for row in cursor.execute('SELECT * FROM clerigo'):
        clerigo.append(row)

    for row in cursor.execute('SELECT * FROM clerigo_afastar_mortos_vivos'):
        clerigo_afastar.append(row)

    for row in cursor.execute('SELECT primeiro_circulo,\
                               segundo_circulo, terceiro_circulo\
                               FROM clerigo_magia'):
        clerigo_magias.append(row)

    return tuple(clerigo), tuple(clerigo_afastar), tuple(clerigo_magias)


def buscaHdA():
    connection = sqlite3.connect('Database/bancodedados.db')
    cursor = connection.cursor()
    hda = []
    for row in cursor.execute('SELECT * FROM hda'):
        hda.append(row)
    return tuple(hda)


def buscaLadrao():
    connection = sqlite3.connect('Database/bancodedados.db')
    cursor = connection.cursor()
    ladrao, ladrao_talentos = [], []
    for row in cursor.execute('SELECT * FROM ladrao'):
        ladrao.append(row)
    for row in cursor.execute('SELECT * FROM ladrao_talentos'):
        ladrao_talentos.append(row)
    return tuple(ladrao), tuple(ladrao_talentos)


def buscaMago():
    connection = sqlite3.connect('Database/bancodedados.db')
    cursor = connection.cursor()
    mago, mago_magias = [], []
    for row in cursor.execute('SELECT * FROM mago'):
        mago.append(row)
    for row in cursor.execute('SELECT primeiro_circulo,\
                               segundo_circulo, terceiro_circulo\
                               FROM mago_magia'):
        mago_magias.append(row)
    return tuple(mago), tuple(mago_magias)


def buscaRacas():
    connection = sqlite3.connect('Database/bancodedados.db')
    cursor = connection.cursor()
    racas = []
    for row in cursor.execute('SELECT * FROM racas'):
        racas.append(row)
    return tuple(racas)
