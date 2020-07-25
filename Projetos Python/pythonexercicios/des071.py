tot = mais1 = mp = c = 0
barato = ''
while True:
    n = str(input('Digite o nome do produto: '))
    p = float(input('Digite o preço do produto: R$'))
    tot += p
    c += 1
    if p > 1000:
        mais1 += 1
    if c == 1 or p < mp:
        mp = p
        barato = n
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
print(f'O total gasto foi de R${tot:.2f}')
print(f'{mais1} produto(s) custam mais de R$1,000.00')
print(f'O produto mais barato é {barato}')
