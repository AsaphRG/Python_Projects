v1 = int(input('Diga o termo inicial da sua PA: '))
r = int(input('Diga a razão da sua PA: '))
termos = 10
cont = 0
while cont < termos:
    cont += 1
    v1 += r
    print(v1, end=' ')
    if cont == termos:
        termos += int(input('\nQuantos termos mais você quer ver dessa PA? '))
