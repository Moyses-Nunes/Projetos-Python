c = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    c += 1
    if n < 0:
        print('Programa encerrado!')
        break
    else:
        for m in range(1, 11):
            print(f'{n} x {m} = {n * m}')

