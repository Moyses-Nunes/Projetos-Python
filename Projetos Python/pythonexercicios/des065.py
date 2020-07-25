n = 0
s = 0
cont = 0
while n != 999:
    n = int(input('Digite um número (digite 999 para acabar): '))
    if n != 999:
        s += n
        cont += 1
print('Foram digitados {} números e a soma entre eles é {}'.format(cont, s))
