from time import sleep
from random import randint
result = False
cont = 0
alea = randint(0, 10)
while result == False:
    tent = int(input('Tente adivinhar o valor que escolhi: '))
    cont += 1
    if tent == alea:
        result = True
    else:
        print('Não é esse...', end=' ')
        sleep(1)
        if tent < alea:
            print('Mais!')
        elif tent > alea:
            print('Menos!')
print(f'Você acertou o número que eu escolhi em {cont} tentativas.')
