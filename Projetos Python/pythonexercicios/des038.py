n = int(input('Digite um número inteiro: '))
b = int(input('Digite: \n[1] para binário \n[2] para octal \n[3] para hexadecimal \n Sua opção: '))
if b == 1:
    print('{} convertido para binário é {}'.format(n, bin(n)[2:]))
elif b == 2:
    print('{} convertido para octal é {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('{} em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida')



