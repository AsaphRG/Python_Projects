num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
print('Para encerrar digite S')
while True:
    var = int(input('Insira um número entre 0 e 20: '))
    while var < 0 or var > 20:
        var = int(input('Insira um número entre 0 e 20: '))
    print(num[var])
