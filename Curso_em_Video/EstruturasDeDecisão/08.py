p1 = float(input('Me diga o valor do primeiro produto: '))
p2 = float(input('Me diga o valor do segundo produto: '))
p3 = float(input('Me diga o valor do terceiro produto: '))
menor = p1
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p2 and p3 < p1:
    menor = p3
print(f'Você deveria comprar o que custa R${menor}')
