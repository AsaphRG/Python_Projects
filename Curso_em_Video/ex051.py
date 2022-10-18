v = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão: '))
for c in range(1, 11):
    print(v)
    v += r

print('-=' * 30)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for b in range(primeiro, décimo + 1, razão):
    print(f'{b} ', end='> ')
print('ACABOU')
