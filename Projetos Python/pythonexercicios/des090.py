from time import sleep
lista = []
dados = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    dados.append(nome)
    dados.append(n1)
    dados.append(n2)
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if op == 'N':
        break
print('=-'*20)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('='*30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
print('=-'*20)
while True:
    r = int(input('De qual aluno deseja ver o detalhamento? (999 interrompe) '))
    if r == 999:
        print('Finalizando...')
        sleep(1)
        break
    if r <= len(lista) - 1:
        print(f'As notas do aluno {lista[r][0]} foram {lista[r][1]} e {lista[r][2]}')
print('<<<VOLTE SEMPRE>>>')


