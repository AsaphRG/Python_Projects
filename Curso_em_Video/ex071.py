n50 = n20 = n10 = n5 = n1 = 0
saque = int(input('Valor que deseja sacar: R$').strip())
n100 = saque // 100
resto = saque % 100
if resto >= 50:
    n50 = resto // 50
    resto = resto % 50
if resto >= 20:
    n20 = resto // 20
    resto = resto % 20
if resto >= 10:
    n10 = resto // 10
    resto = resto % 10
if resto >= 5:
    n5 = resto // 5
    resto = resto % 5
if resto >= 1:
    n1 = resto // 1
    resto = resto % 1
print(f'=' * 20 + ' Banco do Asaph ' + '=' * 30)
print(f'Você pediu R${saque:.2f}. Serão:')
if n100 > 0:
    print(f'> {n100:.0f} notas de R$100.')
if n50 > 0:
    print(f'> {n50:.0f} notas de R$50.')
if n20 > 0:
    print(f'> {n20:.0f} notas de R$20.')
if n10 > 0:
    print(f'> {n10:.0f} notas de R$10.')
if n5 > 0:
    print(f'> {n5:.0f} notas de R$5.')
if n1 > 0:
    print(f'> {n1:.0f} notas de R$1.')
print('Pega essa porra e vai embora, foda-se.\nVolte sempre!')
