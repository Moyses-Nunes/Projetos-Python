lista = []
dados = {}
s = m = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    s += dados['idade']
    lista.append(dados.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? ')).strip().upper()[0]
    if op == 'N':
        break
print('=-'*20)
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
m = s / len(lista)
print(f'A média das idades é de {m:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média de idade: ',end='')
for c in lista:
    if c['idade'] > m:
        for k, v in c:
            print(f'{k} = {v}')
