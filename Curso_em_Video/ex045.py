import random
import time

cont = 0
print("Para encerrar digite sair.")
while True:
    rr = random.randint(1, 3)
    e = str(input('Pedra, papel ou tesoura?\n')).lower()
    if e == "sair":
        break
    else:
        print('Jo...')
        time.sleep(1)
        print('Ken...')
        time.sleep(1)
        print('Po!')
        if rr == 1:
            print(f'Pedra!')
        elif rr == 2:
            print(f'Papel!')
        else:
            print(f'Tesoura!')
        if rr == 1 and e == 'pedra':
            print('Empatamos.')
        elif rr == 1 and e == 'papel':
            print('Droga, você ganhou.')
            cont += 1
        elif rr == 1 and e == 'tesoura':
            print('Eu ganhei!')
        elif rr == 2 and e == 'pedra':
            print('Eu ganhei!')
        elif rr == 2 and e == 'papel':
            print('Empatamos.')
        elif rr == 2 and e == 'tesoura':
            print('Droga, eu perdi.')
            cont += 1
        elif rr == 3 and e == 'pedra':
            print('Droga, eu perdi.')
            cont += 1
        elif rr == 3 and e == 'papel':
            print('Eu ganhei!')
        elif rr == 3 and e == 'tesoura':
            print('Empatamos.')
        else:
            print('Você colocou errado.')
print(f"Você ganhou {cont} vezes.")