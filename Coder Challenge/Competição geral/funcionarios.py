"""4 – Outro desejo de Duck seria estimular os melhores e mais produtivos funcionários com uma bonificação."""
from colorama import Fore, Style
import main, pyodbc, pandas
titulo = "Controle de funcionários"
global cursor


def menu():
    """
    Menu de navegação.
    """
    global cursor
    cursor = main.conexao()
    while True:
        main.cabecalho(titulo)
        print()
        print("1 - Registrar funcionário\n2 - Consultar funcionários\n3 - Atualizar dados\n4 - Apagar funcionário\n0 - Voltar ao menu principal\n")
        while True:
            atividade = input("O que deseja fazer? ")
            if atividade.isnumeric() and 0 <= int(atividade) < 5:
                atividade = int(atividade)
                break
            else:
                print(f"{Fore.RED}Insira um número válido.{Style.RESET_ALL}")
        main.limpaTela()
        if atividade == 1:
            registraFuncionario()
        elif atividade == 2:
            consultaFuncionario()
        elif atividade == 3:
            atualizaFuncionario()
        elif atividade == 4:
            apagaFuncionario()
        elif atividade == 0:
            break


def registraFuncionario():
    """
    Esse método coleta informações inseridas pelo usuário, envia para o método calculaBonificacao e então injeta os valores no SQL.
    """
    titulo = "Registro de Funcionário"
    while True:
        main.cabecalho(titulo)
        while True:
            nome = input("Insira o nome: ").strip()
            while True:
                tipo = input("\n1 - Pedreiro\n2 - Servente\n3 - Assistente administrativo\n\nInsira cargo: ").strip()
                if tipo.isnumeric() and 0 < int(tipo) < 4:
                    tipo = int(tipo)
                    break
                else:
                    print(f"{Fore.RED}Insira um valor válido.{Style.RESET_ALL}")
            bonificacao = input("Bonificacao [S/N]: ").strip().upper()
            if bonificacao == "":
                bonificacao = "N"
            cargo, diaria, porcentagem, valorBonus, valorFinal = calculoBonificacao(tipo, bonificacao)
            try:
                cursor.execute(f"""
                    INSERT INTO DuckSystems.dbo.ControleDeFuncionarios (Nome, Cargo, Diaria, Bonus, Porcentagem, [Valor do Bonus], [Valor Total])
                    VALUES ('{nome}', '{cargo}', {diaria}, '{bonificacao}', {porcentagem}, {valorBonus}, {valorFinal});
                    """)
                cursor.commit()
            except pyodbc.IntegrityError:
                print(f"{Fore.RED}Valores repetidos não são permitidos em CPF.{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}O registro foi inserido com sucesso.{Style.RESET_ALL}")
                break
        while True:
            encerrar = input("Quer cadastrar um novo funcionário? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um valor válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()


def calculoBonificacao(tipo, bonificacao):
    """
    Processa os valores recebidos.
    :return: Retorna os valores relativos ao cargo, diaria, porcentagem de bonificação, valor da bonificação e valor total do pagamento.
    """
    if tipo == 1 or tipo == "Pedreiro":
        cargo = "Pedreiro"
        diaria = 190
    elif tipo == 2 or tipo == "Servente":
        cargo = "Servente"
        diaria = 95
    elif tipo == 3 or tipo == "Assistente administrativo":
        cargo = "Assistente administrativo"
        diaria = 80.8
    if bonificacao == "S":
        while True:
            porcentagem = input("Insira a porcentagem de bonificação sem o %: ").strip()
            if porcentagem.isnumeric():
                porcentagem = float(porcentagem)
                break
            else:
                print(f"{Fore.RED}Insira um valor válido.{Style.RESET_ALL}")
    else:
        porcentagem = 0.0
    valorBonus = (diaria * porcentagem / 100)
    valorFinal = valorBonus + diaria
    return cargo, diaria, porcentagem, valorBonus, valorFinal


def consultaFuncionario():
    """
    Esse método faz uma consulta ao banco de dados e retorna os valores recuperados em uma tabela organizada por ordem alfabética, de acordo com o nome do funcionário.
    """
    while True:
        nome = []
        cargo = []
        diaria = []
        bonificacao = []
        porcentagem = []
        valorBonus = []
        valorFinal = []
        titulo = "Tipo de Consulta"
        main.cabecalho(titulo)
        print()
        print("1 - Completa\n2 - Pedreiros\n3 - Serventes\n4 - Assistentes administrativo\n5 - Buscar um funcionario\n")
        while True:
            atividade = input("O que deseja fazer? ")
            if atividade.isnumeric() and 0 < int(atividade) <= 6:
                atividade = int(atividade)
                break
            else:
                print(f"{Fore.RED}Insira um número válido.{Style.RESET_ALL}")
        print()
        main.limpaTela()
        titulo = "Consulta funcionarios"
        main.cabecalho(titulo)
        if atividade == 1:
            consulta = """
            SELECT [Nome]
                  ,[Cargo]
                  ,[Diaria]
                  ,[Bonus]
                  ,[Porcentagem]
                  ,[Valor do Bonus]
                  ,[Valor Total]
              FROM [DuckSystems].[dbo].[ControleDeFuncionarios]
                ORDER BY Nome;"""
        elif atividade == 2:
            consulta = """
            SELECT [Nome]
                  ,[Cargo]
                  ,[Diaria]
                  ,[Bonus]
                  ,[Porcentagem]
                  ,[Valor do Bonus]
                  ,[Valor Total]
              FROM [DuckSystems].[dbo].[ControleDeFuncionarios]
                WHERE Cargo = 'Pedreiro'
                ORDER BY Nome;"""
        elif atividade == 3:
            consulta = """
            SELECT [Nome]
                  ,[Cargo]
                  ,[Diaria]
                  ,[Bonus]
                  ,[Porcentagem]
                  ,[Valor do Bonus]
                  ,[Valor Total]
              FROM [DuckSystems].[dbo].[ControleDeFuncionarios]
                WHERE Cargo = 'Servente'
                ORDER BY Nome;"""
        elif atividade == 4:
            consulta = """
            SELECT [Nome]
                  ,[Cargo]
                  ,[Diaria]
                  ,[Bonus]
                  ,[Porcentagem]
                  ,[Valor do Bonus]
                  ,[Valor Total]
              FROM [DuckSystems].[dbo].[ControleDeFuncionarios]
                WHERE Cargo = 'Assistente administrativo'
                ORDER BY Nome;"""
        elif atividade == 5:
            funcionario = input("Consultar funcionário: ").strip()
            consulta = f"""
            SELECT [Nome]
                  ,[Cargo]
                  ,[Diaria]
                  ,[Bonus]
                  ,[Porcentagem]
                  ,[Valor do Bonus]
                  ,[Valor Total]
              FROM [DuckSystems].[dbo].[ControleDeFuncionarios]
                WHERE NomeFuncionario = '{funcionario}'
                ORDER BY Nome;"""
        cursor.execute(consulta)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            nome.append(tabela[x][0])
            cargo.append(tabela[x][1])
            diaria.append(tabela[x][2])
            bonificacao.append(tabela[x][3])
            porcentagem.append(f"{tabela[x][4]}%")
            valorBonus.append(tabela[x][5])
            valorFinal.append(tabela[x][6])
            x += 1
        chaves = {'Nome': nome, 'Cargo': cargo, 'Diaria': diaria, 'Bonus': bonificacao, 'Porcentagem': porcentagem, 'Valor do Bonus': valorBonus, 'Valor Total': valorFinal}
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


def atualizaFuncionario():
    """
    Esse método apresenta uma tabela com todos os funcionários e recebe as informações do usuário, alterando, no banco de dados, os valores relacionados ao ID oferecido pelo usuário. Caso os valores alterados impactem no valor final a ser pago ao funcionário o método envia os dados necessários para o calculaBonificacao para fazer o processamento necessário para a atualização dos valores.
    """
    while True:
        nome = []
        cargo = []
        diaria = []
        bonificacao = []
        porcentagem = []
        valorBonus = []
        valorFinal = []
        id_func = []
        titulo = "Alterar cadastro"
        main.cabecalho(titulo)
        consulta = """
        SELECT [Nome]
              ,[Cargo]
              ,[Diaria]
              ,[Bonus]
              ,[Porcentagem]
              ,[Valor do Bonus]
              ,[Valor Total]
              ,[ID_Funcionario]
          FROM [DuckSystems].[dbo].[ControleDeFuncionarios]
            ORDER BY Nome;"""
        cursor.execute(consulta)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            nome.append(tabela[x][0])
            cargo.append(tabela[x][1])
            diaria.append(tabela[x][2])
            bonificacao.append(tabela[x][3])
            porcentagem.append(f"{tabela[x][4]}%")
            valorBonus.append(tabela[x][5])
            valorFinal.append(tabela[x][6])
            id_func.append(tabela[x][7])
            x += 1
        chaves = {'ID_Funcionario': id_func, 'Nome': nome, 'Cargo': cargo, 'Diaria': diaria, 'Bonus': bonificacao, 'Porcentagem': porcentagem}
        chaves = pandas.DataFrame(chaves)
        pandas.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None, 'display.width', 10000)
        if chaves.empty:
            print("A consulta não retornou nenhum valor.")
        else:
            print(chaves)
        while True:
            while True:
                alterDado = input("Dado a ser alterado: ").strip()
                if alterDado == "Cargo":
                    while True:
                        tipo = input("\n1 - Pedreiro\n2 - Servente\n3 - Assistente administrativo\n\nInsira cargo: ").strip()
                        if tipo.isnumeric() and 0 < int(tipo) < 4:
                            tipo = int(tipo)
                            break
                        else:
                            print(f"{Fore.RED}Insira um valor válido.{Style.RESET_ALL}")
                else:
                    alterValor = input("Valor a ser inserido: ").strip()
                confirmacao = int(input("Confirme o ID do registro: ").strip())
                if alterDado != "" and alterValor != "" and confirmacao in id_func:
                    break
                else:
                    print(f"{Fore.RED}Preencha todas as informações corretamente.{Style.RESET_ALL}")
            if alterDado == "Porcentagem":
                bonificacao[id_func.index(confirmacao)] = "S"
            if alterDado == "Cargo" or alterDado == "Bonus" or alterDado == "Porcentagem":
                chave = id_func.index(confirmacao)
                if alterDado == "Cargo":
                    tipo = alterValor
                    Bonificacao = bonificacao[chave]
                elif alterDado == "Bonus":
                    tipo = cargo[chave]
                    Bonificacao = alterValor.upper()
                else:
                    tipo = cargo[chave]
                    Bonificacao = bonificacao[chave]
                Cargo, Diaria, Porcentagem, valorDeBonus, valorFinalDeBonus = calculoBonificacao(tipo, Bonificacao)
                try:
                    cursor.execute(f"""
                    UPDATE dbo.ControleDeFuncionarios
                    SET [Cargo] = '{Cargo}', [Diaria] = {Diaria}, [Bonus] = '{Bonificacao}', [Porcentagem] = {Porcentagem}, [Valor do Bonus] = {valorDeBonus}, [Valor Total] = {valorFinalDeBonus}
                    WHERE ID_Funcionario = '{confirmacao}';
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
                        UPDATE dbo.ControleDeFuncionarios
                        SET [{alterDado}] = '{alterValor}'
                        WHERE ID_Funcionario = '{confirmacao}';
                        """)
                    cursor.commit()
                except pyodbc.ProgrammingError:
                    print(f"{Fore.RED}Insira dados válidos.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}Dados inseridos com sucesso.{Style.RESET_ALL}")
                    break
        while True:
            encerrar = input("\nDeseja alterar outro cadastro? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um comando válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()


def apagaFuncionario():
    """
    Esse método apresenta uma tabela com os funcionários registrados e apaga o relacionado ao ID oferecido pelo usuário.
    """
    while True:
        nome = []
        cargo = []
        diaria = []
        bonificacao = []
        porcentagem = []
        valorBonus = []
        valorFinal = []
        id_func = []
        titulo = "Apagar registro"
        main.cabecalho(titulo)
        consulta = """
        SELECT [Nome]
              ,[Cargo]
              ,[Diaria]
              ,[Bonus]
              ,[Porcentagem]
              ,[Valor do Bonus]
              ,[Valor Total]
              ,[ID_Funcionario]
          FROM [DuckSystems].[dbo].[ControleDeFuncionarios]
            ORDER BY Nome;"""
        cursor.execute(consulta)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            nome.append(tabela[x][0])
            cargo.append(tabela[x][1])
            diaria.append(tabela[x][2])
            bonificacao.append(tabela[x][3])
            porcentagem.append(f"{tabela[x][4]}%")
            valorBonus.append(tabela[x][5])
            valorFinal.append(tabela[x][6])
            id_func.append(tabela[x][7])
            x += 1
        chaves = {'ID_Funcionario': id_func, 'Nome': nome, 'Cargo': cargo, 'Diaria': diaria, 'Bonus': bonificacao, 'Porcentagem': porcentagem, '[Valor do Bonus]': valorBonus, '[Valor Total]': valorFinal}
        chaves = pandas.DataFrame(chaves)
        pandas.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None, 'display.width', 10000)
        if chaves.empty:
            print("A consulta não retornou nenhum valor.")
        else:
            print(chaves)
        while True:
            while True:
                confirmacao = int(input("Insira o ID do registro: ").strip())
                if confirmacao in id_func:
                    break
                else:
                    print(f"{Fore.RED}Preencha todas as informações corretamente.{Style.RESET_ALL}")
            try:
                cursor.execute(f"""
                    DELETE FROM dbo.ControleDeFuncionarios WHERE ID_Funcionario = {confirmacao};
                    """)
                cursor.commit()
            except pyodbc.ProgrammingError:
                print(f"{Fore.RED}Insira dados válidos.{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}Registro removido com sucesso.{Style.RESET_ALL}")
                break
        while True:
            encerrar = input("\nDeseja apagar outro registro? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um comando válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()
