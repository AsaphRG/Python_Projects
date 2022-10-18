import datetime
ano = datetime.date.today().year
menores = 0
maiores = 0
for c in range(1, 8):
    nascimento = int(input(f'Diga o ano de nascimento da {c}º pessoa: '))
    if ano - nascimento <= 18:
        menores += 1
    else:
        maiores += 1
print(f'''Temos {maiores} maiores de idade.
Também temos {menores} menores de idade.''')
