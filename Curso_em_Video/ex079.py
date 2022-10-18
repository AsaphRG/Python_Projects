lis = []
while True:
    n = int(input('Insira um valor: '))
    if n in lis:
        print('Este número já está na lista.')
    else:
        lis.append(n)
    continuar = ' '
    while continuar[0] not in 'Ss':
        continuar = str(input('Você quer continuar? {S/N)').strip())
        if continuar[0] in 'Nn':
            break
        elif continuar[0] not in 'Ss':
            print('Insira um valor válido.')
    if continuar[0] in 'Nn':
        break
print(sorted(lis))
