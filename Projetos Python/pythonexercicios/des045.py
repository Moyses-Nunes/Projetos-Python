from random import randint
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura' ]
print('''Vamos jogar JOKENPO!
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
pc = randint(0, 2)
jogador = int(input('Sua opção: '))
print('jO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('O PC escolheu {} e o JOGADOR {}'.format(lista[pc], lista[jogador]))
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('PC VENCE')
    else:
        print('OPÇÃO INVÁLIDA')
elif pc == 1:
    if jogador == 0:
        print('PC VENCE ')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA')
elif pc == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('PC VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')
else:
    print('OPÇÃO INVÁLIDA')
