from datetime import date
m = date.today().year - 18
tup = 0
tdown = 0
for c in range(1, 8):
    a = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    if m > a:
        tup += 1
    else:
        tdown += 1
print('{} Pessoas são de maior e {} são de menor'.format(tup, tdown))


