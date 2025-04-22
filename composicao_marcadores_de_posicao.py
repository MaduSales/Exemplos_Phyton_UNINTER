nota = 8
s1 = 'Sua nota foi %i na disciplina de Algoritmos' % nota
print(s1)


# Exemplo com delimitador de casas decimais
nota = 8.5
s1 = 'Sua nota foi %.1f na disciplina de Algoritmos' % nota
print(s1)


# Exemplo com duas variáveis: 
nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Sua nota foi %d na disciplina de %s' % (nota, disciplina)
print(s1)


# Exemplo composição moderna
nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou {} na disciplina de {}' .format(nota,disciplina)
print(s1)



# Exemplo composição F-String
nota = 8.5
disciplina = 'Algoritmos'
s1 = f 'Você tirou {nota} na disciplina de {disciplina}'
print(s1)
