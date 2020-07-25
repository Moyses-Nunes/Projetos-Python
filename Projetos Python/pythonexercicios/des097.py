def area(l, c):
    a = l * c
    print(f'A área do terreno é de {a:.1f}m².')


l = float(input('Informe a largura do terreno: '))
c = float(input('Informe o comprimento do terreno: '))
area(l, c)
