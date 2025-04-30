# Operador Lógico - NOT
x = True
y = False
print(not x)
print(not y)


# Operador Lógico - AND
x = True
y = True
print(x and y)

# ==================
x = False
y = True
print(x and y)


# Operador Lógico - OR
x = False
y = True
print(x or y)


# Juntando todos:
x = 10
y = 1
z = 5
print(x > y or not z == y and y != y + z / x) # Aqui temos 2 blocos de operações lógicas. Deve ter 2 condições verdadeiras finais para o resultado ser verdadeiro.
