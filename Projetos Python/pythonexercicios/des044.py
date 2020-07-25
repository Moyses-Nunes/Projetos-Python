print(6 * '-=-', 'MOCA LOJA', 6 * '-=-')
valor = float(input('Digite o valor da compra: R$'))
fp = int(input('''FORMA DE PAGAMENTO:
[1] À vista (dinheiro ou cheque)
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão
Opção: '''))
if fp == 1:
    print('O valor total a ser pago é R${:.2f}'.format(valor - (valor * 0.1)))
elif fp == 2:
    print('O total a ser pago é R${:.2f}'.format(valor - (valor * 0.05)))
elif fp == 3:
    print('O valor total de R${:.2f} deverá ser pago em 2 parcelas de R${:.2f}'.format(valor, valor / 2))
elif fp == 4:
    qtd = int(input('Em quantas parcelas deseja pagar? '))
    parcela = valor * 1.2 / qtd
    print('O valor total será de R${:.2f}, pago em {} parcelas de R${:.2f} com juros, cada.'.format(valor * 1.2, qtd, parcela))
else:
    print('DIGITO INVÁLIDO')
