from random import randint
from time import sleep

print("Para encerrar digite Sair")
while True:
    r = randint(1, 6)
    v = input('Vamos jogar, eu pensei em um número entre 0 e 5, tente adivinhar qual é!\n')
    try:
        v = int(v)
    except:
        v = v.strip().upper()
        if v == "SAIR":
            break
        else:
            print('Insira um número.')
    print('Vamos ver se você acertou...')
    vb = r == v
    if vb:
        sleep(3)
        print('Você acertou!')
    elif not vb:
        sleep(3)
        print('Tente de novo')
