import datetime
i = int(input('Qual ano você nasceu?\n'))
n = datetime.date.today().year
if n - i == 18 or n - i == 17:
    print('Está na hora de você se alistar.')
elif n - i > 18:
    print('Já passou do tempo de você se alistar.')
else:
    print('Ainda chegará sua hora, paciência, Padawan.')
