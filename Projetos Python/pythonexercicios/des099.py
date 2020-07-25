from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='')
            sleep(0.25)
            c += p
        print('Fim!')
        print('=-' * 30)
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='')
            sleep(0.25)
            c -= p
        print('Fim!')
        print('=-'*30)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez de brincar de contar!!')

inicio = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passo: '))


print('=-'*30)
contador(inicio, final, passo)
