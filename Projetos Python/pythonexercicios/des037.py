vc = float(input('Qual é o valor da casa que deseja comprar? R$'))
s = float(input('Quanto é o seu salário? R$'))
qa = int(input('Em quantos anos vc vai pagar? '))
p = vc / (12 * qa)
if p > s * 0.3:
    print('O empréstimo não pode ser concedido, as parcelas em {} anos seriam de R${:.2f}'.format(qa, p))
else:
    print('Parabéns, empréstimo concedido, as parcelas serão de R${:.2f} em {} anos'.format(p, qa))
