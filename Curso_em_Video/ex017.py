from math import hypot
o = float(input('Digite o cateto aqui: '))
a = float(input('Digite a adjacente aqui: '))
h = hypot(a, o)
print(f'A hipotenusa de {o} e {a} é {h}.')
