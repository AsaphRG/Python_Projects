func1 = True
while func1 == True:
    v1 = float(input('Digite um número: '))
    v2 = float(input('Digite outro número: '))
    func2 = True
    while func2 == True:
        função = int(input('''O que você deseja fazer?
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
        '''))
        if função == 1:
            print(f'{v1} + {v2} = {v1 + v2}')
        elif função == 2:
            print(f'{v1} * {v2} = {v1 * v2}')
        elif função == 3:
            if v1 > v2:
                maior = v1
            else:
                maior = v2
            if v1 < v2:
                menor = v1
            else:
                menor = v2
            print(f'{maior} > {menor}')
        elif função == 4:
            func2 = False
        elif função == 5:
            func1 = False
            func2 = False
        else:
            print('Opção inválida, tente novamente.')
print('Até a próxima, amigo.')
