produtos = 'Pão', 1, 'Mortadela', 3, 'Leite', 2
#print(f'{produtos[0]:10}R${produtos[1]:5.2f}\n{produtos[2]:10}R${produtos[3]:5.2f}\n{produtos[4]:10}R${produtos[5]:5.2f}')
print('-' * 40)
print(f'{"PADARIA DO SEU JOÃO":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print('-' * 40)
