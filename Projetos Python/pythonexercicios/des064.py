print('-=' * 5, 'FIBONACCI', '-=' * 5)
n = int(input('Quantos termos vc quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
while cont <= n:
    cont += 1
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' - FIM')
