# Tabuada

numero = int(input('Digite um número para saber sua tabuada: '))
incremento = 0


while incremento <= 10:
 resultado = numero * incremento
 print(f'{numero} x {incremento} = {resultado}')
 
 incremento = incremento + 1
