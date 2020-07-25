c = 0
s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma é {s}, foram digitados {c} valores')

