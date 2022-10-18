vs = float(input('Insira o valor do salário. R$'))
if vs <= 280:
    p = 20
    vp = vs / 100 * 20
elif vs <= 700:
    p = 15
    vp = vs / 100 * 15
elif vs <= 1500:
    p = 10
    vp = vs / 100 * 10
else:
    p = 5
    vp = vs / 100 * 5
print(f'Seu salário de R${vs:.2f} será aumentado em {p}% resultando num aumento de R${vp:.2f}, totalizando R${vs + vp:.2f}')
