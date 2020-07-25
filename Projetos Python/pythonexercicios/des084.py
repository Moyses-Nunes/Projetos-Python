lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if op == 'N':
            break
print(f'Os números são: {lista}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
