d = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos quilômetros você percorreu com o carro? '))
pd = d*60
pkm = km*0.15
print(f'O valor do aluguel é de {pd+pkm:.2f}')
