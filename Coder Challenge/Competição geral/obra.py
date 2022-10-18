"""2 – Outra grande dificuldade relatada está em estimar o tempo de duração de uma obra. Por instinto (e fazendo uso de sua longa experiência), ele tem as seguintes informações:
• Quanto maior a metragem da obra, mais tempo ela leva para ser finalizada. Em sua última entrega, trabalhando com um pedreiro e dois serventes, uma obra de 150 m² levou 8 meses para ser entregue;
• A chuva é um fator que influencia muito o tempo de entrega, principalmente em obras que têm início em meses com maior incidência de chuva, pois sempre existe uma demora maior até a fase da cobertura da laje;
• Obras assobradadas levam em torno de 30% a mais de tempo e 20% a mais de material do que obras térreas.

3 – Com o aumento da empresa, Duck percebeu que sua margem de lucro tem sido cada vez menor. Ele gostaria de retomar os 40% de lucro que obtinha na época que trabalhava em apenas uma obra.
• Atualmente os pedreiros recebem R$ 190,00 a diária, enquanto os serventes recebem R$ 95,00. Seu funcionário administrativo recebe dois salários mínimos por mês;
• Além dos custos com os seus funcionários, existe ainda o custo adicional de 10% a 15% com outros prestadores de serviços, como: pintor, eletricista, encanador, gesseiro, etc."""
from colorama import Fore, Style
import math, main, pyodbc, pandas

custo = 866.89  # Dado apurado pelo INCI em agosto de 2021 (https://agenciadenoticias.ibge.gov.br/agencia-noticia/2012-agencia-de-noticias/noticias/31585-custos-da-construcao-desaceleram-para-0-99-em-agosto)
global cursor


def menu():
    """
    Menu de navegação.
    """
    global cursor
    titulo = "Controle de serviços"
    cursor = main.conexao()
    while True:
        main.cabecalho(titulo)
        print()
        print("1 - Registrar obra\n2 - Consultar obras\n3 - Atualizar obra\n4 - Apagar obra\n0 - Voltar ao menu principal\n")
        while True:
            atividade = input("O que deseja fazer? ")
            if atividade.isnumeric() and 0 <= int(atividade) < 5:
                atividade = int(atividade)
                break
            else:
                print("\033[1;31mInsira um número.\033[0;0m")
        print()
        main.limpaTela()
        if atividade == 1:
            registraObra()
        elif atividade == 2:
            consultaObras()
        elif atividade == 3:
            atualizaObra()
        elif atividade == 4:
            apagaObra()
        elif atividade == 0:
            break

def registraObra():
    """
    Esse método coleta informações inseridas pelo usuário, envia para o método calculoDeObra e então injeta os valores no SQL..
    """
    titulo = "Registro de obra"
    while True:
        while True:
            main.cabecalho(titulo)
            while True:
                cliente = input("Nome do cliente: ").strip()
                if cliente != "":
                    break
                else:
                    print(f"{Fore.RED}Insira um nome.{Style.RESET_ALL}")
            while True:
                cpf = input("CPF/CNPJ do cliente: ").strip()
                if cpf != "":
                    break
                else:
                    print(f"{Fore.RED}Insira um CPF/CNPJ.{Style.RESET_ALL}")
            while True:
                local = input("Endereço da obra: ").strip()
                if local != "":
                    break
                else:
                    print(f"{Fore.RED}Insira um endereço válido.{Style.RESET_ALL}")
            while True:
                metragem = input("Metros quadrados: ")
                try:
                    metragem = float(metragem)
                    break
                except:
                    print(f"{Fore.RED}Precisa ser um número{Style.RESET_ALL}")
            while True:
                pedreiros = input("Número de pedreiros: ")
                if pedreiros.isnumeric():
                    break
                else:
                    print(f"{Fore.RED}Precisa ser um número válido.{Style.RESET_ALL}")
            while True:
                serventes = input("Número de serventes: ")
                if serventes.isnumeric():
                    break
                else:
                    print(f"{Fore.RED}Precisa ser um número válido.{Style.RESET_ALL}")
            while True:
                chuva = input("A obra inicia num mês chuvoso? [S/N] ").strip().upper()
                if chuva[0] in "SN":
                    break
                else:
                    print(f"{Fore.RED}Por favor insira uma resposta válida.{Style.RESET_ALL}")
            while True:
                assobrado = input("Obra assobrada? [S/N] ").strip().upper()
                if assobrado[0] in "SN":
                    break
                else:
                    print(f"{Fore.RED}Por favor insira uma resposta válida.{Style.RESET_ALL}")
            tempoTotal, meses, dias, custoTotal, lucro, valor = calculoDeObra(metragem, pedreiros, serventes, chuva, assobrado)
            try:
                cursor.execute(f"""
                    INSERT INTO DuckSystems.dbo.ControleDeObras (Cliente, [CPF/CNPJ], Local, Metragem, Pedreiros, Serventes, Chuva, Assobrado, [Tempo em Dias], [Tempo em Mes], Custo, Lucro, [Valor Total])
                    VALUES ('{cliente}', '{cpf}', '{local}', {metragem}, {int(pedreiros)}, {int(serventes)}, '{chuva[0]}', '{assobrado[0]}', {tempoTotal}, '{f'{meses} meses e {dias} dias'}', '{custoTotal}', '{lucro}', '{valor}');
                    """)
                cursor.commit()
            except pyodbc.IntegrityError:
                print(f"{Fore.RED}Valores repetidos não são permitidos em CPF.{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}O registro foi inserido com sucesso.{Style.RESET_ALL}")
                break
        print(f"A obra será concluída em {meses} meses e {dias} dias.\nO custo total da obra será de {custoTotal} e para ter um lucro de {lucro} a obra ficará no valor de {valor}.")
        while True:
            encerrar = input("Quer cadastrar uma nova obra? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um valor válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()


def calculoDeObra(metragem, pedreiros, serventes, chuva, assobrado):
    """
    Processa os valores recebidos
    :return: Retorna os valores relativos ao tempo para concluir a obra e o custo, lucro e valor total, todos convertidos para moeda brasileira.
    """
    funcionarios = int(pedreiros) + int(serventes)
    tempoTotal = math.ceil(float(metragem) / ((6.25 / 30) * int(funcionarios)))
    custoTotal = custo * float(metragem)
    if chuva == "S":
        tempoTotal += tempoTotal * 0.1
    if assobrado == "S":
        tempoTotal += tempoTotal * 0.3
        custoTotal += custoTotal * 0.2
    custoServentes = tempoTotal * 95
    custoPedreiros = tempoTotal * 190
    custoAdministrativo = 80.8 * math.ceil(tempoTotal)  # Levando em conta o dobro do valor do salário mínimo é possível calcular que o valor da diária do trabalho é de R$80,8
    custoTotal += custoAdministrativo + custoPedreiros + custoServentes + (custoTotal * .15)
    meses = math.floor(tempoTotal / 30)
    dias = math.ceil(tempoTotal % 30)
    tempoTotal = math.ceil(tempoTotal)
    lucro = custoTotal * 0.4
    valor = custoTotal + lucro
    custoTotal = f'R${custoTotal:_.2f}'.replace(".", ",").replace("_", ".")
    lucro = f'R${lucro:_.2f}'.replace(".", ",").replace("_", ".")
    valor = f'R${valor:_.2f}'.replace(".", ",").replace("_", ".")
    return tempoTotal, meses, dias, custoTotal, lucro, valor


def consultaObras():
    """
    Esse método faz uma consulta ao banco de dados e retorna os valores recuperados em uma tabela organizada por ordem alfabética de acordo com o nome do cliente.
    """
    titulo = "Consulta a obras"
    while True:
        Cliente = []
        CPF = []
        Local = []
        Metragem = []
        Pedreiros = []
        Serventes = []
        Chuva = []
        Assobrado = []
        TempoTotal = []
        TempoMes = []
        Custo = []
        Lucro = []
        ValorTotal = []
        main.cabecalho(titulo)
        print()
        print("1 - Completa\n2 - Busca por cliente\n")
        while True:
            atividade = input("O que deseja fazer? ")
            if atividade.isnumeric() and 0 < int(atividade) <= 2:
                atividade = int(atividade)
                break
            else:
                print(f"{Fore.RED}Insira um número válido.{Style.RESET_ALL}")
        print()
        if atividade == 1:
            main.limpaTela()
            consulta = """
            SELECT [Cliente]
                  ,[CPF/CNPJ]
                  ,[Local]
                  ,[Metragem]
                  ,[Pedreiros]
                  ,[Serventes]
                  ,[Chuva]
                  ,[Assobrado]
                  ,[Tempo em Dias]
                  ,[Tempo em Mes]
                  ,[Custo]
                  ,[Lucro]
                  ,[Valor Total]
              FROM [DuckSystems].[dbo].[ControleDeObras]
                ORDER BY Cliente;"""
        elif atividade == 2:
            cliente = input("Consulta cliente: ").strip()
            consulta = f"""
            SELECT [Cliente]
                  ,[CPF/CNPJ]
                  ,[Local]
                  ,[Metragem]
                  ,[Pedreiros]
                  ,[Serventes]
                  ,[Chuva]
                  ,[Assobrado]
                  ,[Tempo em Dias]
                  ,[Tempo em Mes]
                  ,[Custo]
                  ,[Lucro]
                  ,[Valor Total]
              FROM [DuckSystems].[dbo].[ControleDeObras]
                WHERE Cliente = '{cliente}'
                ORDER BY Cliente;"""
        cursor.execute(consulta)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            Cliente.append(tabela[x][0])
            CPF.append(tabela[x][1])
            Local.append(tabela[x][2])
            Metragem.append(tabela[x][3])
            Pedreiros.append(tabela[x][4])
            Serventes.append(tabela[x][5])
            Chuva.append(tabela[x][6])
            Assobrado.append(tabela[x][7])
            TempoTotal.append(tabela[x][8])
            TempoMes.append(tabela[x][9])
            Custo.append(tabela[x][10])
            Lucro.append(tabela[x][11])
            ValorTotal.append(tabela[x][12])
            x += 1
        chaves = {'Cliente': Cliente, 'CPF/CNPJ': CPF, 'Local': Local, 'Metragem': Metragem, 'Pedreiros': Pedreiros, 'Serventes': Serventes, 'Chuva': Chuva, 'Assobrado': Assobrado, 'Tempo em Dias': TempoTotal, 'Tempo em Mes': TempoMes, 'Custo de Obra': Custo, 'Lucro': Lucro, 'Valor Total': ValorTotal}
        chaves = pandas.DataFrame(chaves)
        pandas.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None, 'display.width', 10000)
        if chaves.empty:
            print("A consulta não retornou nenhum valor.")
        else:
            print(chaves)
        while True:
            encerrar = input("\nDeseja realizar uma nova consulta? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um comando válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()


def atualizaObra():
    """
    Esse método apresenta uma tabela com todas as obras e recebe as informações do usuário, alterando, no banco de dados, os valores relacionados ao ID oferecido pelo usuário. Caso os valores alterados impactem em custo, lucro e valor total o método envia todos os dados necessários para o calculoDeObra para fazer o devido processamento e atualizar esses valores também.
    """
    titulo = "Alterar dados de obras"
    while True:
        main.cabecalho(titulo)
        Cliente = []
        CPF = []
        Local = []
        Metragem = []
        Pedreiros = []
        Serventes = []
        Chuva = []
        Assobrado = []
        TempoTotal = []
        TempoMes = []
        Custo = []
        Lucro = []
        ValorTotal = []
        id_obra = []
        consulta = """
        SELECT [Cliente]
              ,[CPF/CNPJ]
              ,[Local]
              ,[Metragem]
              ,[Pedreiros]
              ,[Serventes]
              ,[Chuva]
              ,[Assobrado]
              ,[Tempo em Dias]
              ,[Tempo em Mes]
              ,[Custo]
              ,[Lucro]
              ,[Valor Total]
              ,[ID_Obra]
          FROM [DuckSystems].[dbo].[ControleDeObras]
            ORDER BY Cliente;"""
        cursor.execute(consulta)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            Cliente.append(tabela[x][0])
            CPF.append(tabela[x][1])
            Local.append(tabela[x][2])
            Metragem.append(tabela[x][3])
            Pedreiros.append(tabela[x][4])
            Serventes.append(tabela[x][5])
            Chuva.append(tabela[x][6])
            Assobrado.append(tabela[x][7])
            TempoTotal.append(tabela[x][8])
            TempoMes.append(tabela[x][9])
            Custo.append(tabela[x][10])
            Lucro.append(tabela[x][11])
            ValorTotal.append(tabela[x][12])
            id_obra.append(tabela[x][13])
            x += 1
        chaves = {'ID_Obra': id_obra, 'Cliente': Cliente, 'CPF/CNPJ': CPF, 'Local': Local, 'Metragem': Metragem, 'Pedreiros': Pedreiros, 'Serventes': Serventes, 'Chuva': Chuva, 'Assobrado': Assobrado}
        chaves = pandas.DataFrame(chaves)
        pandas.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None, 'display.width', 10000)
        if chaves.empty:
            print("A consulta não retornou nenhum valor.")
        else:
            print(chaves)
        while True:
            while True:
                alterDado = input("Dado a ser alterado: ").strip()
                alterValor = input("Valor a ser inserido: ").strip()
                while True:
                    try:
                        confirmacao = int(input("Confirme o ID da obra: ").strip())
                        break
                    except:
                        print(f"{Fore.RED}Insira um ID de obra válido.{Style.RESET_ALL}")
                if alterDado != "" and alterValor != "" and confirmacao in id_obra:
                    break
                else:
                    print(f"{Fore.RED}Preencha todas as informações corretamente.{Style.RESET_ALL}")
            if alterDado == "Metragem" or alterDado == "Pedreiros" or alterDado == "Serventes" or alterDado == "Chuva" or alterDado == "Assobrado":
                chave = id_obra.index(confirmacao)
                if alterDado == "Metragem":
                    metragem = alterValor
                    pedreiros = Pedreiros[chave]
                    serventes = Serventes[chave]
                    chuva = Chuva[chave]
                    assobrado = Assobrado[chave]
                elif alterDado == "Pedreiros":
                    metragem = Metragem[chave]
                    pedreiros = alterValor
                    serventes = Serventes[chave]
                    chuva = Chuva[chave]
                    assobrado = Assobrado[chave]
                elif alterDado == "Serventes":
                    metragem = Metragem[chave]
                    pedreiros = Pedreiros[chave]
                    serventes = alterValor
                    chuva = Chuva[chave]
                    assobrado = Assobrado[chave]
                elif alterDado == "Chuva":
                    metragem = Metragem[chave]
                    pedreiros = Pedreiros[chave]
                    serventes = Serventes[chave]
                    chuva = alterValor
                    assobrado = Assobrado[chave]
                elif alterDado == "Assobrado":
                    metragem = Metragem[chave]
                    pedreiros = Pedreiros[chave]
                    serventes = Serventes[chave]
                    chuva = Chuva[chave]
                    assobrado = alterValor.upper()
                tempoTotal, meses, dias, custoTotal, lucro, valor = calculoDeObra(metragem, pedreiros, serventes, chuva, assobrado)
                try:
                    cursor.execute(f"""
                    UPDATE dbo.ControleDeObras
                    SET [Metragem] = {metragem}, [Pedreiros] = {pedreiros}, [Serventes] = {serventes}, [Chuva] = '{chuva[0]}', [Assobrado] = '{assobrado}', [Tempo em Dias] = {tempoTotal}, [Tempo em Mes] = '{f'{meses} meses e {dias} dias'}', [Custo] = '{custoTotal}', [Lucro] = '{lucro}', [Valor Total] = '{valor}'
                    WHERE ID_Obra = {confirmacao};
                """)
                    cursor.commit()
                except pyodbc.ProgrammingError:
                    print(f"{Fore.RED}Insira dados válidos.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}Dados inseridos com sucesso.{Style.RESET_ALL}")
                    break
            else:
                try:
                    cursor.execute(f"""
                        UPDATE dbo.ControleDeObras
                        SET [{alterDado}] = '{alterValor}'
                        WHERE ID_Obra = '{confirmacao}';
                        """)
                    cursor.commit()
                except pyodbc.ProgrammingError:
                    print(f"{Fore.RED}Insira dados válidos.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}Dados inseridos com sucesso.{Style.RESET_ALL}")
                    break
        while True:
            encerrar = input("Deseja alterar outro dado? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um comando válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()


def apagaObra():
    """
    Esse método apresenta uma tabela com as obras registradas e apaga a relacionada ao ID oferecido pelo usuário.
    """
    while True:
        titulo = "Apagar registro"
        Cliente = []
        CPF = []
        Local = []
        Metragem = []
        Pedreiros = []
        Serventes = []
        Chuva = []
        Assobrado = []
        TempoTotal = []
        TempoMes = []
        Custo = []
        Lucro = []
        ValorTotal = []
        id_obra = []
        main.cabecalho(titulo)
        consulta = """
        SELECT [Cliente]
              ,[CPF/CNPJ]
              ,[Local]
              ,[Metragem]
              ,[Pedreiros]
              ,[Serventes]
              ,[Chuva]
              ,[Assobrado]
              ,[Tempo em Dias]
              ,[Tempo em Mes]
              ,[Custo]
              ,[Lucro]
              ,[Valor Total]
              ,[ID_Obra]
          FROM [DuckSystems].[dbo].[ControleDeObras]
            ORDER BY Cliente;"""
        cursor.execute(consulta)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            Cliente.append(tabela[x][0])
            CPF.append(tabela[x][1])
            Local.append(tabela[x][2])
            Metragem.append(tabela[x][3])
            Pedreiros.append(tabela[x][4])
            Serventes.append(tabela[x][5])
            Chuva.append(tabela[x][6])
            Assobrado.append(tabela[x][7])
            TempoTotal.append(tabela[x][8])
            TempoMes.append(tabela[x][9])
            Custo.append(tabela[x][10])
            Lucro.append(tabela[x][11])
            ValorTotal.append(tabela[x][12])
            id_obra.append(tabela[x][13])
            x += 1
        chaves = {'ID_Obra': id_obra, 'Cliente': Cliente, 'CPF/CNPJ': CPF, 'Local': Local, 'Metragem': Metragem, 'Pedreiros': Pedreiros, 'Serventes': Serventes, 'Chuva': Chuva, 'Assobrado': Assobrado, 'Tempo em Dias': TempoTotal, 'Tempo em Mes': TempoMes, 'Custo de Obra': Custo, 'Lucro': Lucro, 'Valor Total': ValorTotal}
        chaves = pandas.DataFrame(chaves)
        pandas.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None, 'display.width', 10000)
        if chaves.empty:
            print("A consulta não retornou nenhum valor.")
        else:
            print(chaves)
        while True:
            confirmacao = int(input("Insira o ID da obra a ser apagada: ").strip())
            if confirmacao in id_obra:
                break
            else:
                print(f"{Fore.RED}Insira um ID existente.{Style.RESET_ALL}")
        try:
            cursor.execute(f"""
                    DELETE FROM dbo.ControleDeObras WHERE ID_Obra = {confirmacao};
                    """)
            cursor.commit()
        finally:
            print(f"{Fore.GREEN}Registro removido com sucesso.{Style.RESET_ALL}")
        while True:
            encerrar = input("Deseja apagar outro registro? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um comando válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()
