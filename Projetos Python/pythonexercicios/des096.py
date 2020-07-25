dados = {}
gols = []
time = []
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dados['gols'] = gols
    dados['total'] = (sum(dados['gols']))
    dados['partidas'] = partidas
    print('=-'*30)
    time.append(dados.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continar? '))[0].upper()
    if op == 'N':
        break
for j in time:
    print(f'O jogador {j} tem o nome {[0]}')
    print(f'O jogador {[j][0]} jogou {[3]} partidas.')
    for i, p in enumerate(gols):
        print(f'    ==> Na partida {i}, fez {p} gols.')
        print(f'Foi um total de {dados["total"]} gols!')
