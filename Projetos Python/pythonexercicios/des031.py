d = float(input('Qual a distância da viagem em km? '))
if d > 200:
    print('A passagem custa R${}'.format(d * 0.45))
else:
    print('A passagem custa R${}'.format(d * 0.5))
