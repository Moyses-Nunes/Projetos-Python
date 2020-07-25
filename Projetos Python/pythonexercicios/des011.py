d = float(input('Quantos km percorridos?'))
qd = int(input('Quantos dias foi alugado?'))
pqd = qd * 60
pd = d * 0.15
print('O total a pagar é de R${:.2f}'.format(pqd + pd))
