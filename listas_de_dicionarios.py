# Listas de dicionários
games = []
game1 = {'nome':'Super Mario',

         'videogame':'Super Nintendo',

         'ano':1990}

game2 = {'nome':'Zelda Ocarina of Time',

         'videogame':'Nintendo 64',

         'ano':1998}

game3 = {'nome':'Pokemon Yellow',

         'videogame':'Game Boy',

         'ano':1999}

games = [game1, game2, game3]

print(games)
----------------------------------------------------------------
----------------------------------------------------------------
# Populando listas de dicionários
games = []
game = {}

for i in range(3):
  game['nome'] = input('Qual o nome do jogo? ')
  game['desenvolvedor'] = input('Qual o nome do desenvolvedor? ')
  game['ano'] = input('Qual o ano de lançamento do jogo? ')

  games.append(game.copy())
print('-' * 20)

for jogos in games:
  for chave, valor in jogos.items():
    print('A chave {} tem o valor {}'.format(chave, valor))
