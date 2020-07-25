print('Digite 6 números inteiros.')
s = 0
c = 0
for n in range(1, 7):
    a = int(input('Digite o {} número inteiro: '.format(n)))
    if a % 2 == 0:
        s += a
        c += 1
print('A soma  dos {} números pares é {}'.format(c, s))




