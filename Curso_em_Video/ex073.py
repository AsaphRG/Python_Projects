times = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná'
print(f'Os primeiros colocados são: {times[0:5]}')
print(f'Os últimos colocados são: {times[-1:-5:-1]}')
print(sorted(times))
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
