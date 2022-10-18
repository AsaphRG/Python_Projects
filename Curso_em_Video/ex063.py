cont = 2
n = int(input('Quantos elementos da sequência Fibonacci você quer ver? '))
v1 = 0
v2 = 1
print(f'{v1} > {v2}', end='')
while cont < n:
    v3 = v1 + v2
    print(f' > {v3}', end='')
    v1 = v2
    v2 = v3
    cont += 1
