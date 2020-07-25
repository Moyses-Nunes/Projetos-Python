import random
import time
n = int(input('Em qual número eu pensei? '))
nc = random.randint(0, 5)
print('PROCESSANDO..')
time.sleep(2)
print('Eu pensei no número {}'.format(nc))
if n == nc:
    print('Parabéns, pensei no mesmo número!')
else:
    print('Infelizmente vc errou!')

