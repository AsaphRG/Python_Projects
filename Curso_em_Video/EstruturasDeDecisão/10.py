t = input('Qual turno você estuda? ((M)atutino, (V)espertino ou (N)oturno)\n').upper().strip()
if t == 'M' or t == 'MATUTINO' or t == 'MANHÃ' or t == 'MANHA':
    print('Bom dia!')
elif t == 'V' or t == 'VESPERTINO' or t == 'TARDE':
    print('Boa tarde!')
elif t == 'N' or t == 'NOTURNO' or t == 'NOITE':
    print('Boa noite')
else:
    print('Valor inválido.')