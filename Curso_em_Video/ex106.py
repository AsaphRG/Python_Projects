c = ('\033[m',          # 0 - Sem cor
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[0;30;107m'    # 6 - Branco
     )


def ajuda(msg):
    título(f'Acessando o manual do comando \'{msg}\'', 4)
    print(c[6], end='')
    help(msg)
    print(c[0], end='')

def título(msg, cor=0):
    print(c[cor], end="")
    print("=" * (len(msg) + 4))
    print("  " + msg)
    print("=" * (len(msg) + 4))
    print(c[0], end="")


while True:
    título(f'Sistema de ajuda PyHelp', 2)
    msg = str(input("Função ou Biblioteca > "))
    if msg.upper() == "FIM":
        break
    else:
        ajuda(msg)
título("ATÉ LOGO!", 1)
