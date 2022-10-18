aluno = {'nome': str(input('Nome do aluno: ').strip().capitalize()), 'media': float(input(f'Insira a média do aluno: '))}
if aluno['media'] >= 7.0:
    aluno['resultado'] = 'Aprovado'
else:
    aluno['resultado'] = 'Reprovado'
print(f'O aluno {aluno["nome"]} ficou com média {aluno["media"]} e foi {aluno["resultado"]}.')
