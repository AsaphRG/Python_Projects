lis = []
n = 0
lmxv = []
lmnv = []

for c in range(5):
    lis.append(int(input(f'Insira um valor na casa {n + 1}: ')))
    n += 1
print(f'Você digitou os valores {lis}.')
mxv = max(lis)
mnv = min(lis)
for pos, c in enumerate(lis):
    if c == mxv:
        lmxv.append(pos + 1)
    elif c == mnv:
        lmnv.append(pos + 1)
print(f'O maior número foi {mxv} nas posições {lmxv}.')
print(f'O menor valor foi {mnv} nas posições {lmnv}.')
