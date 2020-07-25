n = int(input('Digite um número inteiro: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[m\nO número {} foi divisível {} vezes'.format(n, t))
if t == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele n é primo')
