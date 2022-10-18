"""1 – Duck utiliza uma caderneta para anotar todos os detalhes de seu negócio, sendo majoritariamente utilizada para anotar os contatos dos fornecedores, parceiros e funcionários que trabalham em suas obras. Porém, na última sexta-feira, após o tradicional “churrasco da laje”, sua caderneta desapareceu, levando consigo todos os dados de contatos. Agora, será necessário refazer tod o o trabalho. Duck busca modernizar e organizar melhor seus contatos além de utilizar uma solução mais segura que não tenha risco de perda dos dados;"""
from string import capwords
from colorama import Fore, Style
import main, pyodbc, pandas

espaco = 8
global cursor


def menu():
    """
    Menu de navegação.
    """
    titulo = "Agenda de Contatos"
    global cursor
    cursor = main.conexao()
    while True:
        main.cabecalho(titulo)
        print()
        print("1 - Registrar contato\n2 - Consultar agenda\n3 - Atualizar contato\n4 - Apagar contato\n0 - Voltar ao menu principal\n")
        while True:
            atividade = input("O que deseja fazer? ")
            if atividade.isnumeric() and 0 <= int(atividade) < 5:
                atividade = int(atividade)
                break
            else:
                print(f"{Fore.RED}Insira um número válido.{Style.RESET_ALL}")
        print()
        main.limpaTela()
        if atividade == 1:
            registraContato()
        elif atividade == 2:
            consultaContatos()
        elif atividade == 3:
            atualizaContato()
        elif atividade == 4:
            apagaContato()
        elif atividade == 0:
            break


def registraContato():
    """
    Esse método coleta informações inseridas pelo usuário e injeta no SQL.
    """
    titulo = "Registro de contato"
    while True:
        while True:
            main.cabecalho(titulo)
            while True:
                nome = input("Insira o nome: ").strip()
                if nome != "" and nome.isalpha():
                    break
                else:
                    print(f"{Fore.RED}Nome é obrigatório.{Style.RESET_ALL}")
            sobrenome = input("Insira o sobrenome: ").strip()
            while True:
                cpf = input("Insira o CPF/CNPJ: ").strip()
                if cpf != "":
                    break
                else:
                    print(f"{Fore.RED}CPF é obrigatório.{Style.RESET_ALL}")
            while True:
                relacao = int(input("\n1 - Fornecedor\n2 - Funcionário\n3 - Cliente\n4 - Amigo\nInsira o tipo de contato: "))
                if 0 < relacao < 5:
                    break
                else:
                    print(f"{Fore.RED}Insira um valor válido.{Style.RESET_ALL}")
            numero = input("\nInsira um telefone: ").strip()
            email = input("Insira um email: ").strip().lower()
            endereco = capwords(input("Insira um endereço: ").strip())
            try:
                cursor.execute(f"""
                    INSERT INTO DuckSystems.dbo.AgendaDeContatos (Nome, Sobrenome, CPF, ID_Relacao, Telefone, Email, Endereco)
                    VALUES ('{nome}', '{sobrenome}', '{cpf}', {relacao}, '{numero}', '{email}', '{endereco}');
                    """)
                cursor.commit()
            except pyodbc.IntegrityError:
                print(f"{Fore.RED}Valores repetidos não são permitidos em CPF.{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}O registro foi inserido com sucesso.{Style.RESET_ALL}")
                break
        while True:
            encerrar = input("Quer cadastrar um novo cliente? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um valor válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()


def consultaContatos():
    """
    Esse método faz uma consulta ao banco de dados e retorna os valores recuperados em uma tabela organizada por ordem alfabética, primeiro pelo relacionamento registrado e depois pelo nome do contato.
    """
    while True:
        Nome = []
        Sobrenome = []
        CPF = []
        Relacao = []
        Telefone = []
        Email = []
        Endereco = []
        titulo = "Tipo de Consulta"
        main.cabecalho(titulo)
        print()
        print("1 - Completa\n2 - Fornecedores\n3 - Funcionários\n4 - Clientes\n5 - Amigos\n6 - Buscar um contato\n")
        while True:
            atividade = input("O que deseja fazer? ")
            if atividade.isnumeric() and 0 < int(atividade) <= 6:
                atividade = int(atividade)
                break
            else:
                print(f"{Fore.RED}Insira um número válido.{Style.RESET_ALL}")
        print()
        main.limpaTela()
        titulo = "Consulta contatos"
        main.cabecalho(titulo)
        if atividade == 1:
            consulta = """
                SELECT [Nome]
                      ,[Sobrenome]
                      ,[CPF]
                      ,[dbo].[Relacionamento].[Relacao]
                      ,[Telefone]
                      ,[Email]
                      ,[Endereco]
                  FROM [DuckSystems].[dbo].[AgendaDeContatos]
                    INNER JOIN dbo.Relacionamento on dbo.AgendaDeContatos.ID_Relacao = dbo.Relacionamento.ID_Relacao
                    ORDER BY Relacao, Nome;"""
        elif atividade == 2:
            consulta = """
                SELECT [Nome]
                      ,[Sobrenome]
                      ,[CPF]
                      ,[dbo].[Relacionamento].[Relacao]
                      ,[Telefone]
                      ,[Email]
                      ,[Endereco]
                  FROM [DuckSystems].[dbo].[AgendaDeContatos]
                    INNER JOIN dbo.Relacionamento on dbo.AgendaDeContatos.ID_Relacao = dbo.Relacionamento.ID_Relacao
                    WHERE dbo.AgendaDeContatos.ID_Relacao = 1
                    ORDER BY Relacao, Nome;"""
        elif atividade == 3:
            consulta = """
                SELECT [Nome]
                      ,[Sobrenome]
                      ,[CPF]
                      ,[dbo].[Relacionamento].[Relacao]
                      ,[Telefone]
                      ,[Email]
                      ,[Endereco]
                  FROM [DuckSystems].[dbo].[AgendaDeContatos]
                    INNER JOIN dbo.Relacionamento on dbo.AgendaDeContatos.ID_Relacao = dbo.Relacionamento.ID_Relacao
                    WHERE dbo.AgendaDeContatos.ID_Relacao = 2
                    ORDER BY Relacao, Nome;"""
        elif atividade == 4:
            consulta = """
                SELECT [Nome]
                      ,[Sobrenome]
                      ,[CPF]
                      ,[dbo].[Relacionamento].[Relacao]
                      ,[Telefone]
                      ,[Email]
                      ,[Endereco]
                  FROM [DuckSystems].[dbo].[AgendaDeContatos]
                    INNER JOIN dbo.Relacionamento on dbo.AgendaDeContatos.ID_Relacao = dbo.Relacionamento.ID_Relacao
                    WHERE dbo.AgendaDeContatos.ID_Relacao = 3
                    ORDER BY Relacao, Nome;"""
        elif atividade == 5:
            consulta = """
                SELECT [Nome]
                      ,[Sobrenome]
                      ,[CPF]
                      ,[dbo].[Relacionamento].[Relacao]
                      ,[Telefone]
                      ,[Email]
                      ,[Endereco]
                  FROM [DuckSystems].[dbo].[AgendaDeContatos]
                    INNER JOIN dbo.Relacionamento on dbo.AgendaDeContatos.ID_Relacao = dbo.Relacionamento.ID_Relacao
                    WHERE dbo.AgendaDeContatos.ID_Relacao = 4
                    ORDER BY Relacao, Nome;"""
        elif atividade == 6:
            contato = input("Insira o contato a ser consultado: ").strip()
            consulta = f"""
                SELECT [Nome]
                      ,[Sobrenome]
                      ,[CPF]
                      ,[dbo].[Relacionamento].[Relacao]
                      ,[Telefone]
                      ,[Email]
                      ,[Endereco]
                  FROM [DuckSystems].[dbo].[AgendaDeContatos]
                    INNER JOIN dbo.Relacionamento on dbo.AgendaDeContatos.ID_Relacao = dbo.Relacionamento.ID_Relacao
                    WHERE dbo.AgendaDeContatos.Nome = '{contato}'
                    ORDER BY Relacao, Nome;"""
        cursor.execute(consulta)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            Nome.append(tabela[x][0])
            Sobrenome.append(tabela[x][1])
            CPF.append(tabela[x][2])
            Relacao.append(tabela[x][3])
            Telefone.append(tabela[x][4])
            Email.append(tabela[x][5])
            Endereco.append(tabela[x][6])
            x += 1
        chaves = {'Nome': Nome, 'Sobrenome': Sobrenome, 'CPF': CPF, 'Relacionamento': Relacao, 'Telefone': Telefone, 'Email': Email, 'Endereco': Endereco}
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


def atualizaContato():
    """
    Esse método apresenta uma tabela com todos os contatos e recebe as informações do usuário, alterando, no banco de dados, os valores relacionados ao CPF oferecido pelo usuário.
    """
    while True:
        Nome = []
        Sobrenome = []
        CPF = []
        Relacao = []
        Telefone = []
        Email = []
        Endereco = []
        titulo = "Atualizar contato"
        main.cabecalho(titulo)
        cursor.execute("""
        SELECT [Nome]
              ,[Sobrenome]
              ,[CPF]
              ,[dbo].[Relacionamento].[Relacao]
              ,[Telefone]
              ,[Email]
              ,[Endereco]
          FROM [DuckSystems].[dbo].[AgendaDeContatos]
            INNER JOIN dbo.Relacionamento on dbo.AgendaDeContatos.ID_Relacao = dbo.Relacionamento.ID_Relacao
            ORDER BY Relacao, Nome;
        """)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            Nome.append(tabela[x][0])
            Sobrenome.append(tabela[x][1])
            CPF.append(tabela[x][2])
            Relacao.append(tabela[x][3])
            Telefone.append(tabela[x][4])
            Email.append(tabela[x][5])
            Endereco.append(tabela[x][6])
            x += 1
        chaves = {'Nome': Nome, 'Sobrenome': Sobrenome, 'CPF': CPF, 'Relacionamento': Relacao, 'Telefone': Telefone, 'Email': Email, 'Endereco': Endereco}
        chaves = pandas.DataFrame(chaves)
        pandas.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None, 'display.width', 10000)
        if chaves.empty:
            print("A consulta não retornou nenhum valor.")
        else:
            print(chaves)
        while True:
            while True:
                alterDado = input("Dado a ser alterado: ").strip()
                alterValor = input("Valor a ser inserido: ").strip().lower()
                confirmacao = input("Confirme o dado a ser alterado com o CPF de quem deseja alterar: ").strip()
                if alterDado != "" and alterValor != "" and confirmacao in CPF:
                    break
                else:
                    print(f"{Fore.RED}Preencha todas as informações corretamente.{Style.RESET_ALL}")
            try:
                cursor.execute(f"""
                    UPDATE dbo.AgendaDeContatos
                    SET {alterDado} = '{alterValor}'
                    WHERE CPF = '{confirmacao}';
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


def apagaContato():
    """
    Esse método apresenta uma tabela com os contatos e apaga o contato relacionado ao CPF oferecido pelo usuário.
    """
    while True:
        Nome = []
        Sobrenome = []
        CPF = []
        Relacao = []
        Telefone = []
        Email = []
        Endereco = []
        titulo = "Apagar contato"
        main.cabecalho(titulo)
        cursor.execute("""
            SELECT [Nome]
                  ,[Sobrenome]
                  ,[CPF]
                  ,[dbo].[Relacionamento].[Relacao]
                  ,[Telefone]
                  ,[Email]
                  ,[Endereco]
            FROM [DuckSystems].[dbo].[AgendaDeContatos]
                INNER JOIN dbo.Relacionamento on dbo.AgendaDeContatos.ID_Relacao = dbo.Relacionamento.ID_Relacao
                ORDER BY Relacao, Nome;
            """)
        tabela = cursor.fetchall()
        x = 0
        while x < len(tabela):
            Nome.append(tabela[x][0])
            Sobrenome.append(tabela[x][1])
            CPF.append(tabela[x][2])
            Relacao.append(tabela[x][3])
            Telefone.append(tabela[x][4])
            Email.append(tabela[x][5])
            Endereco.append(tabela[x][6])
            x += 1
        chaves = {'Nome': Nome, 'Sobrenome': Sobrenome, 'CPF': CPF, 'Relacionamento': Relacao, 'Telefone': Telefone, 'Email': Email, 'Endereco': Endereco}
        chaves = pandas.DataFrame(chaves)
        pandas.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None, 'display.width', 10000)
        if chaves.empty:
            print("A consulta não retornou nenhum valor.")
        else:
            print(chaves)
        while True:
            confirmacao = input("Insira o CPF do contato a ser apagado: ").strip()
            if confirmacao in CPF:
                break
            else:
                print(f"{Fore.RED}Insira um CPF existente.{Style.RESET_ALL}")
        try:
            cursor.execute(f"""
                    DELETE FROM dbo.AgendaDeContatos WHERE CPF = '{confirmacao}';
                    """)
            cursor.commit()
        finally:
            print(f"{Fore.GREEN}Registro removido com sucesso.{Style.RESET_ALL}")
        while True:
            encerrar = input("Quer remover outro registro? [S/N] ").strip().upper()
            if encerrar in "SN":
                break
            else:
                print(f"{Fore.RED}Insira um comando válido.{Style.RESET_ALL}")
        main.limpaTela()
        if encerrar == "N":
            break
    main.limpaTela()
