pessoas = {'nome':'Gutsavo', 'sexo':'M', 'idade':22}

print(f'O {pessoas["nome"]} tem sexo {pessoas["sexo"]} e {pessoas["idade"]} anos')
print('='*20)

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('='*20)

for k, v in pessoas.items():
    print(f'O {k} é {v}')
# del pessoas['sexo'] // serve para deletar keys
print('='*20)

pessoas['nome'] = 'Moysés'
print(pessoas['nome'])
print('='*20)

pessoas['peso'] = 70
print(pessoas.items())
print('='*20)

brasil = list()
estado1 = {'uf': 'Bahia', 'sigla': 'BA'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(brasil)
print(brasil[0])
print(brasil[0]['sigla'])
print('='*20)

estado = dict()
br = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    br.append(estado.copy())
for e in br:
    for v in e.values():
        print(v, end=' ')
    print()
