def aumentar(n=0, p=0):
    r = n + ((p / 100) * n)
    return r


def diminuir(n=0, p=0):
    r = n - ((p / 100) * n)
    return r


def metade(n=0):
    r = n / 2
    return r


def dobro(n=0):
    r = n * 2
    return r

def moeda(p, m='R$'):
    return f'{m}{p:.2f}'.replace('.', ',')


