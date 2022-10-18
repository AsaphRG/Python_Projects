sexo = ''
teste = False
while teste == False:
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()[0]
    if sexo in 'FfMm':
        teste = True
    else:
        print('Digite um sexo válido.')

print('-=' * 30)

sex = str(input('Informe seu sexo [F/M]: ')).strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
print(f'Sexo {sexo} registrado com sucesso.')
