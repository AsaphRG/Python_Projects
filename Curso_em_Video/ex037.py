n = int(input('Insira um número: '))
b = int(input('Me diga como convertê-lo.\nDigite 1 para binário, 2 para octal e 3 para hexadecimal.\n'))
if b == 1:
    print(f'{n} em binário é igual a {bin(n)[2:]}.')
elif b == 2:
    print(f'{n} em octal é igual a {oct(n)[2:]}.')
elif b == 3:
    print(f'{n} em hexadecimal é igual a {hex(n)[2:]}.')
else:
    print('Código inválido.')
