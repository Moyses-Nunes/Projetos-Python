from datetime import date
ano = int(input('Digite em que ano vc nasceu: '))
idade = date.today().year - ano
if idade <= 9:
    print('Idade: {} \nCategoria : mirim'.format(idade))
elif 14 >= idade > 9:
    print('Idade: {} \nCategoria: Infantil'.format(idade))
elif 19 >= idade > 14:
    print('Idade: {} \nCategoria: Junior'.format(idade))
elif 25 >= idade > 19:
    print('Idade: {} \nCategoria: Sênior'.format(idade))
else:
    print('Idade: {} \nCategoria: Master'.format(idade))
