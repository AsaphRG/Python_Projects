f = str(input('Escreva uma frase: ')).strip()
m = ' '
m += f.replace(' ', '').lower()
c = m[len(m):0:-1]
if c == m[1:len(m)]:
    print(f'{f} é um palíndromo.')
else:
    print(f'{f.capitalize()} não é um palíndromo.')
print(c.capitalize())

print('-=' * 30)

palavras = f.upper().split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
