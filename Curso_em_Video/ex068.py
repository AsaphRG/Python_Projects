from random import randint
cont = 0
while True:
    print('-' * 30)
    while True:
        escolha = str(input('Par ou ímpar?')).strip().upper()
        if escolha == 'PAR' or escolha == 'IMPAR' or escolha == 'ÍMPAR':
            break
    computador = randint(0, 10)
    n = int(input('Diga seu valor: '))
    print('-' * 30)
    modulo = (computador + n) % 2
    print(computador + n)
    if modulo == 0:
        if escolha == 'PAR':
            print('Você ganhou!')
            cont += 1
        else:
            print("Você perdeu!")
            break
    else:
        if escolha == 'IMPAR' or escolha == 'ÍMPAR':
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
if cont == 0:
    print(f'Bem... isso é constrangedor, você não ganhou nenhuma...')
else:
    print(f'Você ganhou {cont} vezes, parabéns!')
input('')
