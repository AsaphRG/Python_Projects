"""Nós orgulhosamente apresentamos o DUCK SYSTEMS, uma CRUD pensada para garantir que o nosso amigo Duck não precise mais se preocupar em cuidar de sua agenda de contatos e consiga retomar o controle de seu negócio.

Abaixo segue o enunciado do desafio proposto. O desafio em si está cada um no respectivo módulo que o resolveu.

Desafio
Após muitos anos de trabalho duro como pedreiro, nosso amigo Pato percebeu que já tinha passado da hora de tentar subir mais um degrau em sua vida profissional. Queria ser o primeiro pato futebolista, mas seus planos foram frustrados pela ascensão de Alexandre Pato; então, resolveu que seria o primeiro pedreiro futebolista, mas seus sonhos foram por água abaixo com o aparecimento e o sucesso do Luva de Pedreiro. Sem saber que outro rumo tomar, resolveu usar seus anos de experiência para abrir um novo negócio: uma pequena construtora. Em pouco tempo ele já contava com 10 funcionários, sendo: três pedreiros, cinco serventes, um serralheiro e mais um funcionário no setor administrativo.
Embora não fosse nenhum pato-aranha, sua trajetória empresarial teve um início próspero. Porém, como lhe disse certa vez seu tio, Benjamin Parker Duck: “com grandes poderes vêm grandes responsabilidades”. Assim, nosso amigo logo descobriu que a vida de empresário não é nada fácil. Com o rápido crescimento da empresa, passou a enfrentar diversos problemas para entregar as obras contratadas dentro dos prazos acordados e com a qualidade esperada pelos clientes. Quando era sozinho, era fácil gerenciar tudo na sua caderneta de notas, mas agora, com tantos clientes e colaboradores, quase sempre se perdia e fazia confusões com suas anotações.
Em um jantar com seu amigo Mark McQuack - um grande especialista da área de TI e cocriador das ferramentas Ducker (gerenciamento de contêineres) e do famoso buscador VaiPatoVai! -, Duck confidenciou seus problemas na condução da empresa. Mark sugeriu a Duck que buscasse a construção de um software que pudesse apoiar na gestão da empresa, aproveitando-se do fato de que nossa região é um polo tecnológico.
Duck, animado com a perspectiva de melhora na entrega de suas obras, entrou em contato com um time de TI. Ele então relatou suas principais dificuldades (abaixo), solicitando a construção de ferramentas que poderiam transformar sua empresa (e sua vida)."""
from colorama import Fore, Style
import agenda, obra, funcionarios, os, pyodbc
titulo = f"{'Bem vindo ao':^40}\n{'DUCK SYSTEMS':^40}"


def conexao():
    """
    Conecta ao servidor e retorna o cursor.
    """
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost\sqlserver2019;ENCRYPT=no;DATABASE=DuckSystems;UID=SrDuck;PWD=senha123')
    cursor = cnxn.cursor()
    return cursor


def limpaTela():
    """
    Confere qual é o sistema operacional onde está rodando e executa o código correspondente.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def cabecalho(titulo):
    """
    Só faz um cabeçalho bonitinho. :)
    """
    espaco = 40
    print("=" * espaco)
    print()
    print(f"{titulo:^40}")
    print()
    print("=" * espaco)


if __name__ == "__main__":
    """
    Método principal do programa.
    """
    while True:
        cabecalho(titulo)
        print()
        print("1 - Acessar agenda\n2 - Acessar gerenciador de obras\n3 - Acessar gerenciador de funcionários\n0 - Encerrar programa\n")
        while True:
            atividade = input("O que deseja fazer? ")
            if atividade.isnumeric() and 0 <= int(atividade) < 4:
                atividade = int(atividade)
                break
            else:
                print(f"{Fore.RED}Insira um número válido.{Style.RESET_ALL}")
        print()
        limpaTela()
        if atividade == 1:
            agenda.menu()
        elif atividade == 2:
            obra.menu()
        elif atividade == 3:
            funcionarios.menu()
        elif atividade == 0:
            break
