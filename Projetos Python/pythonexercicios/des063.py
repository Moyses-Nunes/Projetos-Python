print('-=' * 5, 'CÁLCULO DE UMA PA', '-=' * 5)
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
pa = p
mais = 10
tot = 0
while mais != 0:
    tot += mais
    while cont <= tot:
        print(pa, end='')
        cont += 1
        pa += r
        print(' -> ', end='')
    print('Pausa')
    mais = int(input('Quantos termos deseja acrescentar? '))
print('PA finalizada com {} termos'.format(tot))
