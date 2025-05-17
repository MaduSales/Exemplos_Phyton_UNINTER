# Dicionários
game = {'nome':'Super Mario', 'desenvolvedora':'Nintendo', 'ano':1990}
# Métodos
print(game.keys())
print(game.values())
print(game.items())

# Varredura
for keys,values in game.items():
  print('{}:{}'.format(keys, values))
