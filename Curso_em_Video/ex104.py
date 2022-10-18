def leiaint():
    while True:
        num = input("Insira um número: ")
        if num.isnumeric():
            num = int(num)
            break
        else:
            print("\033[31mERRO! Digite um valor inteiro.\033[m")
    return num


n = leiaint()
print(f"Você digitou {n}.")
