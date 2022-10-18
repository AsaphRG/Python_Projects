pmaior = 0
pmenor = 0
for c in range(1, 6):
    pp = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        pmaior = pp
        pmenor = p
    else:
        if pp > pmaior:
            pmaior = pp
        elif pp < pmenor:
            pmenor = pp
print(f'{pmaior} e {pmenor}')
