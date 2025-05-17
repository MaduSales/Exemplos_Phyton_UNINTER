# Dicionários de Listas
games = {'nome':['Super Mario', 'Zelda Ocarina of Time','Pokemon Yellow'],

         'videogame':['Super Nintendo','Nintendo 64','Game Boy'],

         'ano':[1990,19998,1999]}

print(games)
----------------------------------------------------------------
----------------------------------------------------------------
# Populando dicionário de listas
games = {'nome':[],'desenvolvedor':[],'ano':[]}

for i in range(3):
  nome = input('Qual o nome do jogo? ')
  desenvolvedor = input('Qual o nome do desenvolvedor? ')
  ano = input('Qual o ano de lançamento do jogo? ')

  games['nome'].append(nome)
  games['desenvolvedor'].append(desenvolvedor)
  games['ano'].append(ano)

print(games)
