from sistemas import *

global esc


def caminho(esc):
    if esc == "prologo":
        print("A CIDADELA DO CAOS".center(TAM))
        imprimir("""
Nas profundezas da cidadela do Caos, o terrível feiticeiro Balthus Dire, está conspirando e planejando a derrocada do povo generoso do Vale dos Salgueiros. Seus planos de combate estão prontos, seu exército assustador equipado, e o ataque é indiscutivelmente iminente.

Convocado por uma súplica desesperada de ajuda, VOCÊ é a única esperança do Vale dos Salgueiros. Aluno brilhante do Grande Mago de Yore e um mestre da magia, só você pode empreender uma missão que atinja o próprio coração do mundo de pesadelo de Balthus Dire. Que criaturas monstruosas esperam por você lá?
""")
        esc = "jogador"

    elif esc == "jogador":
        magia()
        separador()
        Jogador = status()
        Jogador['Nome'] = str(input("Diga seu nome: ")).strip().lower().capitalize()
        print(f"Esse é o seu personagem:".center(TAM))
        print()
        print(f"Nome: {Jogador['Nome']}".center(TAM))
        print("Habilidade  |  Energia  |  Sorte".center(TAM))
        print(f"    {Jogador['Habilidade']:2}       |    {Jogador['Energia']:2}     |   {Jogador['Sorte']:2}   ".center(
            TAM))
        print()
        listaMagias()
        esc = "intro"
        segurador()

    elif esc == "intro":
        print("HISTÓRIA".center(TAM))
        imprimir("""
O ordeiro e generoso povo do Vale dos Salgueiros vive há oito anos sob o terror e medo do feiticeiro Balthus Dire. Teror - porque o poder dele é realmente a terrorizante - e medo causados pela notícia que acabou chegando aos ouvidos desse povo, vinda dos domínios do feiticeiro, de que seus ambiciosos planos de conquista começariam pelo próprio Vale.

Um fiel Semi-Elfo enviado em uma missão de espionagem à Torre Negra voltou galopando para o Vale há três dias com uma mensagem desesperada. Do interior das cavernas de Rocha Escarpada, Balthus Dire tinha recrutado um exército de Caóticos e se preparava para atacar com eles o Vale dentro de uma semana.

O bom Rei Salamon era um homem de ação. Foram enviados mensageiros por todo o Vale no mesmo dia para preparar as defesas e convocar os homens para a guerra. Foram enviados também cavaleiros à Grande Floresta de Yore para avisar aos Semi-Elfos que moravam lá e fazer um apelo para que se aliassem às forças. O Rei Salamon era também um homem sábio. Ele sabia muito bem que as notícias inevitavelmente chegariam aos ouvidos do Grande Mago de Yore, um mestre da magia branca de grandes poderes, que vivia nas profundezas da floresta. O mago era velho e não resistiria a uma batalha destas proporções. Mas ele havia ensinado suas artes a vários jovens magos, ee talvez um de seus discípulos de magia ajudasse o rei e seus súditos com coragem e ambição.

Você é o aluno brilhante do Grande Mago de Yore. Ele tem sido um Mestre duro, e sua própria impaciência muitas vezes foi mais forte do que você. Talvez um pouco precipitadamente você partiu de imediato para a corte de Salamon. O rei recebeu-o entusiasticamente e explicou seu plano. A batalha poderia ser evitada sem derramamento de sangue se Balthus fosse assassinado antes que seu exército pudesse ser reunido.

A missão que você tem pela frente é extremamente perigosa. Balthus Dire está cercado, em sua Cidadela, por uma multidão de criaturas assombrosas. Embora a Magia seja a sua arma mais forte, haverá momentos em que você terá que confiar em sua espada para sobreviver.

O Rei Salamon expôs a você como seria a sua missão e o advertiu dos que estavam à sua frente. Há um caminho melhor para atravessar a Cidadela. Se você o descobrir, terá êxito com um mínimo de risco para a sua pessoa. Talvez você precise de várias viagens para descobrir o caminho mais fácil para atravessar a Cidadela.

Você deixa o Vale dos Salgueiros na longa caminhada para a Torre Negra. No sopé da colina de Rocha Escarpada, você pode ver sua silhueta contra o céu escuro...
""")
        esc = 1
        segurador()

    elif esc == 1:
        imprimir("""O sol de põe. Enquanto o crepúsculo se transforma em escuridão, você começa a subir a colina na direção da ameaçadora forma que se desenha contra o céu noturno. A Cidadela fica a menos de uma hora de escalada.

A uma certa distância de seus muros, você pára para descansar - um erro, uma vez que, dessa posição, ela parece um espectro medonho do qual não se pode escapar. Os cabelos no seu pescoço se arrepiam enquanto você a observa.

Mas você se envergonha de seus medos. Com inflexível decisão, você marcha adiante na direção do portão principal, onde você sabe que encontrar guardas à sua espera. Você considera suas opções. Já pensou em se apresentar como um especialista em plantas medicinais que veio tratar de um guarda com febre. Poderia também se dizer um comerciante ou artesão - talvez um carpinteiro. Poderia até mesmo ser um nômade que buscasse abrigo para a noite.

Enquanto você pondera as possibilidades, e as histórias que terá que contar aos guardas, acaba chegando à trilha principal que conduz aos portões. Duas lanternas brilham em cada um dos lados da porta levadiça.

Você ouve grunhidos abafados ao se aproximar, e vê duas criaturas de aparência absurda. Do lado esquerdo está uma criatura horrível, com a cabeça de um cachorro e o corpo de um gorila, flexionando seus braços fortíssimos. Do outro lado, encontra-se de fato o seu oposto, com a cabeça de um gorila no corpo de um cachorro grande. Este último guarda se aproxima nas suas quatro patas. Para a alguns metros de distância diante de você, ergue-se sobre as patas traseiras e dirige a palavra a você.
""")
        while True:
            imprimir("""O que você fará? 
Se apresentará como um especialista em plantas medicinais [Apresentar]
Dirá que é um comerciante [Comerciante]
Pedirá abrigo para pernoitar [Abrigo]""")
            esc = escolha()
            if esc == "APRESENTAR":
                esc = 261
                break
            elif esc == "COMERCIANTE":
                esc = 230
                break
            elif esc == "ABRIGO":
                esc = 20
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 2:
        imprimir("""Um pouco adiante na passagem há uma porta do lado direito. Esta porta está coberta por estranhos caracteres, em uma linguagem que você não compreende. Você tentará abrir a porta [Porta] ou continuará seguindo a passagem? [Passagem]
""")
        while True:
            esc = escolha()
            if esc == "PORTA":
                esc = 142
                break
            elif esc == "PASSAGEM":
                esc = 343
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 3:
        while True:
            imprimir("""Eles te encaram, suas opções são:""")
            conferirEquipamento('Miríade de Bolso', 'Aranha em um Vidro', 'Pequenas Amoras')
            imprimir(
                "Desembainhar a espada e lutar contra eles. [Lutar]\nSe dirigir para a porta mais distante. [Porta]")
            esc = escolha()
            if esc == "MIRÍADE DE BOLSO":
                if testarEquipamento("Miríade de Bolso"):
                    esc = 327
                    gastarEquipamento('Miríade de Bolso')
                    break
                else:
                    erro()
            elif esc == "ARANHA EM UM VIDRO":
                if testarEquipamento("Aranha em um Vidro"):
                    esc = 59
                    gastarEquipamento('Aranha em um Vidro')
                    break
                else:
                    erro()
            elif esc == "PEQUENAS AMORAS":
                if testarEquipamento("Pequenas Amoras"):
                    esc = 236
                    gastarEquipamento('Pequenas Amoras')
                    break
                else:
                    erro()
            elif esc == "LUTAR":
                esc = 286
                break
            elif esc == "PORTA":
                esc = 366
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 4:
        imprimir("""Você faz aparecer uma bola de fogo e a manda voando no rosto da criatura. Porém, fica assistindo desanimado ao vê-la ricochetear sem nenhum efeito!
""")
        while True:
            imprimir("    Você pode:")
            conferirMagia('Cópia de Criatura')
            imprimir("Desembainhar sua espada e lutar. [Lutar]")
            esc = escolha()
            if esc == "CÓPIA DE CRIATURA":
                if testarMagia('Cópia de Criatura'):
                    esc = 19
                    gastarMagia('Cópia de Criatura')
                    break
                else:
                    erro()
            elif esc == "LUTAR":
                esc = 303
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 5:
        imprimir("""Você experimenta a maçaneta da porta e ela gira, abrindo para um outro corredor. Logo adiante, a passagem vira para a direita e termina pouco depois em outra porta. Nesta porta há um letreiro que diz “Por Favor Toque a Campainha para Chamar o Mordomo”. Uma corda – evidentemente a campainha – pende ao lado da porta.
""")
        while True:
            imprimir("    Tocar a campanhainha. [Campainha]\n    Experimentar a maçaneta da porta. [Porta]")
            esc = escolha()
            if esc == "CAMPAINHA":
                esc = 40
                break
            elif esc == "PORTA":
                esc = 361
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 6:
        imprimir("    O caminho segue ao longo do rio por vários metros e depois volta a penetrara"
                 "na rocha. Você segue o caminho por algum tempo.")
        esc = 367
        segurador()

    elif esc == 7:
        imprimir("""    A porta está trancada. 
""")
        while True:
            if testarMagia('Força'):
                imprimir(
                    "Você pode lançar um Encanto da Força sobre você mesmo e tentar arrancar a porta das suas dobradiças.")
            imprimir("Você pode tentar pô-la abaixo, batendo nela com o ombro. [Ombrada]")
            esc = escolha()
            if esc == "OMBRADA":
                esc = 268
                break
            elif esc == "FORÇA":
                if testarMagia('Força'):
                    esc = 116
                    gastarMagia('Força')
                    break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 8:
        imprimir("""Ela observa espantada o aparecimento de uma réplica perfeita dela mesma entre vocês dois. Ela recua um pouco, e você orienta a sua criação para o ataque. Mas, quando elas se aproximam uma da outra, acontece uma coisa estranha. Elas parecem ser incapazes de chegar perto uma da outra, como duas extremidades giratórias, e sempre se separam bruscamente de um salto. Porém, sua própria cópia pelo menos forçou a criatura a se afastar de você para uma certa distância, permitindo que você corra para a entrada principal da Cidadela.
""")
        esc = 218
        segurador()

    elif esc == 9:
        imprimir("""Sob o seu Encanto da Ilusão, a multidão de espectadores olha você começar a jogar. Você observa umas duas rodadas e a tensão cresce. Você resolve que é melhor sair do aposento sem mais perda de tempo.
""")
        esc = 31
        segurador()

    elif esc == 10:
        imprimir("""Você tateia pela rocha e acaba por encontrar uma pequena alavanca. Ao puxar esta alavanca, a face da rocha esfarela um pouco e aparece uma pequena abertura. Você sobe por esta abertura e chega a uma passagem. Descendo a passagem para a esquerda, você vê uma porta e resolve investigar.
""")
        esc = 249
        segurador()

    elif esc == 11:
        while True:
            imprimir("Você pode usar:")
            conferirMagia('Ouro dos Tolos', 'Cópia de Criatura', 'Percepção Extra-Sensorial', 'Fraqueza')
            imprimir("Desembainhar a sua espada e lutar. [Lutar]")
            esc = escolha()
            if esc == "OURO DOS TOLOS":
                if testarMagia('Ouro dos Tolos'):
                    esc = 36
                    gastarMagia('Ouro dos Tolos')
                    break
                else:
                    erro()
            elif esc == "CÓPIA DE CRIATURA":
                if testarMagia('Cópia de Criatura'):
                    esc = 262
                    gastarMagia('Cópia de Criatura')
                    break
                else:
                    erro()
            elif esc == "PERCEPÇÃO EXTRA-SENSORIAL":
                if testarMagia('Percepção Extra-Sensorial'):
                    esc = 128
                    gastarMagia('Percepção Extra-Sensorial')
                    break
                else:
                    erro()
            elif esc == "FRAQUEZA":
                if testarMagia('Fraqueza'):
                    esc = 152
                    gastarMagia('Fraqueza')
                    break
                else:
                    erro()
            elif esc == "LUTAR":
                esc = 16
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 12:
        imprimir("""Ele fica parado diante de você, respirando pesadamente. O Encanto dele evidentemente foi bastante exaustivo. Você pode usar essa oportunidade para:
""")
        while True:
            imprimir("""Deslocar-se rapidamente para o armário das armas. [Armário]
Pular para debaixo da mesa. [Mesa]
Correr para a janela. [Janela]
""")
            esc = escolha()
            if esc == "ARMÁRIO":
                esc = 274
                break
            elif esc == "MESA":
                esc = 335
                break
            elif esc == "JANELA":
                esc = 78
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 14:
        imprimir("""A sombra do muro dificulta muito a visão. Uma pedra solta desliza, e você perde o equilíbrio, oscilando à beira do que você tem consciência de que deve ser um poço profundo.
""")
        if testarSorte():
            imprimir(
                "Mas você teve sorte e recuperou o equilíbrio, caimnhando em segurança. Você então dá a volta no poço e continua.")
            esc = 79
        else:
            imprimir("Você não deu sorte e caiu no poço.")
            esc = 100

    elif esc == 15:
        imprimir("""A adaga é realmente uma obra de arte e sem dúvida valia um bom preço. A lâmina é feita de metal brilhante, e o cabo é de um couro verde peculiar, com pedras incrustadas. Você lê uma inscrição que diz que esta é uma adaga de arremesso encantada que nunca erra. Em um combate futuro, você poderá usar esta adaga para arremessar em um adversário. Ela causará automaticamente a perda de dois pontos de energia sem necessidade de jogar dados para conhecer a força de ataque. Mas você só poderá usá-la mais uma vez. Você põe a adaga em seu cinturão e parte na direção da Cidadela.
""")
        equipamento('Adaga Encantada')
        esc = 245
        segurador()

    elif esc == 16:
        imprimir("    Batalhe!")
        fugiu = batalha("Gark", 7, 11, 4)
        if fugiu:
            esc = 99
        else:
            esc = 180

    elif esc == 17:
        imprimir("""Todo tipo de alimentos estranhos pode ser encontrado nos armários. Globos oculares, línguas, lagartixas, frascos de líquidos, ervas e frutos silvestres de diferentes formas e tamanhos. Uma garrafa em especial, contendo um líquido verde transparente, chama a sua atenção. Você não tem tempo para ler o rótulo no momento, por isso você a põe no bolso rapidamente, enquanto elas não estão olhando. Você lhes diz que a cozinha parece estar em ordem e sai pela porta do lado oposto da cozinha.
""")
        equipamento("Garrafa com Líquido Verde")
        esc = 93
        segurador()

    elif esc == 18:
        imprimir("""Ele aponta para uma seção logo acima do chão, que você examina. Finalmente, você escolhe um volume e senta para ler. Balthus Dire aparentemente é o terceiro de uma linhagem de Feiticeiros Senhores da Guerra que governa a Torre Negra e o Reino da Rocha Escarpada. Chegou ao poder depois da morte de seu pai, Craggen Dire, há alguns anos atrás. Os Dires são mestres de Magia Negra há gerações, mas sua força e poder duram somente no período noturno; a luz do sol é uma espécie de veneno para eles. Pouco tempo depois da morte de seu pai, Balthus Dire casou-se com Lady Lucretia, ela também uma Feiticeira de Magia Negra, e desde então eles vêm reinando juntos sobre o Reino da Rocha Escarpada. Ao terminar o livro, você repara que o bibliotecário está com a mão junto ao ouvido, aparentemente escutando alguma coisa. Ele dirige a você um olhar inquisitivo. Você pode procurar outro livro útil, que possa ajuda-lo na sua empreitada [Procurar] ou tentar sair da biblioteca pela porta atrás dele. [Sair]
""")
        while True:
            esc = escolha()
            if esc == "PROCURAR":
                esc = 84
                break
            elif esc == "SAIR":
                esc = 31
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 19:
        imprimir("""A escada geme quando você põe o pé nela. Você tenta subir o mais silenciosamente possível, mas a madeira velha range sob o seu peso. De repente, um dos degraus estala, como se acionasse um dispositivo de algum tipo. Para sua surpresa, todos os degraus viram para baixo! Você está agora de pé em uma rampa lisa e inclinadíssima! Por mais que você tente, não consegue manter o equilíbrio e acaba escorregando pela rampa, rolando de ponta cabeça.
""")
        while True:
            if not testarMagia('Levitação'):
                esc = 254
                break
            else:
                conferirMagia('Levitação')
                imprimir("Ou você irá cair? [Não usar]")
                esc = escolha()
                if esc == "LEVITAÇÃO":
                    gastarMagia('Levitação')
                    esc = 363
                    break
                elif esc == "NÃO USAR":
                    esc = 254
                    break

    elif esc == 20:
        imprimir("""O Macaco-Cachorro diz que não é permitido a ninguém entrar na Torre Negra depois que anoitece – você terá que procurar em outro lugar. Você pode se resignar a lutar. Ou pode pegar uma pedra e lançar um Encanto do Ouro dos Tolos sobre ela, oferecendo-a como uma pepita de ouro, para suborna-los, convencendo-os a deixar você entrar.
""")
        while True:
            conferirMagia('Ouro dos Tolos')
            imprimir("Desembainhar a espada e lutar. [Lutar]")
            esc = escolha()
            if esc == "OURO DOS TOLOS":
                if testarMagia('Ouro dos Tolos'):
                    gastarMagia('Ouro dos Tolos')
                    esc = 96
                    break
                else:
                    erro()
            elif esc == "LUTAR":
                esc = 288
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 21:
        imprimir("""“O que traz você a estas paragens?” ela pergunta. Você conta a ela sua história, evitando cuidadosamente revelar a sua verdadeira missão. Ela aconselha você a afastar-se desse lugar, caso conheça alguma magia. As criaturas que você encontrou até agora não se comparam com as que habitam o interior da Torre da Cidadela propriamente dita. Ela diz que você jamais encontrará o senhor sem conseguir primeiro o Velo e deseja sorte para você em sua missão e você segue adiante.
""")
        aumentarSorte(2)
        esc = 6
        segurador()

    elif esc == 22:
        imprimir("Você abre a porta e sai em um corredor longo e escuro.")
        esc = 188
        segurador()

    elif esc == 23:
        imprimir("""Você abre a porta e sai em uma passagem que continua direto para frente por algum tempo. Vira para a esquerda, depois para a direita, até que você chega a um arco à sua frente que dá para um grande aposento. Você caminha na direção do aposento e entra nele.
""")
        esc = 169
        segurador()

    elif esc == 24:
        imprimir("""Você prova o vinho e, enquanto está apreciando o seu sabor, ouve um ruído tilintante. Você se vira para olhar na direção de onde o ruído está vindo e fica horrorizado ao ver que as garrafas nas prateleiras estão se mexendo sozinhas. Uma garrafa voa do lugar onde está e se projeta na sua direção, errando por pouco a sua cabeça e se espatifando na parede atrás de você. Uma outra voa na sua direção, depois outra, até que você está recebendo uma chuva de garrafas vindas de todas as direções. Você toma consciência de que sua única defesa é usar o Encanto do Escudo.
""")
        if testarMagia('Escudo'):
            gastarMagia('Escudo')
            esc = 372
        else:
            esc = 219
        segurador()

    elif esc == 25:
        imprimir("""A porta abre, dando para um aposento grande e circular. Você coça a cabeça, intrigado. No centro do aposento, vê uma pequena “ilha”, cercada por um fosso largo, na qual está uma arca, trancada por ferrolhos metálicos. O fosso é largo demais para ser pulado e é muito fundo. Logo na entrada, há um pedaço de corda. Existe uma outra porta do outro lado do aposento, dando para fora dele.
Ignora a caixa e contorna o fosse até a outra porta? [Ignorar]Vá para 206
Lança um Encanto da Força e salta sobre o fosso? Vá para 133
Pega a corda e formula um plano? [Plano]Vá para 239
""")
        conferirMagia('Força')
        esc = escolha()
        while True:
            if esc == "IGNORAR":
                esc = 206
                break
            elif esc == "PLANO":
                esc = 239
                break
            elif esc == "FORÇA":
                if testarMagia('Força'):
                    esc = 133
                    gastarMagia('Força')
                    break
                else:
                    erro()
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 26:
        imprimir("""Você lançará:
""")
        if testarMagia('Fogo') or testarMagia('Fraqueza') or testarMagia('Cópia de Criatura'):
            while True:
                conferirMagia('Fogo', 'Fraqueza', 'Cópia de Criatura')
                esc = escolha()
                if esc == "FOGO":
                    if testarMagia('Fogo'):
                        esc = 87
                        gastarMagia('Fogo')
                        break
                    else:
                        erro()
                elif esc == "FRAQUEZA":
                    if testarMagia('Fraqueza'):
                        esc = 345
                        gastarMagia('Fraqueza')
                        break
                    else:
                        erro()
                elif esc == "CÓPIA DE CRIATURA":
                    if testarMagia('Cópia de Criatura'):
                        esc = 101
                        gastarMagia('Cópia de Criatura')
                        break
                    else:
                        erro()
                elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                    aumentarStatus(esc)
                else:
                    erro()
        else:
            esc = 304

    elif esc == 27:
        imprimir("""Quando você mostra as Peças de Ouro, as três criaturas interrompem seu caminho. Eles engasgam ao olhar para suas moedas. Uma mão invisível as agarra e coloca no chão. Elas olham para você, e uma voz pede mais. Você pega todas as suas Peças de Ouro e joga no centro do aposento. Uma voz soa, dizendo: “Bem, estranho, você é realmente bem-vindo na casa dos MIKS. Agradecemos o seu presente. Se está seguindo adiante, vá pela porta à sua frente, mas tome cuidado com os Ganjees. Desejamos sorte para você na sua jornada“. Você pode acrescentar um ponto de Sorte pelos votos de sucesso dos Miks e sair pela porta à sua frente.
""")
        aumentarSorte(1)
        esc = 206
        segurador()

    elif esc == 28:
        imprimir("""Você lança o Encanto e faz aparecer uma bola de fogo nas suas mãos. Eles interrompem seu caminho e observam você atentamente. Você joga a bola na direção deles, e eles gritam de medo, rolando aterrorizados para longe de você, com medo de seus óbvios poderes. Enquanto você ainda tem controle sobre o Encanto, cria mais três bolas de fogo menores e as arremessa sobre cada um deles. Eles uivam e se dispersam, rolando pelo corredor para longe de você. Você pode agora prosseguir pela passagem da esquerda [Esquerda] ou pela passagem da direita. [Direita]
""")
        while True:
            esc = escolha()
            if esc == "ESQUERDA":
                esc = 243
                break
            elif esc == "DIREITA":
                esc = 2
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 29:
        imprimir("""Cautelosamente, você se aproxima do homenzinho. Ao chegar perto, um único olho se abre e olha diretamente no seu rosto. Um sorriso largo se espalha de orelha a orelha na criatura e ela desaparece! “Bom dia para você!” diz uma vozinha chilreante atrás de você, e, ao voltar-se, você o vê ali, ainda sorrindo. “Sou O’Seamus, o Duende!”, ele diz, dando risinhos, e estende a mão para você. Ele parece suficientemente amigável – você aperta a mão dele e tenta fazer amizade [Amizade] ou desembainha sua espada? [Lutar]
""")
        while True:
            esc = escolha()
            if esc == "AMIZADE":
                esc = 271
                break
            elif esc == "LUTAR":
                esc = 131
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 30:
        imprimir("""A fera é imensamente poderosa. Você desembainha a sua espada e a batalha começa:
""")
        batalha('Fera das Garras', 9, 14)
        esc = 241
        segurador()

    elif esc == 31:
        imprimir("""Você sai do aposento pela porta do outro lado, a qual abre para uma passagem curta que termina em uma grande porta de madeira. A maçaneta desta porta gira, deixando que você entre em uma grande câmara.
""")
        esc = 169
        segurador()

    elif esc == 32:
        imprimir("""Passando por sobre os corpos, você se aproxima do portão e chama o porteiro, para em seguida se esconder na escuridão quando ele se aproxima. Ele vê os corpos e sai para investigar, e, enquanto isso, você aproveita para esgueirar-se rapidamente pelo portão e trancá-lo do lado de fora.
""")
        esc = 251
        segurador()

    elif esc == 33:
        imprimir("""Quando você tenta se levantar, o Orca e o Goblin agarram você e o seguram no chão, enquanto o Anão avança com sua clara.
""")
        esc = 213
        segurador()

    elif esc == 34:
        imprimir("""A chave gira e, retirando a tranca, você abre a caixa, encontrando outra chave, dessa vez talhada em um metal verde cintilante. Você experimentará esta nova chave de terceira caixa [Caixa] ou sairá do aposento com as duas chaves? [Sair]
""")
        while True:
            esc = escolha()
            if esc == "CAIXA":
                esc = 89
                break
            elif esc == "SAIR":
                esc = 237
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 35:
        imprimir("""Você se concentra na sua Ilusão. Você pode convencê-lo de que ele está sendo atacado por um inimigo [Ataque] (vá para 364), ou fazer com que você desapareça, na esperança de que ele virá procurar por você [Desaparecer] (vá para 246).
""")
        while True:
            esc = escolha()
            if esc == "ATAQUE":
                esc = 364
                break
            elif esc == "DESAPARECER":
                esc = 246
                break
            elif esc == "HABILIDADE" or esc == "SORTE" or esc == "ENERGIA":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 36:
        imprimir("""“Bah!”, diz o Gark, “não é tão fácil me enganar. Jogue fora estes pedaços de latão’. A criatura tem a ideia de que, se você está oferecendo um suborno deve ser um invasor, o que – para um Gark – é uma demonstração assombrosa de raciocínio lógico! Ele dá um tapa em você com sua mão enorme, jogando você sem sentidos no chão. As últimas palavras que você se lembra antes de desmaiar são ditas pelo Gark orgulhoso: “Para a cadeia com esse aqui!”.
""")
        esc = 234
        segurador()

    elif esc == 37:
        imprimir("""Você puxa a pele e a criatura solta silvos altos. Todas as suas cabeças recuam e ela permanece quieta, observando você. Há uma porta do outro lado do aposento, e você lentamente se desloca na direção dela. Quando você está na metade do caminho, uma das cabeças se projeta e arranca o velo das suas mãos. Mas, ao invés de atacar você, a Hidra se encolhe de volta em um dos cantos. Você segue para a porta cautelosamente.
""")
        esc = 229
        segurador()

    elif esc == 38:
        imprimir("""A porta abre para uma passagem curta, calçada com pedras pequenas. A uma pequena distância mais adiante, uma porta elaboradamente entalhada assinala o fim da passagem. Mas, logo antes da porta, uma passagem lateral sai para a esquerda. Você se aproximada da porta, tentando escutar quaisquer sinais de vida do lado de dentro. Quando sua mão toca a maçaneta, uma voz diz: “Não bata; simplesmente entre!” vinda de dentro. Você entrará no aposento, conforme as instruções [Entrar] ou resolverá desistir desse aposento e tomar a passagem que sai para a esquerda? [Desistir]
""")
        while True:
            esc = escolha()
            if esc == "ENTRAR":
                esc = 132
                break
            elif esc == "DESISTIR":
                esc = 306
                break
            elif esc == "HABILIDADE" or esc == "ENERGIA" or esc == "SORTE":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 39:
        imprimir("""Você pega o Vidro e, ao fazer isso, os Ganjees ficam ofegantes. “Racknee!” diz uma voz. “Você voltou!” E com estas palavras uma mão invisível arranca o vidro das suas mãos, coloca-o no chão e abre a tampa. O Homem-Aranha volta-se na sua direção e solta um pequeno grunhido. Você desembainha a sua espada quando a fera avança a passos rápidos para você, furiosamente. Você terá que lutar contra esta criatura:
""")
        acerto = batalha("Homem-Aranha", 7, 5)
        if acerto:
            esc = 208
        else:
            esc = 248

    elif esc == 40:
        imprimir("""Depois de vários minutos, a porta se abre lentamente, e uma criatura corcunda e deformada, com dentes podres, cabelos desgrenhados e roupas esfarrapadas, aparece na sua frente. “Sim senhor (heh, heh) – o que posso fazer pelo senhor?” rosna a criatura semi-humana. “Estou sendo esperado”, você responde e passa por ele, atravessando a porta com confiança. Ele fica um pouco surpreso com seu comportamento e gagueja, sem saber se entra em conflito com você ou não. “Onde é a recepção?” você pergunta. Ele olha para você de soslaio com um dos olhos e faz um gesto na direção de uma bifurcação para a esquerda, a pouca distância dali. Você acreditará nele e tomará a bifurcação para a esquerda [Esquerda] ou não confiará nesta criatura imprevisível e tomará a bifurcação da direita? [Direita]
""")
        while True:
            esc = escolha()
            if esc == "ESQUERDA":
                esc = 243
                break
            elif esc == "DIREITA":
                esc = 2
                break
            elif esc == "HABILIDADE" or esc == "ENERGIA" or esc == "SORTE":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 41:
        imprimir("""As três mulheres se juntam, fazendo um círculo, e sussurram umas com as outras. Com um risinho, uma delas volta-separa você e diz: “Está bem, estranho, nós vamos ajudá-lo no seu caminho”. Ela fita você com olhos frios de pedra e aponta primeiro para você, e depois parede atrás dela. O aposento fica escuro, você sente uma sensação de movimento e, quando a escuridão clareia, você está em outro aposento.
""")
        esc = 257
        segurador()

    elif esc == 42:
        imprimir("""Ela pisca, e os jatos de fogo desaparecem. Você pode:
""")
        while True:
            imprimir("""Dar uma desculpa, dizendo que perdeu o presente, e voltar para a sacada, onde pode escolher a porta do meio [Meio] ou a porta mais distante. [Distante]
""")
            conferirEquipamento('Espelho de Prata', 'Escova de Cabelo', 'Vidro contendo o Homem=Aranha')
            esc = escolha()
            if esc == "ESPELHO DE PRATA":
                if testarEquipamento('Espelho de Prata'):
                    gastarEquipamento('Espelho de Prata')
                    esc = 138
                    break
                else:
                    erro()
            elif esc == "ESCOVA DE CABELO":
                if testarEquipamento('Escova de Cabelo'):
                    gastarEquipamento('Escova de Cabelo')
                    esc = 91
                    break
                else:
                    erro()
            elif esc == "VIDRO CONTENDO O HOMEM-ARANHA":
                if testarEquipamento('Vidro contendo o Homem-Aranha'):
                    gastarEquipamento('Vidro contendo o Homem-Aranha')
                    esc = 223
                    break
                else:
                    erro()
            elif esc == "MEIO":
                esc = 64
                break
            elif esc == "DISTANTE":
                esc = 304
                break
            elif esc == "HABILIDADE" or esc == "ENERGIA" or esc == "SORTE":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 43:
        imprimir("""Quando você lança o encanto, ele afrouxa o aperto. Gradualmente, sua força diminui, até que ele acaba por soltar o aperto e cai para trás, ofegante, no chão. Você se sente fraco enquanto seu braço pinga sangue. Você prossegue no seu caminho.
""")
        esc = 14
        segurador()

    elif esc == 44:
        imprimir("""O aposento para de sacudir e você cai no chão. O armário das armas está trancado, mas você pode arrebentar a fechadura. Ou pode tirar a sua mochila e procurar uma arma para usar. O que você fará:
""")
        while True:
            imprimir("""Escolher uma arma do armário? [Arma]
Pegar um artefato na mochila? [Artefato]
""")
            esc = escolha()
            if esc == "ARMA":
                esc = 353
                break
            elif esc == "ARTEFATO":
                esc = 277
                break
            elif esc == "HABILIDADE" or esc == "ENERGIA" or esc == "SORTE":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 45:
        imprimir("""Se seu estômago aguentar, você poderá experimentar:
""")
        while True:
            imprimir("""Um pouco da carne pendurada. [Carne]
Um pedaço de fruta. [Fruta]
Uma fatia de queijo. [Queijo]
Um naco de pão. [Pão]
""")
            escolha()
            if esc == "CARNE":
                esc = 166
                break
            elif esc == "FRUTA":
                esc = 313
                break
            elif esc == "QUEIJO":
                esc = 253
                break
            elif esc == "PÃO":
                esc = 97
                break
            elif esc == "HABILIDADE" or esc == "ENERGIA" or esc == "SORTE":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 46:
        imprimir("""Com um gesto, você estica a mão para frente aponta o chão sob os pés do feiticeiro. Fumaça e chamas irrompem do chão. Balthus Dire salta para trás, um pouco admirado, e em seguida fecha os olhos para se concentrar. Ao se abrirem, você vê um fogo que queima dentro das próprias pupilas, e ele avança por entre as chamas que você criou. Pegando um punhado de pedras em brasa, ele atira isso em você. Você se abaixa para se desviar [Abaixar] ou pula para o lado? [Pular]
""")
        while True:
            esc = escolha()
            if esc == "ABAIXAR":
                esc = 195
                break
            elif esc == "PULAR":
                esc = 74
                break
            elif esc == "HABILIDADE" or esc == "ENERGIA" or esc == "SORTE":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 47:
        while True:
            if testarMagia('Cópia de Criatura') or testarMagia('Ilusão') or testarMagia('Levitação'):
                imprimir("""Que encanto você usará:
""")
                conferirMagia('Cópia de Criatura', 'Ilusão', 'Levitação')
                esc = escolha()
                if esc == 'CÓPIA DE CRIATURA':
                    if testarMagia('Cópia de Criatura'):
                        gastarMagia('Cópia de Criatura')
                        esc = 8
                        break
                    else:
                        erro()
                elif esc == 'ILUSÃO':
                    if testarMagia('Ilusão'):
                        gastarMagia('Ilusão')
                        esc = 173
                        break
                    else:
                        erro()
                elif esc == 'LEVITAÇÃO':
                    if testarMagia('Levitação'):
                        gastarMagia('Levitação')
                        esc = 259
                        break
                    else:
                        erro()
                elif esc == 'HABILIDADE' or esc == 'ENERGIA' or esc == 'SORTE':
                    aumentarStatus(esc)
                else:
                    erro()
            else:
                imprimir("""Você recua em direção ao monumento no centro do pátio e se enconde dela.""")
                esc = 209
                segurador()
                break

    elif esc == 48:
        imprimir(
            """“Nunca!” grita o feiticeiro, voltando das sombras para enfrentar você. Dessa vez, é você quem sente o tremor do medo, ao ver que ele também se transformou – mas em uma criatura que poderia fazer com que um Demônio do Fogo ficasse paralisado. O rosto de Balthus Dire tornou-se feio e com feições de bruxa, e seus cabelos agora são pequenas serpentes que se contorcem e soltam silvos. Você fugirá desta criatura [Fugir] ou avançará com seu Tridente? [Lutar]""")
        while True:
            esc = escolha()
            if esc == "FUGIR":
                esc = 232
                break
            elif esc == "LUTAR":
                esc = 199
                break
            elif esc == "HABILIDADE" or esc == "ENERGIA" or esc == "SORTE":
                aumentarStatus(esc)
            else:
                erro()

    elif esc == 49:
        imprimir(
            """A criatura fica olhando fixamente para você com ar inquisitivo, como se estivesse insegura em relação a você.""")
        esc = 255
        segurador()

    elif esc == 50:
        esc = 164

    elif esc == 51:
        imprimir(
            """Você distribui loucamente golpes com sua espada, mas não consegue atingir a criatura. Ou ela é extremamente rápida, ou não possui um corpo sólido que possa ser atingido. Seus dentes estão agora rasgando a sua carne, e você sente sangue na perna. Você terá que se proteger com sua mágica ou enfrentar uma morte certa, trazida por esta criatura que não se vê.""")
        if testarMagia('Força') or testarMagia('Fraqueza'):
            while True:
                conferirMagia('Força', 'Fraqueza')
                imprimir("Não fazer nada. [Nada]")
                esc = escolha()
                if esc == 'FORÇA':
                    if testarMagia('Força'):
                        gastarMagia('Força')
                        esc = 301
                        break
                    else:
                        erro()
                elif esc == 'FRAQUEZA':
                    if testarMagia('Fraqueza'):
                        gastarMagia('Fraqueza')
                        esc = 159
                        break
                    else:
                        erro()
                elif esc == 'NADA':
                    esc = 280
                    break
                elif esc == "HABILIDADE" or esc == "ENERGIA" or esc == "SORTE":
                    aumentarStatus(esc)
                else:
                    erro()
        else:
            esc = 280

    elif esc == 288:
        batalha("Gorila-Cachorro", 7, 4)
        batalha("Cachorro-Gorila", 6, 6)
        esc = 32

    else:
        imprimir("Capítulo não concluído.")
        esc = False
    return esc
