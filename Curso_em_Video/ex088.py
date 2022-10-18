from random import randint
from time import sleep
n =[]
jogos = []

qj = int(input('Quantos jogos você deseja? '))
print('-=' * 30)
for b in range(0, qj):
    while True:
        alea = randint(0, 60)
        if alea not in n:
            n.append(alea)
        if len(n) == 6:
            break
    print(f'Jogo {b + 1}: {n}')
    sleep(1)
    jogos.append(n[:])
    n.clear()
print('-=' * 30)