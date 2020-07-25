dados = dict()
dados['nome'] = str(input('Nome: '))
dados['nasc'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 ñ têm): '))
if dados['ctps'] == 0:
    while dados['ctps'] == 0:
        print('Não tem CTPS')
        break
dados['contratacao'] = int(input('Ano de contratação: '))
dados['salario'] = float(input('Salário: R$'))
dados['idade'] = 2020 - dados['nasc']
dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - 2020)
for k, v in dados.items():
    print(f'O item {k} tem valor {v}')


