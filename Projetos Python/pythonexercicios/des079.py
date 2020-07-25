num = [2, 5, 9, 8, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(3)
if 8 in num:
    num.remove(8)
else:
    print('Não achei o número 8')
print(num)
print(f'Essa lista tem {len(num)} elementos')
print('=-' * 20)
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('=-' * 20)
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
