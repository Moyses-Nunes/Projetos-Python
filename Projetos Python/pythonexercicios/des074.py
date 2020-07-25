ns = ('zero', 'um', 'dois', 'tres', 'quatro',
          'cinco', 'seis', 'sete', 'oito',
          'nove', 'dez', 'onze', 'doze',
          'treze', 'quartoze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Vc digitou o número {ns[n]}')
        op = ' '
        while op not in 'NS':
            op = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if op == 'N':
            break
    else:
        print('Tente novamente. ', end='')

