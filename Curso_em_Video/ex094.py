pessoas = list()
media = 0
i = 0
mulheres = ""

while True:
    pessoa = {'nome': str(input('Nome: ').strip().capitalize())}
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ").strip().capitalize()[0])
        if pessoa['sexo'] in "MF":
            break
        print("Insira apenas Masculino ou Feminino.")
    pessoa['idade'] = int(input("Insira idade: "))
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ').strip().upper()[0])
        if resp in "SN":
            break
        print("Insira somente S ou N.")
    if resp == "N":
        break
while i < len(pessoas):
    media += pessoas[i]['idade']
    i += 1
media /= len(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.\nA média de idade das pessoas é de {media}.')
i = 0
while i < len(pessoas):
    if pessoas[i]['sexo'] == "F":
        if mulheres == "":
            mulheres = pessoas[i]['nome'] + " "
        else:
            mulheres = mulheres, pessoas[i]['nome'] + " "
    i += 1
print(f'As mulheres cadastradas foram: ', end="")
for c in mulheres:
    print(c, end="")
i = 0
print('\nLista das pessoas que estão acima da média de idade: ')
while i < len(pessoas):
    if pessoas[i]['idade'] > media:
        print(f'{pessoas[i]["nome"]} está acima da média e tem {pessoas[i]["idade"]}.')
    i += 1
