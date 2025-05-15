# O asterisco indica que a função pode receber um número variável de argumentos, que serão empacotados em uma tupla
def soma(*num):
  acumulador = 0
  for i in num:
    acumulador += i
  return acumulador

soma(1,2,6,10)
