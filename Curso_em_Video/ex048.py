s = 0
r = 0
for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            r += 1
            s += c
print(s)
print(r)

print('-=' * 30)

t = 0
e = 0
for b in range(3, 501, 3):
    if b % 2 != 0:
        e += 1
        t += b
print(t)
print(e)

print('-=' * 30)

soma = 0
cont = 0
for z in range(1, 501, 2):
    if z % 3 == 0:
        soma += z
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')
