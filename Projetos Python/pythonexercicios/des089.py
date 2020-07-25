from time import sleep
from random import randint
lista = []
qtd = int(input('Quantos jogos deseja sortear? '))
for p in range(0, qtd):
    palpite = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60),
               randint(0, 60), randint(0, 60)]
    lista.append(palpite[:])
    palpite.clear()
print('Os palpites sorteados são:')
print('=-'*5, 'PALPITES', '=-'*5)
print('='*30)
for c in lista:
    print(f'{c}')
    print('='*30)
    sleep(1)
