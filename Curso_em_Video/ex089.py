notas = []
nome = []
alunos = []
contador = 0

while True:
    nome.append(str(input('Insira o nome: ')).strip().capitalize())
    notas.append(float(input('Insira a nota 1: ')))
    notas.append(float(input('Insira a nota 2: ')))
    nome.append(notas[len(notas) - 2:len(notas)])
    alunos.append(nome[len(nome) - 2:len(nome)])
    contador += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    nome.clear()
    notas.clear()
    if continuar == 'N':
        break
print('Índice |  Aluno  |   Média')
print('-' * 30)
for i in range(0, len(alunos)):
    print(f'   {i}   |{alunos[i][0]:9}: {(alunos[i][1][0] + alunos[i][1][1]) / 2:9}')
while True:
    ver = int(input('Você quer ver as notas de qual aluno? (999 para encerrar) '))
    if ver == 999:
        break
    else:
        print(alunos[ver][1][0], alunos[ver][1][1])
