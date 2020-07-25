s = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n
        c = c + 1
print('A soma dos {} valores é {}'.format(c, s))
