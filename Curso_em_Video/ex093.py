aproveitamento = {'jogador': str(input('Nome do jogador: ').strip().capitalize())}
gols = list()
total = int(input(f"Quantas partidas {aproveitamento['jogador']} jogou? "))

for c in range(total):
    gols.append(int(input(f"Quantos gols {aproveitamento['jogador']} fez na partida {c+1}? ")))
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = sum(gols)
print("-=" * 30)
print(aproveitamento)
print("-=" * 30)
for k, v in aproveitamento.items():
    print(f"O campo {k} tem o valor {v}.")
print("-=" * 30)
print(f"O jogador {aproveitamento['jogador']} jogou {len(aproveitamento['gols'])} partidas.")
for c in range(len(aproveitamento['gols'])):
    print(f"    => Na partida {c+1} ele fez {aproveitamento['gols'][c]} gols.")
print("-=" * 30)
