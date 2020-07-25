ex = str(input('Digite uma expressão: '))
abre = []
fecha = []
for s in ex:
    if s == '(':
        abre.append(1)
    elif s == ')':
        fecha.append(1)
if len(abre) != len(fecha):
    print('Equação inválida!')
else:
    print('Equação válida!')
