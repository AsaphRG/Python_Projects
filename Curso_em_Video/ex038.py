n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print(f'{n1:.0f} é maior que {n2:.0f}.')
elif n2 > n1:
    print(f'{n2:.0f} é maior que {n1:.0f}.')
else:
    print('O dois números são iguais.')
