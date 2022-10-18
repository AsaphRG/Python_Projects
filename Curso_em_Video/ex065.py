func = 'S'
cont = acum = 0
while func == 'S':
    var = int(input('Digite um valor: '))
    if cont == 0:
        maior = menor = var
    else:
        if var > maior:
            maior = var
        elif var < menor:
            menor = var
    cont += 1
    acum += var
    func = str(input('Você quer continuar inserindo valores? [S/N] ')).strip().upper()[0]
print(f'A soma dos seus valores é {acum}, você digitou {cont} números, o maior foi {maior} e o menor foi {menor}.')
