n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
novo1 = 0
novo2 = 0
while op != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        s = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, s))
    elif op == 2:
        m = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
    elif op == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    elif op == 4:
        novo1 = int(input('Digite o primeiro novo número: '))
        novo2 = int(input('Digite o segundo novo número: '))
        n1 = novo1
        n2 = novo2
    elif op == 5:
        print('Obg, volte sempre')
    else:
        print('Opção inválida!')
    print('-=' * 10)
print('Acabou')
