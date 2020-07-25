n = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'O valor 9 aparece {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 está na {n.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares são ', end='')
for p in n:
    if p % 2 == 0:
        print(p, end=' ')
