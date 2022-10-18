from random import randint
tup = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
#for pos, c in enumerate(tup):
#    if pos == 0:
#        maior = tup[pos]
#        menor = tup[pos]
#    else:
#        if maior < tup[pos]:
#            maior = tup[pos]
#        if menor > tup[pos]:
#            menor = tup[pos]
print(tup)
#print(maior)
#print(menor)
print(f'O maior valor sorteado foi {max(tup)}')
print(f'O menor valor sorteado foi {min(tup)}')
