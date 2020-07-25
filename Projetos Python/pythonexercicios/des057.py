velho = ''
soma = 0
midade = 0
media = 0
totmul = 0
for n in range(1, 5):
    print('-=' * 10, '{}° PESSOA'.format(n), '-=' * 10)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M]/[F]: ')).strip()
    soma += idade
    media = soma / 4
    if n == 1 and sexo in'Mm':
        midade = idade
        velho = nome
    if sexo in 'Mm' and idade > midade:
        midade = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        totmul += 1
print('A \033[31mmédia \033[mde \033[31midade \033[mdo grupo é de \033[31m{} anos\033[m'.format(media))
print('O homem mais velho tem \033[31m{} \033[manos e se chama \033[31m{}'.format(midade, velho))
print('\033[mO total de mulheres com \033[31mmenos \033[mde \033[31m20 \033[manos é {}'.format(totmul))
