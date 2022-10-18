v = int(input('Insira um número: '))
cont = 0
for c in range(1, v + 1):
    if v % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {v} foi divisível {cont} vezes.')
if cont == 2:
    print(f'Por isso ele não é um número primo.')
else:
    print(f'Por isso ele é um número primo.')
