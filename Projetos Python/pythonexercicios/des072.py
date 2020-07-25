print('=' * 20)
print('{:^20}'.format('CAICA ELETRÔNICO'))
print('=' * 20)
valor = int(input('Digite o valor que deseja sacar: R$'))
totced = 0
tot = valor
ced = 50
while True:
   if tot >= ced:
       tot -= ced
       totced += 1
   else:
       if totced > 0:
           print(f'{totced} nota de {ced} reais')
       if ced == 50:
           ced = 20
       elif ced == 20:
           ced = 10
       elif ced == 10:
           ced = 1
       totced = 0
       if tot == 0:
           break

