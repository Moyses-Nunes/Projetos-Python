from math import sqrt
co = float(input('Digite o cateto o posto:'))
ca = float(input('Digite o cateto adjacente:'))
h = sqrt(co ** 2 + ca ** 2)
print('A hipotenusa é {:.2f}'.format(h))

