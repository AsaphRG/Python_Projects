vc = float(input('Qual o valor da casa?\n'))
s = float(input('Qual o valor do salário?\n'))
a = float(input('Em quantos anos você vai pagar a casa?\n'))
m = a * 12
r = (vc / m)
p = (s / 100) * 30
print(f'Para pagar uma casa de R${vc:.2f} em {a:.0f} anos a prestação será de R${r:.2f}.')
if r < p:
    print(f'Seu empréstimo foi aprovado.')
else:
    print('Seu empréstimo foi negado.')
