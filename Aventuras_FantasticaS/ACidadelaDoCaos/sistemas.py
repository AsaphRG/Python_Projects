from time import sleep
from random import randint
from math import floor


global Jogador, Inimigo, Magia, Equipamentos
TAM = 100
Equipamentos = list()
Jogador = dict()
Magia = dict()
Inimigo = dict()


def escolha():
    conferirMagia('Habilidade', 'Energia', 'Sorte')
    return input("\n    Você decide: ").strip().upper()

def aumentarStatus(magia):
    if magia == "HABILIDADE":
        if testarMagia('Habilidade'):
            gastarMagia('Habilidade')
            magiaHabilidade()
            imprimir(f"\n    Você tem {Jogador['Habilidade']} pontos de Habilidade.\n")
        else:
            erro()
    elif magia == "ENERGIA":
        if testarMagia('Energia'):
            gastarMagia('Energia')
            magiaEnergia()
            imprimir(f"\n    Você tem {Jogador['Energia']} pontos de Energia.\n")
        else:
            erro()
    elif magia == "SORTE":
        if testarMagia('Sorte'):
            gastarMagia('Sorte')
            magiaSorte()
            imprimir(f"\n    Você tem {Jogador['Sorte']} pontos de Sorte.\n")
        else:
            erro()
    else:
        erro()


def separador():
    """
    -> separador insere um tracejado na tela.
    """
    print("\n" + ":" * TAM + "\n")

def erro():
    """
    -> errado insere mensagem de erro para o jogador.
    """
    imprimir("Tente novamente.")

def segurador():
    input("    Aperte [Enter] para prosseguir.")

def imprimir(txt):
    """
    -> imprimir recebe uma string e a imprime caractere por caractere.
    :param txt: Recebe a string.
    """
    paragrafo = 0
    cont = 0
    for c in range(len(txt)):
        if paragrafo == 0:
            print("    ", end="")
            cont += 4
        if cont == TAM - 1:
            print(txt[c], end="\n", flush=True)
            cont = 0
            paragrafo += 1
        else:
            #sleep(0.01)
            print(txt[c], end="", flush=True)
            cont += 1
            paragrafo += 1
        if txt[c] == "\n":
            cont = 0
            paragrafo = 0
    print()

def status():
    """
    -> status define as estatísticas do jogador.
    :return: Retorna o dicionário Jogador com os parâmetros Habilidade, Energia e Sorte.
    """
    global T_HABILIDADE, T_ENERGIA, T_SORTE
    T_HABILIDADE = (randint(1, 6) + 6)
    T_ENERGIA = randint(1, 6) + randint(1, 6) + 12
    T_SORTE = randint(1, 6) + 6
    Jogador['Habilidade'] = T_HABILIDADE
    Jogador['Energia'] = T_ENERGIA
    Jogador['Sorte'] = T_SORTE
    return Jogador

def aumentarSorte(num):
    Jogador['Sorte'] += num

def batalha(nome, habilidade, energia, fuga=0):
    """
    -> batalha calcula o resultado do encontro contra um inimigo, ficando em loop até que a vida de um dos dois chega a zero.
    :param Jogador: Recebe os dados do jogador.
    :param Inimigo: Recebe os dados do inimigo oferecido pelo arquivo da aventura.
    :return: Retorna o resultado da batalha, se falso encerra o jogo.
    """
    global esc
    cont_a = 0
    cont = 0
    Inimigo['Habilidade'] = int(habilidade)
    Inimigo['Energia'] = int(energia)
    imprimir("A batalha começa!")
    while True:
        if cont_a == 4 and nome == "Fera das Garras":
            return
        if testarMagia('Energia'):
            if input("    Usar Encanto Energia? [S/N] ").strip().upper()[0] == "S":
                gastarMagia('Energia')
                magiaEnergia()
        if cont == fuga and cont != 0:
            fugir = input(f"    Fugir de {nome} [S/N]: ").strip().upper()[0]
            if fugir == "S":
                imprimir(f"A fuga tem perdas maiores do que a humilhação de fugir de {nome}.")
                Jogador['Energia'] -= 2
                return True
        I_Forca = randint(1, 6) + randint(1, 6) + int(Inimigo['Habilidade'])
        J_Forca = randint(1, 6) + randint(1, 6) + int(Jogador['Habilidade'])
        imprimir(f"""Você tirou: {J_Forca}         Inimigo tirou: {I_Forca}""")
        if J_Forca > I_Forca:
            imprimir(f"Você acertou o {nome}.")
            cont_a += 1
            if str(input("    Quer testar sua sorte? [S/N]: ").strip().upper()[0]) == "S":
                if testarSorte():
                    imprimir("Você teve sorte e seu ataque foi avassalador.")
                    Inimigo['Energia'] -= 4
                else:
                    imprimir("Você não teve sorte e o seu ataque pegou de raspão.")
                    Inimigo['Energia'] -= 1
            else:
                imprimir(f"Você o atingiu e {nome} sentiu o ataque.")
                Inimigo['Energia'] -= 2
        elif J_Forca < I_Forca:
            imprimir(f"{nome} te acertou.")
            if str(input("    Quer testar sua sorte? [S/N]: ").strip().upper()[0]) == "S":
                Sorte = testarSorte()
                if Sorte:
                    Inimigo['Energia'] -= 1
                    imprimir(f"Você teve sorte e o ataque pegou de raspão. Você tem {Jogador['Energia']} de vida.")
                else:
                    Inimigo['Energia'] -= 3
                    imprimir(f"Você não teve sorte e o ataque pegou em cheio. Você tem {Jogador['Energia']} de vida.")
            else:
                Jogador['Energia'] -= 2
                imprimir(f"Você sentiu a dor de seu ataque. Você tem {Jogador['Energia']} de vida.")
            if nome == "Homem-Aranha":
                return True
        else:
            imprimir("Seus ataques se encontram e ninguém se fere.")
        cont += 1
        if Inimigo['Energia'] <= 0:
            imprimir("Você venceu a luta.")
            esc = True
            break
        elif Jogador['Energia'] <= 0:
            imprimir("Você foi morto.")
            esc = False
            break
        else:
            sleep(3)

def testarSorte():
    """
    -> testarSorte aleatoriza valores e compara com a estatística Sorte do Jogador.
    :return: Retorna um valor booleano.
    """
    Sorte = randint(1, 6) + randint(1, 6)
    if Sorte <= Jogador['Sorte']:
        Jogador['Sorte'] -= 1
        return True
    else:
        Jogador['Sorte'] -= 1
        return False

def magia():
    global Magia
    P_Magia = randint(1, 6) + randint(1, 6) + 6
    print("ENCANTOS".center(TAM))
    print()
    linha = "1 Cópia de Criatura          |  7 Sorte"
    print(f"{linha:44}".center(TAM))
    linha = "2 Percepção Extra-Sensorial  |  8 Escudo"
    print(f"{linha:44}".center(TAM))
    linha = "3 Fogo                       |  9 Habilidade"
    print(f"{linha:44}".center(TAM))
    linha = "4 Ouro dos Tolos             | 10 Energia"
    print(f"{linha:44}".center(TAM))
    linha = "5 Ilusão                     | 11 Força"
    print(f"{linha:44}".center(TAM))
    linha = "6 Levitação                  | 12 Fraqueza"
    print(f"{linha:44}".center(TAM))
    print()
    imprimir("Se quiser saber os efeitos de cada magia digite Magias.\nVocê pode escolher {P_Magia} magias.")
    Magia = {'Cópia de Criatura': 0, 'Percepção Extra-Sensorial': 0, 'Fogo': 0, 'Ouro dos Tolos': 0, 'Ilusão': 0, 'Levitação': 0, 'Sorte': 0, 'Escudo': 0, 'Habilidade': 0, 'Energia': 0, 'Força': 0, 'Fraqueza': 0}
    c = 0
    while c < P_Magia:
        #esc_magia = input("    Escolha um número de magia (Você pode escolher cada magia mais de uma vez): ")
        esc_magia = randint(1, 12)
        try:
            esc_magia = int(esc_magia)
        except:
            esc_magia = str(esc_magia).strip().upper()
        if esc_magia == 1:
            Magia['Cópia de Criatura'] += 1
            imprimir(f"Você possui {Magia['Cópia de Criatura']} usos de Cópia de Criatura")
            c += 1
        elif esc_magia == 2:
            Magia['Percepção Extra-Sensorial'] += 1
            imprimir(f"Você possui {Magia['Percepção Extra-Sensorial']} usos de Percepção Extra-Sensorial")
            c += 1
        elif esc_magia == 3:
            Magia['Fogo'] += 1
            imprimir(f"Você possui {Magia['Fogo']} usos de Fogo")
            c += 1
        elif esc_magia == 4:
            Magia['Ouro dos Tolos'] += 1
            imprimir(f"Você possui {Magia['Ouro dos Tolos']} usos de Ouro dos Tolos")
            c += 1
        elif esc_magia == 5:
            Magia['Ilusão'] += 1
            imprimir(f"Você possui {Magia['Ilusão']} usos de Ilusão")
            c += 1
        elif esc_magia == 6:
            Magia['Levitação'] += 1
            imprimir(f"Você possui {Magia['Levitação']} usos de Levitação")
            c += 1
        elif esc_magia == 7:
            Magia['Sorte'] += 1
            imprimir(f"Você possui {Magia['Sorte']} usos de Sorte")
            c += 1
        elif esc_magia == 8:
            Magia['Escudo'] +=1
            imprimir(f"Você possui {Magia['Escudo']} usos de Escudo")
            c += 1
        elif esc_magia == 9:
            Magia['Habilidade'] += 1
            imprimir(f"Você possui {Magia['Habilidade']} usos de Habilidade")
            c += 1
        elif esc_magia == 10:
            Magia['Energia'] += 1
            imprimir(f"Você possui {Magia['Energia']} usos de Energia")
            c += 1
        elif esc_magia == 11:
            Magia['Força'] += 1
            imprimir(f"Você possui {Magia['Força']} usos de Força")
            c += 1
        elif esc_magia == 12:
            Magia['Fraqueza'] += 1
            imprimir(f"Você possui {Magia['Fraqueza']} usos de Fraqueza")
            c += 1
        elif esc_magia == "MAGIAS":
            imprimir("""
Cópia de Criatura: Este encanto permitirá que você faça aparecer uma réplica perfeita de qualquer criatura contra a qual você esteja lutando. A réplica terá os mesmos índices de Habilidade e Energia e os mesmos poderes do Original. Mas a réplica estará sob seu controle, e você poderá, por exemplo, instruí-la para que ataque a criatura original e ficar assistindo a batalha de camarote!

Percepção Extra-Sensorial: Com este encanto, você poderá sintonizar comprimentos de ondas psíquicas. Isso poderá ajudá-lo a ler a mente de uma criatura ou descobrir o que está por trás de uma porta trancada. Porém, ás vezes, este encanto pode dar informações equivocadas, se houver mais de uma fonte psíquica perto de uma outra.

Fogo: Todas as criaturas têm medo do fogo, e este encanto dá o poder de fazer aparecer fogo segundo a sua vontade. Você poderá causar uma pequena explosão no chão que queimará por vários segundos ou criar um a barreira de fogo para manter criaturas à distância.

Ouro dos Tolos: Este encanto transformará pedra comum em uma pilha do que parece ser ouro. Contudo, o encanto é apenas uma forma de encanto da ilusão - embora mais confiável do que o Encanto da ilusão abaixo - e a pilha de ouro logo voltará a ser pedra.

Ilusão: Este é um encanto poderoso, mas que não é muito confiável. Através deste encanto, você poderá criar uma ilusão convincente (por exemplo, que você se transformou em serpente, ou que o chão está coberto de carvão em brasa) para enganar uma criatura. O encanto ficará imediatamente sem efeito se acontecer qualquer coisa que desfaça a ilusão (por exemplo, você convence uma criatura que se transformou em uma serpente e então imediatamente atinge sua cabeça com um golpe de espada!). É eficiente sobretudo com criaturas inteligentes.

Levitação: Você pode lançar este encanto sobre objetos, adversários ou até sobre você mesmo. Livra quem o recebe dos efeitos da gravidade e assim fará com que tudo que esteja sob a sua influência flutue livremente no ar, sob seu controle.

Sorte: Este encanto, juntamente com os encantos de Habilidade e Energia, é especial porque pode ser lançado a qualquer momento durante a sua aventura, a não ser durante uma batalha. Você não precisa esperar que apareça a opção em uma página. Uma vez lançado, recuperará o seu índice de Sorte em metade de seu índice de Sorte Inicial (se a sua Sorte inicial for um número ímpar, subtraia o meio de sobra). Este encanto nunca levará o seu índice de Sorte a um número superior a seu nível Inigial Portante, se você lançar dois encantos de Sorte juntos, o seu índice de Sorte voltará apenas a ser igual a seu nível Inicial.

Escudo: Ao lançar este encanto, você cria um escudo invisível à sua frente que o protegerá de objetos físicos, por exemplo flechas, espadas ou criaturas. O escudo não tem efeito contra a magia e, evidentemente, se nada fora dele pode tocar em você, você também não poderá tocar em nada fora dele.

Habilidade: Este encanto restabelecerá o seu índice de Habilidade, aumentando-o em metade de seu valor Inicial, e pode ser lançado a qualquer momento durante a sua aventura, a não ser em uma batalha. Para conhecer todas as regras, veja o Encanto da Sorte acima. O Encanto da Habilidade funciona exatamente da mesma maneira.

Energia: Este encanto recuperará o seu índice de Energia, aumentando-o em metade de seu valor Inicial, e pode ser lançado a qualquer momento durante a sua aventura. Veja o Encanto da Sorte para conhecer as regras completas.

Força: Este encanto tem o efeito de aumentar muito a sua força, e é muito útil quando se luta contra criaturas fortes. Porém, deve ser utilizado com cautela, já que é difícil controlar a sua própria força quando ela aumenta demais!

Fraqueza: Criaturas fortes são reduzidas por este encanto a miseráveis fracotes. Não tem efeito contra todas as criaturas, mas, quando tem efeito, a criatura se torna frágil e muito menos perigosa em uma batalha.
""")
        else:
            erro()

def listaMagias():
    print("Você possui:".center(TAM))
    linha = f"{Magia['Cópia de Criatura']:2} Cópia de Criatura          | {Magia['Sorte']:2} Sorte"
    print(f'{linha:45}'.center(TAM))
    linha = f"{Magia['Percepção Extra-Sensorial']:2} Percepção Extra-Sensorial  | {Magia['Escudo']:2} Escudo"
    print(f'{linha:45}'.center(TAM))
    linha = f"{Magia['Fogo']:2} Fogo                       | {Magia['Habilidade']:2} Habilidade"
    print(f'{linha:45}'.center(TAM))
    linha = f"{Magia['Ouro dos Tolos']:2} Ouro dos Tolos             | {Magia['Energia']:2} Energia"
    print(f'{linha:45}'.center(TAM))
    linha = f"{Magia['Ilusão']:2} Ilusão                     | {Magia['Força']:2} Força"
    print(f'{linha:45}'.center(TAM))
    linha = f"{Magia['Levitação']:2} Levitação                  | {Magia['Fraqueza']:2} Fraqueza"
    print(f'{linha:45}'.center(TAM))
    print()

def testarMagia(teste):
    if Magia[teste] > 0:
        return True
    else:
        return False

def conferirMagia(* teste):
    for item in teste:
        if testarMagia(item):
            imprimir(f"Usar Encanto de {item}. [{item}]")

def gastarMagia(magia):
    Magia[magia] -= 1

def magiaHabilidade():
    global T_HABILIDADE
    if T_HABILIDADE > Jogador['Habilidade'] + floor(T_HABILIDADE/2):
        Jogador['Habilidade'] += floor(T_HABILIDADE/2)
    else:
        Jogador['Habilidade'] = T_HABILIDADE

def magiaSorte():
    global T_SORTE
    if T_SORTE > Jogador['Sorte'] + floor(T_SORTE/2):
        Jogador['Sorte'] += floor(T_SORTE/2)
    else:
        Jogador['Sorte'] = T_SORTE

def magiaEnergia():
    global T_ENERGIA
    if T_ENERGIA > Jogador['Energia'] + floor(T_ENERGIA/2):
        Jogador['Energia'] += floor(T_ENERGIA/2)
    else:
        Jogador['Energia'] = T_ENERGIA

def equipamento(equip):
    Equipamentos.append(equip)

def testarEquipamento(teste):
    if teste in Equipamentos:
        return True
    else:
        return False

def conferirEquipamento(* teste):
    for item in teste:
        if testarEquipamento(item):
            imprimir(f"Dar {item}. [{item}]")

def gastarEquipamento(item):
    Equipamentos.remove(item)
