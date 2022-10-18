acum = 0
cont = 0
true = False
while true == False:
    v = int(input('Insira um número [999 para parar]: '))
    if v == 999:
        true = True
    else:
        acum += v
        cont += 1
print(f'Você digitou {cont} números e a soma deles é {acum}.')
