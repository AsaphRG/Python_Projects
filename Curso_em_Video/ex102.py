def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    n: Recebe o número a ser fatorado.
    show (opcional): Mostrar ou não a conta.
    return: Retorna o valor da fatoração.
    """
    num = 1
    for c in range(n, 0, -1):
        if show:
            num *= c
            if c == 1:
                print(c, end=" = ")
            else:
                print(c, end=" X ")
        else:
            num *= c
    print(num)


fatorial(5)
help(fatorial)
