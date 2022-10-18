h = float(input('Insira sua altura em metros: '))
p = float(input('Insira seu peso: '))
imc = p / (h * h)
margemi = 18.5 * (h * h)
margemf = 24.9 * (h * h)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, o ideal é de 18.5, você está abaixo do peso, precisa engordar {(p - margemi) * -1:.1f}KG.')
elif imc <=24.9:
    print(f'Seu IMC é de {imc:.1f}, seu peso está ótimo, continue assim! Você deve ficar entre {margemi:.1f}KG e {margemf:.1f}KG.')
elif imc <= 29.9:
    print(f'Seu IMC é de {imc:.1f}, o ideal é 24.9, você está com sobrepeso, precisa emagrecer {p - margemf:.1f}KG')
elif imc <= 34.9:
    print(f'Seu IMC é de {imc:.1f}, o ideal é 24.9, você está com obesidade grau 1, precisa emagrecer {p - margemf:.1f}KG')
elif imc <= 39.9:
    print(f'Seu IMC é de {imc:.1f}, o ideal é 24.9, você está com obesidade grau 2, precisa emagrecer {p - margemf:.1f}KG')
else:
    print(f'Seu IMC é de {imc:.1f}, o ideal é 24.9, você está com obesidade grau 3, precisa emagrecer {p - margemf:.1f}KG')
input('Aperte ENTER para encerrar')
