from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = randint(0, 9999)
        print(f'Inserido {matriz[l][c]} na posição [{l}, {c}].')
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print('')

'''n = 0
for c in range(0, 3):
    matriz[0].append(int(input(f'Insira um valor na posição [0, {n}]: ')))
    n += 1
n = 0
for c in range(0, 3):
    matriz[1].append(int(input(f'Insira um valor na posição [1, {n}]: ')))
    n += 1
n = 0
for c in range(0, 3):
    matriz[2].append(int(input(f'Insira um valor na posição [2, {n}]: ')))
    n += 1
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]\n[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]\n[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')'''
