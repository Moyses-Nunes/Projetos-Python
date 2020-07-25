s = float(input('Digite o seu salário: R$'))
if s > 1250:
    print('Seu novo salário é R${:.2f}'.format(s * 1.1))
if s <= 1250:
    print('Seu novo salário é R${:.2f}'.format(s * 1.15))

