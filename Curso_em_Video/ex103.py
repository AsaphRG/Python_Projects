def ficha(nome="", num=""):
    if nome == "":
        nome = "<desconhecido>"
    if num == "":
        num = 0
    return print(f'O jogador {nome} fez {num} gols no campeonato.')


ficha(input("Nome do jogador: "), input("Número de gols: "))
