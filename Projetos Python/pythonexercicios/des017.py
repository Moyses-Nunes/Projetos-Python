import random
a1 = input('Digite o primeiro aluno: ')
a2 = input('Digite o segundo aluno: ')
a3 = input('Digite o terceiro aluno: ')
a4 = input('Digite o quarto aluno: ')
alunos = (a1, a2, a3, a4)
esc = random.choice(alunos)
print('O aluno escolhido foi {}'.format(esc))
