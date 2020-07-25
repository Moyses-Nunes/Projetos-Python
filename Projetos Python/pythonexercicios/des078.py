p = ('aprender', 'programar', 'python', 'trabalhar',
     'futebol', 'bahia', 'corona')
for c in p:
    print(f'\nNa palavra {c.upper()}, temos: ', end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end='')

