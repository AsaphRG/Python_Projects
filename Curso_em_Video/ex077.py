letra = ''
lis = 'aprender', 'ganho', 'locução', 'irmão', 'limão', 'zé', 'fé', 'migué', 'órgão', 'prática'
for pos, c in enumerate(lis):
    for i in lis[pos]:
        if i in 'aeiouãáéíó':
            letra += i + ' '
    print(f'Na palavra {c} temos {letra}')
    letra = ''
