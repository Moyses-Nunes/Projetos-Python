lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print('='*20)
for comida in lanche:
    print(f'Vou comer {comida}')
print('='*20)
for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')
print('='*20)
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
print('='*20)
print(sorted(lanche))
print(lanche)
print('='*20)
a = 2, 5, 4
b = 5, 8, 1, 2
c = a + b
print(c)
print('='*20)
print(len(c))
print(c.count(5))
print('='*20)
print(c)
print(c.index(5))
print(c.index(5, 1))
print('='*20)
pessoa = 'Moysés', 18
print(pessoa)
del(pessoa)
#print(pessoa) 'del' serve para deletar a variável

