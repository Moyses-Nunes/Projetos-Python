def leiaDinheiro(msg=''):
    valido = False
    while not valido:
        p = str(input(msg)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[31mErro: Digite um preço válido!\033[m')
        else:
            valido = True
            return float(p)



