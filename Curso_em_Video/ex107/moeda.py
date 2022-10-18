def aumentar(valor, aum):
    aum /= 100
    valor += valor * aum
    return valor

def diminuir(valor, dim):
    dim /= 100
    valor -= valor * dim
    return valor

def dobro(valor):
    valor *= 2
    return valor

def metade(valor):
    valor /= 2
    return valor
