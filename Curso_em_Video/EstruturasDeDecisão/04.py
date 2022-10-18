l = input('Digite uma letra: ').lower().strip()
if l[0] == 'a' or l[0] == 'e' or l[0] == 'i' or l[0] == 'o' or l[0] == 'u' or l[0] == 'y':
    print('A primeira letra que você me mostrou é uma vogal.')
else:
    print('A primeira letra que me mostrou é uma consoante.')
