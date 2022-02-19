atributos = ['Força', 'Destreza', 'Constituição',
             'Inteligência', 'Sabedoria', 'Carisma']

atributos_personagem = []

for i in range(6):
    valor = int(input(f'Digite o valor de seu atributo {atributos[i]}: '))
    atributos_personagem.append(valor)

print(atributos_personagem)
