pessoas = []
todos = []
pesados = []
leves = []
maisp = menosp = 0

while True:
    pessoas.append(str(input('Nome: ')).strip().capitalize())
    pessoas.append(int(input('Peso: ')))
    todos.append(pessoas[:])
    pessoas.clear()
    while True:
        c = input('Quer continuar? ').lower().strip()[0]
        if c in 'sn':
            break
    if c == 'n':
        break

for n, p in enumerate(todos):
    if n == 0:
        maisp = menosp = p
    elif p[1] > maisp[1]:
        maisp = p
    elif p[1] < menosp[1]:
        menosp = p
    if p[1] > 90:
        pesados.append(p[0])
    else:
        leves.append(p[0])

print(f'Foram cadastradas {len(todos)} pessoas.')
print(f'A mais pesada tem {maisp[1]}Kg e são ', end='')
for i in todos:
    if i[1] == maisp[1]:
        print(i[0], end=' ')
print(f'\nA mais leve tem {menosp[1]}Kg e são ', end='')
for g in todos:
    if g[1] == menosp[1]:
        print(g[0], end=' ')
