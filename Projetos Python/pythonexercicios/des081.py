valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor add')
    else:
        print('Valor duplicado... não foi add')
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if op == 'N':
        break
print(sorted(valores))
