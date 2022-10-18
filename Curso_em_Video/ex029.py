vc = float(input('Velocidade do carro em km/h: '))
if vc > 80:
    print(f'Você foi multado em R${(vc - 80) * 7:.2f}')