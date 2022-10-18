nome = input('Me diga seu nome: ').title()

print('-----------------------')

dividido = nome.split()
print(dividido[0])
print(dividido[-1])

print('-----------------------')

print(nome.split()[0])
espaco = nome.rfind(' ')
print(nome[espaco+1:])

print('-----------------------')

print(dividido[0])
print(dividido[len(dividido)-1])
