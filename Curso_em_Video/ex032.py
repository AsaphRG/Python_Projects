import datetime
ano = int(input('Qual ano você deseja saber se é bissexto? Aperte 0 para o ano atual: '))
if ano == 0:
    ano = datetime.today().year
#if ano % 400 == 0:
#    print('Esse é um ano bissexto.')
#else:
#    if ano % 4 == 0:
#        if ano % 100 == 0:
#            print('Esse não é um ano bissexto.')
#        else:
#            print('Esse é um ano bissexto.')
#    else:
#        print('Esse não é um ano bissexto.')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto.')
