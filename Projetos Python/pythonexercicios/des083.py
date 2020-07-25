lista = list()
qtd = 0
while True:
    lista.append(int(input('Digite um número: ')))
    qtd += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if op == 'N':
            break
print(f'Foram digitados {qtd} valores')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está incluido na lista')
else:
    print('O valor 5 não se encontra na lista')
