v = float(input('Qual a vel. do carro? '))
m = (v - 80) * 7
if v > 80:
    print('Você excedeu o limite de velocidade de 80km/h, a multa é de R${:.2f}'.format(m))
else:
    print('Ok, continue abaixo do limite de velocidade')
