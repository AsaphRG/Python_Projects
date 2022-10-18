from random import randint
numeros = [[], []]
for c in range(0, 7):
    valor = randint(0, 9)
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(numeros)
print(f'Os valores pares digitador foram: {numeros[0]}\nOs valores ímpares digitados foram: {numeros[1]}')



'''pares = []
impares = []
numeros = []
for c in range(0, 7):
    n = randint(0, 9)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
numeros.append(pares)
numeros.append(impares)
print(f'Os valores pares digitador foram: {numeros[0]}\nOs valores ímpares digitados foram: {numeros[1]}')
'''
