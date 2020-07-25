def aumentar(n=0, p=0, f=True):
    r = n + ((p / 100) * n)
    return r if f is False else moeda(r)


def diminuir(n=0, p=0, f=True):
    r = n - ((p / 100) * n)
    return r if f is False else moeda(r)


def metade(n=0, f=True):
    r = n / 2
    return r if f is False else moeda(r)


def dobro(n=0, f=True):
    r = n * 2
    return r if f is False else moeda(r)


def moeda(p, m='R$'):
        return f'{m}{p:.2f}'.replace('.', ',')


def resumo(p=0, a=0, r=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p)}')
    print(f'Metade do preço: \t{metade(p)}')
    print(f'{a}% de aumento: \t{aumentar(p, a)}')
    print(f'{r}% de redução: \t{diminuir(p, r)}')
    print('-'*30)


