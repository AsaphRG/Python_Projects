v = int(input('Insira valor: ')), int(input('Insira valor: ')), int(input('Insira valor: ')), int(input('Insira valor: '))
print(v)
print(f'Tem {v.count(9)} números 9.')
tres = v.count(3)
if tres > 0:
    print(f'O número 3 é o {v.index(3) + 1}º algarismo.')
else:
    print(0)
cont = 0
num = ''
for pos, c in enumerate(v):
    if v[pos] % 2 == 0:
        cont += 1
        num += str(v[pos]) + ' '
print(f'Há {cont} números pares e eles são {num}')
#for n in v:
#    if n % 2 == 0:
#        print(n, end=' ')
