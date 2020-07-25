def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO: O usuário interrompeu o programa.\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um valor: ')
print(f'Você digitou o número {num}')




