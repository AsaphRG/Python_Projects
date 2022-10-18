d = float(input('Qual a distância da sua viagem?'))
if d < 200:
    print(f'Sua viagem irá custar R${d * 0.5:.2f}')
else:
    print(f'Sua viagem irá custar R${d * 0.45:.2f}')
