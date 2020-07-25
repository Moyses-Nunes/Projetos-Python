nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é {} \nSeu último nome é {}'.format(n[0], n[len(n)-1]))


