from random import randint

def sort(lista):
    print('SORTEANDO OS VALORES DA LISTA: ', end='')
    for n in range(0, 5):
        v = randint(1, 10)
        lista.append(v)
    print(f'Os valores são {numeros}.')
    print('Pronto!')


def somapar(lista):
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(f'A soma dos valores pares entre {lista} é {s}.')


numeros = list()
sort(numeros)
somapar(numeros)
