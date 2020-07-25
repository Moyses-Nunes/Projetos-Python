f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for a in range(len(j) - 1, -1, -1):
    i += j[a]
print('O inverso de {} é {}'.format(j, i))
if i == j:
    print('Temos um palíndromo')
else:
    print('N é um palíndromo')
