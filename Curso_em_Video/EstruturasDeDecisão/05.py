n1 = int(input('Insira sua primeira nota: '))
n2 = int(input('Insira sua segunda nota: '))
r = (n1 + n2) / 2
if r == 10:
    print('Aprovado com distinção.')
elif r > 7:
    print('Aprovado.')
else:
    print('Reprovado.')
