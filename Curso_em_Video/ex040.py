n = float(input('Qual a sua nota?\n'))
if n < 5:
    print(f'Você está reprovado.')
elif n < 7:
    print('Você está de recuperação.')
else:
    print('Você foi aprovado.')
