s = float(input('Insira o salário: R$'))
if s > 1250:
    print(f'Esse salário terá um aumento de R${(s / 100) * 10}, o novo salário será de R${s + ((s / 100) * 10)}')
else:
    print(f'Esse salário terá um aumento de R${(s / 100) * 15}, o novo salário será de R${s + ((s / 100) * 15)}')
