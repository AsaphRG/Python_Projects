lis = []
lisp = []
lisi = []
continuar = 's'

while continuar != 'n':
    lis.append(int(input('Insira um valor: ').strip().lower()))
    while 'sn' not in continuar:
        continuar = str(input('Deseja continuar? [S/N]').strip().lower())
        if 's' in continuar or 'n' in continuar:
            break
        else:
            print('Comando inválido.')
for pos, c in enumerate(lis):
    if c % 2 == 0:
        lisp.append(c)
    else:
        lisi.append(c)
print(f'{lis}\n{lisp}\n{lisi}')
