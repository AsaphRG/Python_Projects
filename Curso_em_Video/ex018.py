import math
an = float(input('Digite um ângulo aqui: '))
cosseno = math.cos(math.radians(an))
seno = math.sin(math.radians(an))
tangente = math.tan(math.radians(an))
print(f'O ângulo de {an} tem os seguintes valores:\n{cosseno}\n{seno}\n{tangente}')
