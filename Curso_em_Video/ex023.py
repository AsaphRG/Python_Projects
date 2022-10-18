numeros = int(input('Insira valores aqui: '))
u = numeros // 1 % 10
d = numeros // 10 % 10
c = numeros // 100 % 10
m = numeros // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')