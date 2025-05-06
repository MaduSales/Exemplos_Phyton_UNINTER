# Validando dados

x = int(input('Digite um número inteiro maior do que zero: '))

while (x <= 0):
  x = int(input('Tente de novo: '))

print(f'Você digitou {x}.')
