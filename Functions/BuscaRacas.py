from Database.consulta_bancodedados import buscaRacas


def mostraRacas(raca):
    racas = buscaRacas()
    humano = racas[0]

    if raca == 'humano':
        print(f'Raça: {humano[0].title()}')
        print(f'Alinhamento: {humano[1]}')
        print(f'Características Fisicas: {humano[2]}')
        print(f'Idade: {humano[3]}')
        print(f'Atributos: {humano[4]}')
        print(f'Movimento: {humano[5]}')
