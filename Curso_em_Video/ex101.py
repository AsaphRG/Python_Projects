from datetime import date


def voto(ano):
    hoje = int(str(date.today())[0:4])
    idade = hoje - ano
    if idade < 16:
        return f"Com {idade} anos: voto negado."
    elif idade < 18 and idade >= 16 or idade > 65:
        return f"Com {idade} anos: voto opcional."
    else:
        return f"Com {idade} anos: voto obrigatório."


print(voto(1900))
