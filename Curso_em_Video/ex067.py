cont = 1
while True:
    n = int(input('Diga a tabuada que você deseja saber: '))
    if n >= 0:
        for c in range(1, 11):
            print(f'{n:2} x {c:2} = {n * c:2}')
            cont += 1
    else:
        break
print('Foi um prazer te ajudar, volte sempre!')
