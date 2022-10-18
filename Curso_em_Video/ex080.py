lis = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lis[-1]:
        lis.append(n)
        print(f'Adicionado {n} á lista na posição {len(lis)}.')
    else:
        pos = 0
        while pos < len(lis):
            if n <= lis[pos]:
                lis.insert(pos, n)
                break
            pos += 1
        print(f'{n} foi inserido na posição {pos}.')
print(lis)
