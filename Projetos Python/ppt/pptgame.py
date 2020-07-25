def cabeçalho(msg):
    tam = len(msg) + 4
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)


def player1(op1):
    if op1 == 'PEDRA':
        if op2 == 'TESOURA':
            return False


def player2(op2):
    if op2 == 'PEDRA':
        if op1 == 'TESOURA':
            return False


cabeçalho('PEDRA, PAPEL OU TESOURA')
op1 = cabeçalho(player1(str(input('Jogada Player 1: '))))
op2 = cabeçalho(player2(str(input('Jogada Player 2: '))))
