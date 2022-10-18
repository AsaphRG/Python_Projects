n = int(input('Digite um valor: '))
print('\033[31m-=-\033[m' * 20)
if n < 0:
    print('\033[mEsse número é negativo.\033[m')
else:
    print('\033[30mEsse é um número positivo.\033[m')
print('\033[31m-=-' * 20)
