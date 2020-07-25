def notas(*n, sit=False):
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    m = sum(n) / len(n)
    dados['media'] = m
    if sit:
        if 5 < m < 6:
            sit = 'Ruim'
        elif m <= 5:
            sit = 'Péssimo'
        elif 9 > m >= 6:
            sit = 'Regular'
        elif 10 == m or m >= 9:
            sit = 'Excelente'
        dados['situação'] = sit
    print(dados)


notas(8.5, 9, 10, 8.8, sit=True)
