frase = str(input('Digite uma frase: ')).strip()
print('A frase possui {} letras a'.format((frase.upper()).count('A')))
print('A primeira posção da letra é {}'.format((frase.upper()).find('A') + 1) - frase.count(' '))
print('A útima posição em que a letra a aparece é {}'.format((frase.upper()).rfind('A') - frase.count(' ')))

