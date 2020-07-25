c = 0
dados = {}
dados['nome'] = str(input('Nome do aluno: '))
dados['nota'] = float(input('Nota: '))
print('='*30)
if dados['nota'] >= 6:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'
for k, v in dados.items():
    c += 1
    if c == 1:
        print(f'O {k} do aluno é {v}')
    if c == 2:
        print(f'A {k} é {v}')
    if c == 3:
        print(f'A {k} do aluno é {v}')

