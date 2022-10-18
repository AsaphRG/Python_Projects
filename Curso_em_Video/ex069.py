cont1 = conth = m18 = mm20 =  0
while True:
    cont1 += 1
    idade = int(input('Diga a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Diga o seu sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        m18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        mm20 += 1
    func = ' '
    while func not in 'SN':
        func = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if func == 'N':
        break
print(f'Você inseriu {cont1} pessoas e {conth} eram homens, {m18} eram maiores de 18 anos e {mm20} mulheres eram menores de 20 anos.')
