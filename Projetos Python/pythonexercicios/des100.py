def maior(*num):
    c = mai = 0
    for n in num:
        if c == 0:
            mai = n
        c += 1
        if n > mai:
            mai = n
    print(f'Entre {num} temos {len(num)} números e o maior é {mai}')

maior(1, 2, 6, 4)
maior(6, 5, 5)
maior(-2, 7, 2, 0)
maior(8)
