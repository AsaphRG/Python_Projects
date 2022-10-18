resultados = []
while True:
    aluno = {"nome": str(input("Nome do aluno: ").strip().capitalize()), "media": float(input("Média do aluno: ").strip())}
    if aluno["media"] > 7:
        aluno["resultado"] = "Aprovado"
    else:
        aluno["resultado"] = "Reprovado"
    resultados.append(aluno)
    parar = str(input(f"Quer inserir outro aluno?\n").strip().upper())
    if parar[0] == "N":
        break
for i in range(len(resultados)):
    print(f"O aluno {resultados[i]['nome']} ficou com média {resultados[i]['media']} e ficou {resultados[i]['resultado']}.")
