nome = ''

while not nome:  # encerra o laço quando nome não estiver vazio

  nome = input('Digite seu nome: ')
  valor = int(input('Agora digite um valor: '))

  if valor: #Isso é o mesmo que  -> if valor != 0
    print(f'{nome} digitou um número diferente de zero!')
  else:
    print(f'{nome} digitou zero.')
