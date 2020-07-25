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


