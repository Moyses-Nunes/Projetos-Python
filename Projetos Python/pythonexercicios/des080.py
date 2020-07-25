valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'O maior valor é {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print(f'\nO menor valor é {min(valores)} na posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
