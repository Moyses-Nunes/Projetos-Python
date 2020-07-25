n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print('Parabéns, vc ficou acima da média, sua média é {}'.format(m))
else:
    print('Poxa que pena, vc perdeu, sua média é {}'.format(m))
