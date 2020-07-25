matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = tc = sl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l+1}] [{c+1}]: '))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        tc = matriz[0][2] + matriz[1][2] + matriz[2][2]
        sl = matriz[1][0] + matriz[1][1] + matriz[1][2]
    print()
print('=-'*30)
print(f'A soma dos elementos pares é {sp}')
print(f'A soma dos elementos da terceira coluna é {tc}')
print(f'A soma dos elementos da segunda linha é {sl}')
