from random import randint
print('Vou pensar em um número de 0 à 10, tente advinhar..')
np = int(input('Qual número eu pensei? '))
nc = randint(0, 10)
tot = 0
while nc != np:
    if np > nc:
        print('ERROU! menos..')
        np = int(input('Outro número: '))
    if np < nc:
        print('ERROU! mais..')
        np = int(input('Outro número: '))
    tot += 1
print('Acertou mizeravi!!! Depois de {} tentativas'.format(tot + 1))
