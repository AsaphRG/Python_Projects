n = input('Digite três números: ')
n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])
menor = n1
if n2 < n1 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
meio = n1
if n2 > menor and n2 < maior:
    meio = n2
if n3 > menor and n3 < maior:
    meio = n3
print(f'{maior, meio, menor}')
