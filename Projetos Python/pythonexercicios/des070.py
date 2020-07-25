maior = 0
qh = 0
qm = 0
while True:
    id = int(input('Digite a idade: '))
    sex = ' '
    while sex not in 'FM':
        sex = str(input('Digite o sexo: ')).strip().upper()[0]
    if id > 18:
        maior += 1
    if sex == 'M':
        qh += 1
    if sex == 'F' and id < 20:
        qm += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Há {maior} pessoa(s) com mais de 18 anos.')
print(f'Há {qh} homem(s) cadastrados.')
print(f'Há {qm} mulher(es) com menos de 20 anos')
