soma = 0
cont = 1

while cont <= 5:
  x = float(input(f'Digite a {cont}ª nota: '))
  soma += x
  cont += 1 

print(f'Total: {soma}')
