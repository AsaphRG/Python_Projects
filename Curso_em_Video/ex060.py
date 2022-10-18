from math import factorial
n = int(input('Digite um número: '))
fat = factorial(n)
print(f'O fatorial de {n} é {fat}.')

print('-=' * 30)

n = int(input('Digite um número: '))
c = n
f = 1
print(f'Calculando: {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

print('-=' * 30)

v = int(input('Diga um número: '))
f = v
while f > 1:
    f -= 1
    v *= f
print(v)

print('-=' * 30)

b = int(input('Digite um número: '))
for c in range(b, 1, -1):
    b *= (c - 1)
print(b)
