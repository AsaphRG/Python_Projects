media = 0
velho = 0
nomevelho = ''
cont = 0
for c in range(1, 5):
    nome = str(input(f'Diga o nome da {c}ª pesssoa: '))
    idade = int(input(f'Diga a idade da {c}ª pessoa: '))
    sexo = str(input(f'Qual o sexo da {c}ª pessoa [M/F]: '))
    media += idade
    if c == 1:
        velho = idade
        nomevelho = nome
    else:
        if idade > velho and sexo in 'Mm':
            velho = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        cont += 1
print(f'A média de idade do grupo é de {media / c} anos.')
print(f'O grupo é composto por {cont} mulheres menores de 20 anos.')
print(f'O homem mais velho é {nomevelho} e ele tem {velho} anos.')