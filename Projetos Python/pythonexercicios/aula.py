galera = [['João', 19], ['Ana', 33], ['Elias', 45], ['Maria', 39]]
print(galera[0][1])
print(galera[3])
print(galera[2][0])
print('=-' * 20)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('=-' * 20)
pessoas = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)
