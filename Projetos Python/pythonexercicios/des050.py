print('-=' * 10, 'TABUADA', '-=' * 10)
a = int(input('Digite o número q vc quer ver a tabuada: '))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(a, n, a * n))

