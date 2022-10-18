v = float(input('Insira o valor do produto: R$'))
m = int(input('Escolha o método de pagamento:\n[ 1 ] Dinheiro ou cheque á vista\n[ 2 ] Cartão á vista\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\n').strip().lower())
if m == 1:
    print(f'Você receberá um desconto de R${(v / 100) * 10:.2f}, o preço será de R${v - ((v / 100) * 10):.2f}.')
elif m == 2:
    print(f'Você receberá um desconto de R${(v / 100) * 5:.2f}, o preço será de R${v - ((v / 100) * 5):.2f}.')
elif m == 3:
    print(f'O preço será de R${v:.2f} em 2 parcelas de R${v / 2}')
elif m == 4:
    p = int(input('Irá pagar em quantas parcelas?'))
    print(f'Haverá um juro de R${(v / 100) * 20:.2f}, o preço será de R${v + ((v / 100) * 20):.2f} em {p} parcelas de R${(v + ((v / 100) * 20)) / p}')
else:
    print(f'\033[31mDeve ter um erro na entrada do método de pagamento, confira e tente novamente.\033[m')
