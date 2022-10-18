n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
r = n1
if n2 > n1 and n2 > n3:
    r = n2
if n3 > n1 and n3 > n2:
    r = n3
print(f'{r} é o maior número.')
