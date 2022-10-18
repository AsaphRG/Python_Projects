"""
Desafio 1: Caixa Forte do Tio Duck

Para acessar os demais desafios, primeiro é preciso fornecer a combinação do cofre.

Número Único: 713115616677996163438894795559

a) Deixe apenas os dígitos que sejam primos:

b) Deixe apenas os dígitos que sejam pares:

c) Deixe apenas os dígitos que sejam ímpares:

d) Deixe apenas os dígitos que aparecem na sequência de Fibonacci:

e) Reescreva-o de trás pra frente:

f) Coloque a soma de todos os dígitos divisíveis por 3:

g) Coloque a soma dos 7 primeiros dígitos pares com os 7 últimos dígitos ímpares:

h) Usando o seguinte mapeamento de dígito para letra, reescreva seu número com o mapeamento correto:
Infelizmente não consegui salvar o mapeamento, mas ele está registrado no último desafio.
"""

var = str(713115616677996163438894795559)
lista = []

# constrói a lista que vai ser usada pelo algoritmo
for x in var:
    lista.append(int(x))
print(lista)
print()

# primos
print("Primos:", end=" ")
primos = []
for x in lista:
    if str(x) in "2357":
        primos.append(x)
for x in primos:
    print(x, end="")
print()

# pares
print("Pares:", end=" ")
pares = []
for x in lista:
    if x % 2 == 0:
        pares.append(x)
for x in pares:
    print(x, end="")
print()

# ímpares
print("Ímpares:", end=" ")
impares = []
for x in lista:
    if x % 2 != 0:
        impares.append(x)
for x in impares:
    print(x, end="")
print()

# fibonacci
print("Fibonacci:", end=" ")
fibonacci = []
for x in lista:
    if str(x) in "12358":
        fibonacci.append(x)
for x in fibonacci:
    print(x, end="")
print()

# contrario
print("Reverse:", end=" ")
contrario = lista.copy()
contrario.reverse()
for x in contrario:
    print(x, end="")
print()

# /3
print("Divisíveis por 3:", end=" ")
soma3 = 0
for x in lista:
    if x % 3 == 0:
        soma3 += x
print(soma3)

# soma
print("A soma da soma dos 7 primeiros dígitos pares com a soma dos 7 últimos dígitos ímpares:", end=" ")
v1 = v2 = 0
i = x = 0
for x in lista:
    if x % 2 == 0:
        v1 += x
        i += 1
    if i == 7:
        break
i = x = 0
for x in contrario:
    if x % 2 == 1:
        v2 += x
        i += 1
    if i == 7:
        break
print(v1 + v2)

# codificar
print("Código:", end=" ")
txt = []
for x in lista:
    if x == 0:
        txt.append("B")
    elif x == 1:
        txt.append("J")
    elif x == 2:
        txt.append("K")
    elif x == 3:
        txt.append("F")
    elif x == 4:
        txt.append("M")
    elif x == 5:
        txt.append("Y")
    elif x == 6:
        txt.append("T")
    elif x == 7:
        txt.append("L")
    elif x == 8:
        txt.append("O")
    elif x == 9:
        txt.append("G")
for x in txt:
    print(x, end="")
print()
