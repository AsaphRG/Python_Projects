"""
Desafio 2: Fichas Mágicas do Tio Patinhas

Um brinquedo fictício é composto por 5 fichas em fila horizontal, todas as fichas tem formato de moeda e podem mudar de cor de maneira cíclica ao serem tocadas.
A regra de mudança de cor é a seguinte:
·       Quando uma ficha é tocada ela muda para a cor seguinte, seguindo esta ordem:
Preto => Azul => Vermelho => Laranja => Branco => Preto (Reinicia o ciclo)

·       As fichas vizinhas à ficha que foi tocada também mudam de cor (usando a mesma sequência cíclica), só que elas pulam uma cor.

Logo, se a ficha vizinha à ficha tocada era Branca, ela passa a ficar Laranja, pulando assim a cor Vermelha;

Deste modo, se as fichas começarem todas Brancas (BBBBB) e a primeira for tocada, a configuração seguinte será: VLBBB (Vermelho-Laranja-Branco-Branco-Branco).

Agora, se a terceira ficha for tocada, a configuração será: VPVLB (Vermelho-Preto-Vermelho-Laranja-Branco).

Supondo que as fichas comecem todas Brancas (BBBBB) e uma pessoa toque na primeira ficha (primeira ficha à esquerda), na terceira e na quarta, repetindo essa sequência de 3 toques num total de 45 toques, como ficará a configuração final das cores das fichas?

Atenção: Dê a resposta usando apenas a primeira letra de cada cor. Ex.: BBVVP
"""
lista = [4, 4, 4, 4, 4]
cor = ["Preto", "Azul", "Vermelho", "Laranja", "Branco"]
x = 0

while x < 45:
    x += 1
    lista[0] += 1
    lista[1] += 2
    lista[1] += 2
    lista[2] += 1
    lista[3] += 2
    lista[2] += 2
    lista[3] += 1
    lista[4] += 2

print("A sequência é: ", end="")
for x in lista:
    print(cor[x % 5][0], end="")
print()
