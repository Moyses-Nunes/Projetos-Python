import random
n = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
    random.randint(1, 10), random.randint(1, 10))
print('Os números sorteados foram: ', end='')
for c in n:
    print(f'{c}', end=' ')
print(f'\nO maior número é {max(n)}')
print(f'O menor número é {min(n)}')






