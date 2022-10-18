from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    print("-=" * 30, f"\nContagem de {inicio} até {fim} de {passo} em {passo}.")
    if passo == 0:
        for x in range(inicio, fim+1, 1):
            print(x, end=" ")
            sleep(0.25)
    elif inicio < fim:
        for x in range(inicio, fim+1, passo):
            print(x, end=" ")
            sleep(0.25)
    elif inicio > fim:
        for x in range(inicio, fim+1, -passo):
            print(x, end=" ")
            sleep(0.25)
    print("Fim!")
    print("-=" * 30)


print(f"-=" * 30, "\nContagem de 1 a 10 de 1 em 1.")
for i in range(1, 11, 1):
    sleep(0.25)
    print(i, end=" ")
print(f"Fim!\n" + "-=" * 30, "\nContagem de 10 a 0 de 2 em 2.")
for i in range(10, -1, -2):
    sleep(0.25)
    print(i, end=" ")
print(f"Fim!\n" + "-=" * 30, "\nAgora sua vez de fazer uma contagem personalizada.")
contador(int(input("Insira o início: ")), int(input("Insira o fim: ")), int(input("Insira o passo: ")))
