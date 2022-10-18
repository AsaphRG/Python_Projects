import datetime
n = int(input('Qual o seu ano de nascimento?\n'))
a = datetime.date.today().year
print(f'O atleta tem {a - n} anos.')
if a - n <= 9:
    print('Categoria Mirim.')
elif a - n <= 14:
    print('Categoria Infantil.')
elif a - n <= 19:
    print('Categoria Junior.')
elif a - n <= 25:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')
