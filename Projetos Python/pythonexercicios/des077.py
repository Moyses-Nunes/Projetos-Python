lista = ('Lápis', 1.75,
         'Borrcha', 2,
         'caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99)
print('=' * 40)
print('{:^30}'.format('LOJA DO MOCA'))
print('=' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>6.2f}')
