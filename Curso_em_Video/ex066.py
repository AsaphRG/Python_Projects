cont = acum = 0
while True:
    n = int(input('Insira um número [999 para parar]: '))
    if n != 999:
        cont += 1
        acum += n
    else:
        break
print(f'Você inseriu {cont} números, eles somaram o valor de {acum}.')
