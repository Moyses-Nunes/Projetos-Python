op = 'S'
n = 0
s = 0
m = 0
c = 0
maior = 0
menor = 0
while op != 'S':
    n = int(input('Digite um número inteiro: '))
    op = str(input('Deseja parar? [S/N] ')).strip().upper() [0]
    c += 1
    s += n
    m = s / c
    if c == 1:
        maior = n = menor
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('A média entre os {} valores é {}, o MAIOR valor é {} e o MENOR é {}'.format(c, m, maior, menor))