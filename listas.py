# Listas
mochila = ['Machado', 'Camisa','Abacate']
print(mochila)

# São mutáveis
mochila[2] = 'Laranja'
print(mochila)

# Adicionar elementos:
mochila.append('Ovos')
print(mochila)

# Inserir elementos em índices específicos (desloca elementos para o próximo índice)
mochila.insert(3,'Canivete')
print(mochila)

# Remover por índice
del mochila[1]
print(mochila)

# Remover por valor
mochila.remove('Canivete')
print(mochila)
