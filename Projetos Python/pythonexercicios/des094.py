dados = {}
gols = []
time = []
while True:
    gols.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dados['gols'] = gols
    dados['total'] = (sum(dados['gols']))
    print('=-'*30)
    print(dados)
    print('=-'*30)
    dados['partidas'] = partidas
    time.append(dados.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? ')).strip().upper()[0]
    if op == 'N':
        break
for j, d in enumerate(time):
    for k, v in d.values():
        print(f'O campo {k} tem o valor {v}')
        print('=-'*30)
        print(f'O jogador {k} jogou {v[3]} partidas.')
    for i, p in enumerate(gols):
        print(f'    ==> Na partida {i}, fez {p} gols.')
        print(f'Foi um total de {p[2]} gols!')
