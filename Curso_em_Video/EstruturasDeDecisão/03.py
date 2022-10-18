s = input('Qual seu sexo?\n').upper().strip()
if s[0] == 'F':
    print('\033[35mSeu sexo é feminino então.')
elif s[0] == 'M':
    print('\033[34mSeu sexo é masculino então.')
else:
    print('Sexo inválido, seu alternativo do caralho.')
