pessoas = []
dado = []
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dado.append(nome)
    dado.append(peso)
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    op = ' '
    while op not in 'NS':
        op = str(input('Deseja continuar? ')).strip().upper()
    if op == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas são ', end='')
for p in pessoas:
    if p[1] == maior:
        print('[{}]'.format(p[0]))
print(f'As pessoas mais leves são ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]')
