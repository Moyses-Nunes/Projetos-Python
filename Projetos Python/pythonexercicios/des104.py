def ficha(nome='O jogador <desconhecido>', gols=0):
    print(f'{nome} marcou {gols} gols.')


n = str(input('Nome do jogador: '))
g = str(input('Qntd de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
