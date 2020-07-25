from random import randint
c = 0
while True:
    op = str(input('PAR ou ÍMPAR? ')).strip().upper()[0]
    n = int(input('Qual o número? '))
    npc = randint(1, 10)
    s = n + npc
    if op == 'P':
        if s % 2 == 0:
            print(f'Vc ganhou!! Deu par, o pc jogou \033[31m{npc}\033[m e vc \033[31m{n}\033[m')
        else:
            print(f'Vc perdeu!! Deu ímpar, o pc jogou \033[31m{npc}\033[m e vc \033[31m{n}\033[m')
            break
    elif op == 'I':
        if s % 2 != 0:
            print(f'Vc ganhou!! Deu ímpar, o pc jogou \033[31m{npc}\033[m e vc \033[31m{n}\033[m')
        else:
            print(f'Vc perdeu!! Deu par, o pc jogou \033[31m{npc}\033[m e vc \033[31m{n}\033[m')
            break
    c += 1
print(f'Vc ganhou por {c} vezes consecutivas!')
