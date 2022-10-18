from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
c3 = 0
m = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = randint(0, 9)
        print(f'Inserido {matriz[l][c]} na posição [{l}, {c}].')
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            c3 += matriz[l][c]
        if c == 1:
            if matriz[l][c] > m:
                m = matriz[l][c]
print(f'A soma dos valores pares é {soma}.\nA soma dos valores da terceira coluna é {c3}.\nO maior da segunda coluna é {m}.')
