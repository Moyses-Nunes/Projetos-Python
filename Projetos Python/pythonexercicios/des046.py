for a in range(0, 6):
    print('Oi')
print('END')
for a in range(0, 3):
    print(a)
print('end')
for a in range(0, 7, -2):
    print(a)
print('end')
for a in range(0, 7, 2):
    print(a)
print('end')

n = int(input('Digite um número: '))
for a in range(0, n+1):
    print(a)
print('Fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for a in range(i, f+1, p):
    print(a)
print('Fim')

s = 0
for a in range(0, 4):
    n = int(input('Digite valores inteiros: '))
    s += n #s = s + n
print('O somatório é {}'.format(s))

