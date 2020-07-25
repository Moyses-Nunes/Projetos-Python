from random import randint
from time import sleep
from operator import itemgetter
t = 0
jogos = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print('JOGOS SORTEADOS')
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('Ranking:')
for i, m in enumerate(ranking):
    print(f'O {i+1}° colocado é {m[0]} com {m[1]}')
