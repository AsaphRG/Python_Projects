lis = []
continuar = 's'
quantidade = 0

while True:
    lis.append(int(input('Insira um valor: ').strip().lower()))
    while 'sn' not in continuar:
        continuar = str(input('Deseja continuar? [S/N]').strip().lower())
        if 's' in continuar:
            quantidade += 1
            break
        elif 'n' in continuar:
            break
        else:
            print('Comando inválido.')
    if 'n' in continuar:
        break
print(f'Você digitou {quantidade + 1} números.')
print(lis.sort(reverse=True))
if 5 in lis:
    print('O número 5 está na lista.')
else:
    print('O número 5 não estão na lista.')
