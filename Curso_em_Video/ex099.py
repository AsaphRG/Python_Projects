from random import randint


def maior(* num):
    alto = i = 0
    print("-=" * 30)
    print("Analisando os valores passados...")
    while i < len(num):
        print(num[i], end=" ")
        if alto < num[i]:
            alto = num[i]
        i += 1
    print(f"Foram informados {len(num)} valores ao todo.\nO maior valor informado foi {alto}.")


maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10))
maior(randint(0, 10))
maior()
