from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
da = ano + 18
print('Quem nasceu em {} tem {} anos em {}'.format(ano, date.today().year - ano, date.today().year))
if da > date.today().year:
    print('Ainda não chegou a hr do alistamento, falta(m) {} ano(s). \nO ano de alistamento será em {}'.format(da - date.today().year, da))
elif da < date.today().year:
    print('Já passou do tempo de alistamento, se passaram(ou) {} ano(s) do prazo. \nO alistamento foi em {}'.format(date.today().year - da, da))
else:
    print('Está na hr de se alistar!')
