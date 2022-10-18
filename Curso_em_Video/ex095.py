jogadores = list()
gols = list()
aproveitamento = dict()
loop = True

while True:
    aproveitamento = {'jogador': str(input('Nome do jogador: ').strip().capitalize())}
    total = int(input(f"Quantas partidas {aproveitamento['jogador']} jogou? "))
    for c in range(total):
        gols.append(int(input(f"Quantos gols {aproveitamento['jogador']} fez na partida {c+1}? ")))
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = sum(gols)
    jogadores.append(aproveitamento.copy())
    print("-=" * 30)
    print("Dados salvos com sucesso!")
    print("-=" * 30)
    while True:
        teste = str(input("Quer continuar? [S/N] ").strip().upper()[0])
        if teste in "SN":
            break
        print('Insira S para continuar ou N para sair,')
    if teste == "N":
        break
print("-=" * 30)
while True:
    while True:
        loop = True
        teste = str(input("Quer ver os dados dos jogadores? [S/N] ").strip().upper()[0])
        if teste in "SN":
            break
        print("Insira S para continuar ou N para sair.")
    if teste == "N":
        break
    print("-=" * 30)
    while loop:
        for c in jogadores:
            print(c['jogador'])
        dados = str(input("Quer ver os dados de qual jogador? ").strip().capitalize())
        print("-=" * 30)
        for c in jogadores:
            if dados == c['jogador']:
                print(f"O jogador {c['jogador']} jogou {len(c['gols'])} partida(s).")
                for i in range(len(c['gols'])):
                    print(f"    => Na partida {i+1} ele fez {c['gols'][i]} gol(s).")
                loop = False
                print("-=" * 30)
