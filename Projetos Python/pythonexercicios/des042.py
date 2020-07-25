l1 = float(input('Digite o primeiro lado do triangulo: '))
l2 = float(input('Digite o segundo lado do triangulo: '))
l3 = float(input('Digite o terceiro lado do triangulo: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('É possível formar um triangulo! ', end = '')
    if l1 == l2 == l3:
        print('O triangulo é equilátero.')
    if l1 == l2 or l2 == l3 or l1 == l3:
        print('O triangulo é isósceles.')
    if l1 != l2 != l3:
        print('O triangulo é escaleno.')
else:
    print('Não é possível formar um triangulo.')
