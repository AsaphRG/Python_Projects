cont = valor = total = contp = menorv = 0
menorn = ' '
print('-' * 30 + 'LOJAS SUPER BARATÃO' + '-' * 30)
while True:
    nome = str(input('Produto: '))
    valor = float(input('Valor: R$'))
    total += valor
    cont += 1
    if valor > 1000:
        contp += 1
    if cont == 1 or menorv > valor:
        menorv = valor
        menorn = nome
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Deseja inserir mais produtos? [S/N] ')).strip().upper()[0]
    if conti == 'N':
        break
print(f'''Você comprou {cont} produtos.
O total foi de R${total:.2f}.
{contp} produtos custam mais que R$1000.00.
O produto mais barato foi {menorn} e o seu preço foi de R${menorv:.2f}.''')
