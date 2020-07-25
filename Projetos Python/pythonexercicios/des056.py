maior = 0
menor = 0
for c in range(1, 16):
    p = int(input(f'Digite o {c}° numero: '))
    if p == 1:
        p = maior = menor
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior numero é {maior}')
print(f'O menor é {menor}')
