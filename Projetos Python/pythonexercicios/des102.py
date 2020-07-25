def voto(ano):
    idade = 2020 - ano
    if idade > 60:
        resp = print(f'Com {idade} anos o voto é OPICIONAL.')
    if 18 > idade >= 16:
        resp = print(f'Com {idade} anos o voto é OPICIONAL.')
    if 60 > idade >= 18:
        resp = print(f'Com {idade} anos o voto é OBRIGATÓRIO.')
    if idade < 16:
        resp = print(f'Com {idade} anos NÃO VOTA.')
    return resp


ano = int(input('Ano de nascimento: '))
voto(ano)

