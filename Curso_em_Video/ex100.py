from time import sleep
from random import randint


numeros = list()
i = par = 0


def sorteio():
    print("Sorteando os valores da lista: ", end=" ")
    global i
    while i < 5:
        sleep(0.25)
        numeros.append(randint(1, 10))
        print(numeros[i], end=" ")
        i += 1
    sleep(0.25)
    print("Pronto!")
    sleep(0.25)
def somaPar():
    global par
    for c in numeros:
        if c % 2 == 0:
            par += c
    print(f"Somando os valores pares de {numeros}, temos {par}.")


sorteio()
somaPar()
