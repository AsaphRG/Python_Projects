v = int(input('Qual tabuada deseja saber?\n'))
print('\033[31m*-\033[m' * 30)
for c in range(1, 11):
    print(f'{v:2} x {c:2} = {c * v:2}')
    c += 1

print('-=' * 30)

num = int(input('Digite um número para ver sua tabuada: '))
for b in range(1,11):
    print(f'{num} x {b:2} = {num * b}')
