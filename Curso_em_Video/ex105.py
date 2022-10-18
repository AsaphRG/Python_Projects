def notas(*notas, sit=False):
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['média'] = sum(notas)/len(notas)
    if sit:
        if r['média'] >= 7:
            r['situação'] = "BOA"
        elif r['média'] >= 5:
            r['situação'] = "RAZOÁVEL"
        else:
            r['situação'] = "RUIM"
    return r


r = notas(5, 4.5, 8)
print(r)
